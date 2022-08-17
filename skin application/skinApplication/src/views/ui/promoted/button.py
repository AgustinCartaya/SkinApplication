# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Signal, Slot, Qt

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

    def __init__(self, *args, **kwards):
        QPushButton.__init__(self, *args, **kwards)
        self.set_type(Button.BT_ADD)
        self.action_value = ""

    def repaint(self):
        self.setStyle(QApplication.style())

    def set_type(self, type):
        self.setProperty("type", type)
#        if type == Button.BT_ADD:
#            self.setProperty("type", Button.BT_ADD)
#        elif type == Button.BT_CANCEL:
#            self.setProperty("type", Button.BT_ADD)
#        elif type == Button.BT_DELETE:
#            self.setProperty("type", Button.BT_ADD)

    def set_icon(self, icon):
        self.setProperty("bt_icon", icon)
#        if icon == Button.IC_UP:
#            self.setProperty("icon", Button.IC_UP)
#        elif icon == Button.IC_RIGHT:
#            self.setProperty("icon", Button.IC_RIGHT)
#        elif icon == Button.IC_DOWN:
#            self.setProperty("icon", Button.IC_DOWN)
#        elif icon == Button.IC_LEFT:
#            self.setProperty("icon", Button.IC_LEFT)

    def set_action_value(self, action_value):
        self.action_value = action_value
