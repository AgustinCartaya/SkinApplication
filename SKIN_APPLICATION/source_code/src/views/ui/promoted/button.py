# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QPushButton, QApplication
from PySide6.QtCore import Qt, Signal, Slot

class Button(QPushButton):

    BT_ADD = "add"
    BT_CANCEL = "cancel"
    BT_DELETE = "delete"

    IC_UP = "up"
    IC_RIGHT = "right"
    IC_DOWN = "down"
    IC_LEFT = "left"
    IC_LIST = "list"
    IC_MOSAICO = "mosaico"

    PADDING_S = "s"
    PADDING_M = "m"
    PADDING_L = "l"

    def __init__(self, *args, **kwards):
        QPushButton.__init__(self, *args, **kwards)
        self.set_type(Button.BT_ADD)
        self.set_padding(Button.PADDING_L)
        self.action_value = ""

    def set_padding(self, padding):
        self.setProperty("padding", padding)

    def set_type(self, type):
        self.setProperty("type", type)

    def set_icon(self, icon):
        self.setProperty("bt_icon", icon)

    def set_action_value(self, action_value):
        self.action_value = action_value

    def set_decorator(self, decorator):
        self.setProperty("decorator", decorator)

    def get_decorator(self, decorator):
        return self.property(decorator)

    def repaint(self):
        self.setStyle(QApplication.style())
