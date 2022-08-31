# @autor: Agustin CARTAYA

import src.config as cfg
from .db_connection import DBConnection


# This class is in charge of controlling the modifications in the database
class DBController:
    def __init__(self):
        self.db = DBConnection()

    # inserting objects into the database
    def insert(self, table, data):
        if type(data) is not tuple :
            raise ValueError('Upadte data is not tuple', "INSERT_DATA", "NOT_TUPLE")

        self.db.connect()
        if table == cfg.TABLE_DOCTORS:
            self.db.cursor.execute(("INSERT INTO %s VALUES (NULL,?,?,?,?)" % cfg.TABLE_DOCTORS), data)
        elif table == cfg.TABLE_PATIENTS:
            self.db.cursor.execute( ("INSERT INTO %s VALUES (?,?,?,?,?,?,?)" % cfg.TABLE_PATIENTS), data)
        elif table == cfg.TABLE_SKIN_LESIONS:
            self.db.cursor.execute( ("INSERT INTO %s VALUES (?,?,?,?,?)" % cfg.TABLE_SKIN_LESIONS), data)
        elif table == cfg.TABLE_VARIABLE_INPUTS:
            self.db.cursor.execute( ("INSERT INTO %s VALUES (?,?,?,?,?,?,?)" % cfg.TABLE_VARIABLE_INPUTS), data)
        else:
            self.db.connection.close()
            raise ValueError("TABLE", "NOT_FOUND")

        self.db.connection.commit()
        self.db.connection.close()

    # updating objects in the database
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
            raise ValueError("TABLE", "NOT_FOUND")

        self.db.connection.commit()
        self.db.connection.close()

    # deletion of objects in the database
    def delete(self, table, conditions):
        if type(conditions) is not tuple:
            raise ValueError('Upadte conditions is not tuple', "UPDATE_CONDITIONS", "NOT_TUPLE")

        self.db.connect()
        if table == cfg.TABLE_PATIENTS:
            self.db.cursor.execute( ("DELETE FROM %s WHERE id = ?" % cfg.TABLE_PATIENTS), conditions )

        elif table == cfg.TABLE_SKIN_LESIONS:
            self.db.cursor.execute( ("DELETE FROM %s WHERE number = ? AND id_patient = ?" % cfg.TABLE_SKIN_LESIONS), conditions )

        elif table == cfg.TABLE_VARIABLE_INPUTS:
            self.db.cursor.execute( ("DELETE FROM %s WHERE id = ? AND family = ?" % cfg.TABLE_VARIABLE_INPUTS), conditions )

        else:
            self.db.connection.close()
            raise ValueError("TABLE", "NOT_FOUND")

        self.db.connection.commit()
        self.db.connection.close()

    # count objects in a table
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
            raise ValueError("TABLE", "NOT_FOUND")

        count = self.db.cursor.fetchone()[0]
        self.db.connection.close()
        return count

    # getting objects from a table
    def secure_select(self, table, conditions=None, multiples=True):
        if conditions is not None and type(conditions) is not tuple :
            raise ValueError('Select conditions is not tuple', "SELECT_CONDITIONS", "NOT_TUPLE")

        self.db.connect()
        if table == cfg.TABLE_DOCTORS:
            if conditions is None:
                self.db.cursor.execute("SELECT * FROM %s" % cfg.TABLE_DOCTORS)
            else:
                self.db.cursor.execute(("SELECT * FROM %s WHERE last_name = ? AND password = ?" % cfg.TABLE_DOCTORS), conditions)

        elif table == cfg.TABLE_PATIENTS:
#            if conditions is None:
#                self.db.cursor.execute("SELECT * FROM %s" % cfg.TABLE_PATIENTS)
            if multiples:
                self.db.cursor.execute(("SELECT * FROM %s WHERE doctor_id = ?" % cfg.TABLE_PATIENTS), conditions)
            else:
                self.db.cursor.execute(("SELECT * FROM %s WHERE id = ?" % cfg.TABLE_PATIENTS), conditions)

        elif table == cfg.TABLE_SKIN_LESIONS:
            self.db.cursor.execute(("SELECT * FROM %s WHERE id_patient = ?" % cfg.TABLE_SKIN_LESIONS), conditions)

        elif table == cfg.TABLE_VARIABLE_INPUTS:
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
            raise ValueError("TABLE", "NOT_FOUND")

        if multiples:
            rows = self.db.cursor.fetchall()
        else:
            rows = self.db.cursor.fetchone()

        self.db.connection.close()
        return rows

    # checking the existence of an object in a table
    def secure_exists(self, table, conditions):
        if type(conditions) is not tuple :
            raise ValueError('Exists conditions is not tuple', "EXISTS_CONDITIONS", "NOT_TUPLE")

        self.db.connect()
        if table == cfg.TABLE_PATIENTS:
            self.db.cursor.execute(("SELECT EXISTS(SELECT 1 FROM %s WHERE id = ?)" % cfg.TABLE_PATIENTS), conditions)
        elif table == cfg.TABLE_VARIABLE_INPUTS:
            self.db.cursor.execute(("SELECT EXISTS(SELECT 1 FROM %s WHERE id = ? AND family = ?)" % cfg.TABLE_VARIABLE_INPUTS), conditions)
        else:
            self.db.connection.close()
            raise ValueError("TABLE", "NOT_FOUND")

        res = self.db.cursor.fetchone()[0]
        self.db.connection.close()
        return res
