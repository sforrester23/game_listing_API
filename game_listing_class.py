# import the necessaries for using API interface
import requests
from database_connect import *

# define class for game listing, including its attributes
class Game_Listing():
    def __init__(self, id, name, phone, price, location, latitude, longitude):
        self.id = id
        self.name = name
        self.phone = phone
        self.price = price
        self.location = location
        self.latitude = latitude
        self.longitude = longitude
        self.response = []

    # define a method for getting the latitude and longitude based on location
    def get_lat_long(self):
        url = "https://metropolis-api-geocode.p.rapidapi.com/solve"

        querystring = {"address": "{}".format(self.location)}

        headers = {
            'x-rapidapi-host': "metropolis-api-geocode.p.rapidapi.com",
            'x-rapidapi-key': "00306ed142msh759ebccbd55421dp18164ajsndcbff546d8a7"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        self.response.append(response)
