from PySide6.QtCore import Signal, Slot, Qt

from PySide6.QtWidgets import QFrame, QVBoxLayout

#from .label import Label


#import src.util.data_cleaner as data_cleaner
#import src.util.util as util

class FiltersHeader(QFrame):

    s_open = Signal()
    def __init__(self, parent):
        QFrame.__init__(self, parent)

        self.filters_content = None
        self.open = False

    def add_filters_content(self, filters_content):
        self.filters_content = filters_content
        self.close_content()

    def mousePressEvent(self, arg):
        if self.filters_content is not None:
            self.open = not self.open
            if self.open:
                self.open_content()
            else:
                self.close_content()

    def close_content(self):
        self.open = False
        self.filters_content.hide()

    def open_content(self):
        self.open = True
        self.filters_content.show()
        self.s_open.emit()

    def add_open_receaver(self, receaver):
        self.s_open.connect(receaver)

