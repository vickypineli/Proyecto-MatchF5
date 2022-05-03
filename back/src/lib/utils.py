import tempfile
from flask import jsonify


def object_to_json(data):
    if isinstance(data, (list, tuple, set)):
        output = [i.to_dict() for i in data]
    else:
        output = data.to_dict()
    return jsonify(output)


def temp_file():
    return tempfile.NamedTemporaryFile().name
