from flask import jsonify
from models import Message


def get_all_messages():
    all_messages = Message.query.all()
    results = []
    for message in all_messages:
        results.append(message.as_dict())
    # results = [user.as_dict() for user in all_users]
    return jsonify(results)
def create_message(name, messages, quantity):
    new_message = Message(name=name, messages=messages, quantity=quantity)
    db.session.add(new_message)
    db.session.commit()
    return jsonify(new_message.as_dict())
def get_message(id):
    message = Message.query.get(id)
    if message:
        return jsonify(message.as_dict())
    else: 
        return jsonify(message =f'Error getting user at {id}')
def update_message(id, name, messages, quantity):
    message = Message.query.get(id)
    if message:
        message.name = name or message.name
        message.messages = messages or message.messages
        message.quantity = quantity or message.quantity
        db.session.commit()
        return jsonify(message.as_dict())
    else:
        return jsonify(message=f'No message at id {id}')
def delete_message(id):
    message = Message.query.get(id)
    if message:
        db.session.delete(user)
        db.session.commit()
        return redirect('/messages')
    else:
        return jsonify(message=f'No message at id {id}')