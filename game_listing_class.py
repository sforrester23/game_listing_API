# import the necessaries for using API interface
import requests
import json
from database_connect import *

# define class for game listing, including its attributes
class Game_Listing():
    def __init__(self, id, name, phone, price, postcode, latitude = '', longitude = '', town = ''):
        self.id = id
        self.name = name
        self.phone = phone
        self.price = price
        self.postcode = postcode
        self.latitude = latitude
        self.longitude = longitude
        self.town = town

    # method for getting longitude from the current postcode using postcodes.io API
    def get_longitude(self):
        response = requests.get('http://api.postcodes.io/postcodes/{}'.format(self.postcode))
        self.longitude = response.json()['result']['longitude']

    # method for getting longitude from the current postcode using postcodes.io API
    def get_latitude(self):
        response = requests.get('http://api.postcodes.io/postcodes/{}'.format(self.postcode))
        self.latitude = response.json()['result']['latitude']

    # define a method for getting the nearest town based on latitude and longitude
    def get_nearest_town(self):
        url = "https://geocodeapi.p.rapidapi.com/GetNearestCities"

        querystring = {"latitude": "{}".format(self.latitude), "longitude": "{}".format(self.longitude), "range": "0"}

        headers = {
            'x-rapidapi-host': "geocodeapi.p.rapidapi.com",
            'x-rapidapi-key': "00306ed142msh759ebccbd55421dp18164ajsndcbff546d8a7"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        self.town = response.json()[0]['City']
