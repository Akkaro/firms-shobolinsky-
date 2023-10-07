import pandas as pd
import folium
import socket
import json
import requests
def get_ip():
    hostname=socket.gethostname()
    ip_address=socket.gethostbyname(hostname)
    return ip_address

def get_country_by_ip(ip_address):
    IP_API_KEY="7f54f175091db8e4a3709720392a8c76"
    data=f"http://api.ipstack.com/{ip_address}?access_key = 7f54f175091db8e4a3709720392a8c76"
    response=requests.get(f"http://api.ipstack.com/172.28.160.1?access_key = 7f54f175091db8e4a3709720392a8c76")
    # response=requests.get(f"http://api.ipstack.com/{ip_address}",params=IP_API_KEY)
    print(response.json())




def create_map(country="Romania"):
    MAP_KEY = "2ee2aefb3a335aa4a75bb6bf1fd5191f"
    # url= 'https://firms.modaps.eosdis.nasa.gov/mapserver/mapkey_status/?MAP_KEY=' + MAP_KEY

    # data_url='https://firms.modaps.eosdis.nasa.gov/api/area/csv/' + MAP_KEY + '/MODIS_NRT/world/1'
    # data=pd.read_csv(data_url)
    data=pd.read_csv("modis_2022_Afghanistan.csv")

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
        folium.Marker(
            location=[data.iloc[i]['latitude'],data.iloc[i]['longitude']],popup=popup).add_to(n)
    n.show_in_browser()

get_country_by_ip(get_ip())
create_map()


