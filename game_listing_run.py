# import the necessaries
from game_listing_class import *
from database_connect import *
import time

# Make the class instance for the database
server = 'localhost,1433'
database = 'game_listings'
username = 'SA'
password = 'Passw0rd2018'

# create an instance for the database to call all database commands
game_db = DB_Connect(server, database, username, password)

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
        # set up a variable for all listings, never know when it might come in handy...
        all_listings = game_db.get_all_listings()
        # give them options for what games they'd like to view
        print('That\'s awesome. We\'ve got some absolute belters in today...')
        print('We need to refine a bit of what you\'re looking for. Hope that\'s cool.')
        print('Here are some options:')
        print('1: See all games!')
        print('2: See games of a certain name!')
        print('3: See games in a price range!')
        print('4: See games in a certain area!')
        print('5: See games on a particular console!')
        print('6: Buy a Game!')
        print('Type "back" to go back to the main menu...')
        # ask the user for their choice
        user_input_phase_2 = input('Please choose an option from the above: ').strip().upper()
        print(' ')

        # the whole time the user doesn't input 'BACK', continue doing the following
        while user_input_phase_2 != 'BACK':
            # if they select option 1 on the next list, print all listings
            if user_input_phase_2 == '1':
                print('All listings we have today for ya, fren\':')
                game_db.print_all_listings()
                print(' ')
                time.sleep(2)
                print('I\'m workin\' \'ere!')
                time.sleep(2)

            # if they select option 2 on the next list, ask them what game they'd like to see listings for, show them based on that
            elif user_input_phase_2 == '2':
                # set up an empty list for game names
                game_name_list = []
                # build the list from the all_listings variable
                for index in range(len(all_listings)):
                    game_name_list.append(all_listings[index][2])
                # print the options from the list
                print('We\'ve got listings in the following games:')
                for index in range(len(game_name_list)):
                    print(game_name_list[index])
                # ask them what theyre choice is
                user_input_game_name = input('What is the name of the game you would like to see listings for, you scallywag? ')
                # print the information they require
                print('Here\'s what we got back for ya:')
                game_db.read_entry_condition('game_name', user_input_game_name)
                print(' ')
                time.sleep(2)
                print('I\'m workin\' \'ere!')
                time.sleep(2)

            # if they select option 3 on the next list, ask them the lower and upper bounds for price, print all listings based on that
            elif user_input_phase_2 == '3':
                # build a price list, so we can see what the min and max values are to tell the user!
                price_list = []
                for index in range(len(all_listings)):
                    # only add the price if it doesn't already exist in the list
                    if all_listings[index][5] not in price_list:
                        price_list.append(all_listings[index][5])
                # tell the user the range of prices we have
                print('The highest priced item we have is £{}, and the lowest priced item we have is: £{}'.format(max(price_list), min(price_list)))
                # ask them for their range
                user_input_lower_price = input('What is the lowest price you\'d like to view? ')
                user_input_higher_price = input('What is the highest price you\'d like to view? ')
                # print results based on their input
                print('Here\'s what we got back for ya:')
                game_db.read_entry_price_range(user_input_lower_price, user_input_higher_price)
                print(' ')
                time.sleep(2)
                print('I\'m workin\' \'ere!')
                time.sleep(2)

            # if they select option 4 on the next list, ask them what area they'd like to see them in, print all listings based on that criteria
            elif user_input_phase_2 == '4':
                # set up an empty list for locations:
                locations_list = []
                # build the list
                for index in range(len(all_listings)):
                    # only add a new list item if we haven't already got it
                    if all_listings[index][9] not in locations_list:
                        locations_list.append(all_listings[index][9])
                # print them from the list
                print('We\'ve got listings in the following locations:')
                for index in range(len(locations_list)):
                    print(locations_list[index])
                # ask them for their location choice
                user_input_location = input('What area would you like to see games in? ')
                # print listings in that area
                print('Here\'s what we got back for ya:')
                game_db.read_entry_condition('town', user_input_location)
                print(' ')
                time.sleep(2)
                print('I\'m workin\' \'ere!')
                time.sleep(2)

            # if they chose option 5, to see games for a particular console
            elif user_input_phase_2 == '5':
                # set up an empty list for consoles
                console_list = []
                # build the list
                for index in range(len(all_listings)):
                    # only add them to the list if they aren't already in there
                    if all_listings[index][3] not in console_list:
                        console_list.append(all_listings[index][3])
                # print their options
                print('We\'ve got games for the following consoles:')
                for index in range(len(console_list)):
                    print(console_list[index])
                # ask them for their choice of console
                user_input_console_choice = input('Which console would you like to view games for? ')
                # print the game listings on that console
                print('Here\'s what we got back for ya:')
                game_db.read_entry_condition('console', user_input_console_choice)
                print(' ')
                time.sleep(2)
                print('I\'m workin\' \'ere!')
                time.sleep(2)

            # if the user inputs option 6, to buy a game
            elif user_input_phase_2 == '6':
                # ask the user for their choice of game listing ID
                print('Which game would you like to buy?')
                user_input_purchase_choice = int(input('Please enter the listing ID for the game you\'d like to buy: '))
                # delete that entry, so it can't be purchased again
                game_db.delete_entry(user_input_purchase_choice)
                print('You purchased the game from listing #{}! Fantastic choice. Don\'t play it too much and stay in school, kid.'.format(user_input_purchase_choice))
                print(' ')
                time.sleep(2)
                print('I\'m workin\' \'ere!')
                time.sleep(2)


            # if nothing they've put in is a valid option, tell them and then we'll show the menu at the top of the current if statement again
            else:
                print('***************')
                print('Sorry, that\'s not a valid option. Please try again...')
                print('***************')

            # give them options again! If they haven't put in a valid option it'll take them here. If they have, it'll break before they get here
            print('Here are some options:')
            print('1: See all games!')
            print('2: See games of a certain name!')
            print('3: See games in a price range!')
            print('4: See games in a certain area!')
            print('5: See games on a particular console!')
            print('6: Buy a Game!')
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
        try:
            price = int(input('Listing price: '))
        except ValueError:
            print('The Price needs to be a number!')
            continue
        postcode = input('Your postcode: ')
        # make it into a class instance of game listing
        game_listing_input = Game_Listing(username, game_name, console, contact_num, price, postcode)
        # get the longitude, latitude from the API
        game_listing_input.get_longitude()
        game_listing_input.get_latitude()
        # get the nearest town to those longitudes and latitudes from another API
        game_listing_input.get_nearest_town()
        # create an entry for this game listing and push it to the database, to make it persistent
        game_db.create_entry(game_listing_input.username, game_listing_input.name, game_listing_input.console, game_listing_input.phone, game_listing_input.price, game_listing_input.postcode, game_listing_input.latitude, game_listing_input.longitude, game_listing_input.town)
        # tell them they were successful in adding it!
        print('Game listing added! You can check by choosing option 1 to view listings from the main menu.')
        print(' ')
        time.sleep(2)
        print('I\'m workin\' \'ere!')
        time.sleep(2)

    elif user_input == '3':
        # give the user some options for editing listing(s)
        print('So, you\'d like to edit a listing...')
        print('What would you like to do to the listing?')
        print('1: Change a value in an existing listing.')
        print('2: Delete an existing listing.')
        print('Type "back" to go back...')
        user_input_phase_3 = input('Please choose from the above options: ').strip().upper()
        print(' ')
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
                # print a list so the user can see the IDs they might want to edit
                print('You\'d like to edit a listing? I hope you\'re serious about that... Here are the options:')
                game_db.print_all_listings()
                try:
                    user_input_listing_id = int(input('Please input the ID for the listing you\'d like to change: '))
                except ValueError:
                    print('No, SILLY, you have to put in a number!')
                    continue
                print('Checking if we have that listing.....')
                time.sleep(5)
                print('I\'m workin\' \'ere!')
                time.sleep(4)

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
                        try:
                            user_input_new_value = int(input('What is the new desired value for that column?: '))
                        except ValueError as ValErr:
                            print('Sorry, that input needs to be a number!')
                            continue
                        # update it
                        game_db.update_entry(user_input_listing_id, 'price', user_input_new_value)
                        # tell them it's been updated
                        time.sleep(2)
                        print('I\'m workin\' \'ere!')
                        time.sleep(2)
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
                        time.sleep(2)
                        print('I\'m workin\' \'ere!')
                        time.sleep(2)
                        # let them know the update worked
                        print('Update Complete!')
                        print(' ')
                    # otherwise, do the update as normal, using a string as the default input. The rest of the db columns are designed to take in strings, so it's fine
                    else:
                        user_input_new_value = input('What is the new desired value for that column?: ')
                        game_db.update_entry(user_input_listing_id, column_choice_list_sql[user_input_column_choice-1], user_input_new_value)
                        print('Update Complete!')
                        print(' ')
                # if the listing id is not in our list, tell them it's not!
                else:
                    print('***************')
                    print('OOPS! Sorry, that\'s not a listing we have. Please try again...')
                    print('***************')

            elif user_input_phase_3 == '2':
                print('You\'d like to delete a listing? I hope you\'re serious about that... Here are the options:')
                game_db.print_all_listings()
                input_delete = int(input('So which listing would you like to delete? '))
                if input_delete in game_id_list:
                    game_db.delete_entry(input_delete)
                    print('DESTRUCTION COMPLETE!')
                    print(' ')
                else:
                    print('OOPS! Looks like we couldn\'t find that listing... Please try again.')
                    continue

            # if they haven't entered a valid option, tell them!
            else:
                print('***************')
                print('Sorry, that\'s not a valid option. Please try again...')
                print('***************')

            # give the user some options for editing listing(s)
            print('So, you\'d like to edit a listing...')
            print('What would you like to do to the listing?')
            print('1: Change a value in an existing listing.')
            print('2: Delete an existing listing.')
            print('Type "back" to go back to the main menu...')
            user_input_phase_3 = input('Please choose from the above options: ').strip().upper()
            print(' ')

    # let the user know that the option they've inputted is invalid, take them back to the main menu
    else:
        print('***************')
        print('Sorry, that\'s not a valid option. Please try again...')
        print('***************')

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