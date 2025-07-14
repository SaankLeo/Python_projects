import requests

coin=input("Enter the crypto currency (eg bitcoin,etherum): ")
currency=input("Enter the currency (eg inr,usd): ")
url="https://api.coingecko.com/api/v3/simple/price"
params={"ids":coin,
        "vs_currencies":currency

}

response=requests.get(url,params=params)
data=response.json()
a=data[coin][currency]
print(f"Required coin and price: ",a)