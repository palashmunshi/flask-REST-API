from models.user import UsersModel

users = [
    UsersModel('palash', 'hsalap')
]

def authenticate(username, password):
    user = UsersModel.findByUsername(username) #return none if no such user is found
    if user and user.password==password:
        return user

def identity(payload):
    user_id = payload['identity']
    return UsersModel.findById(user_id)