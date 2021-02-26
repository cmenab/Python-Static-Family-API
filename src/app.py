"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, json
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Traer a todos los miembros
@app.route('/members', methods=['GET'])
def get_members():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "family": members
    }
    return jsonify(response_body), 200

# Trae un solo miembro según parametro en la URL
@app.route('/members/<int:position>', methods=['GET'])
def get_member(position):
    member = jackson_family.get_member(position)
    response_body = {
        "family": member
    }
    return jsonify(response_body), 200

# Agrega un miembro a la biblioteca
@app.route('/members', methods=['POST'])
def add_member():
    request_body = request.data
    decoded_object = json.loads(request_body)
    result = jackson_family.add_member(decoded_object)
    if result == True:
        print("Incoming request with the following body", request_body)
        return jsonify(jackson_family.get_all_members()),200
    else:
        return "Error",500

# Borra un miembro de la biblioteca según parametro
@app.route('/members/<int:position>', methods=['DELETE'])
def delete_member(position):
    if type(position) != int:
        return jsonify(jackson_family.get_all_members()),400
    else: 
        result = jackson_family.delete_member(position)
        if result == True:
            print("This is the position to delete: ",position)
            return jsonify(jackson_family.get_all_members()),200
        else:
            return "Error",500
    

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
