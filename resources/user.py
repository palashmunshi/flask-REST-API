from models.user import UsersModel
import sqlite3
from sqlite3.dbapi2 import Cursor
from flask_restful import Resource, reqparse


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help='this field cannot be empty'
    )
    
    
    parser.add_argument('password',
        type=str,
        required=True,
        help='this field cannot be empty'
    )



    def post(self):
        data = UserRegister.parser.parse_args()

        if UsersModel.findByUsername(data['username']):
            return {'message': 'username already exists.'}, 400

        ## connection = sqlite3.connect('mydata.db')
        ## cursor = connection.cursor()


        ## query = "INSERT INTO users VALUES (NULL,?,?)"
        ## cursor.execute(query, (data['username'], data['password']))


        ## connection.commit()
        ## connection.close()

        # user = UsersModel(data['username', data['password']])
        #or
        user = UsersModel(**data) # this will take the arguments as a dictionary whit username:value, password:value and this value is given in the data parser
        user.save_to_db()
        

        return {'message': 'User created successfuly'}, 201