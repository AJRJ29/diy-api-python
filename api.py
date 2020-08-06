from models import app
from flask import request

@app.route('/')
def home():
  return f"Welcome Home"

@app.route('/widgets', methods=['GET', 'POST'])
def widgets():
  if request.method == 'POST':
    return f"Hello Widgets"
  else:
    return "this is the get route"

@app.route('/widgets/:id')
def create_widgets():
  return f"Creating widgets"


@app.route('/widgets/:id', methods=['GET', 'PUT'])
def widgets():
  if request.method == 'PUT':
    return f"Update Widgets"
  else:
    return "this is the get route"

@app.route('/widgets/:id', methods=['GET', 'DELETE'])
def widgets():
  if request.method == 'DELETE':
    return f"Delete Widgets"
  else:
    return "this is the get route"