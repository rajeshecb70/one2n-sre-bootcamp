from . import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(100), nullable=False) # New field Added
   # address = db.Column(db.String(100), nullable=True) # New field Added

    
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

