from PySide6.QtCore import Qt

from PySide6.QtWidgets import QLabel
#from PySide6.QtWidgets import QApplication

# to delete
from src.objects.variable_input import VariableInput
import src.util.util as util


class Label(QLabel):

    def __init__(self, *args, **kwards):
        QLabel.__init__(self, *args, **kwards)

    def set_title(self, title):
        self.setProperty("title", title)

    def set_bold(self, bold):
        self.setProperty("bold", bold)

    def set_decoration(self, decoration):
        self.setProperty("decoration", decoration)

    def setText(self, text, center=False):
        # center
        if center:
            self.setAlignment(Qt.AlignCenter)

        super().setText(text)
