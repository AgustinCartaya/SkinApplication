from PySide6.QtWidgets import QFrame, QHBoxLayout
from PySide6.QtCore import Qt
from .label import Label

from PySide6.QtCore import Signal, Slot

class RequiredSklImgItem(QFrame):

    s_clicked = Signal(str)
    def __init__(self, parent, img_name, min, max, selected=0, click_receaver=None):
        QFrame.__init__(self, parent)

        self.img_name = img_name
        self.min = min
        self.max = max
        self.selected = selected

        self.s_clicked.connect(click_receaver)

        self.__create()

    def __create(self):
        self.layout = QHBoxLayout(self)
        self.layout.setObjectName(u"layout")
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.__create_labels()

    def __create_labels(self):
        self.lb_img_name = Label(self)
        self.lb_img_name.setText(self.img_name, format=True)
        self.layout.addWidget(self.lb_img_name)

        self.lb_min = Label(self)
        self.lb_min.setText(self.min)
        self.layout.addWidget(self.lb_min, 0, Qt.AlignHCenter)

        self.lb_max = Label(self)
        self.lb_max.setText(self.max)
        self.layout.addWidget(self.lb_max, 0, Qt.AlignHCenter)

        self.lb_selected = Label(self)
        self.lb_selected.setText(self.selected)
        self.layout.addWidget(self.lb_selected, 0, Qt.AlignHCenter)

    def set_selected_number(self, number):
        self.lb_selected.setText(number)

    def mousePressEvent(self, arg):
        self.s_clicked.emit(self.img_name)
