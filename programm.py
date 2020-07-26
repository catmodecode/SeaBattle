import eventlet 
import socketio 
from classes.User import User
from classes.UserManager import UserManager
from classes.Room import Room
from classes.RoomManager import RoomManager
 
sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio, static_files={ 
    '/': {'content_type': 'text/html', 'filename': 'index.html'} 
}) 
 
authUsers = UserManager()
playRooms = RoomManager()

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
def disconnect(sid): 
    userIndex = authUsers.getBySid(sid)
    if userIndex != None:
        if authUsers.userList[userIndex].playRoom != None:
            playRooms.deleteRoom(authUsers.userList[userIndex].playRoom)
        authUsers.removeUser(sid)
    print('disconnect ', sid) 
 
if __name__ == '__main__': 
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
