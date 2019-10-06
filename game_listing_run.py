from game_listing_class import *
from database_connect import *

# Make the class instance for the database
server = 'localhost,1433'
database = 'game_listings'
username = 'SA'
password = 'Passw0rd2018'

game_db = DB_Connect(server, database, username, password)
game_listing = Game_Listing(1, 'COD', '07899901479', 40, 'TN27 9SF')

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
# Define an empty string as user_input so that we can get into the while loop
user_input = ''
# The whole time the user hasn't inputted 'EXIT', continue doing the following...
while user_input != 'EXIT':
    # Give them options
    print('What on earth do you want to do today?')
    print('1: Look at games!')
    print('2: List a game!')
    print('3: Edit an existing listing!')
    print('Type exit to leave... Not sure why you\'d ever want to tho?')
    user_input = input('Please select an option: ').strip().upper()
    print(' ')
    # again, define user_input_phase_2 as empty so we can get into the while loop...
    # if the user enters 'BACK' in the next bit, we'll return to the main menu!
    user_input_phase_2 = ''
    # the whole time the user doesn't input 'BACK', continue doing the following
    while user_input_phase_2 != 'BACK':
        # if user picks option 1 on the main menu
        if user_input == '1':
            # give them options
            print('That\'s awesome. We\'ve got some absolute belters in today...')
            print('We need to refine a bit of what you\'re looking for. Hope that\'s cool.')
            print('Here are some options:')
            print('1: See all games!')
            print('2: See games of a certain name!')
            print('3: See games in a price range!')
            print('4: See games in a certain area!')
            print('Type back to go back...')
            user_input_phase_2 = input('Please choose an option from the above ').strip().upper()
            print(' ')

            # if they select option 1 on the next list, print all listings and then break the current while loop
            if user_input_phase_2 == '1':
                game_db.print_all_listings()
                break

            # if they select option 2 on the next list, ask them what game they'd like to see listings for, show them based on that, and then break the current while loop
            elif user_input_phase_2 == '2':
                ### COULD SHOW LIST HERE?
                user_input_game_name = input('What is the name of the game you would like to see listings for, you scallywag?')
                game_db.read_entry_condition('game_name', user_input_game_name)
                break

            # if they select option 3 on the next list, ask them the lower and upper bounds for price, print all listings based on that and then break the current while loop
            elif user_input_phase_2 == '3':
                user_input_lower_price = input('What is the lowest price you\'d like to view? ')
                user_input_higher_price = input('What is the highest price you\'d like to view? ')
                game_db.read_entry_price_range(user_input_lower_price, user_input_higher_price)

            # if they select option 4 on the next list, ask them what area they'd like to see them in, print all listings based on that criteria and then break the current while loop
            elif user_input_phase_2 == '4':
                user_input_location = input('What area would you like to see games in? ')
                game_db.read_entry_condition('town', user_input_location)

            # if nothing they've put in is a valid option, tell them and then we'll show the menu at the top of the current if statement again
            else:
                print('Sorry, that\'s not a valid option. Please try again...')
        

        else:
            print('Sorry, that\'s not a valid option. Please try again...')

