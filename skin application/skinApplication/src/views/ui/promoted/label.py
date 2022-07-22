from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QApplication


class Label(QLabel):

    def __init__(self, *args, **kwards):
        QLabel.__init__(self, *args, **kwards)


    def set_title(self, title):
        self.setProperty("title", title)
