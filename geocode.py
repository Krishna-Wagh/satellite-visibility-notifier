# geocode.py
from opencage.geocoder import OpenCageGeocode
import os
from dotenv import load_dotenv

load_dotenv()

GEOCODER_KEY = os.getenv("OPENCAGE_API_KEY")
geocoder = OpenCageGeocode(GEOCODER_KEY)

def get_coordinates(city_name):
    results = geocoder.geocode(city_name)
    if results and len(results):
        lat = results[0]['geometry']['lat']
        lon = results[0]['geometry']['lng']
        return lat, lon
    else:
        print("City not found.")
        return None, None
