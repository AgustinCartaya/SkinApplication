# This Python file uses the following encoding: utf-8

import src.config as cfg
from .db_connection import DBConnection

class DBController:
    def __init__(self):
        self.db = DBConnection()
        # self.test()

    def insert(self, table, data):
        self.db.connect()
        if table == cfg.TABLE_DOCTORS:
            self.db.cursor.execute(("INSERT INTO %s VALUES (NULL,?,?,?,?)" % cfg.TABLE_DOCTORS), data)
        if table == cfg.TABLE_PATIENTS:
            self.db.cursor.execute( ("INSERT INTO  %s VALUES (?,?,?,?,?,?)" % cfg.TABLE_PATIENTS), data)
        self.db.connection.commit()
        self.db.connection.close()

    def update(self, table, data, conditions):
        self.db.connect()
        conditions_str = self.conditions_to_str(conditions)
        if table == cfg.TABLE_PATIENTS:
            self.db.cursor.execute( ( "UPDATE %s SET first_name = ?, last_name = ?, birth_date = ?, gender = ?, medical_information = ? WHERE %s" % (cfg.TABLE_PATIENTS, conditions_str)), data)
        self.db.connection.commit()
        self.db.connection.close()

    def count_all(self, table):
        self.db.connect()
        count = 0

        text_query = "SELECT Count(*) FROM %s" % table
        self.db.cursor.execute(text_query)

        count = self.db.cursor.fetchone()[0]
        self.db.connection.close()
        return count

    def conditions_to_str(self, conditions):
        dict_len = len(conditions)
        conditions_str = ""
        for condition_key in conditions:
            conditions_str = conditions_str + condition_key + " = \'" + conditions[condition_key] + "\'"
            if dict_len > 1:
                conditions_str = conditions_str + " AND "
            dict_len = dict_len - 1
        return conditions_str

    def select(self, table, *columns, **conditions):
        self.db.connect()
        columns_str = "*"
        conditions_str = ""
        
        if len(columns) > 0:
            columns_str = ','.join(columns)
        
        if len(conditions) > 0:
            conditions_str = "WHERE " + self.conditions_to_str(conditions)

        text_query = "SELECT %s FROM %s %s" % (columns_str, table, conditions_str)
        self.db.cursor.execute(text_query)
        rows = self.db.cursor.fetchall()
        self.db.connection.close()
        return rows

    def exists(self, table, **conditions):
        self.db.connect()
        conditions_str = ""

        if len(conditions) > 0:
            conditions_str = "WHERE " + self.conditions_to_str(conditions)


        text_query = "SELECT EXISTS(SELECT 1 FROM %s %s)" % (table, conditions_str)

        self.db.cursor.execute(text_query)
        res = self.db.cursor.fetchone()[0]
        self.db.connection.close()
        return res



    def test(self):
        self.db.connect()
        many_doctors = [
            ('Agustin', 'Cartaya', "1234", "ag@gmail.com"),
            ('Monica', 'Cartaya', "1234", "ag@gmail.com"),
            ('Miguel', 'Cartaya', "1234", "ag@gmail.com")
        ]
        self.db.cursor.executemany("INSERT INTO  DOCTORS VALUES (NULL,?,?,?,?)", many_doctors)

        self.db.cursor.execute("SELECT * FROM DOCTORS")
        print(self.db.cursor.fetchall())
        self.db.connection.commit()
        self.db.connection.close()
