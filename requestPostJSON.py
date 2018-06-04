import requests
import simplejson as json

url = "https://www.googleapis.com/urlshortener/v1/url"
payload = {"longUrl": "http://www.google.com/"}
headers = {
    "Content-Type": "application/json"
    }
r = requests.post(url, json=payload, headers=headers)

print(json.loads(r.text)["error"]["code"])
