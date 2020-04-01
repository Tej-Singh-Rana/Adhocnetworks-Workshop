# importing module
import urllib.request
import json
# tracking ip addr with help of geolocation
with urllib.request.urlopen("https://geolocation-db.com/json") as url:
    data = json.loads(url.read().decode())  # print details city,state,country
    key = list(data.keys())             # print the key data
    value = list(data.values())       # print the value data
    track = value[key.index("IPv4")]
    print(track)
