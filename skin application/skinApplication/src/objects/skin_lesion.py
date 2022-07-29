# This Python file uses the following encoding: utf-8
from .data_object import *

class SkinLesion(DataObject):
    def __init__(self, number, *args):

        self.number = number

        if len(args) > 0:
            self.caracteristics = args[0]
            if len(args) > 1:
                self.images = args[1]
                if len(args) == 3:
                    self.ai_results = args[2]

    def to_string(self):
        return ("(" + str(self.number) + ", " +
            self.caracteristics + ", " +
            self.images + ", " +
            self.ai_results + ", " +
            ")")
