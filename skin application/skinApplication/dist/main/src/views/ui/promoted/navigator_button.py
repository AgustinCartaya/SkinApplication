#from PySide6.QtWidgets import QPushButton
# from PySide6.QtWidgets import QApplication

from .button import *

class NavigatorButton(Button):

    def __init__(self, *args, **kwards):
        Button.__init__(self, *args, **kwards)
#        self.clicked.connect(self.switch)
#        self.select(False)

    def set_position(self, pos):
        if pos == 1:
            self.setProperty("position", "top-left")
        elif pos == 2:
            self.setProperty("position", "top-right")
        elif pos == 3:
            self.setProperty("position", "bottom-right")
        elif pos == 4:
            self.setProperty("position", "bottom-left")

#    def is_selected(self):
#        return self.property("selected")


#    def select(self, value):
#        self.setProperty("selected", value)
#        self.setStyle(QApplication.style())

