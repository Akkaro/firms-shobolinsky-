from flask import Flask, render_template
from pymongo.mongo_client import MongoClient
import requests
import pandas as pd

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

    response = requests.get(url, headers=headers, params=querystring)

    addToDatabase(response)

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


def addToDatabase(news_json):
    header = ['_type', 'name', 'url', 'image', '_type', 'thumbnail', '_type', 'contentUrl', 'width', 'height', 'description', 'provider', 'datePublished']

    sure_json = news_json.json()
    df = pd.read_json(sure_json)

    for each in df:
        row = {}
        for field in header:
            row[field] = each[field]
        data.test.insert_one(row)


'''image	
_type	"ImageObject"
thumbnail	
_type	"ImageObject"
contentUrl	"https://www.bing.com/th?id=OVFT.aSCK8kFAXFx4eYkNn3HrEy&pid=News"
width	700
height	466
description	"As the extreme weather of climate change makes destructive summers like this year's more and more likely, the province’s independent forests watchdog is calling for radical action to make our landscapes more resistant to fire."
provider	
0	
_type	"Organization"
name	"cbc.ca on MSN.com"
image	
_type	"ImageObject"
thumbnail	
_type	"ImageObject"
contentUrl	"https://www.bing.com/th?id=ODF.4NbuPrmIxu0JD126LE1gxQ&pid=news"
datePublished	"2023-10-07T08:00:00.0000000Z"
'''