from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QApplication


class CheckButton(QPushButton):

    def __init__(self, *args, **kwards):
        QPushButton.__init__(self, *args, **kwards)
        self.clicked.connect(self.switch)
        self.select(False)
        self.__group = None

    def switch(self):
        if self.__group is None:
            self.select(not self.property("selected"))
        else:
            if not self.property("selected"):
                self.deselect_others()
                self.select(True)

    def is_selected(self):
        return self.property("selected")

    def select(self, value):
        self.setProperty("selected", value)
        self.setStyle(QApplication.style())

    def add_group(self, group):
        self.__group = group

    def deselect_others(self):
        for bt in self.__group:
            bt.select(False)
