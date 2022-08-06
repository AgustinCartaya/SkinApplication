from PySide6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout,
        QGridLayout)

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
        pass
#        print("enterEvent")

    def leaveEvent(self, event):
        pass
#        print("leaveEvent")

    def mousePressEvent(self, arg):
        self.s_check_patient.emit(self.p.id)
