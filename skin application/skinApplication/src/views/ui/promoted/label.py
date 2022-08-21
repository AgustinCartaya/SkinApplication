from PySide6.QtCore import Qt

from PySide6.QtWidgets import QLabel
#from PySide6.QtWidgets import QApplication

import src.util.util as util
import src.util.variable_inputs as var_inputs

class Label(QLabel):

    def __init__(self, *args, **kwards):
        QLabel.__init__(self, *args, **kwards)


    def set_title(self, title):
        self.setProperty("title", title)

    def set_decoration(self, decoration):
        self.setProperty("decoration", decoration)

    def setText(self, text, colon = False, format=False, parenthesis=False, center=False, scale_input=None, before=None):
        if type(text) in (list, tuple):
            text = " ".join(text)
        elif type(text) in (int, float):
            # scaled values
            if scale_input is not None:
                text = var_inputs.get_scalized_str(scale_input[0], text, scale_input[1])
            else:
                text = str(text)
        elif type(text) is bool:
            if text:
                text = "Yes"
            else:
                text = "No"

        # formatting
        if format:
            text = util.file_name_to_title(text)

        # parenthesis
        if parenthesis:
            text = "(" + text + ")"

        # colon
        if colon:
            text = text + " :"

        # center
        if center:
            self.setAlignment(Qt.AlignCenter)

        # before
        if before:
            text = before + text

        super().setText(text)
