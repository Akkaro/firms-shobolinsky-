import pandas as pd
import folium
from folium.plugins import MarkerCluster
import socket
import json
import requests
from website.auth import *

def get_ip():
    url="https://checkip.amazonaws.com"
    request=requests.get(url)
    return request.text[:-1]

def get_region_by_ip(ip_address):
    IP_API_KEY="7f54f175091db8e4a3709720392a8c76"
    data=f"http://api.ipstack.com/{ip_address}?access_key=7f54f175091db8e4a3709720392a8c76"
    response=requests.get(f"http://api.ipstack.com/5.2.195.101?access_key=7f54f175091db8e4a3709720392a8c76")
    # response=requests.get(f"http://api.ipstack.com/{ip_address}",params=IP_API_KEY)
    # response=requests.get(data)
    data_json=response.json()
    data=json.dumps(data_json)
    datas=json.loads(data)
    return datas['country_code']
    # print(response)
    # print(response.json())




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
    country_for_us=country_boxes_filtered[country_boxes_filtered['alpha-2']==region]
    return str(country_for_us.iloc[0]['alpha-3'])

def prepare_data(code):
    MAP_KEY = "2ee2aefb3a335aa4a75bb6bf1fd5191f"
    print(code)
    data_url='https://firms.modaps.eosdis.nasa.gov/api/country/csv/' + MAP_KEY + '/MODIS_NRT/'+code+'/2'

    # data_url=f"https://firms.modaps.eosdis.nasa.gov/api/area/csv/{MAP_KEY}/MODIS_NRT/{code}/1"
    data=pd.read_csv(data_url)
    print(data)
    return data

def create_map(data):
    n=folium.Map(location=[20,0],tiles="OpenStreetMap",zoom_start=2)
    for i in range(0,len(data)):
        html = f"""
                <p>You can use any html here! Let's do a list:</p>
                <ul>
                    <li>Item 1</li>
                    <li>Item 2</li>
                </ul>
                </p>
                <p>And that's a <a href="https://www.python-graph-gallery.com">link</a></p>
                """
        iframe = folium.IFrame(html=html, width=100, height=100)
        popup = folium.Popup(iframe, max_width=2650)
        m=folium.Marker(
            location=[data.iloc[i]['latitude'], data.iloc[i]['longitude']], popup=popup)
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
    n.save("website/templates/map.html")