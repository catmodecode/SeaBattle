from classes.User import User

class UserManager:
    userList = []

    def addUser(self, User):
        self.userList.append(User)
        print(User.name,' user added')

    def getBySid(self, sid):
        return self.userList.index(next((user for user in self.userList if user.sid == sid), None)) 

    def getList(self):
        return(self.userList)
    
    def removeUser(self,sid):
        leaveUser = next((user for user in self.userList if user.sid == sid), None)
        self.userList.remove(next((user for user in self.userList if user.sid == sid), None))
        print(leaveUser.name,'user removed')
