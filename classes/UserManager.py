from User import User

class UserManager:
    userList = []

    def addUser(self, User):
        self.userList.append(User)

    def getList(self):
        return(self.userList)
    
    def removeUser(self,sid):
        self.userList.remove(next((user for user in self.userList if user.sid == sid), None))

pepe = User('12','lalka')
lalka = User('11','pepe')

pepeList = UserManager()
pepeList.addUser(pepe)
pepeList.addUser(lalka)

print(pepeList.getList())

pepeList.removeUser('12')

print(pepeList.getList())


