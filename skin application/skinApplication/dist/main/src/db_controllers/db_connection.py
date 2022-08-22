# This Python file uses the following encoding: utf-8
from os.path import exists

import sqlite3
import src.config as cfg
import src.util.util as util

class DBConnection:
    def __init__(self):
        pass
        # self.test()

    def connect(self):
        self.connection = sqlite3.connect(cfg.DB_PATH_NAME)
        self.cursor = self.connection.cursor()

    def verify_db_existence(self):
        if not exists(cfg.DB_PATH_NAME):
            self.create_db()
        return True

    def create_db(self):
        self.connect()
        self.create_tables()
        self.connection.close()

    def create_tables(self):
        sql_as_string = util.read_file(cfg.DB_SCRIPT_PATH_NAME)
        self.cursor.executescript(sql_as_string)

    

