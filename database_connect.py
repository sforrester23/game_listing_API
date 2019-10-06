# import the necessaries to connect db to python
import pyodbc

# define a class structure for database connection, including its attributes
class DB_Connect():
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connect_db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.connect_db.cursor()

    # define a method for carrying out queries, encapsulate it so it can only be used by other methods in this file
    def __filter_query(self, query):
        return self.cursor.execute(query)

    # method for extracting all listings from the db
    def get_all_listings(self):
        return self.__filter_query("SELECT * FROM game_info").fetchall()

    # define a set of methods to CRUD our data in the database
    # C - create
    def create_entry(self, username, name, console, phone_number, price, postcode, latitude = '', longitude = '', town = ''):
        self.__filter_query("INSERT INTO game_info (username, game_name, console, contact_number, price, postcode, latitude, longitude, town) VALUES ('{}', '{}', '{}', '{}', {}, '{}', {}, {}, '{}')".format(username, name, console, phone_number, price, postcode, latitude, longitude, town))
        self.connect_db.commit()

    # R - read (based on either game_listing, game_name, price range)
    def print_all_listings(self):
        all_game_query = self.__filter_query("SELECT * FROM game_info")
        while True:
            record = all_game_query.fetchone()
            if record is None:
                break
            print('Listing ID: {} -- Game Name: {} -- Console: {} -- Price: £{} -- Username: {} -- Contact Number: {} -- Location: {}'.format(record[0], record[2], record[3], record[5], record[1], record[4], record[9]))

    def read_entry_game_id(self, listing_id):
        record = self.__filter_query("SELECT * FROM game_info WHERE listing_ID = {}".format(listing_id)).fetchone()
        return 'Listing ID: {} -- Game Name: {} -- Console: {} -- Price: £{} -- Username: {} -- Contact Number: {} -- Location: {}'.format(record[0], record[2], record[3], record[5], record[1], record[4], record[9])

    def read_entry_condition(self, column_condition, column_value):
        game_condition_query = self.__filter_query("SELECT * FROM game_info WHERE {} = '{}'".format(column_condition, column_value))
        while True:
            record = game_condition_query.fetchone()
            if record is None:
                break
            print('Listing ID: {} -- Game Name: {} -- Console: {} -- Price: £{} -- Username: {} -- Contact Number: {} -- Location: {}'.format(record[0], record[2], record[3], record[5], record[1], record[4], record[9]))

    def read_entry_price_range(self, lower_bound, upper_bound):
        price_range_query = self.__filter_query("SELECT * FROM game_info WHERE price >= {} AND price <= {}".format(lower_bound, upper_bound))
        while True:
            record = price_range_query.fetchone()
            if record is None:
                break
            print('Listing ID: {} -- Game Name: {} -- Console: {} -- Price: £{} -- Username: {} -- Contact Number: {} -- Location: {}'.format(
                    record[0], record[2], record[3], record[5], record[1], record[4], record[9]))

    # U - update
    # we'll only update values based on listing ID, as it's unique
    def update_entry(self, listing_id, column_to_update, new_value):
        # if its price, longitude or latitude you'd like to update, we need to change the query so it doesn't make an integer a string
        if column_to_update == 'price' or column_to_update == 'longitude' or column_to_update == 'latitude':
            self.__filter_query("UPDATE game_info SET {} = {} WHERE listing_ID = {}".format(column_to_update, new_value, listing_id))
            self.connect_db.commit()
        # if its not price, we need to make sure the query takes an integer to input as the new value
        else:
            self.__filter_query("UPDATE game_info SET {} = '{}' WHERE listing_ID = {}".format(column_to_update, new_value, listing_id))
            self.connect_db.commit()

    # D - delete
    # based on game ID only (don't want to delete multiple entries of the same game)
    def delete_entry(self, listing_id):
        self.__filter_query("DELETE FROM game_info WHERE listing_ID = {}".format(listing_id))



