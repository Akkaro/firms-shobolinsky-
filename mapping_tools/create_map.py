import pandas as pd
import folium
from folium.plugins import MarkerCluster
import socket
import json
import requests
from website.auth import *
import math
from datetime import date
from website.Database import *

def get_date():
    return date.today()
    
    
    
def get_coordinates_and_country(ip_address):
    region=get_region_by_ip(ip_address)
    latitude=region['latitude']
    longitude=region['longitude']
    code,region=country_code_prep(region)
    return (float)(longitude),(float)(latitude),code

def get_ip():
    url="https://checkip.amazonaws.com"
    request=requests.get(url)
    return request.text[:-1]

def get_region_by_ip(ip_address):
    IP_API_KEY="7f54f175091db8e4a3709720392a8c76"
    # data=f"http://api.ipstack.com/5.2.195.101?access_key=7f54f175091db8e4a3709720392a8c76"
    # data="http://api.ipstack.com/134.201.250.155?access_key=7f54f175091db8e4a3709720392a8c76"
    response=requests.get(f"http://api.ipstack.com/{ip_address}?access_key=7f54f175091db8e4a3709720392a8c76")
    # response = requests.get(f"http://api.ipstack.com/134.201.250.155?access_key=7f54f175091db8e4a3709720392a8c76")
    # response=requests.get(data)
    data_json=response.json()
    data=json.dumps(data_json)
    datas=json.loads(data)
    return datas
    # print(response)
    # print(response.json())



def get_csv():
    ip_address = get_ip()
    region=get_region_by_ip(ip_address)
    code,region=country_code_prep(region)
    data_url='https://firms.modaps.eosdis.nasa.gov/api/country/csv/' + MAP_KEY + '/MODIS_NRT/'+code+'/2'
    data=pd.read_csv(data_url)
    return data
    
    
def country_code_prep(region):
    MAP_KEY = "2ee2aefb3a335aa4a75bb6bf1fd5191f"
    # url= 'https://firms.modaps.eosdis.nasa.gov/mapserver/mapkey_status/?MAP_KEY=' + MAP_KEY

    # data_url='https://firms.modaps.eosdis.nasa.gov/api/area/csv/' + MAP_KEY + '/MODIS_NRT/world/1'

    # data_from_db=GetDataFromDb()
    # data_json=parse_json_2(data_from_db)
    # data=pd.read_json(data_json)


    country_boxes_trans=pd.read_json("mapping_tools/country_codes_good")
    country_boxes=country_boxes_trans.transpose()
    country_boxes_filtered=country_boxes[['alpha-2','alpha-3']]
    country_for_us=country_boxes_filtered[country_boxes_filtered['alpha-2']==region['country_code']]
    return str(country_for_us.iloc[0]['alpha-3']),region

def prepare_data(code,region):
    MAP_KEY = "2ee2aefb3a335aa4a75bb6bf1fd5191f"
    print(code)
    data_url='https://firms.modaps.eosdis.nasa.gov/api/country/csv/' + MAP_KEY + '/MODIS_NRT/'+code+'/2'

    # data_url=f"https://firms.modaps.eosdis.nasa.gov/api/area/csv/{MAP_KEY}/MODIS_NRT/{code}/1"
    db_list = GetDataFromDb()
    data=pd.read_csv(data_url)

    return data,region

