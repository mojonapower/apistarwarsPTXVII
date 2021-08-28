from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #cuando dice unique=True significa que este valor no puede repetirse
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email
            # do not serialize the password, its a security breach
        }

class Favorite():
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    nameFavorite = db.Column(db.String(30), unique= False, nullable=False)
    typeFavorite = db.Column(db.String(30), unique= False, nullable=False)
    rel = db.relationship('User')

    def __repr__(self):
        return '<Favorite %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "nameFavorite": self.nameFavorite,
            "typeFavorite": self.typeFavorite
            # do not serialize the password, its a security breach
        }
