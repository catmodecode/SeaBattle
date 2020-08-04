from classes.Cell import Cell
from classes.Ship import Ship

class Field:
    def __init__(self):
        self.seaField = []
        for x in range(10):
            self.seaField.append([Cell() for y in range(10)])

    shipList = []

    def setShipList(self, clientShipList):
        for ship in range(len(clientShipList)):
            self.shipList.append(Ship())
            self.shipList[ship].type = clientShipList[ship]['type']
            self.shipList[ship].size = clientShipList[ship]['size']
            self.shipList[ship].direction = clientShipList[ship]['direction']
            self.shipList[ship].coordinate = clientShipList[ship]['coordinate']
    
    def printField(self):
        for x in range(10):
            for y in range(10):
                if self.seaField[x][y].status == 'empty':
                    print('O', end = ' ')
                else:
                    print('X', end = ' ')
            print('')