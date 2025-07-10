
# n2yo_api.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("N2YO_API_KEY")
BASE_URL = "https://api.n2yo.com/rest/v1/satellite"

def get_satellite_passes(sat_id, lat, lon, alt=0, days=10, min_elevation=300):
    url = f"{BASE_URL}/visualpasses/{sat_id}/{lat}/{lon}/{alt}/{days}/{min_elevation}/&apiKey={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get("passes", [])
    else:
        print(f"API error: {response.status_code}")
        print("🔧 Response Text:", response.text)
        return []

