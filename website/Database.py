from flask import Flask, render_template
from pymongo.mongo_client import MongoClient
import requests

from website.auth import *

Database = Flask(__name__)


uri = "mongodb+srv://NEjjjO:fuckyou69@shoby0.bcrmqu3.mongodb.net/?retryWrites=true&w=majority"


client = MongoClient(uri)


data = client.Mindenis

news = client.Mindenis.test


user_data=data.Update_Data

fire = data.Minden

fire_kicsi = data.Minden #rovid

fires = data.EarthData24H




def GetSpecData():
    print([fire for fire in user_data.find({"acq_date": "2023-10-07"})])

@Database.route('/GetDataFromApi/')
def GetDataFromApi():
    print("databazeben")

    url = "https://bing-news-search1.p.rapidapi.com/news/search"

    querystring = {"q":"wildfire","safeSearch":"Off","textFormat":"Raw","freshness":"Day"}

    headers = {
        "X-BingApis-SDK": "true",
        "X-RapidAPI-Key": "d200955f50msh92a2f4a24776d7ap18f706jsn899c4532cd92",
        "X-RapidAPI-Host": "bing-news-search1.p.rapidapi.com"
    }
    print("hol vagy")
    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())



def GetNewsFromDb():
    list = []
    for new in news.find():
        list.append(new)
    return list


def GetDataFromDb():
    list = []
    for fires in user_data.find():
        list.append(fires)
    return list

