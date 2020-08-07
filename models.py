from flask import Flask
from flask_sqlalchemy import SQLAlchemy
  
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/message'


db = SQLAlchemy(app)
class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String, unique=True, nullable=False)
  name = db.Column(db.String, nullable=False)

  messeges = db.relationship('Messege', lazy=True, back_populates='user')

  def as_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "email": self.email,
    }

  def __repr__(self):
    return f'User(id={self.id}, email="{self.email}", name="{self.name}")'

class Message(db.Model):
  __tablename__ = 'messages'
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String(150), unique=True, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'))

  user = db.relationship('User', lazy=True, back_populates='messges')

  def as_dict(self):
    return {
      "id": self.id,
      "content": self.content,
      "user_id": self.user_id,
    }

  def __repr__(self):
    return f'User(id={self.id}, email="{self.email}", display_name="{self.display_name}")'
