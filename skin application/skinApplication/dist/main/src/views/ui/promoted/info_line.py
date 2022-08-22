from PySide6.QtCore import Signal, Slot, Qt

from PySide6.QtWidgets import QFrame, QHBoxLayout, QCheckBox, QSpacerItem, QSizePolicy

from .label import Label

import src.util.util as util

class InfoLine(QFrame):

    def __init__(self, parent):
        QFrame.__init__(self, parent)
        self.__create()

    def __create(self):
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(50)

    def add_info(self, info_list):
        for info in info_list:
            self.c_info = QFrame(self)
            self.ly_info = QHBoxLayout(self.c_info)

            self.lb_info_name = Label(self.c_info)
            self.lb_info_name.setText(info[0], format=True, colon=True)
            self.ly_info.addWidget(self.lb_info_name)

            self.i_info_content = Label(self.c_info)
            self.i_info_content.setText(info[1])
            self.ly_info.addWidget(self.i_info_content)

            self.layout.addWidget(self.c_info, 0, Qt.AlignHCenter)

