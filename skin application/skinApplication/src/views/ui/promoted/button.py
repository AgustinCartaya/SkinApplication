# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QApplication

class Button(QPushButton):

    BT_ADD = 1
    BT_CANCEL = 2
    BT_DELETE = 3
    def __init__(self, *args, **kwards):
        QPushButton.__init__(self, *args, **kwards)
        self.set_type(Button.BT_ADD)

    def repaint(self):
        self.setStyle(QApplication.style())

    def set_type(self, type):
        if type == Button.BT_ADD:
            self.setProperty("type", "add")
        if type == Button.BT_CANCEL:
            self.setProperty("type", "cancel")
        if type == Button.BT_DELETE:
            self.setProperty("type", "delete")

