import eventlet 
import socketio 
from classes.User import User
from classes.UserManager import UserManager
 
sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio, static_files={ 
    '/': {'content_type': 'text/html', 'filename': 'index.html'} 
}) 
 
authUsers = UserManager()

@sio.event 
def connect(sid, environ): 
    print('connect ', sid) 
 
@sio.event
def auth(sid, name):
    if next((user for user in authUsers.userList if user.sid == sid), None) == None:
        authUsers.addUser(User(sid, name))
    else:
        authUsers.userList[authUsers.getBySid(sid)].setName(name)

@sio.event 
def my_message(sid, data): 
    print('message ', data)
 
@sio.event 
def disconnect(sid): 
    authUsers.removeUser(sid)
    print('disconnect ', sid) 
 
if __name__ == '__main__': 
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
