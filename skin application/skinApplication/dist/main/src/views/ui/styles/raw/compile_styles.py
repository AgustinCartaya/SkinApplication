import os
from os.path import exists
import random


def uppath(_path, n):
    return os.sep.join(_path.split(os.sep)[:-n])

def file_to_string(file_path_name):
    _file = open(file_path_name)
    return _file.read()

def compile_styles():
    # global
    f_colors = file_to_string(uppath(__file__, 1)+"/colors.css")
    f_global = file_to_string(uppath(__file__, 1)+"/global.css")

    colors = {}
    f_colors = f_colors.replace(";", "")

    for line in f_colors.split('\n'):
        if line.startswith('@'):
            color = line.replace(" ", "").split('=')
            colors[color[0]] = color[1]


    for key in colors:
        f_global = f_global.replace(key, colors[key])

    with open(uppath(__file__,2)+'/global.css', 'w') as f:
        f.write(f_global)

