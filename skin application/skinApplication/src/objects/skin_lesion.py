# This Python file uses the following encoding: utf-8
from .data_object import *

class SkinLesion(DataObject):
    def __init__(self, number, name, diameter, type, risk, notes, *args):

        self.number = number
        self.name = name
        self.diameter = diameter
        self.type = type
        self.risk = risk
        self.notes = notes

        if len(args) > 0:
            self.images = args[0]
            if len(args) > 1:
                self.ai_results = [1]

    def to_string(self):
        return  ("(" + str(self.number) + ", " +
            self.name + ", " +
            str(self.diameter) + ", " +
            self.type + ", " +
            self.risk + ", " +
            self.notes + ", " +
            ")")
