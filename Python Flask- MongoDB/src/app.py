from flask import Flask, request, jsonify,Response
from flask_pymongo import PyMongo
import pymongo
import requests
from pymongo import MongoClient
import pymongo
from bson import json_util
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["pythonflaskmongodb"]
mycol = mydb["pythonflaskdb"]

app = Flask(__name__)
@app.route('/users', methods=['POST'])
def create_user():
    URL = 'https://www.easports.com/fifa/ultimate-team/api/fut/item?page=1' #configutation of url
    # Receiving Data
    data = requests.get(URL) 
    data = data.json() 
    mycol.insert_one(data)  
    return {"databese": "created"}
    

@app.route('/users', methods=['GET'])
def get_users():
    users = mycol.find()
    response = json_util.dumps(users)
    return Response(response, mimetype="application/json")

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    print(id)
    user = mycol.find_one({'_id': ObjectId(id), })
    response = json_util.dumps(user)
    return Response(response, mimetype="application/json")

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    mycol.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'User' + id + ' Deleted Successfully'})
    response.status_code = 200
    return response

@app.route('/users/Updated', methods=['PUT'])
def update_user():
    
    URL = 'https://www.easports.com/fifa/ultimate-team/api/fut/item?page=2' #configuramos la url
    data = requests.get(URL) 
    data = data.json() 
    mycol.insert_one(data)
    response = jsonify({'message': 'database Updated Successfuly'})
    response.status_code = 200
    return response
    


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == "__main__":
    app.run(debug=True)