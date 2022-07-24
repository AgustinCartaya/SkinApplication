# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QApplication, QWidget, QStackedWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QScreen
from PySide6.QtCore import QObject, Signal, Slot

import src.util.util as util
import src.config as cfg

from .views.patients import PatientsView
from .views.create_account import CreateAccountView
from .views.login import LoginView
from .views.add_patient import AddPatientView 
from .views.add_patient_mi import AddPatientMiView
from .views.add_patient_preview import AddPatientPreiewView

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.set_initial_state()
#        self._actual_view = None
        self._layers = QStackedWidget()
        self.setCentralWidget(self._layers)
#        self.actual_view = self._layers

        self._add_patient_view = None
        self.add_patient_mi_view = None


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
        st = util.file_to_string(cfg.GLOBAL_STYLES_PATH_NAME)
        self.setStyleSheet(st)


#    @property
#    def actual_view(self):
#        return self._actual_view

#    @actual_view.setter
#    def actual_view(self, view):
#        self._actual_view = view
#        self.setCentralWidget(self._actual_view)

    def set_view(self, view):
        if self._layers.indexOf(view) == -1:
            self._layers.addWidget(view)
        self._layers.setCurrentWidget(view)


    @Slot(str,str,dict)
    def change_view(self, view_from, view_to, atts):
        if view_to == cfg.CREATE_ACCOUNT_VIEW:
#            self.actual_view = CreateAccountView(self)
            self.set_view(CreateAccountView(self))

        elif view_to == cfg.LOGIN_VIEW:
#            self.actual_view = LoginView(self)
            self.clean_views()
            self.set_view(LoginView(self))

        elif view_to == cfg.PATIENTS_VIEW:
#            self.actual_view = PatientsView(self)
            self.clean_views()
            self.set_view(PatientsView(self))

        elif view_to == cfg.ADD_PATIENT_VIEW:
            if view_from == cfg.PATIENTS_VIEW:
                self._add_patient_view = AddPatientView(self)
            elif view_from == cfg.ADD_PATIENT_MI_VIEW:
                self._add_patient_view.p_info = atts
            elif view_from == cfg.ADD_PATIENT_PREVIEW_VIEW:
                self._layers.removeWidget(self._layers.currentWidget())
#            self.actual_view = self._add_patient_view
            self.set_view(self._add_patient_view)

        elif view_to == cfg.ADD_PATIENT_MI_VIEW:
            if (view_from == cfg.ADD_PATIENT_VIEW and
                self.add_patient_mi_view is None):
                self.add_patient_mi_view = AddPatientMiView(self, atts)
            elif view_from == cfg.ADD_PATIENT_VIEW:
                self.add_patient_mi_view.p_info = atts
            elif view_from == cfg.ADD_PATIENT_PREVIEW_VIEW:
                self._layers.removeWidget(self._layers.currentWidget())
#            if (view_from == cfg.ADD_PATIENT_VIEW and
#                len(self._add_patient_view.p_info['medical_info']) == 0):
#                self.add_patient_mi_view = AddPatientMiView(self, atts)
#            self.actual_view = self.add_patient_mi_view
            self.set_view(self.add_patient_mi_view)

        elif view_to == cfg.ADD_PATIENT_PREVIEW_VIEW:
#            self.actual_view = AddPatientPreiewView(self, atts)
#            self.set_view(AddPatientPreiewView(self, atts))

#            if self.add_patient_preview_view is None:
#                self.add_patient_preview_view = AddPatientPreiewView(self, atts)
#            else:
#                self.add_patient_preview_view.p_info = atts
            self.set_view(AddPatientPreiewView(self, atts))
        print(self._layers.count())

    def clean_views(self):
        nb = self._layers.count()
        for i in range(nb):
            self._layers.removeWidget(self._layers.currentWidget())
        self._add_patient_view = None
        self.add_patient_mi_view = None

#    @property
#    def actual_view(self):
#        return self._actual_view

#    @actual_view.setter
#    def actual_view(self, view):
#        self._actual_view = view
#        self.setCentralWidget(self._actual_view)

#    @Slot(str,str,dict)
#    def change_view(self, view_from, view_to, atts):
#        if view_to == cfg.CREATE_ACCOUNT_VIEW:
#            self.actual_view = CreateAccountView(self)

#        elif view_to == cfg.LOGIN_VIEW:
#            self.actual_view = LoginView(self)

#        elif view_to == cfg.PATIENTS_VIEW:
#            self.actual_view = Patients(self)

#        elif view_to == cfg.ADD_PATIENT_VIEW:
#            if view_from == cfg.PATIENTS_VIEW:
#                self._add_patient_view = AddPatientView(self)
#            elif view_from == cfg.ADD_PATIENT_MI_VIEW:
#                self._add_patient_view.append_medical_information(atts)
#            self.actual_view = self._add_patient_view

#        elif view_to == cfg.ADD_PATIENT_MI_VIEW:
#            if (view_from == cfg.ADD_PATIENT_VIEW and
#                len(self._add_patient_view.p_info['medical_info']) == 0):
#                self.add_patient_mi_view = AddPatientMiView(self, atts)
#            self.actual_view = self.add_patient_mi_view

#        elif view_to == cfg.ADD_PATIENT_PREVIEW_VIEW:
#            self.actual_view = AddPatientPreiewView(self, atts)
