from .button import *

class NavigatorButton(Button):

    def __init__(self, *args, **kwards):
        Button.__init__(self, *args, **kwards)

    def set_position(self, pos):
        if pos == 1:
            self.setProperty("position", "top-left")
        elif pos == 2:
            self.setProperty("position", "top-right")
        elif pos == 3:
            self.setProperty("position", "bottom-right")
        elif pos == 4:
            self.setProperty("position", "bottom-left")
