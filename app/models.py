from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True) 
    password_hash = db.Column(db.String(64))
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic') 

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(300))
    timestamp = db.Column(db.DateTime, index = True, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'user {self.username}'