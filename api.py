from models import app, Message
from flask import jsonify, request
from crud.message_crud import get_all_messages, create_message, get_message, update_message, delete_message

@app.route('/')
def home():
  return f"Welcome Home"

@app.route('/users', methods=['GET', 'POST'])
def user_index_create():
  if request.method == 'GET':
    return get_all_users()
  else:
    return jsonify(message='route coming soon')

@app.route('/messages', methods=['GET', 'POST'])
def message_index_create():
    if request.method == 'GET':
        return get_all_messages()
    if request.method == 'POST':
        return create_message(name=request.form['name'], messages=request.form['messages'], quantity=request.form['quantity'])
@app.route('/messages/<id>', methods=['GET', 'PUT', 'DELETE'])
def message_show_put_delete(id):
    if request.method == 'GET':
        return get_user(id)
    if request.method == 'PUT':
        return get_message(id)
    if request.method == 'DELETE':
        return delete_message(id)