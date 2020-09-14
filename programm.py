import socketio
from aiohttp import web
import eventlet
from classes.User import User
from classes.UserManager import UserManager
from classes.Room import Room
from classes.RoomManager import RoomManager
from classes.Field import Field

sio = socketio.AsyncServer(cors_allowed_origins='*',async_mode='aiohttp')
app = web.Application()
sio.attach(app)

authUsers = UserManager()
playRooms = RoomManager()
battlefield = Field()

@sio.event 
def connect(sid, environ): 
    print('connect ', sid)
 
@sio.event
def auth(sid, name):
    if next((user for user in authUsers.userList if user.sid == sid), None) == None:
        authUsers.addUser(User(sid, name))
    else:
        authUsers.userList[authUsers.getBySid(sid)].setName(name)

@sio.event
def quickroom(sid, data):
    playRooms.listReadyRoom()
    if playRooms.readyRoom != []:
        playRooms.readyRoom[0].setUserTwo(authUsers.userList[authUsers.getBySid(sid)])
        room = playRooms.readyRoom[0]
        print(room.userOne.name, room.userTwo.name, room.link)
    else:
        room = Room(authUsers.userList[authUsers.getBySid(sid)],'public')
        playRooms.addRoom(room,authUsers.userList[authUsers.getBySid(sid)])
        print (room.userOne.name, room.link)
    return room.link

@sio.event 
def my_message(sid, data): 
    print('message ', data)

@sio.event
def shipIn(sid, data):
    if authUsers.getBySid(sid) != None:
        playRooms.setPlayerShip(sid,data)
    else:
        return('failure')

@sio.event
def shot(sid,data):
    result = playRooms.shotAtCoordinate(sid,data)
    userIndex = authUsers.getBySid(sid)
    nRoom = authUsers.userList[userIndex].playRoom
    if sid == playRooms.roomList[nRoom].userOne.sid:
        sio.emit = ('shooting',playRooms.roomList[nRoom].playerTwoField,playRooms.roomList[nRoom].userOne.sid)
        sio.emit = ('shooting',playRooms.roomList[nRoom].playerTwoField,playRooms.roomList[nRoom].userTwo.sid)
    else:
        sio.emit = ('shooting',playRooms.roomList[nRoom].playerOneField,playRooms.roomList[nRoom].userOne.sid)
        sio.emit = ('shooting',playRooms.roomList[nRoom].playerOneField,playRooms.roomList[nRoom].userTwo.sid)
    if result == 'Player One Win' or result == 'Player Two Win':
        if userIndex != None:
            if authUsers.userList[userIndex].playRoom != None:
                playerOne = authUsers.getBySid(playRooms.roomList[nRoom].userOne.sid)
                playerTwo = authUsers.getBySid(playRooms.roomList[nRoom].userTwo.sid)
                authUsers.userList[playerOne].playRoom = None
                authUsers.userList[playerTwo].playRoom = None
                playRooms.deleteRoom(nRoom)
    return result


@sio.event 
def disconnect(sid):
    userIndex = authUsers.getBySid(sid)
    if userIndex != None:
        if authUsers.userList[userIndex].playRoom != None:
            playRooms.deleteRoom(authUsers.userList[userIndex].playRoom)
        authUsers.removeUser(sid)
    print('disconnect ', sid) 
 
if __name__ == '__main__': 
    web.run_app(app, port=5000)
