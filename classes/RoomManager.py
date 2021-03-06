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
        itemField = None
        for roomItem in self.roomList:
            if roomItem.userOne.sid == playerSid:
                itemField = roomItem.playerOneField
                roomItem.userOne.ready = True
                if roomItem.userTwo:
                    if roomItem.userTwo.ready:
                        roomItem.userOne.turn = True
            elif roomItem.userTwo.sid == playerSid:
                itemField = roomItem.playerTwoField
                roomItem.userTwo.ready = True
                if roomItem.userOne.ready:
                    roomItem.userOne.turn = True
            itemField.setShipList(shipData)
            for shipItem in itemField.shipList:
                if shipItem.canShipPlaced(itemField):
                    shipItem.shipPlacing(itemField)
                else:
                    return ('failure')
            itemField.printField(itemField)
        return('succesful')

    def heavenOrHell(self,player,playerField):
        if playerField.lives <= 0:
            player.live = False
            return ('Hell')
        else:
            return('Heaven')
        
    def shotAtCoordinate(self,playerSid,cData):
        itemField = None
        result = None
        roomIndex = -1
        for roomItem in self.roomList:
            roomIndex += 1
            if roomItem.userOne.sid == playerSid:
                itemField = roomItem.playerTwoField
                if roomItem.userOne.turn != True:
                    return ('Fail')
                else:
                    result = itemField.canShooted(cData['x'],cData['y'])
                    if result == 'miss':
                        roomItem.userOne.turn = False
                        roomItem.userTwo.turn = True  
                itemField.printField(roomItem.playerTwoField)
                if self.heavenOrHell(roomItem.userTwo,itemField) == 'Hell':
                    result = 'Player One Win'
            elif roomItem.userTwo.sid == playerSid:
                itemField = roomItem.playerOneField
                if roomItem.userTwo.turn != True:
                    return ('Fail')
                else:
                    result = itemField.canShooted(cData['x'],cData['y'])
                    if result == 'miss':
                        roomItem.userOne.turn = True
                        roomItem.userTwo.turn = False  
                itemField.printField(roomItem.playerOneField)
                if self.heavenOrHell(roomItem.userTwo,itemField) == 'Hell':
                    result = 'Player Two Win'
            return result
    
    def deleteRoom(self, roomIndex):
        roomLink = None
        if self.roomList[roomIndex].userOne.playRoom != None:
            self.roomList[roomIndex].userOne.playRoom = None
        if (self.roomList[roomIndex].userTwo != None) and (self.roomList[roomIndex].userTwo.playRoom != None):
            self.roomList[roomIndex].userTwo.playRoom = None
        roomLink = self.roomList[roomIndex].link
        self.roomList.remove(self.roomList[roomIndex])
        print('room',roomLink,'deleted successfully')
