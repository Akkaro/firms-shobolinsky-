from pymongo.mongo_client import MongoClient
from pymongo import MongoClient
import csv
from mapping_tools.create_map import *
from datetime import datetime

# Let's set your map key that was emailed to you. It should look something like 'abcdef1234567890abcdef1234567890'
MAP_KEY = 'b5b8459b6dd404d86ff6370540ec4fd7'
#MAP_KEY = 'abcdef1234567890abcdef1234567890'


uri = "mongodb+srv://NEjjjO:fuckyou69@shoby0.bcrmqu3.mongodb.net/?retryWrites=true&w=majority"

'''
# Let's see last four days MODIS data for Peru
peru_url = 'https://firms.modaps.eosdis.nasa.gov/api/country/csv/' + MAP_KEY + '/MODIS_NRT/ROU/1'

df_peru = pd.read_csv(peru_url)

header = ['country_id', 'latitude', 'longitude', 'country_id', 'latitude', 'longitude', 'brightness', 'scan', 'track', 'acq_date', 'acq_time', 'satellite', 'instrument', 'confidence',	'version', 'bright_t31', 'frp',	'daynight']
df_peru.to_csv('my.csv')
csvFile = open('my.csv', 'r')
reader = csv.DictReader(csvFile)

for each in reader:
    row = {}
    for field in header:
        row[field] = each[field]
    db.Update_Data.insert_one(row)
 
#fire.insert_one(peru_url)
print(df_peru)
'''
def add_user_report():
  mongoClient = MongoClient(uri)
  db = mongoClient.Mindenis
  Update_Data = db.Update_Data
  header = ['country_id', 'latitude', 'longitude', 'brightness', 'scan', 'track', 'acq_date', 'acq_time', 'satellite', 'instrument', 'confidence',	'version', 'bright_t31', 'frp',	'daynight']
  
  longitude,latitude,CountryID = get_coordinates_and_country(get_ip())
  each = str(CountryID) + "," + str(longitude) + "," + str(latitude)
 
  now = datetime.now()

  current_time = now.strftime("%H:%M:%S")

  current_date = now.strftime("%H:%M:%S")

  sample_dict = {
    "country_id": str(CountryID),
    "latitude": str(latitude),
    "longitude": str(longitude),
    "acq_date": str(current_date),
    "acq_time": str(current_time)
  }

  db.Update_Data.insert_one(sample_dict)
  
  print("belepettttttttttttttttttttttttttttttttttttttttttt")
  
