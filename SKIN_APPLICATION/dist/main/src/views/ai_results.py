# @autor: Agustin CARTAYA

from .view_object import *
from .ui.ui_ai_results import Ui_ai_results
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy, QFrame, QFileDialog
from .ui.promoted.label import Label
from .ui.promoted.form_item import FormItem

from src.objects.timeline_point import TimelinePoint


class AIResultsView(ViewObject):
    def __init__(self, mv, results, ai, patient, skin_lesion):
        super().__init__(mv)

        self.results = results
        self.ai = ai
        self.p = patient
        self.skl = skin_lesion

        self.load_ui()
        self.connect_ui_signals()

        self.__carge_results()

    def load_ui(self):
        self.ui = Ui_ai_results()
        self.ui.setupUi(self)

        # title
        self.ui.lb_ai_name.setText(tf.f(self.ai.name, translate=False))
        self.ui.lb_title.set_title(1)
        self.ui.lb_ai_name.set_title(1)
        self.ui.lb_results.set_title(2)

        # navigator
        self.ui.bt_relaunch.set_position(2)


    def connect_ui_signals(self):
        self.ui.bt_back.clicked.connect(self.__back)
        self.ui.bt_relaunch.clicked.connect(self.__relaunch)

    def __carge_results(self):
        for res_name, res_content in self.results.items():
            res = FormItem(self.ui.c_results)
            res.initialize(res_name, res_content)
            self.ui.ly_results_content.addWidget(res)

    @Slot()
    def __back(self):
        self.__save_results()
        self.ai.reset_actual_patient_and_skin_lesion()
        self.s_change_view.emit(cfg.AI_RESULTS_VIEW, cfg.UPSERT_SKIN_LESION_VIEW, {"patient" : self.p, "skin_lesion": self.skl})

    def __relaunch(self):
        self.__save_results()
        self.s_change_view.emit(cfg.AI_RESULTS_VIEW, cfg.AI_LAUNCHER_VIEW, {})

    def __save_results(self):
        self.skl.ai_results[self.ai.name] = self.results
        self.skl.update()

        TimelinePoint.upsert_point(self.skl)

