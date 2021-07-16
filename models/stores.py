from db import db

class StoreModel(db.Model):

    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key = True ) # now we are also creating an id for each item as well because it is good to have these in the long run
    name = db.Column(db.String(80))
        
    items = db.relationship('ItemModel', lazy='dynamic') #the lazy='dynamic means that this will not create each item as an object when we create a store i.e. it saves us time to craete stores.

    def __init__(self, name):
        self.name = name
          

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]} #whenever this method is called only then it will create each item in the store as an object.


    @classmethod
    def findByName(cls, name):

        return cls.query.filter_by(name=name).first()  #SELECT * FROM items WHERE name=name... this is what it means and the first() will give us the first item which matches the name
        # in the above line for more filters we can add the arguments in filter_by function.
 
    def save_to_db(self):   
        db.session.add(self)
        db.session.commit()  #this can not only insert but update as well. hence we dont need the insert and the update method

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()