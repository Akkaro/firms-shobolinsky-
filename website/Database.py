from flask import Flask
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests
import json
from bson import ObjectId



Database = Flask(__name__)

url = "https://eu-central-1.aws.data.mongodb-api.com/app/data-ixqoi/endpoint/data/v1/action/findOne"

payload = json.dumps({
    "collection": "listingsAndReviews",
    "database": "sample_airbnb",
    "dataSource": "Shoby0",
    "projection": {
        "_id": 3
    }
})
headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': '652125c3e7f767ae3108aa32',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

uri = "mongodb+srv://NEjjjO:fuckyou69@shoby0.bcrmqu3.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

db = client.Mindenis

fire = db.Minden

@Database.route('/Database')
def hello_world():  # put application's code here
    return 'fuck you'


def GetDataFromDb():
    list = []
    for fires in fire.find():
        list.append(fires)
    return list