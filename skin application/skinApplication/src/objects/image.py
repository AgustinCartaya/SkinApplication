# This Python file uses the following encoding: utf-8
from .data_object import *

class Image(DataObject):
    def __init__(self, src):
        self.src = src


