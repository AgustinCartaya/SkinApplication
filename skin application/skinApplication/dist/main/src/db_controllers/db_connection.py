# @autor: Agustin CARTAYA

from os.path import exists

import sqlite3
import src.config as cfg
import src.util.util as util

# class responsible for connecting to the database
class DBConnection:

    # database connection
    def connect(self):
        self.connection = sqlite3.connect(cfg.DB_PATH_NAME)
        self.cursor = self.connection.cursor()

    # verifying the existence of the database
    # if the database does not exist it is created
    def verify_db_existence(self):
        if not exists(cfg.DB_PATH_NAME):
            self.create_db()
        return True

    # creation of the database
    def create_db(self):
        self.connect()
        self.create_tables()
        self.connection.close()

    # creating the database tables
    # the script DB_SCRIPT_PATH_NAME a contains the entire database structure
    def create_tables(self):
        sql_as_string = util.read_file(cfg.DB_SCRIPT_PATH_NAME)
        self.cursor.executescript(sql_as_string)

    

