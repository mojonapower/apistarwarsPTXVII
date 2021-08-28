from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#models nos permite crear las tablas a nuestra base de datos
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #cuando dice unique=True significa que este valor no puede repetirse
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email
            # do not serialize the password, its a security breach
        }

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    nameFavorite = db.Column(db.String(30), unique= False, nullable=False)
    typeFavorite = db.Column(db.String(30), unique= False, nullable=False)
    rel = db.relationship('User')
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "nameFavorite": self.nameFavorite,
            "typeFavorite": self.typeFavorite
            # do not serialize the password, its a security breach
        }

class Personajes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique= True, nullable=False)
    homeworld = db.Column(db.String(30), unique= False, nullable=False)#FK
    age = db.Column(db.Integer)
    vehicle = db.Column(db.String(30), unique= False, nullable=False)#FK

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "homeworld": self.homeworld,
            "vehicle": self.vehicle,
            "age": self.age,
            # do not serialize the password, its a security breach
        }