from flask import Flask
from flask_sqlalchemy import SQLAlchemy
  
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/flasql'
app.config['FLASK_ENV'] = 'development'
app.config['FLASK_APP'] = 'api.py'

db = SQLAlchemy(app)
class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String, unique=True, nullable=False)
  name = db.Column(db.String, nullable=False)

  messeges = db.relationship('Post', lazy=True, back_populates='user')

  def as_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "email": self.email,
    }

  def __repr__(self):
    return f'User(id={self.id}, email="{self.email}", name="{self.name}")'

class Messege(db.Model):
  __tablename__ = 'messeges'
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String(150), unique=True, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'))

  user = db.relationship('User', lazy=True, back_populates='messeges')

  def __repr__(self):
    return f'User(id={self.id}, email="{self.email}", display_name="{self.display_name}")'