def create_map(data,region):
    n=folium.Map(location=[20,0],tiles="OpenStreetMap",zoom_start=2)

    latitude_use_min=(float)(region['latitude'])-0.0002
    latitude_use_max=(float)(region['latitude'])+0.0002
    longitude_max=(float)(region['longitude'])+0.0002
    longitude_min=(float)(region['longitude'])-0.0002
    for i in range(0,len(data)):
        html2 = f"""
                            <p>Fire detected by {data.iloc[i]['instrument']}</p>
                            <ul>
                                <li>Longitude: {data.iloc[i]['longitude']}</li>
                                <li>Latitude: {data.iloc[i]['latitude']}</li>
                                <li>Detection time: {data.iloc[i]['acq_date']}</li>
                            </ul>
                            </p>
                            """
        iframe = folium.IFrame(html=html2, width=200, height=200)
        popup = folium.Popup(iframe, max_width=2650)
        m=folium.Marker(
            location=[data.iloc[i]['latitude'], data.iloc[i]['longitude']],icon=folium.Icon("red"), popup=popup)
        m.add_to(n)
        # if (region=="NA") & (data.iloc[i]['longitude'] >= -150) & (data.iloc[i]['latitude']>=40) & (data.iloc[i]['longitude']<=-49) & (data.iloc[i]['latitude']<=79):
        #     m.add_to(n)
        # elif (region=="NA") & (data.iloc[i]['longitude'] >= -180) & (data.iloc[i]['latitude']>=50) & (data.iloc[i]['longitude']<=-139) & (data.iloc[i]['latitude']<=72):
        #     m.add_to(n)
        # elif (region=="NA") & (data.iloc[i]['longitude'] >= -160.5) & (data.iloc[i]['latitude']>=17.5) & (data.iloc[i]['longitude']<=-63.8) & (data.iloc[i]['latitude']<=50):
        #     m.add_to(n)
        # elif (region=="NA") & (data.iloc[i]['longitude'] >= -119.5) & (data.iloc[i]['latitude']>=7) & (data.iloc[i]['longitude']<=-58.8) & (data.iloc[i]['latitude']<=33.5):
        #     m.add_to(n)
        # elif (region=="SA") & (data.iloc[i]['longitude'] >= -112) & (data.iloc[i]['latitude']>=60) & (data.iloc[i]['longitude']<=-26) & (data.iloc[i]['latitude']<=13):
        #     m.add_to(n)
        # elif (region == "EU") & (data.iloc[i]['longitude'] >= -26) & (data.iloc[i]['latitude'] >= 34) & (data.iloc[i]['longitude'] <= 35) & (data.iloc[i]['latitude'] <= 82):
        #     m.add_to(n)
        # elif (region == "AF") & (data.iloc[i]['longitude'] >= -27) & (data.iloc[i]['latitude'] >= -10) & (data.iloc[i]['longitude'] <= 52) & (data.iloc[i]['latitude'] <= 37.5):
        #     m.add_to(n)
        # elif (region == "AF") & (data.iloc[i]['longitude'] >= 10) & (data.iloc[i]['latitude'] >= -36) & (data.iloc[i]['longitude'] <= 58.5) & (data.iloc[i]['latitude'] <= -4):
        #     m.add_to(n)
        # elif (region=="AS") & (data.iloc[i]['longitude'] >= 26) & (data.iloc[i]['latitude'] >= 9) & (data.iloc[i]['longitude'] <= 180) & (data.iloc[i]['latitude'] <= 83.5):
        #     m.add_to(n)
        # elif (region=="AS") and (data.iloc[i]['longitude'] >= 54) and (data.iloc[i]['latitude'] >= 5.5) and (data.iloc[i]['longitude'] <= 102) and (data.iloc[i]['latitude'] <= 40):
        #     m.add_to(n)
        # elif (region=="AS") & (data.iloc[i]['longitude'] >= 88) & (data.iloc[i]['latitude'] >= -12) & (data.iloc[i]['longitude'] <= 163) & (data.iloc[i]['latitude'] <= 31):
        #     m.add_to(n)
        # elif (region=="OC") & (data.iloc[i]['longitude'] >= 110) & (data.iloc[i]['latitude'] >= -55) & (data.iloc[i]['longitude'] <= 180) & (data.iloc[i]['latitude'] <= -10):
        #     m.add_to(n)
    # n.show_in_browser()
    data_from_db=GetDataFromDb()
    data_json=parse_json_2(data_from_db)
    data=pd.read_json(data_json)
    for i in range(0,len(data)):
        html1 = f"""
                            <p>Fire detected by {data.iloc[i]['instrument']}</p>
                            <ul>
                                <li>Longitude: {data.iloc[i]['longitude']}</li>
                                <li>Latitude: {data.iloc[i]['latitude']}</li>
                                <li>Detection time: {data.iloc[i]['acq_date']}</li>
                            </ul>
                            </p>
                            <div vertical layout>
                                <div><a href="website/templates/home.html"><button>Confirm</button></a></div>
                                <div><a href="website/templates/home.html"><button>Deny</button></a></div>
                            </div>
                            """
        html2 = f"""
                            <p>Fire detected by {data.iloc[i]['instrument']}</p>
                            <ul>
                                <li>Longitude: {data.iloc[i]['longitude']}</li>
                                <li>Latitude: {data.iloc[i]['latitude']}</li>
                                <li>Detection time: {data.iloc[i]['acq_date']}</li>
                            </ul>

                            """
        if (data.iloc[i]['longitude']<= longitude_max ) & (data.iloc[i]['latitude'] <= latitude_use_max) & (data.iloc[i]['longitude']>=longitude_min) & (data.iloc[i]['latitude']>=latitude_use_min):
            iframe = folium.IFrame(html=html1, width=200, height=200)
        else:
            iframe = folium.IFrame(html=html2, width=200, height=200)
        popup = folium.Popup(iframe, max_width=2650)
        m=folium.Marker(
            location=[data.iloc[i]['latitude'], data.iloc[i]['longitude']], icon=folium.Icon("green"),popup=popup)
        m.add_to(n)

    n.save("website/templates/map.html")
