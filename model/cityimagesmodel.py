import random
import http.client
import json
from urllib.parse import quote


def initCityImage():
   print("Init city image done!!!") 
        
# Return weather_data from external api
acess = "h6c7CFlXi5eFdYH5cA8HCGaQi8GhtXPlzq2w2f51k18"

def getCityImage(cityName):
    conn = http.client.HTTPSConnection("api.unsplash.com")
    payload = ''
    headers = {}
    encodedCityName = quote(cityName)
    conn.request("GET", "/search/photos?page=1&per_page=1&content_filter=high&order_by=lates&query=" + encodedCityName + "&client_id=" + acess, payload, headers)
    res = conn.getresponse()
    data = res.read()
    decodedString = data.decode("utf-8")
    j = json.loads(decodedString)
    image_url = j['results'][0]['urls']['regular']
    return image_url
   


    