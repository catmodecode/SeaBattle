from classes.Cell import Cell
from classes.Ship import Ship

class Field:
    def __init__(self):
        self.seaField = []
        for x in range(10):
            self.seaField.append([Cell() for y in range(10)])

    shipList = []
    lives = 0

    def setShipList(self, clientShipList):
        self.shipList = []
        for ship in range(len(clientShipList)):
            self.shipList.append(Ship())
            self.shipList[ship].type = clientShipList[ship]['type']
            self.shipList[ship].size = clientShipList[ship]['size']
            self.shipList[ship].direction = clientShipList[ship]['direction']
            self.shipList[ship].coordinate = clientShipList[ship]['position']
            self.shipList[ship].hp = self.shipList[ship].size
        self.lives = 10
    
    def printField(self,field):
        print('')
        for y in range(10):
            for x in range(10):
                if field.seaField[x][y].status == 'empty':
                    print('O', end = ' ')
                elif field.seaField[x][y].status == 'ship':
                    print('S', end = ' ')
                elif field.seaField[x][y].status == 'hit':
                    print('-', end = ' ')
                elif field.seaField[x][y].status == 'destroyed':
                    print('X', end = ' ')
                elif field.seaField[x][y].status == 'miss':
                    print('M', end = ' ')
            print('')

    def shotStatusReturn(self,shotX,shotY):
        return self.seaField[shotX][shotY].status

    def canShooted(self,shotX,shotY):
        result = None
        for shipItem in self.shipList:
            shipX = shipItem.coordinate['x']
            shipY = shipItem.coordinate['y']
            if shipItem.direction:
                if shotY == shipY and shipX <= shotX <= shipItem.size + shipX:
                    if self.seaField[shotX][shotY].status == 'ship':
                        self.seaField[shotX][shotY].status = 'hit'
                        result = 'hit'
                        shipItem.hp -= 1
                        if shipItem.hp <= 0:
                            self.lives -= 1
                            for counter in range(shipItem.size):
                                self.seaField[shipX + counter][shipY].status = 'destroyed'
                elif self.seaField[shotX][shotY].status == 'empty':
                    self.seaField[shotX][shotY].status = 'miss'
                    result = 'miss'
            else:
                if shotX == shipX and shipY <= shotY <= shipItem.size + shipY:
                    if self.seaField[shotX][shotY].status == 'ship':
                        self.seaField[shotX][shotY].status = 'hit'
                        result = 'hit'
                        shipItem.hp -= 1
                        if shipItem.hp <= 0:
                            self.lives -= 1
                            for counter in range(shipItem.size):
                                self.seaField[shipX][shipY + counter].status = 'destroyed'
                elif self.seaField[shotX][shotY].status == 'empty':
                    self.seaField[shotX][shotY].status = 'miss'
                    result = 'miss'
        return result