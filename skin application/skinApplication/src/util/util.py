import os
import random
from datetime import date

import src.config as cfg


def uppath(_path, n):
    return os.sep.join(_path.split(os.sep)[:-n])


def file_to_string(file_path_name):
    _file = open(file_path_name)
    return _file.read()


def generate_id(base_text):
    return base_text[:2].upper() + str(random.randint(1000, 9999)) + base_text[-2:].upper()


def sort_list_of_tuples(list, index, asc=True):
    return sorted(list, key=lambda tup: tup[index], reverse=(not asc))


def sort_list(list, asc=True):
    return sorted(list, reverse=(not asc))


def calc_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def read_file_list(file_name, separator="\n", path=cfg.FILES_PATH):

    file_path_name = path + cfg._S + file_name
    _file = open(file_path_name)
    file_lines = _file.read()
    lst = str_to_list(file_lines)
#    for line in file_lines:
#        print(line)
#        if len(line.replace(" ","")) > 0:
#            lst.append(line)
    return lst


def get_file_list(path):
    return os.listdir(path)


def file_name_to_title(txt):
    return txt.replace("_", " ").capitalize()


def title_to_file_name(txt):
    return txt.strip().replace(" ", "_").lower()

def str_to_list(text, sep="\n"):
    return [s.strip() for s in list(filter(None, text.split(sep)))]
