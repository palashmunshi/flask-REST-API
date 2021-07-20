from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
# import sqlite3 
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()                            
    parser.add_argument(                                             
        "price",
        type=float,
        required= True,
        help="this field cannot be left blank."
    )

    parser.add_argument(                                             
        "store_id",
        type=int,
        required= True,
        help="Every Item needs a store id."
    )


    @jwt_required()
    def get(self, name):

        item = ItemModel.findByName(name)
        if item:
            return item.json()
        return {'message':'item not found.'}, 404

    def post(self, name):
            
        if ItemModel.findByName(name):
            return {'message': "an item with name '{}' already exists.".format(name)}, 404
        
        data = Item.parser.parse_args()
        
        # item = {"name":name, "price": data["price"]}# this was used before we had the item model.
        #now that we have an item model we'll use the below code
        # item = ItemModel(name, data['price'], data['store_id'])
        #or
        item = ItemModel(name, **data)
        try:
            item.save_to_db()
        except Exception as e:
            print('erroe sdf:',e)
            return {'message': 'an error has ocurred in inserting item'}, 500  #this code will try to insert the item but if any error comes up, it will show this message
        
        return item.json(), 201
        
    def delete(self, name):

        # connection = sqlite3.connect('mydata.db') # this method is not reqwuired as the item model is deleting the items.
        # cursor = connection.cursor()

        # query = "DELETE FROM items WHERE name=?"

        # cursor.execute(query, (name, ))
        # connection.commit()
        # connection.close()

        # return {"message": "item deleted"}

        item = ItemModel.findByName(name)
        if item:
            item.delete_from_db()
        
            return {'message': 'Item has been deleted'} 
        
        return {"message": "This item does not exist in the table"}
    

    def put(self, name):
        
        data = Item.parser.parse_args()
        item = ItemModel.findByName(name) 
        # updated_item = {'name':name , 'price':data['price']}  this was used before we had the item model.
        #now that we have an item model we'll use the below code
        # updated_item = ItemModel(name, data['price'])
        
        if item==None:

            # item = ItemModel(name, data['price'], data['store_id'])
            #or
            item = ItemModel(name, **data)

            # try:
            #     # ItemModel.insert(updated_item)
            #     updated_item.save_to_db() #coz we have the item model
            # except:
            #     return {'message': 'an error has ocurred while inserting'}, 500
        else:
            item.price = data['price']
            # try:
                # ItemModel.update(updated_item)
            #     updated_item.update()
            # except:
            #     return {'message': 'an error has ocurred while udating the item'}, 500
        item.save_to_db()
        
        return item.json()
    
    
class ItemsList(Resource):
    def get(self):
        
        return {"items" : [item.json() for item in ItemModel.find_all()]} #we could also use lamba funtion like below
        # return {"items": list(map(lambda x: x.json(), ItemModel.query.all()))}

        
        # connection = sqlite3.connect('mydata.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM items"

        # result = cursor.execute(query)
        # items=[]
        # for row in result:
        #     items.append({'name':row[0] , 'price':row[1]})
        
        # connection.close()

        # return {'items': items}