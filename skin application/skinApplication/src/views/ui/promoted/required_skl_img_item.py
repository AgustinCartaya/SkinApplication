from .promoted_container import *

from PySide6.QtWidgets import QApplication


class RequiredSklImgItem(PromotedContainer):

    s_clicked = Signal(str)
    def __init__(self, parent):
        super().__init__(parent)
        self.img_name = ""
        self.min = 0
        self.max = 0
        self.selected = 0
        self._pre_charge()

    def initialize(self, img_name, min, max, selected=0, click_receaver=None):
        self.img_name = img_name
        self.min = min
        self.max = max
        self.selected = selected

        if click_receaver is not None:
            self.s_clicked.connect(click_receaver)

        self.__fill_content()

    def _pre_charge(self):
        self.layout = QHBoxLayout(self)
        self.layout.setObjectName(u"layout")
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.__create_labels()

    def __create_labels(self):
        self.lb_img_name = Label(self)
        self.layout.addWidget(self.lb_img_name)

        self.lb_min = Label(self)
        self.layout.addWidget(self.lb_min, 0, Qt.AlignHCenter)

        self.lb_max = Label(self)
        self.layout.addWidget(self.lb_max, 0, Qt.AlignHCenter)

        self.lb_selected = Label(self)
        self.layout.addWidget(self.lb_selected, 0, Qt.AlignHCenter)

    def __fill_content(self):
        self.lb_img_name.setText(self.img_name, format=True)
        self.lb_min.setText(self.min)
        self.lb_max.setText(self.max)
        self.set_selected_number(self.selected)

    def set_selected_number(self, number):
        self.lb_selected.setText(number)

        if number < self.min:
            self.setProperty("satisfied", False)
        else:
            self.setProperty("satisfied", True)

        self.repaint()

    def repaint(self):
        self.setStyle(QApplication.style())

    def mousePressEvent(self, arg):
        self.s_clicked.emit(self.img_name)
