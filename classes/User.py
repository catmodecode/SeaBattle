class User:   
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name
    
    def setName(self, name):
        self.name = name
        
    def get(self):
        return({'name':self.name,'sid':self.sid})