class Ship:
    direction = True
    size = 0
    hp = 0
    type = None
    coordinate = {'x':0,'y':0}

    def canShipPlaced(self,field):
        canPlaced = True
        upBorderX = self.coordinate['x'] - 1
        if upBorderX < 0:
            upBorderX = 0
        elif upBorderX > 9:
            upBorderX = 9
        upBorderY = self.coordinate['y'] - 1
        if upBorderY < 0:
            upBorderY = 0
        elif upBorderY > 9:
            upBorderY = 9
        if self.direction == True:
            downBorderY = self.coordinate['y'] + 1
            if downBorderY < 0:
                downBorderY = 0
            elif downBorderY > 9:
                downBorderY = 9
            downBorderX = self.coordinate['x'] + self.size
            if downBorderX < 0:
                downBorderX = 0
            elif downBorderX > 9:
                downBorderX = 9
        else:
            downBorderX = self.coordinate['x'] + 1
            if downBorderX < 0:
                downBorderX = 0
            elif downBorderX > 9:
                downBorderX = 9
            downBorderY = self.coordinate['y'] + self.size
            if downBorderY < 0:
                downBorderY = 0
            elif downBorderY > 9:
                downBorderY = 9
        for shipX in range(upBorderX,downBorderX+1):
            for shipY in range(upBorderY,downBorderY+1):
                if field.seaField[shipX][shipY].status == 'empty':
                    canPlaced = canPlaced
                else:
                    canPlaced = False
        return canPlaced
    
    def shipPlacing(self,field):
        if self.direction == True:
            for shipPLace in range(self.size):
                field.seaField[self.coordinate['x'] + shipPLace][self.coordinate['y']].status = 'ship'
        else:
            for shipPLace in range(self.size):
                field.seaField[self.coordinate['x']][self.coordinate['y'] + shipPLace].status = 'ship'
    
