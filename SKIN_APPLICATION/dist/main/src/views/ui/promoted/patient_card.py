from .promoted_container import *
from PySide6.QtWidgets import QApplication

from src.objects.patient import Patient


class PatientCard(PromotedContainer):

    s_check_patient = Signal(str)
    def __init__(self, parent):
        super().__init__(None)

        self.p = None
        self._pre_charge()

    def _pre_charge(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.__create_content_center()
        self.__create_content_bottom()

        self.layout.setStretch(0, 5)
        self.layout.setStretch(1, 1)

    def initialize(self, patient, click_receaver):
        self.p = patient
        self.s_check_patient.connect(click_receaver)
        self.__fill_information()

    def __create_content_center(self):
        self.c_center = QFrame(self)
        self.c_center.setObjectName(u"c_center")
        ly_center = QVBoxLayout(self.c_center)
        self.layout.addWidget(self.c_center)

        self.c_center_name = QFrame(self)
        ly_center_name = QVBoxLayout(self.c_center_name)
        ly_center_name.setContentsMargins(0, 0, 0, 0)
        ly_center.addWidget(self.c_center_name, 0, Qt.AlignCenter)

        self.lb_last_name = Label(self.c_center)
        ly_center_name.addWidget(self.lb_last_name, 0, Qt.AlignCenter)

        self.lb_first_name = Label(self.c_center)
        ly_center_name.addWidget(self.lb_first_name, 0, Qt.AlignCenter)

    def __create_content_bottom(self):
        self.c_bottom = QFrame(self)
        self.c_bottom.setObjectName(u"c_bottom")
        ly_bottom = QVBoxLayout(self.c_bottom)
        self.layout.addWidget(self.c_bottom)

        self.lb_id = Label(self.c_bottom)
        self.lb_id.setObjectName(u"lb_id")
        ly_bottom.addWidget(self.lb_id, 0, Qt.AlignCenter)

    def __fill_information(self):
        self.lb_last_name.setText(tf.f(self.p.last_name, translate=False, upper=True))
        self.lb_first_name.setText(tf.f(self.p.first_name, translate=False))
        self.lb_id.setText(self.p.id)

    def enterEvent(self, event):
        self.c_center.setProperty("hover", True)
        self.c_bottom.setProperty("hover", True)
        self.repaint()

    def leaveEvent(self, event):
        self.c_center.setProperty("hover", False)
        self.c_bottom.setProperty("hover", False)
        self.repaint()

    def repaint(self):
        self.setStyle(QApplication.style())

    def mousePressEvent(self, arg):
        self.s_check_patient.emit(self.p.id)
