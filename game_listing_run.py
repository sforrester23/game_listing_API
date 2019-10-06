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
print('\\\\\\\\\\\\\\\\\\\\ MAIN MENU //////////')
print('What on earth do you want to do today?')
print('1: Look at games!')
print('2: List a game on our amazing website!')
print('3: Edit an existing listing!')
print('Type exit to leave... Not sure why you\'d ever want to tho?')
user_input = input('Please select an option: ').strip().upper()
print(' ')
# send the user a goodbye message, should they choose to leave
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
        print('Type "back" to go back to the main menu...')
        # ask the user for their choice
        user_input_phase_2 = input('Please choose an option from the above: ').strip().upper()
        print(' ')

        # the whole time the user doesn't input 'BACK', continue doing the following
        while user_input_phase_2 != 'BACK':
            # if they select option 1 on the next list, print all listings and then break the current while loop
            if user_input_phase_2 == '1':
                print('All listings we have today:')
                game_db.print_all_listings()

            # if they select option 2 on the next list, ask them what game they'd like to see listings for, show them based on that, and then break the current while loop
            elif user_input_phase_2 == '2':
                ### COULD SHOW LIST HERE?
                user_input_game_name = input('What is the name of the game you would like to see listings for, you scallywag?')
                print('Here\'s what we got back for ya:')
                game_db.read_entry_condition('game_name', user_input_game_name)

            # if they select option 3 on the next list, ask them the lower and upper bounds for price, print all listings based on that and then break the current while loop
            elif user_input_phase_2 == '3':
                user_input_lower_price = input('What is the lowest price you\'d like to view? ')
                user_input_higher_price = input('What is the highest price you\'d like to view? ')
                print('Here\'s what we got back for ya:')
                game_db.read_entry_price_range(user_input_lower_price, user_input_higher_price)

            # if they select option 4 on the next list, ask them what area they'd like to see them in, print all listings based on that criteria and then break the current while loop
            elif user_input_phase_2 == '4':
                user_input_location = input('What area would you like to see games in? ')
                print('Here\'s what we got back for ya:')
                game_db.read_entry_condition('town', user_input_location)

            # if nothing they've put in is a valid option, tell them and then we'll show the menu at the top of the current if statement again
            else:
                print('Sorry, that\'s not a valid option. Please try again...')

            # give them options again! If they haven't put in a valid option it'll take them here. If they have, it'll break before they get here
            print('Here are some options:')
            print('1: See all games!')
            print('2: See games of a certain name!')
            print('3: See games in a price range!')
            print('4: See games in a certain area!')
            print('Type "back" to go back to the main menu...')
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
        print('Game listing added! You can check by choosing option 1 to view listings from the main menu.')

    elif user_input == '3':
        # give the user some options for editing listing(s)
        print('So, you\'d like to edit a listing...')
        print('What would you like to do to the listing?')
        print('1: Change a value in an existing listing.')
        print('2: Delete an existing listing.')
        print('Type "back" to go back...')
        user_input_phase_3 = input('Please choose from the above options: ').strip().upper()
        # build a list of listing IDs so we can check if what the user inputs is contained in the list, and therefore valid
        record = game_db.get_all_listings()
        game_id_list = []
        for index in range(len(record)):
            game_id_list.append(record[index][0])
        # we'd also like a list of options for the user to choose from, this way we can print them more easily and also assign from this list what to do next, based on the users choice. We only make it up to postcode, as the user should not be able to change lat, long or town
        column_choice_list = ['Username', 'Game Name', 'Console', 'Contact Number', 'Price', 'Postcode']
        # list to match up those user friendly outputs to what they're actually called in SQL db, for accessing by queries
        column_choice_list_sql = ['username', 'game_name', 'console', 'contact_number', 'price', 'postcode']
        # the whole time the user doesn't type in 'back', continue doing the following
        while user_input_phase_3 != 'BACK':
            # if the user chooses option 1, to update information in the listing
            if user_input_phase_3 == '1':
                # ask them the id of the listing they'd like to edit
                user_input_listing_id = int(input('Please input the id for the listing you\'d like to change: '))
                # check if the listing id is in our list, i.e. is it valid
                if user_input_listing_id in game_id_list:
                    # if it is, tell them it is, then do this
                    print('Eeeexceeellent, that\'s a listing we have!')
                    print(' ')
                    # ask them where they want to change the value (which column)
                    print('Which column would you like to change the value in?')
                    # print some options from the pre-designed list
                    for index in range(len(column_choice_list)):
                        print(index+1, ': ', column_choice_list[index])
                    # ask them for their chouce
                    user_input_column_choice = int(input('Please select from the above options: '))
                    # special case: when the value they want to change is a price (i.e. an integer), we need a different query for it
                    if user_input_column_choice == 5:
                        # ask them what they want to change it to
                        user_input_new_value = int(input('What is the new desired value for that column?: '))
                        # update it
                        game_db.update_entry(user_input_listing_id, 'price', user_input_new_value)
                        # tell them it's been updated
                        print('Update Complete!')
                    # special case: when the value they want to change is a postcode, i.e. we need to get new lat, long and town information and update that too. The way it's set up is you can only get said information if you already have a class instance for that listing set up.
                    elif user_input_column_choice == 6:
                        user_input_new_value = input('What is the new desired value for that column?: ')
                        # because we're getting data straight from the listing we don't have a class instance for it, so we need to make one
                        # get the data for that listing ID
                        record_to_change = game_db.cursor.execute("SELECT * FROM game_info WHERE listing_ID = {}".format(user_input_listing_id)).fetchone()
                        # make the class instance
                        game_listing_change = Game_Listing(record_to_change[1], record_to_change[2], record_to_change[3], record_to_change[4], record_to_change[5], user_input_new_value)
                        # get the lat, long and hence town values from the API
                        game_listing_change.get_longitude()
                        game_listing_change.get_latitude()
                        game_listing_change.get_nearest_town()
                        # update each column for that entry of id with the new data, from the class instance
                        game_db.update_entry(user_input_listing_id, 'username', game_listing_change.username)
                        game_db.update_entry(user_input_listing_id, 'game_name', game_listing_change.name)
                        game_db.update_entry(user_input_listing_id, 'console', game_listing_change.console)
                        game_db.update_entry(user_input_listing_id, 'contact_number', game_listing_change.phone)
                        game_db.update_entry(user_input_listing_id, 'price', game_listing_change.price)
                        game_db.update_entry(user_input_listing_id, 'username', game_listing_change.username)
                        game_db.update_entry(user_input_listing_id, 'postcode', game_listing_change.postcode)
                        game_db.update_entry(user_input_listing_id, 'latitude', game_listing_change.latitude)
                        game_db.update_entry(user_input_listing_id, 'longitude', game_listing_change.longitude)
                        game_db.update_entry(user_input_listing_id, 'town', game_listing_change.town)
                        # let them know the update worked
                        print('Update Complete!')
                    # otherwise, do the update as normal, using a string as the default input
                    else:
                        user_input_new_value = input('What is the new desired value for that column?: ')
                        game_db.update_entry(user_input_listing_id, column_choice_list_sql[user_input_column_choice-1], user_input_new_value)
                        print('Update Complete!')
                # if the listing id is not in our list, tell them it's not!
                else:
                    print('OOPS! Sorry, that\'s not a listing we have. Please try again...')
            elif user_input_phase_3 == '2':
                input_delete = int(input('So which listing would you like to delete? '))
                game_db.delete_entry(input_delete)
                print('DESTRUCTION COMPLETE!')

            # give the user some options for editing listing(s)
            print('So, you\'d like to edit a listing...')
            print('What would you like to do to the listing?')
            print('1: Change a value in an existing listing.')
            print('2: Delete an existing listing.')
            print('Type "back" to go back to the main menu...')
            user_input_phase_3 = input('Please choose from the above options: ').strip().upper()
    # let the user know that the option they've inputted is invalid, take them back to the main menu
    else:
        print('Sorry, that\'s not a valid option. Please try again...')

    # Give them options again (main menu)
    print('\\\\\\\\\\\\\\\\\\\\ MAIN MENU //////////')
    print('What on earth do you want to do today?')
    print('1: Look at games!')
    print('2: List a game on our amazing website!')
    print('3: Edit an existing listing!')
    print('Type exit to leave... Not sure why you\'d ever want to tho?')
    user_input = input('Please select an option: ').strip().upper()
    print(' ')
    # send the user a goodbye message, should they choose to leave
    if user_input == 'EXIT':
        print('Goodbye, we hope to see you again!')


