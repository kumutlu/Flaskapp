from flask import jsonify
from dict import names

def addNameEntry(name, value):
  print(name, value)
  names[name] = value
  print(names)
  return jsonify(result=names)

def delete_entry(key):
    print(key)
    if key in names:
        del names[key]
        return jsonify(names=names)
    else:
        return ("Please enter a valid key")

def update_key_value(key, value):
    print(key, value)
    if key in names:
        names[key] = value
        return jsonify(names=names)
    else:
        return ("Please enter a valid key")