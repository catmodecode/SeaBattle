from classes.User import User

class Room:
    def __init__(self, user, status):
        statusList = ['public', 'private']
        if status not in statusList:
            status = statusList[0]    
        self.status = status
        self.link = user.sid
        self.userOne = user
        self.userTwo = None

    def setUserTwo(self,user):
        self.userTwo = user
        self.status = 'full'
        print(user.name,'connected to room')

