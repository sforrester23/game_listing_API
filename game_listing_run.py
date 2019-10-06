from game_listing_class import *
from database_connect import *

game_listing = Game_Listing(1, 'COD', '07899901479', 40, 'TN27 9SF')

game_listing.get_latitude()
game_listing.get_longitude()
game_listing.get_nearest_town()

print(game_listing.latitude)
print(game_listing.longitude)
print(game_listing.town)
