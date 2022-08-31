from PySide6.QtWidgets import ( QFrame,
                                QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout,
                                QSpacerItem, QSizePolicy)

from PySide6.QtCore import Qt, Signal, Slot, QSize

from .label import Label
from .button import Button
from .line_edit import LineEdit

import src.util.util as util
import src.util.data_cleaner as data_cleaner
import src.util.text_filter as tf

from abc import ABC, abstractmethod


class PromotedContainer(QFrame):

    def __init__(self, parent):
        QFrame.__init__(self, parent)

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def _pre_charge(self):
        pass
