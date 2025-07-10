import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("N2YO_API_KEY")
sat_id = 25544  # ISS (ZARYA)
lat, lon, alt = 19.054999, 72.8692035, 50  # Mumbai
seconds = 1  # get current position only

url = f"https://api.n2yo.com/rest/v1/satellite/visualpasses/25544/41.702/-76.014/0/2/300/&apiKey={API_KEY}"

print("🔧 Final URL:", url)
response = requests.get(url)

print("📡 Status Code:", response.status_code)
print("📄 Response:")
print(response.text)
