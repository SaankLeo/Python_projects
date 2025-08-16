

import requests


url="https://newsapi.org/v2/top-headlines"

params={
    "country":"us",
    "apiKey":"22449d8f25af491bb2d4a244429118b1",
    "category":"sports" ,
    }

response=requests.get(url,params=params)

posts=response.json()

for post in posts["articles"]:
    print("Title:",post["title"],post["source"],post['author'])
    



