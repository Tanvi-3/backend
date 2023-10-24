from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random
import http.client

from model.weather2 import *

weather_api = Blueprint('weather_api', __name__,
                   url_prefix='/api/weather')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(weather_api)

class WeatherAPI:
    # not implemented
    
    # getWeather()
    class _Read(Resource):
        def get(self, weather):
            return jsonify(getWeatherAPIData(weather))

    api.add_resource(_Read, '/<string:weather>')

if __name__ == "__main__": 
    # server = "http://127.0.0.1:5000" # run local
    server = 'https://flask.nighthawkcodingsociety.com' # run from web
    url = server + "/api/weather"
    responses = []  # responses list
    