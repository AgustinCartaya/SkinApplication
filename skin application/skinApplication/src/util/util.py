import os
from os.path import exists
import random
from datetime import date

def uppath(_path, n):
    return os.sep.join(_path.split(os.sep)[:-n])

def file_to_string(file_path_name):
    _file = open(file_path_name)
    return _file.read()

def generate_id(base_text):
    return base_text[:2].upper() + str(random.randint(1000,9999)) + base_text[-2:].upper()

def sort_list_of_tuples(list, index, asc=True):
    return sorted(list, key=lambda tup: tup[index], reverse = not asc)

def sort_list(list, asc=True):
    return sorted(list, reverse = not asc)

def calc_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
