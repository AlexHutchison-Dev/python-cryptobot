import sqlite3
import requests
import json


#Kralen trading api
API_url='https://demo-futures.kraken.com/derivatives/api/v3/tickers'


# SQLite3 database connection
db = sqlite3.connect("BTCCAD.db")

r = requests.get(API_url)
content_json = r.json().items
# content_text = r.text()
# content_content = r.content()

print(json.loads(r))

print("Responce from kraken demo server:")
for key, value in content_json:
    print(key, ":", value, "\n")
    print("     |||         ")
