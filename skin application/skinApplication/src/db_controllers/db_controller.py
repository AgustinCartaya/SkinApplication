# This Python file uses the following encoding: utf-8

import src.config as cfg
from .db_connection import DBConnection

class DBController:
    def __init__(self):
        self.db = DBConnection()
#        self.test()

    def insert(self, table, data):
        if type(data) is not tuple :
            raise ValueError('Upadte data is not tuple', "INSERT_DATA", "NOT_TUPLE")

        self.db.connect()
        if table == cfg.TABLE_DOCTORS:
            self.db.cursor.execute(("INSERT INTO %s VALUES (NULL,?,?,?,?)" % cfg.TABLE_DOCTORS), data)
        elif table == cfg.TABLE_PATIENTS:
            self.db.cursor.execute( ("INSERT INTO %s VALUES (?,?,?,?,?,?)" % cfg.TABLE_PATIENTS), data)
        elif table == cfg.TABLE_SKIN_LESIONS:
            self.db.cursor.execute( ("INSERT INTO %s VALUES (?,?,?,?,?)" % cfg.TABLE_SKIN_LESIONS), data)
        elif table == cfg.TABLE_VARIABLE_INPUTS:
            self.db.cursor.execute( ("INSERT INTO %s VALUES (?,?,?,?,?,?,?)" % cfg.TABLE_VARIABLE_INPUTS), data)
        else:
            self.db.connection.close()
            raise ValueError('Insert table not found', "INSERT_TABLE", "NOT_FOUND")

        self.db.connection.commit()
        self.db.connection.close()

    def update(self, table, data, conditions):
        if type(data) is not tuple :
            raise ValueError('Upadte data is not tuple', "UPDATE_DATA", "NOT_TUPLE")
        if type(conditions) is not tuple:
            raise ValueError('Upadte conditions is not tuple', "UPDATE_CONDITIONS", "NOT_TUPLE")

        self.db.connect()
        if table == cfg.TABLE_PATIENTS:
            self.db.cursor.execute( ("UPDATE %s SET first_name = ?, last_name = ?, birth_date = ?, gender = ?, medical_information = ? WHERE id = ?" % cfg.TABLE_PATIENTS), (data + conditions))
        elif table == cfg.TABLE_SKIN_LESIONS:
            self.db.cursor.execute( ("UPDATE %s SET location = ?, characteristics = ?, ai_results = ? WHERE number = ? AND id_patient = ?" % cfg.TABLE_SKIN_LESIONS), (data + conditions) )
        elif table == cfg.TABLE_VARIABLE_INPUTS:
            self.db.cursor.execute( ("UPDATE %s SET name = ?, type = ?, items = ?, scale = ? WHERE id = ? AND family = ?" % cfg.TABLE_VARIABLE_INPUTS), (data + conditions) )

        else:
            self.db.connection.close()
            raise ValueError('Upadte table not found', "UPDATE_TABLE", "NOT_FOUND")

        self.db.connection.commit()
        self.db.connection.close()

    def delete(self, table, conditions):
        if type(conditions) is not tuple:
            raise ValueError('Upadte conditions is not tuple', "UPDATE_CONDITIONS", "NOT_TUPLE")

        self.db.connect()
        if table == cfg.TABLE_VARIABLE_INPUTS:
            self.db.cursor.execute( ("DELETE FROM %s WHERE id = ? AND family = ?" % cfg.TABLE_VARIABLE_INPUTS), conditions )
        else:
            self.db.connection.close()
            raise ValueError('Upadte table not found', "UPDATE_TABLE", "NOT_FOUND")

        self.db.connection.commit()
        self.db.connection.close()

    def count_all(self, table, conditions=None):
        if conditions is not None and type(conditions) is not tuple :
            raise ValueError('Count all conditions is not tuple', "COUNT ALL CONDITIONS", "NOT_TUPLE")

        self.db.connect()
        count = 0

        if table == cfg.TABLE_DOCTORS:
            self.db.cursor.execute("SELECT Count(*) FROM %s" % cfg.TABLE_DOCTORS)
        elif table == cfg.TABLE_PATIENTS:
            self.db.cursor.execute("SELECT Count(*) FROM %s" % cfg.TABLE_PATIENTS)
        elif table == cfg.TABLE_SKIN_LESIONS:
            self.db.cursor.execute("SELECT Count(*) FROM %s" % cfg.TABLE_SKIN_LESIONS)
        elif table == cfg.TABLE_VARIABLE_INPUTS:
            if conditions is None:
                self.db.cursor.execute("SELECT Count(*) FROM %s" % cfg.TABLE_VARIABLE_INPUTS)
            else:
                self.db.cursor.execute(("SELECT Count(*) FROM %s WHERE family = ? AND owner = ?" % cfg.TABLE_VARIABLE_INPUTS), conditions)
        else:
            self.db.connection.close()
            raise ValueError('Count all table not found', "COUNT_ALL_TABLE", "NOT_FOUND")

        count = self.db.cursor.fetchone()[0]
        self.db.connection.close()
        return count

    # NOT SECURISED !!!
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

    # NOT SECURISED !!!
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


    def secure_select(self, table, conditions=None, multiples=True):
        if conditions is not None and type(conditions) is not tuple :
            raise ValueError('Select conditions is not tuple', "SELECT_CONDITIONS", "NOT_TUPLE")

        self.db.connect()
