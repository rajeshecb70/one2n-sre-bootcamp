from . import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.Integer, nullable=False) 
    gender = db.Column(db.String(100), nullable=False)
    #address = db.Column(db.String(100), nullable=True) #  field removed

    
    def __init__(self, name, age, phone_number, gender, address):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.gender = gender
     #   self.address = address