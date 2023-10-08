import plotly.express as px
import pandas as pd
import sqlite3
from mapping_tools.create_map import get_csv


data = get_csv()
for i in range(0,len(data)):
    try:

        fig = px.scatter_mapbox(data.iloc[i],
                            lon = data.iloc[i]['longitude'],
                            lat = data.iloc[i]['latitude'],
                            zoom = 5,
                            color = data.iloc[i]['bright_t31'],
                            size = data.iloc[i]['frp'],
                            width = 900,
                            height = 600,
                            title = 'NSW Wildland Fire Apr 2022'
                            )
        fig.update_layout(mapbox_style = "open-street-map")
        fig.update_layout(margin = {"r":0,"t":50,"l":0,"b":10})
        fig.write_html('myfiremap.html')
        print('plot complete..')
    except Exception as e:
        print(e)
    finally:
        if cnn:
            cnn.close()
            print('connection closed..')
    print('done.')