#        if table == cfg.TABLE_DOCTORS:
#            self.db.cursor.execute("SELECT Count(*) FROM %s" % cfg.TABLE_DOCTORS)
#        elif table == cfg.TABLE_PATIENTS:
#            self.db.cursor.execute("SELECT Count(*) FROM %s" % cfg.TABLE_PATIENTS)
#        elif table == cfg.TABLE_SKIN_LESIONS:
#            self.db.cursor.execute("SELECT Count(*) FROM %s" % cfg.TABLE_SKIN_LESIONS)
        if table == cfg.TABLE_VARIABLE_INPUTS:
            if conditions is None:
                self.db.cursor.execute("SELECT * FROM %s" % cfg.TABLE_VARIABLE_INPUTS)
            elif len(conditions) == 1:
                if multiples:
                    self.db.cursor.execute(("SELECT * FROM %s WHERE family = ?" % cfg.TABLE_VARIABLE_INPUTS), conditions)
                else:
                    self.db.cursor.execute(("SELECT * FROM %s WHERE id = ?" % cfg.TABLE_VARIABLE_INPUTS), conditions)
            elif len(conditions) == 2:
                self.db.cursor.execute(("SELECT * FROM %s WHERE family = ? AND owner = ?" % cfg.TABLE_VARIABLE_INPUTS), conditions)

        else:
            self.db.connection.close()
            raise ValueError('Count all table not found', "COUNT_ALL_TABLE", "NOT_FOUND")

        if multiples:
            rows = self.db.cursor.fetchall()
        else:
            rows = self.db.cursor.fetchone()

        self.db.connection.close()
        return rows


    def secure_exists(self, table, conditions):
        if type(conditions) is not tuple :
            raise ValueError('Exists conditions is not tuple', "EXISTS_CONDITIONS", "NOT_TUPLE")

        self.db.connect()
#        if table == cfg.TABLE_DOCTORS:
#            self.db.cursor.execute("SELECT Count(*) FROM %s" % cfg.TABLE_DOCTORS)
#        elif table == cfg.TABLE_PATIENTS:
#            self.db.cursor.execute("SELECT Count(*) FROM %s" % cfg.TABLE_PATIENTS)
#        elif table == cfg.TABLE_SKIN_LESIONS:
#            self.db.cursor.execute("SELECT Count(*) FROM %s" % cfg.TABLE_SKIN_LESIONS)
        if table == cfg.TABLE_VARIABLE_INPUTS:
            self.db.cursor.execute(("SELECT EXISTS(SELECT 1 FROM %s WHERE id = ? AND family = ?)" % cfg.TABLE_VARIABLE_INPUTS), conditions)
        else:
            self.db.connection.close()
            raise ValueError('Count all table not found', "COUNT_ALL_TABLE", "NOT_FOUND")

        res = self.db.cursor.fetchone()[0]
        self.db.connection.close()
        return res

    def conditions_to_str(self, conditions, sep = "AND"):
        dict_len = len(conditions)
        conditions_str = ""
        for condition_key in conditions:
            conditions_str = conditions_str + condition_key + " = \'" + conditions[condition_key] + "\'"
            if dict_len > 1:
                conditions_str = conditions_str + " " + sep + " "
            dict_len = dict_len - 1
        return conditions_str

#    def test(self):
#        self.db.connect()
#        many_doctors = [
#            ('Agustin', 'Cartaya', "1234", "ag@gmail.com"),
#            ('Monica', 'Cartaya', "1234", "ag@gmail.com"),
#            ('Miguel', 'Cartaya', "1234", "ag@gmail.com")
#        ]
#        self.db.cursor.executemany("INSERT INTO DOCTORS VALUES (NULL,?,?,?,?)", many_doctors)

#        self.db.cursor.execute("SELECT * FROM DOCTORS")
#        print(self.db.cursor.fetchall())
#        self.db.connection.commit()
#        self.db.connection.close()
