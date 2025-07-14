import requests
import pprint  # ✅ Import pprint module

url = "http://api.weatherapi.com/v1/forecast.json"
params = {
    "key": "60fda9d80d334460898190135252706",
    "q": "10001",         # location
    "days": "2"           # number of days to get forecast for
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    
    # ✅ Use pprint to explore the full data structure
    pprint.pprint(data,depth=2)

else:
    print("Error", response.status_code, response.text)