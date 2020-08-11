from classes.Room import Room
from classes.User import User
from classes.Field import Field

class RoomManager:
    roomList = []
    readyRoom = []

    def addRoom(self, room, user):
        user.playRoom = len(self.roomList)
        self.roomList.append(room)

    def listRoom(self):
       return(self.roomList)

    def listReadyRoom(self):
        self.readyRoom = []
        if len(self.roomList) != 0:
            for room in self.roomList:
                if (room.status != 'full') and (room.status != 'private'):
                    self.readyRoom.append(room)

    def setPlayerShip(self,playerSid,shipData):
        for roomItem in self.roomList:
            if roomItem.userOne.sid == playerSid:
                roomItem.playerOneField.setShipList(shipData)
                for shipItem in roomItem.playerOneField.shipList:
                    if shipItem.canShipPlaced(roomItem.playerOneField):
                        shipItem.shipPlacing(roomItem.playerOneField)
                    else:
                        return ('failure')
                roomItem.playerOneField.printField(roomItem.playerOneField)
            elif roomItem.userTwo.sid == playerSid:
                roomItem.playerTwoField.setShipList(shipData)
                for shipItem in roomItem.playerTwoField.shipList:
                    if shipItem.canShipPlaced(roomItem.playerTwoField):
                        shipItem.shipPlacing(roomItem.playerTwoField)
                    else:
                        return ('failure')
                roomItem.playerTwoField.printField(roomItem.playerTwoField)
        return('succesful')

    def shotAtCoordinate(self,playerSid,coordinateData):
        itemField = None
        for roomItem in self.roomList:
            if roomItem.userOne.sid == playerSid:
                itemField = roomItem.playerTwoField                       
            elif roomItem.userTwo.sid == playerSid:
                itemField = roomItem.playerOneField       
            itemField.canShooted(coordinateData['x'],coordinateData['y'])
            itemField.printField(roomItem.playerTwoField)                
    
    def deleteRoom(self, roomIndex):
        roomLink = None
        if self.roomList[roomIndex].userOne.playRoom != None:
            self.roomList[roomIndex].userOne.playRoom = None
        if (self.roomList[roomIndex].userTwo != None) and (self.roomList[roomIndex].userTwo.playRoom != None):
            self.roomList[roomIndex].userTwo.playRoom = None
        roomLink = self.roomList[roomIndex].link
        self.roomList.remove(self.roomList[roomIndex])
        print('room',roomLink,'deleted successfully')
