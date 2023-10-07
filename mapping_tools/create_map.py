import pandas as pd
import folium
from folium.plugins import MarkerCluster
import socket
import json
import requests
def get_ip():
    url="https://checkip.amazonaws.com"
    request=requests.get(url)
    return request.text[:-1]

def get_country_by_ip(ip_address):
    IP_API_KEY="7f54f175091db8e4a3709720392a8c76"
    data=f"http://api.ipstack.com/{ip_address}?access_key=7f54f175091db8e4a3709720392a8c76"
    response=requests.get(f"http://api.ipstack.com/5.2.195.101?access_key=7f54f175091db8e4a3709720392a8c76")
    # response=requests.get(f"http://api.ipstack.com/{ip_address}",params=IP_API_KEY)
    # response=requests.get(data)
    print(response.json())




def create_map(country):
    MAP_KEY = "2ee2aefb3a335aa4a75bb6bf1fd5191f"
    # url= 'https://firms.modaps.eosdis.nasa.gov/mapserver/mapkey_status/?MAP_KEY=' + MAP_KEY

    data_url='https://firms.modaps.eosdis.nasa.gov/api/area/csv/' + MAP_KEY + '/MODIS_NRT/world/1'
    data=pd.read_csv(data_url)
    # data=pd.read_csv("modis_2022_Afghanistan.csv")

    n=folium.Map(location=[20,0],tiles="OpenStreetMap",zoom_start=2)
    # map_cluster_canada=MarkerCluster(name="Canada").add_to(n)
    # map_cluster_alaska = MarkerCluster(name="Alaska").add_to(n)
    # map_cluster_usa = MarkerCluster(name="USA").add_to(n)
    # map_cluster_camerica = MarkerCluster(name="Central America").add_to(n)
    # map_cluster_samerica = MarkerCluster(name="South America").add_to(n)
    # map_cluster_europe = MarkerCluster(name="Europe").add_to(n)
    # map_cluster_ncafrica = MarkerCluster(name="North and Central Africa").add_to(n)
    # map_cluster_safrica = MarkerCluster(name="South Africa").add_to(n)
    # map_cluster_rasia = MarkerCluster(name="Rusia and Asia").add_to(n)
    # map_cluster_sasia = MarkerCluster(name="South Asia").add_to(n)
    # map_cluster_seasia = MarkerCluster(name="South East Asia").add_to(n)
    # map_cluster_australia = MarkerCluster(name="Australia and New Zealand").add_to(n)

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
        # if (data.iloc[i]['longitude'] >= -150) & (data.iloc[i]['latitude']>=40) & (data.iloc[i]['longitude']<=-49) & (data.iloc[i]['latitude']<=79):
        #     map_cluster_canada.add_child(m)
        # elif (data.iloc[i]['longitude'] >= -180) & (data.iloc[i]['latitude']>=50) & (data.iloc[i]['longitude']<=-139) & (data.iloc[i]['latitude']<=72):
        #     map_cluster_alaska.add_child(m)
        # elif (data.iloc[i]['longitude'] >= -160.5) & (data.iloc[i]['latitude']>=17.5) & (data.iloc[i]['longitude']<=-63.8) & (data.iloc[i]['latitude']<=50):
        #     map_cluster_usa.add_child(m)
        # elif (data.iloc[i]['longitude'] >= -119.5) & (data.iloc[i]['latitude']>=7) & (data.iloc[i]['longitude']<=-63.8) & (data.iloc[i]['latitude']<=79):
        #     pass
    n.show_in_browser()
print(get_ip().strip())
get_country_by_ip(get_ip())


