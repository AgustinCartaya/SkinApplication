# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QApplication, QWidget, QStackedWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QScreen
from PySide6.QtCore import QObject, Signal, Slot, QTimer

import src.util.util as util
import src.config as cfg
from PySide6.QtWidgets import QStatusBar
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
from .views.ai_results import AIResultsView
from .views.timeline import TimelineView

from .views.ui.promoted.label import Label


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, ai_dict):
        super(MainWindow, self).__init__()

        self.ai_dict = ai_dict

        self._layers = QStackedWidget()

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.hide()

        self.set_initial_state()
        self.setCentralWidget(self._layers)

        self.lb_message = Label(self.statusBar)
        self.statusBar.addWidget(self.lb_message)


        self.images_view = None
        self.ai_laucher_view = None
        self.timeline_view = None

        self.upsert_patient_view = None
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
        self.statusBar.setStyleSheet(st)


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
                self.upsert_patient_view = UpsertPatientView(self)
            elif view_from == cfg.UPSERT_PATIENT_PREVIEW_VIEW:
                self._layers.removeWidget(self._layers.currentWidget())
            elif view_from == cfg.CHECK_PATIENT_VIEW:
                self.upsert_patient_view = UpsertPatientView(self, atts["patient"], "edit")
            self.set_view(self.upsert_patient_view)

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
            if view_from == cfg.IMAGES_VIEW:
                self.set_view(self.ai_laucher_view)
                self.ai_laucher_view.set_selected_images(atts["selected_images_name"], atts["selected_images"])

            elif view_from == cfg.AI_RESULTS_VIEW:
                self.remove_last_view()

            else:
                self.clean_views()
                self.ai_laucher_view = AILauncherView(self, atts["ai"], atts["patient"], atts["skin_lesion"])
                self.set_view(self.ai_laucher_view)

        elif view_to == cfg.IMAGES_VIEW:
            if atts["collet_mode"]:
                self.images_view = ImagesView(self, atts["images"], atts["patient"], atts["skin_lesion"], atts["collet_mode"], atts["selected_images"])
            else:
                self.images_view = ImagesView(self, atts["images"], atts["patient"], atts["skin_lesion"], atts["collet_mode"])
            self.set_view(self.images_view)

        elif view_to == cfg.AI_RESULTS_VIEW:
            self.set_view(AIResultsView(self, atts["results"], atts["ai"], atts["patient"], atts["skin_lesion"]))

        elif view_to == cfg.TIMELINE_VIEW:
            self.timeline_view = TimelineView(self, atts["patient"], atts["skin_lesion"])
            self.set_view(self.timeline_view)


        print(self._layers.count())

    def remove_last_view(self):
        self._layers.removeWidget(self._layers.currentWidget())
        self._layers.currentWidget().refresh()

    def clean_views(self):
        nb = self._layers.count()
        for i in range(nb):
            self._layers.removeWidget(self._layers.currentWidget())
        self.upsert_patient_view = None
        self.upsert_patient_mi_view = None
        self.images_view = None
        self.ai_laucher_view = None
        self.timeline_view = None

    def closeEvent(self, event):
        nb_widgets = self._layers.count()
        for i in range(nb_widgets):
            self._layers.widget(i).close()

    def show_message(self, text, msg_type):
        self.lb_message.setText(text)
        self.statusBar.show()
        QTimer.singleShot(4000, self.hide_status_bar)

    def hide_status_bar(self):
        self.statusBar.hide()

