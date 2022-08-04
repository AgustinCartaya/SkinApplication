from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QApplication

import src.util.util as util
class Label(QLabel):

    def __init__(self, *args, **kwards):
        QLabel.__init__(self, *args, **kwards)


    def set_title(self, title):
        self.setProperty("title", title)

    def set_decoration(self, decoration):
        self.setProperty("decoration", decoration)

    def setText(self, text, colon = False):
        if type(text) in (list, tuple):
            text = " ".join(text)
        elif type(text) in (int, float):
            text = str(text)
        if colon:
            text = text + " :"
        super().setText(util.file_name_to_title(text))
