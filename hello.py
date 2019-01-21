
from flask import Flask, url_for ,request
from flask import jsonify
from CRUD_funtions import addNameEntry, delete_entry, update_key_value
from dict import names

app = Flask(__name__)






@app.route('/names', methods=['GET', 'POST', 'DELETE', 'PATCH'])

def getNames():

  if request.method == 'POST':
      data = request.json
      print(data)
      print(data['newName'], data['value'])
      return addNameEntry(data['newName'], data['value'])

  elif request.method == 'GET':
      return jsonify(names=names)

  elif request.method == 'DELETE':
      data = request.json
      print(data)
      print(data['key_to_delete'])
      return delete_entry(data["key_to_delete"])

  elif request.method == 'PATCH':
      data = request.json
      print(data)
      print(data["key"], data["value"])
      return update_key_value(data["key"], data["value"])