from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random
import http.client

from model.cityimagesmodel import *

cityImage_api = Blueprint('cityImage_api', __name__,
                   url_prefix='/api/cityimage')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(cityImage_api)

class CityImageAPI:
    # not implemented

    class _Read(Resource):
        def get(self, cityName):
            return_dictionary = {"image_url": getCityImage(cityName)}
            return jsonify(return_dictionary)


    api.add_resource(_Read, '/<string:cityName>')

if __name__ == "__main__": 
    # server = "http://127.0.0.1:5000" # run local
    server = 'https://flask.nighthawkcodingsociety.com' # run from web
    url = server + "/api/cityimage"
    responses = []  # responses list