import random
import http.client
import json
from urllib.parse import quote

weather_data = []


# Initialize jokes
def initWeather():
    weather_data = []
        
# Return weather_data from external api


def getWeatherAPIData(weather):
    conn = http.client.HTTPSConnection("api.weatherapi.com")
    payload = ''
    headers = {}
    encodedWeather = quote(weather)
    conn.request("GET", "/v1/current.json?key=a4b8eb5455a44c2e921174419231610&q=" + encodedWeather +"&aqi=no", payload, headers)
    res = conn.getresponse()
    data = res.read()
    decodedString = data.decode("utf-8")
    j = json.loads(decodedString)
    temp_f= j['current']["feelslike_f"]
    weatherIcon_url = ""
    if temp_f<=60:
        weatherIcon_url= "http://localhost:8531/static/assets/cloud_clipart.png"
    elif temp_f < 70 and temp_f>60:
        weatherIcon_url= "http://localhost:8531/static/assets/partly_sunny.png"
    else:
        weatherIcon_url= "http://localhost:8531/static/assets/sunny_weather.png"
    print(weatherIcon_url)
    j['current']['weatherIcon_url'] = weatherIcon_url
    return j

# Test Joke Model
if __name__ == "__main__": 
    initWeather()  # initialize jokes
    
