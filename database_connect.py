# import the necessaries to connect db to python
import pyodbc

# define a class structure for database connection, including its attributes
class db_connect():
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

