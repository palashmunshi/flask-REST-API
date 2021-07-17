import os

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemsList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('postgresq1://nlzynnlfynjdbl:600f547c773abad18f700181f7d73b7e76ae92f664ad878cccbd3741a86a4053@ec2-23-20-124-77.compute-1.amazonaws.com:5432/d1m4ik4s24qcge', 'sqlite:///mydata.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.secret_key = 'palash'   
api= Api(app)



jwt = JWT(app, authenticate, identity)  


api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(ItemsList, '/items' )
api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':    
    db.init_app(app)
    
    app.run(port=5000, debug=True)

    
    

