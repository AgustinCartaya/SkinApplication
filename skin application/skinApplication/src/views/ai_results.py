from .view_object import *
from .ui.ui_ai_results import Ui_ai_results
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy, QFrame, QFileDialog
from .ui.promoted.label import Label

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

        # navigator
        self.ui.bt_relaunch.set_position(2)

        # title
        self.ui.lb_ai_name.setText(tf.f(self.ai.name, translate=False))

    def connect_ui_signals(self):
        self.ui.bt_back.clicked.connect(self.__back)
        self.ui.bt_relaunch.clicked.connect(self.__relaunch)

    def __carge_results(self):
        for res_name, res_content in self.results.items():
            ly_result = QHBoxLayout()
            ly_result.setContentsMargins(0, 0, 0, 0)
            ly_result.setSpacing(4)

            lb_result_name = Label(self.ui.c_results)
            lb_result_name.setText(tf.f(res_name, colon=True, format=True))
            ly_result.addWidget(lb_result_name)

            lb_result_content = Label(self.ui.c_results)
            lb_result_content.setText(tf.f(res_content, translate=False))
            ly_result.addWidget(lb_result_content)

            # spacer
            hs = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Fixed)
            ly_result.addItem(hs)


            self.ui.ly_results_content.addLayout(ly_result)

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
        self.skl.update_data()

        TimelinePoint.upsert_point(self.skl)

