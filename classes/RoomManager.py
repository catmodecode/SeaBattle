from classes.Room import Room
from classes.User import User

class RoomManager:
    roomList = []
    readyRoom = []

    def addRoom(self, room, user):
        user.playRoom = len(self.roomList)
        self.roomList.append(room)
        print('room',str(len(self.roomList)-1),'created successfully')

    def listRoom(self):
       print('list of rooms returned') 
       return(self.roomList)

    def listReadyRoom(self):
        self.readyRoom = []
        if len(self.roomList) != 0:
            for room in self.roomList:
                if (room.status != 'full') and (room.status != 'private'):
                    self.readyRoom.append(room)
        print('the list of available rooms has been successfully generated')

    def deleteRoom(self, roomIndex):
        if self.roomList[roomIndex].userOne.playRoom != None:
            self.roomList[roomIndex].userOne.playRoom = None
        if (self.roomList[roomIndex].userTwo != None) and (self.roomList[roomIndex].userTwo.playRoom != None):   
            self.roomList[roomIndex].userTwo.playRoom = None
        self.roomList.remove(self.roomList[roomIndex])
        print('room',roomIndex,'deleted successfully')
