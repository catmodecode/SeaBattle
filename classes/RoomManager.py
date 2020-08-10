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
        for roomItem in range(len(self.roomList)):
            if self.roomList[roomItem].userOne.sid == playerSid:
                self.roomList[roomItem].playerOneField.setShipList(shipData)
                for item in range(len(self.roomList[roomItem].playerOneField.shipList)):
                    if self.roomList[roomItem].playerOneField.shipList[item].canShipPlaced(self.roomList[roomItem].playerOneField):
                        self.roomList[roomItem].playerOneField.shipList[item].shipPlacing(self.roomList[roomItem].playerOneField)
                    else:
                        return ('failure')
                self.roomList[roomItem].playerOneField.printField(self.roomList[roomItem].playerOneField)
            elif self.roomList[roomItem].userTwo.sid == playerSid:
                self.roomList[roomItem].playerTwoField.setShipList(shipData)
                for item in range(len(self.roomList[roomItem].playerTwoField.shipList)):
                    if self.roomList[roomItem].playerTwoField.shipList[item].canShipPlaced(self.roomList[roomItem].playerTwoField):
                        self.roomList[roomItem].playerTwoField.shipList[item].shipPlacing(self.roomList[roomItem].playerTwoField)
                    else:
                        return ('failure')
                self.roomList[roomItem].playerTwoField.printField(self.roomList[roomItem].playerTwoField)
        return('succesful')

    def shotAtCoordinate(self,playerSid,coordinateData):
        for roomItem in self.roomList:
            if roomItem.userOne.sid == playerSid:
                roomItem.playerTwoField.canShooted(coordinateData['x'],coordinateData['y'])
                roomItem.playerTwoField.printField(roomItem.playerTwoField)                        
            elif roomItem.userTwo.sid == playerSid:
                roomItem.playerOneField.canShooted(coordinateData['x'],coordinateData['y'])
                roomItem.playerOneField.printField(roomItem.playerOneField)                        
    
    def deleteRoom(self, roomIndex):
        roomLink = None
        if self.roomList[roomIndex].userOne.playRoom != None:
            self.roomList[roomIndex].userOne.playRoom = None
        if (self.roomList[roomIndex].userTwo != None) and (self.roomList[roomIndex].userTwo.playRoom != None):
            self.roomList[roomIndex].userTwo.playRoom = None
        roomLink = self.roomList[roomIndex].link
        self.roomList.remove(self.roomList[roomIndex])
        print('room',roomLink,'deleted successfully')
