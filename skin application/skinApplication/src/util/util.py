import os
from os.path import exists
import random


def uppath(_path, n):
    return os.sep.join(_path.split(os.sep)[:-n])

def file_to_string(file_path_name):
    _file = open(file_path_name)
    return _file.read()

def generate_id(base_text):

    return base_text[:2].upper() + str(random.randint(1000,9999)) + base_text[-2:].upper()

