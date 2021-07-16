# import sqlite3  #this is no longer required
from db import db


class ItemModel(db.Model):

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key = True ) # now we are also creating an id for each item as well because it is good to have these in the long run
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2)) #up till 2 decimal places.    

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))  #foreignKey('the name of the table.column name') 
    store = db.relationship('StoreModel')
    
    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}


    @classmethod
    def findByName(cls, name):
        # connection = sqlite3.connect('mydata.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM items WHERE name=?"
        # result = cursor.execute(query, (name, ))

        # row = result.fetchone()

        # connection.close()
        # if row:
        #     # return cls(row[0], row[1])
        #     #or
        #     return cls(*row)

        return cls.query.filter_by(name=name).first()  #SELECT * FROM items WHERE name=name... this is what it means and the first() will give us the first item which matches the name
        # in the above line for more filters we can add the arguments in filter_by function.
        
    
    # def insert(self):
        
        # connection = sqlite3.connect('mydata.db')
        # cursor = connection.cursor()

        # query = "INSERT INTO items VALUES (?,?)"

        # cursor.execute(query, (self.name, self.price))

        # connection.commit()
        # connection.close()
    def save_to_db(self):   
        db.session.add(self)
        db.session.commit()  #this can not only insert but update as well. hence we dont need the insert and the update method

    
    # def update(self):
    #     connection = sqlite3.connect('mydata.db')
    #     cursor = connection.cursor()

    #     query = "UPDATE items SET price=? WHERE name=?"

    #     cursor.execute(query, (self.price, self.name))

    #     connection.commit()
    #     connection.close()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

