from PySide6.QtWidgets import QFrame
from PySide6.QtWidgets import QApplication

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QFormLayout, QFrame, QHBoxLayout, QVBoxLayout, QLabel

class ResultPreview(QFrame):

    def __init__(self, ann, title, read_more,  *args, **kwards):
        QFrame.__init__(self, *args, **kwards)
        self.ann = ann
        self.title = title
        self.read_more = read_more

        self.__create()

    def __create(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.__create_title()
        self.__create_content()
        self.__create_read_more()


    def __create_read_more(self):
        self.lb_read_more = QLabel(self)
        self.lb_read_more.setText(self.read_more)
        self.layout.addWidget(self.lb_read_more, 0, Qt.AlignHCenter|Qt.AlignBottom)

    def __create_title(self):
        self.c_title = QFrame(self)
        self.c_title.setMaximumSize(QSize(16777215, 20))

        self.c_title_layout = QHBoxLayout(self.c_title)
        self.c_title_layout.setContentsMargins(0, 0, 0, 0)

        self.lb_title = QLabel(self.c_title)
        self.lb_title.setText(self.title)
        self.lb_title.setMaximumSize(QSize(16777215, 20))

        self.c_title_layout.addWidget(self.lb_title, 0, Qt.AlignHCenter)

        self.layout.addWidget(self.c_title)


    def __create_content(self):
        self.c_content = QFrame(self)

        self.c_content_layout = QFormLayout(self.c_content)
        self.c_content_layout.setVerticalSpacing(12)
        self.c_content_layout.setContentsMargins(9, 0, 9, 0)

        count = 0
        for key in self.ann:
            lb_ann_title = QLabel(self.c_content)
            lb_ann_title.setText(key)
            self.c_content_layout.setWidget(count, QFormLayout.LabelRole, lb_ann_title)

            lb_ann_content = QLabel(self.c_content)
            lb_ann_content.setText(self.ann[key])
            self.c_content_layout.setWidget(count, QFormLayout.FieldRole, lb_ann_content)

            count = count +1


        self.layout.addWidget(self.c_content)
