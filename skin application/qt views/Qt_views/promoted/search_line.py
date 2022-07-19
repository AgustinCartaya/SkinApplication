from PySide6.QtWidgets import QFrame
# from PySide6.QtWidgets import QApplication


class SearchLine(QFrame):

    def __init__(self, *args, **kwards):
        QFrame.__init__(self, *args, **kwards)
#        self.change_color()
#        self.textChanged.connect(self.change_color)


#    def change_color(self):
#        self.setProperty("empty", self.text() == '' )
#        print(self.property("empty"))
#        self.setStyle(QApplication.style())
