from flask_restful import Resource
from flask_sqlalchemy.model import NameMetaMixin
from models.stores import StoreModel

class Store(Resource):
    def get (self, name):
        store = StoreModel.findByName(name)
        if store:
            return store.json()
        return {"message": " store not found"}

    def post(self, name):
        if StoreModel.findByName(name):
            return {"message": "A store with name '{}' already exist".format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except Exception as e:
            return {"message": "an error has been occured while creating a store"}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.findByName(name)
        if store:
            store.delete_from_db()
            return {"message": "store has been deleted."}

        return {"message": "no such store exists as of now."}


class StoreList(Resource):
    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}