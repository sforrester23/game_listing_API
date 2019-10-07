from game_listing_class import *
from database_connect import *

# Make the class instance for the database
server = 'localhost,1433'
database = 'game_listings'
username = 'SA'
password = 'Passw0rd2018'

# create an instance for the database to call all database commands
game_db = DB_Connect(server, database, username, password)
# make a game listing class instance
game_listing = Game_Listing('BarryThreeFeet', 'Sonic', 'SEGA MegaDrive', '0781513131', 20, 'TN279SF')
# game_listing.get_longitude()
# print(game_listing.longitude)

# attempt to test the get_longitude method, it should assign the longitude 0.626069 for the postcode TN27 9SF
def get_longitude_test():
    assert game_listing.get_longitude()
    assert game_listing.longitude == 0.626069

# attempt to test the get_all_listings method, the first row's first index value should be the ID 1
def get_all_listings_test():
    assert game_db.get_all_listings()[0][0] == 1