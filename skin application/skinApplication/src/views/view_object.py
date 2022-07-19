# python common
import os
from pathlib import Path
import sys

from abc import ABC, abstractmethod

# Qt common
from PySide6.QtCore import QObject, Signal, Slot, QDate   
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

# My common
import src.config as cfg
from src.db_controllers.db_connection import DBConnection

class ViewObject(QWidget, QObject):

    def __init__(self, mw):
        super(ViewObject, self).__init__()
        self.MW = mw

    @abstractmethod
    def load_ui(self):
        pass

    @abstractmethod
    def connect_ui_signals(self):
        pass

    def load_test_ui(self, ui_file_name):
       loader = QUiLoader()
       ui_path = os.fspath(Path(__file__).resolve().parent / "ui"/ ui_file_name)
       ui_file = QFile(ui_path)
       ui_file.open(QFile.ReadOnly)
       loader.load(ui_file, self)
       ui_file.close()