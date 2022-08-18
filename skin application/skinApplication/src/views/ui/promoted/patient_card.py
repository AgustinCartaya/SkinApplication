from PySide6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout, QApplication)

from PySide6.QtCore import Qt
from .label import Label

from src.objects.patient import Patient
from PySide6.QtCore import Signal


class PatientCard(QFrame):

    s_check_patient = Signal(str)
    def __init__(self, parent, patient, receaver):
        QFrame.__init__(self, None)

        self.p = patient
        self.s_check_patient.connect(receaver.check_patient)

        self.__create()

    def __create(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.__create_content_center()
        self.__create_content_bottom()

        self.layout.setStretch(0, 5)
        self.layout.setStretch(1, 1)

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
        self.lb_last_name.setText(self.p.last_name.upper())
        ly_center_name.addWidget(self.lb_last_name, 0, Qt.AlignCenter)

        self.lb_first_name = Label(self.c_center)
        self.lb_first_name.setText(self.p.first_name)
        ly_center_name.addWidget(self.lb_first_name, 0, Qt.AlignCenter)

    def __create_content_bottom(self):
        self.c_bottom = QFrame(self)
        self.c_bottom.setObjectName(u"c_bottom")
        ly_bottom = QVBoxLayout(self.c_bottom)
        self.layout.addWidget(self.c_bottom)

        self.lb_id = Label(self.c_bottom)
        self.lb_id.setObjectName(u"lb_id")
        self.lb_id.setText(self.p.id)
        ly_bottom.addWidget(self.lb_id, 0, Qt.AlignCenter)

    def setTitle(self, type_info):
        # a modificar
        lb_text = Label(self)
        lb_text.setText(getattr(self.p, type_info))
#            if len(text) > 10:
#                bt.setText(text[:10] + "...")
#            else:
#                bt.setText(text)
#            bt.setMinimumSize(QSize(100, 100))
        self.layout.addWidget(lb_text, 0, Qt.AlignCenter)

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
