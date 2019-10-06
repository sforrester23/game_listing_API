from game_listing_class import *
from database_connect import *

# Make the class instance for the database
server = 'localhost,1433'
database = 'game_listings'
username = 'SA'
password = 'Passw0rd2018'

game_db = DB_Connect(server, database, username, password)
# game_listing = Game_Listing('snowflake_smasher_86', 'COD', 'Xbox', '07899901479', 40, 'TN27 9SF')
# print(game_listing)

# game_listing.get_latitude()
# game_listing.get_longitude()
# game_listing.get_nearest_town()
#
# print(game_listing.latitude)
# print(game_listing.longitude)
# print(game_listing.town)

# Welcome the user
print('WELCOME TO BUY-S3LL-G4M3Z.COM!!! WHERE GAMING IS A STATE OF MIND... And the mind is one big game...')
print(' ')
# Give them options (main menu)
print('What on earth do you want to do today?')
print('1: Look at games!')
print('2: List a game on our amazing website!')
print('3: Edit an existing listing!')
print('Type exit to leave... Not sure why you\'d ever want to tho?')
user_input = input('Please select an option: ').strip().upper()
print(' ')
if user_input == 'EXIT':
    print('Goodbye, we hope to see you again!')
# The whole time the user hasn't inputted 'EXIT', continue doing the following...
while user_input != 'EXIT':

    # if the user chooses option 1 from the main menu
    if user_input == '1':
        # give them options for what games they'd like to view
        print('That\'s awesome. We\'ve got some absolute belters in today...')
        print('We need to refine a bit of what you\'re looking for. Hope that\'s cool.')
        print('Here are some options:')
        print('1: See all games!')
        print('2: See games of a certain name!')
        print('3: See games in a price range!')
        print('4: See games in a certain area!')
        print('Type back to go back...')
        # ask the user for their choice
        user_input_phase_2 = input('Please choose an option from the above: ').strip().upper()
        print(' ')

        # the whole time the user doesn't input 'BACK', continue doing the following
        while user_input_phase_2 != 'BACK':
            # if they select option 1 on the next list, print all listings and then break the current while loop
            if user_input_phase_2 == '1':
                print('All listings we have today:')
                game_db.print_all_listings()
                break

            # if they select option 2 on the next list, ask them what game they'd like to see listings for, show them based on that, and then break the current while loop
            elif user_input_phase_2 == '2':
                ### COULD SHOW LIST HERE?
                user_input_game_name = input('What is the name of the game you would like to see listings for, you scallywag?')
                print('Here\'s what we got back for ya:')
                game_db.read_entry_condition('game_name', user_input_game_name)
                break

            # if they select option 3 on the next list, ask them the lower and upper bounds for price, print all listings based on that and then break the current while loop
            elif user_input_phase_2 == '3':
                user_input_lower_price = input('What is the lowest price you\'d like to view? ')
                user_input_higher_price = input('What is the highest price you\'d like to view? ')
                print('Here\'s what we got back for ya:')
                game_db.read_entry_price_range(user_input_lower_price, user_input_higher_price)
                break

            # if they select option 4 on the next list, ask them what area they'd like to see them in, print all listings based on that criteria and then break the current while loop
            elif user_input_phase_2 == '4':
                user_input_location = input('What area would you like to see games in? ')
                print('Here\'s what we got back for ya:')
                game_db.read_entry_condition('town', user_input_location)
                break

            # if nothing they've put in is a valid option, tell them and then we'll show the menu at the top of the current if statement again
            else:
                print('Sorry, that\'s not a valid option. Please try again...')

            # give them options again! If they haven't put in a valid option it'll take them here. If they have, it'll break before they get here
            print('Here are some options:')
            print('1: See all games!')
            print('2: See games of a certain name!')
            print('3: See games in a price range!')
            print('4: See games in a certain area!')
            print('Type back to go back...')
            user_input_phase_2 = input('Please choose an option from the above: ').strip().upper()
            print(' ')

    # if the user picks option 2 from the main menu
    elif user_input == '2':
        # get the user to input the game data of the game they'd like to list
        print('Please enter some information regarding the game you\'d like to list:')
        username = input('Your username: ')
        game_name = input('Game name: ')
        console = input('Console: ')
        contact_num = input('Your contact number: ')
        price = input('Listing price: ')
        postcode = input('Your postcode: ')
        # make it into a class instance of game listing
        game_listing_input = Game_Listing(username, game_name, console, contact_num, price, postcode)
        # get the longitude, latitude from the API
        game_listing_input.get_longitude()
        game_listing_input.get_latitude()
        # get the nearest town to those longitudes and latitudes from another API
        game_listing_input.get_nearest_town()
        breakpoint()
        # create an entry for this game listing and push it to the database, to make it persistent
        game_db.create_entry(game_listing_input.username, game_listing_input.name, game_listing_input.console, game_listing_input.phone, game_listing_input.price, game_listing_input.postcode, game_listing_input.latitude, game_listing_input.longitude, game_listing_input.town)
        # tell them they were successful in adding it!
        print('Game listing added!')

    # let the user know that the option they've inputted is invalid, take them back to the main menu
    else:
        print('Sorry, that\'s not a valid option. Please try again...')

    # Give them options again (main menu)
    print('What on earth do you want to do today?')
    print('1: Look at games!')
    print('2: List a game on our amazing website!')
    print('3: Edit an existing listing!')
    print('Type exit to leave... Not sure why you\'d ever want to tho?')
    user_input = input('Please select an option: ').strip().upper()
    print(' ')

