from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QApplication

class LineEdit(QLineEdit):
    def __init__(self, *args, **kwards):
        QLineEdit.__init__( self, *args, **kwards)
        self.change_color()
        self.textChanged.connect(self.change_color)


    def change_color(self):
        self.setProperty("empty", self.text() == '' )
        print(self.property("empty"))
        self.setStyle(QApplication.style())

