# @autor: Agustin CARTAYA

import os
from pathlib import Path
import sys

from abc import ABC, abstractmethod

# Qt common

from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QObject, Signal, Slot, QDate, QFile, QRegularExpression
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtUiTools import QUiLoader

# My common
import src.config as cfg
from src.db_controllers.db_connection import DBConnection
import src.internal.errors as err

from .ui.promoted.button import Button
import src.util.data_cleaner as data_cleaner
import src.util.util as util
import src.util.text_filter as tf

class ViewObject(QWidget, QObject):
    s_change_view = Signal(str,str,dict)
    def __init__(self, mv):
        super(ViewObject, self).__init__()
        if mv is not None:
            self.mv = mv
            self.GLOBAL = mv.GLOBAL
            self.s_change_view.connect(mv.change_view)

    @abstractmethod
    def load_ui(self):
        pass

    @abstractmethod
    def connect_ui_signals(self):
        pass

    def refresh(self):
        pass

    def close(self):
        pass

    def show_message(self, text, msg_type):
        self.mv.show_message(text, msg_type)

    def load_test_ui(self, ui_file_name):
       loader = QUiLoader()
       ui_path = os.fspath(Path(__file__).resolve().parent / "ui"/ ui_file_name)
       ui_file = QFile(ui_path)
       ui_file.open(QFile.ReadOnly)
       loader.load(ui_file, self)
       ui_file.close()

    def create_text_validator(self, regex_text):
        return data_cleaner.create_text_validator(regex_text)

