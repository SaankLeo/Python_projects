import requests


url="http://api.weatherapi.com/v1/forecast.json"

params={
    "key":"60fda9d80d334460898190135252706",
    "q":"10001",
    "days": "2"
}

response=requests.get(url,params=params)

if response.status_code==200:
    data=response.json()
    forecast_days=data["forecast"]["forecastday"]

    for day in forecast_days:
        date=day['date']
        avg_temp=day['day']['avgtemp_c']
        max_temp = day['day']['maxtemp_c']
        min_temp = day['day']['mintemp_c']

    print(f"Date: {date}")
    print(f"Avg Temp (°C): {avg_temp}")
    print(f"Max Temp (°C): {max_temp}")
    print(f"Min Temp (°C): {min_temp}")
    print("-" * 30)


else:
    print("Error",response.status_code,response.text)

