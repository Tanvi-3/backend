from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from model.weather2 import *

weather_api = Blueprint('weather_api', __name__,
                   url_prefix='/api/weather')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(weather_api)

class WeatherAPI:
    # not implemented
    class _Create(Resource):
        def post(self, weather):
            addWeather(weather)
            pass
            
    # getWeather()
    class _Read(Resource):
        def get(self):
            return jsonify(getWeather())


        
    api.add_resource(_Create, '/create/<string:weather>')
    api.add_resource(_Read, '/')

if __name__ == "__main__": 
    # server = "http://127.0.0.1:5000" # run local
    server = 'https://flask.nighthawkcodingsociety.com' # run from web
    url = server + "/api/weather"
    responses = []  # responses list
    