import os
import random
from datetime import date
import re
import src.config as cfg
import shutil
from datetime import datetime, timedelta

def uppath(_path, n):
    return os.sep.join(_path.split(os.sep)[:-n])


def gen_path(*args):
    path = ""
    nb = len(args)
    for i in range(nb):
        if i < nb-1:
            path = path + args[i] + cfg._S
        else:
            path = path + args[i]
    return path


def _get_file_path_name(path, name):
    if name is None:
        return path
    else:
        return gen_path(path,name)


# verification
def is_dir(path, name=None):
    return os.path.isdir(_get_file_path_name(path,name))


def is_file(path, name=None):
    return os.path.isfile(_get_file_path_name(path,name))


# obtaining list
def get_file_dir_list(path):
    return os.listdir(path)


def get_file_list(path):
    return [name for name in get_file_dir_list(path) if os.path.isfile(gen_path(path,name))]


def get_dir_list(path):
    return [name for name in get_file_dir_list(path) if os.path.isdir(gen_path(path,name))]


# file traitement
def read_file(path, name=None):
    file_path_name = _get_file_path_name(path, name)

    if is_file(file_path_name):
        file_content = ""
        with open(file_path_name, 'r') as f:
            file_content = f.read()
        return file_content
    else:
        return ""


def read_file_list(path, name=None, sep="\n"):
    lst = str_to_list(read_file(path, name), sep)
    return lst


def create_file(content, path, name=None):
    file_path_name = _get_file_path_name(path, name)
    with open(file_path_name, 'w') as f:
        f.write(content)


def apped_to_file(text, path, name=None):
    file_path_name = _get_file_path_name(path, name)
    with open(file_path_name, 'a') as f:
        f.write(text)

def delete_file(path, name=None):
    file_path_name = _get_file_path_name(path, name)
    if is_file(file_path_name):
        os.remove(file_path_name)

# create dir
def create_dir(path, name=None):
    if name is None:
        os.mkdir(path)
    else:
        os.mkdir(gen_path(path,name))


# copy
def copy_file(src, target):
    shutil.copy(src, target)


# sorting
def sort_list_of_tuples(list, index, asc=True):
    return sorted(list, key=lambda tup: tup[index], reverse=(not asc))


def sort_list(list, asc=True):
    return sorted(list, reverse=(not asc))


def file_name_to_title(txt):
    return txt.replace("_", " ").capitalize()


def title_to_file_name(txt):
    return re.sub(' +', ' ', txt.strip()).replace(" ", "_").lower()


def str_to_list(text, sep="\n"):
    return [s.strip() for s in list(filter(lambda x: len(x.strip()) > 0, text.split(sep)))]


def calc_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def generate_id(base_text):
    return base_text[:2].upper() + str(random.randint(1000, 9999)) + base_text[-2:].upper()


def in_range(val, min, max, include=True):
    if include:
        if val >= min and val <= max:
            return True
    else:
        if val > min and val < max:
            return True
    return False


def str_to_date(text):
    return datetime.strptime(text, '%d-%m-%Y')


def strs_to_dates(*args):
    lst = []
    for t in args:
        if type(t) == datetime:
            lst.append(t)
        else:
            lst.append(str_to_date(t))
    return lst


def compare_with_dates(val_1, val_2):
    if type(val_1) == datetime and type(val_2) == str:
        val_2 = str_to_date(val_2)
    elif type(val_2) == datetime and type(val_1) == str:
        val_1 = str_to_date(val_1)
    return val_1 == val_2


def in_range_with_dates(val, min, max, include=True):
    if type(max) == datetime or type(min) == datetime or type(val) == datetime:
        (val, min, max) = strs_to_dates(val, min, max)
    return in_range(val, min, max, include)


def contains_one(src, values, case_sensitive = True):
    if type(values) == str:
        if case_sensitive:
            if values in src:
                return True
        else:
            if values.lower() in src.lower():
                return True

    elif type(values) == list:
        for val in values:
            if val in src:
                return True
    return False


def get_in_range_value(val, min, max):
    if val > max:
        return max
    elif val < min:
        return min
    return val


def get_file_name_extension(path):
    return os.path.basename(path)


def get_file_name(path):
    _fe = get_file_name_extension(path).split('.')
    if len(_fe) > 2:
        return ".".join(_fe[0:-1])
    return _fe[0]
