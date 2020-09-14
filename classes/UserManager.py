from classes.User import User

class UserManager:
    userList = []

    def addUser(self, User):
        self.userList.append(User)
        print(User.name,'join')

    def getBySid(self, sid):
        index = 0
        for user in self.userList:
            if user.sid == sid:
                return index
            index += 1
        index = None
        return index

    def getList(self):
        return(self.userList)
    
    def removeUser(self,sid):
        leaveUser = next((user for user in self.userList if user.sid == sid), None)
        self.userList.remove(next((user for user in self.userList if user.sid == sid), None))
        print(leaveUser.name,'left')
