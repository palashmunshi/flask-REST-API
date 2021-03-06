import os

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from resources.user import UserRegister, User
from resources.item import Item, ItemsList
from resources.store import Store, StoreList
from db import db

app = Flask(__name__)

db_url = os.environ.get('DATABASE_URL')

app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("://", "ql://", 1)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///mydata.db')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['PROPAGATE_EXCEPTIONS']=  True  #this will allow flask extensions to retrun error. without this it will return 500 error code just saying internal server error....very annoying.
app.secret_key = 'palash'   
api= Api(app)



jwt = JWT(app, authenticate, identity)  


api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(ItemsList, '/items' )
api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')


if __name__ == '__main__':    
    db.init_app(app)
    app.run(port=5000, debug=True)

    
    

