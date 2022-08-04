from PySide6.QtWidgets import QFrame, QHBoxLayout
from PySide6.QtCore import Qt
from .label import Label

from PySide6.QtCore import Signal, Slot

class RequiredImageType(QFrame):

#    s_edit_items = Signal(str)
    def __init__(self, parent, img_name, min, max):
        QFrame.__init__(self, parent)

        self.img_name = img_name
        self.min = min
        self.max = max

        self.__create()


    def __create(self):
        self.layout = QHBoxLayout(self)
        self.layout.setObjectName(u"layout")
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.__create_labels()

    def __create_labels(self):
        self.lb_img_name = Label(self)
        self.lb_img_name.setText(self.img_name)
        self.layout.addWidget(self.lb_img_name)

        self.lb_min = Label(self)
        self.lb_min.setText(str(self.min))
        self.layout.addWidget(self.lb_min, 0, Qt.AlignHCenter)

        self.lb_max = Label(self)
        self.lb_max.setText(str(self.max))
        self.layout.addWidget(self.lb_max, 0, Qt.AlignHCenter)

        self.lb_selected = Label(self)
#        self.lb_selected.setText(self.img_name)
        self.layout.addWidget(self.lb_selected, 0, Qt.AlignHCenter)
