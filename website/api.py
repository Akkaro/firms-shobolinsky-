from pymongo.mongo_client import MongoClient
from pymongo import MongoClient
import csv
from mapping_tools.create_map import *

# Let's set your map key that was emailed to you. It should look something like 'abcdef1234567890abcdef1234567890'
MAP_KEY = 'b5b8459b6dd404d86ff6370540ec4fd7'
#MAP_KEY = 'abcdef1234567890abcdef1234567890'


uri = "mongodb+srv://NEjjjO:fuckyou69@shoby0.bcrmqu3.mongodb.net/?retryWrites=true&w=majority"

mongoClient = MongoClient(uri)
db = mongoClient.Mindenis
Update_Data = db.Update_Data
  
#client = MongoClient(uri)

#db = client.Mindenis

#fire = db.Update_Data

mongoClient = MongoClient(uri)
db = mongoClient.Mindenis
Update_Data = db.Update_Data



# now let's check how many transactions we have
import pandas as pd
url = 'https://firms.modaps.eosdis.nasa.gov/mapserver/mapkey_status/?MAP_KEY=' + MAP_KEY
try:
  df = pd.read_json(url,  typ='series')
  print(df)
except:
  # possible error, wrong MAP_KEY value, check for extra quotes, missing letters
  print ("There is an issue with the query. \nTry in your browser: %s" % url)
  
def get_transaction_count() :
  count = 0
  try:
    df = pd.read_json(url,  typ='series')
    count = df['current_transactions']
  except:
    print ("Error in our call.")
  return count

tcount = get_transaction_count()
print ('Our current transaction count is %i' % tcount)

da_url = 'https://firms.modaps.eosdis.nasa.gov/api/data_availability/csv/' + MAP_KEY + '/all'
df = pd.read_csv(da_url)
print(df)

# now let's see how many transactions we use by querying this end point

start_count = get_transaction_count()
pd.read_csv(da_url)
end_count = get_transaction_count()
print ('We used %i transactions.' % (end_count-start_count))

# now remember, after 10 minutes this will reset


# in this example let's look at VIIRS NOAA-20, entire world and the most recent day
area_url = 'https://firms.modaps.eosdis.nasa.gov/api/area/csv/' + MAP_KEY + '/VIIRS_NOAA20_NRT/world/1'
start_count = get_transaction_count()
df_area = pd.read_csv(area_url)
end_count = get_transaction_count()
print ('We used %i transactions.' % (end_count-start_count))

df_area

# We can also focus on a smaller area ex. South Asia and get the last 3 days of records
area_url = 'https://firms.modaps.eosdis.nasa.gov/api/area/csv/' + MAP_KEY + '/VIIRS_NOAA20_NRT/54,5.5,102,40/3'
df_area = pd.read_csv(area_url)
df_area

# We can also focus on smaller area ex. South Asia and get last 3 days of records
countries_url = 'https://firms.modaps.eosdis.nasa.gov/api/countries'
df_countries = pd.read_csv(countries_url, sep=';')
df_countries

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

def add_user_report():
  mongoClient = MongoClient(uri)
  db = mongoClient.Mindenis
  Update_Data = db.Update_Data
  header = ['country_id', 'latitude', 'longitude', 'country_id', 'latitude', 'longitude', 'brightness', 'scan', 'track', 'acq_date', 'acq_time', 'satellite', 'instrument', 'confidence',	'version', 'bright_t31', 'frp',	'daynight']
  
  each = "1," + "orszag," + "longitude," + "latitude," + "brightness"
  
  for field in header:
        row[field] = each[field]
  db.Update_Data.insert_one(row)
  
