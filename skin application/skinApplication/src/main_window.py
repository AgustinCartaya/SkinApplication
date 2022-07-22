# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QScreen
from PySide6.QtCore import QObject, Signal, Slot   
import src.util.util as util

from .config import *
from .views.patients import Patients
from .views.create_account import CreateAccountView
from .views.login import LoginView
from .views.add_patient import AddPatientView 
from .views.add_patient_p2 import AddPatientP2View

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.set_initial_state()
        self._actual_view = None


    def set_initial_state(self):
        self.setWindowTitle("Skin app")
        self.setMinimumSize(1000, 650)
        self.center()
        self.load_style_sheet()
        # self.showMaximized()

    def center(self):
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

    def load_style_sheet(self):
        st = util.file_to_string(
            util.uppath(__file__, 1) + "/views/ui/styles/global.css")
        self.setStyleSheet(st)

    @property
    def actual_view(self):
        return self._actual_view

    @actual_view.setter
    def actual_view(self, view):
        self._actual_view = view
        self.setCentralWidget(self._actual_view)

    @Slot(str,str,str)  
    def change_view(self, view_from, view_to, atts):
        if view_to == CREATE_ACCOUNT_VIEW:
            self.actual_view = CreateAccountView(self)
        elif view_to == LOGIN_VIEW:
            self.actual_view = LoginView(self)
        elif view_to == PATIENTS_VIEW:
            self.actual_view = Patients(self)
        elif view_to == ADD_PATIENT_VIEW:
            self.actual_view = AddPatientView(self)
        elif view_to == ADD_PATIENT_P2_VIEW:
            self.actual_view = AddPatientP2View(self)

