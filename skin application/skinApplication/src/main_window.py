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
from .views.upsert_patient import UpsertPatientView
from .views.upsert_patient_mi import UpsertPatientMiView
from .views.upsert_patient_preview import UpsertPatientPreiewView
from .views.check_patient import CheckPatientView
from .views.upsert_skin_lesion import UpsertSkinLesionView
from .views.ai_launcher import AILauncherView
from .views.images import ImagesView

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, ai_dict):
        super(MainWindow, self).__init__()

        self.ai_dict = ai_dict

        self.set_initial_state()
        self._layers = QStackedWidget()
        self.setCentralWidget(self._layers)

        self._upsert_patient_view = None
        self.upsert_patient_mi_view = None


    def set_initial_state(self):
        self.setWindowTitle("Skin app")
        self.setMinimumSize(1000, 650)
        self.center()
        self.load_style_sheet()

    def center(self):
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

    def load_style_sheet(self):
        st = util.read_file(cfg.GLOBAL_STYLES_PATH_NAME)
        self.setStyleSheet(st)


    def set_view(self, view):
        if self._layers.indexOf(view) == -1:
            self._layers.addWidget(view)
        self._layers.setCurrentWidget(view)


    @Slot(str,str,dict)
    def change_view(self, view_from, view_to, atts):

        if view_to == cfg.ANCIENT_VIEW:
            self.remove_last_view()

        elif view_to == cfg.CREATE_ACCOUNT_VIEW:
            self.set_view(CreateAccountView(self))

        elif view_to == cfg.LOGIN_VIEW:
            self.clean_views()
            self.set_view(LoginView(self))

        elif view_to == cfg.PATIENTS_VIEW:
            self.clean_views()
            self.set_view(PatientsView(self))

        elif view_to == cfg.UPSERT_PATIENT_VIEW:
            if view_from == cfg.PATIENTS_VIEW:
                self._upsert_patient_view = UpsertPatientView(self)
            elif view_from == cfg.UPSERT_PATIENT_PREVIEW_VIEW:
                self._layers.removeWidget(self._layers.currentWidget())
            elif view_from == cfg.CHECK_PATIENT_VIEW:
                self._upsert_patient_view = UpsertPatientView(self, atts["patient"], "edit")
            self.set_view(self._upsert_patient_view)

        elif view_to == cfg.UPSERT_PATIENT_MI_VIEW:
            if self.upsert_patient_mi_view is None:
                self.upsert_patient_mi_view = UpsertPatientMiView(self, atts["patient"], atts["mode"])
            elif view_from == cfg.UPSERT_PATIENT_PREVIEW_VIEW:
                self._layers.removeWidget(self._layers.currentWidget())
            self.set_view(self.upsert_patient_mi_view)

        elif view_to == cfg.UPSERT_PATIENT_PREVIEW_VIEW:
            self.set_view(UpsertPatientPreiewView(self, atts["patient"], atts["mode"]))

        elif view_to == cfg.CHECK_PATIENT_VIEW:
            self.clean_views()
            self.set_view(CheckPatientView(self, atts["patient_id"]))

        elif view_to == cfg.UPSERT_SKIN_LESION_VIEW:
            self.clean_views()
            self.set_view(UpsertSkinLesionView(self, self.ai_dict, atts["patient"], atts["skin_lesion"]))

        elif view_to == cfg.AI_LAUNCHER_VIEW:
            self.clean_views()
            self.set_view(AILauncherView(self, atts["ai"], atts["patient"], atts["skin_lesion"]))

        elif view_to == cfg.IMAGES_VIEW:
            self.set_view(ImagesView(self))


#        print(self._layers.count())

    def remove_last_view(self):
        self._layers.removeWidget(self._layers.currentWidget())

    def clean_views(self):
        nb = self._layers.count()
        for i in range(nb):
            self._layers.removeWidget(self._layers.currentWidget())
        self._upsert_patient_view = None
        self.upsert_patient_mi_view = None
