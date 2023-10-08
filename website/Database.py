from flask import Flask
from pymongo.mongo_client import MongoClient
import requests
import json
from bson import ObjectId



Database = Flask(__name__)


uri = "mongodb+srv://NEjjjO:fuckyou69@shoby0.bcrmqu3.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)


data = client.Mindenis


user_data=data.Update_Data

fire = data.Minden

fire_kicsi = data.Minden #rovid

fire = data.EarthData24H

def GetSpecData():
    print([fire for fire in user_data.find({"acq_date": "2023-10-07"})])


def GetDataFromDb():
    list = []
    for fires in user_data.find():
        list.append(fires)
    return list

