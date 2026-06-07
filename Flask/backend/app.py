from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

MONGO_URL = os.getenv('MONGO_URL')

client = pymongo.MongoClient(MONGO_URL)

db = client.test

collection = db['flask-tutorial']

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    formData = dict(request.json)
    collection.insert_one(formData)
    return "Success"

@app.route('/view')
def view():
    data = collection.find()
    data = list(data)
    for item in data:
        print(item)
        del item['_id']

    data = {
        'data': data
    }
    return jsonify(data)
 
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=9000)