import sqlite3
from db import db

class UsersModel(db.Model):
    
    __tablename__ = 'users' #because we are using the 'users' table to store 

    id = db.Column(db.Integer, primary_key = True) #the primary key=true means that this is unique
    username = db.Column(db.String(80)) #80 characters(max) for a username
    password = db.Column(db.String(80)) #same as above

    def __init__(self, username, password):  #we are not not using id as a parameter because it is already being auto incremented in line 8 (primary key)
         
        self.username = username
        self.password = password

    @classmethod    
    def findByUsername(cls, username):
        
        return cls.query.filter_by(username=username).first()
        
        # connetion = sqlite3.connect('mydata.db')
        # cursor = connetion.cursor()

        # query = "SELECT * FROM users WHERE username=?"      #the where clause returns only those rows with the username
        # result = cursor.execute(query, (username,))
        # row = result.fetchone()
        # if row:
        #     #user = cls(row[0], row[1], row[2]) or
        #     user = cls(*row)
        # else:
        #     user = None

        # connetion.close()
        # return user

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod    
    def findById(cls, _id):

        return cls.query.filter_by(id=_id).first()

        # connetion = sqlite3.connect('mydata.db')
        # cursor = connetion.cursor()

        # query = "SELECT * FROM users WHERE id=?"      #the where clause returns only those rows with the username
        # result = cursor.execute(query, (_id,))
        # row = result.fetchone()
        # if row:
        #     #user = cls(row[0], row[1], row[2]) or
        #     user = cls(*row)
        # else:
        #     user = None

        # connetion.close()
        # return user
