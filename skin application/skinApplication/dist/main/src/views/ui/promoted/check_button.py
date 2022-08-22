#from PySide6.QtWidgets import QPushButton
#from PySide6.QtWidgets import QApplication

from .button import *

class CheckButton(Button):

    s_switch = Signal(Button)
    def __init__(self, *args, **kwards):
        Button.__init__(self, *args, **kwards)
        self.clicked.connect(self.__switch_attempt)
        self.select(False)
        self.has_group = False

    @Slot()
    def __switch_attempt(self):
        if self.has_group:
            self.s_switch.emit(self)
        else:
            self.switch()

    def switch(self):
        self.select(not self.property("selected"))

    def is_selected(self):
        return self.property("selected")

    def select(self, value):
        self.setProperty("selected", value)
        self.repaint()
#        self.setStyle(QApplication.style())

#    def add_group(self, group):
#        self.__group = group


#    def deselect_others(self):
#        for bt in self.__group:
#            bt.select(False)


    def add_group(self, group_receaver):
        self.s_switch.connect(group_receaver)
        self.has_group = True
