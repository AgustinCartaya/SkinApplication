from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QFormLayout, QWidget, QFrame, QHBoxLayout, QVBoxLayout, QSpacerItem, QScrollArea, QSizePolicy

from .label import Label

class SkinLesionPreviewInfo(QFrame):

    def __init__(self, parent, results, title, is_ai_result = False,  *args, **kwards):
        QFrame.__init__(self, parent)
        self.results = results
        self.title = title
        self.is_ai_result = is_ai_result
#        self.read_more = read_more

        self.__create()

    def __create(self):
        self.setMaximumSize(QSize(16777215, 200))

        self.p_layout = QVBoxLayout(self)
        self.p_layout.setContentsMargins(0, 0, 0, 0)

        self.__create_scroll_area()
        self.__create_title()
        self.__create_content()
#        self.__create_read_more()

        # spacer
        self.vs_description_down = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(self.vs_description_down)

    def __create_scroll_area(self):
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)

        self.c_scroll_area = QWidget(self.scroll_area)
        self.scroll_area.setWidget(self.c_scroll_area)

        self.layout = QVBoxLayout(self.c_scroll_area)
        self.layout.setSpacing(20)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.p_layout.addWidget(self.scroll_area)

#    def __create_read_more(self):
#        self.lb_read_more = Label(self)
#        self.lb_read_more.setText(self.read_more)
#        self.layout.addWidget(self.lb_read_more, 0, Qt.AlignHCenter|Qt.AlignBottom)

    def __create_title(self):
        self.c_title = QFrame(self)
        self.c_title.setMaximumSize(QSize(16777215, 20))

        self.c_title_layout = QHBoxLayout(self.c_title)
        self.c_title_layout.setContentsMargins(0, 0, 0, 0)

        self.lb_title = Label(self.c_title)
        self.lb_title.setText(self.title)
        self.lb_title.setMaximumSize(QSize(16777215, 20))

        self.c_title_layout.addWidget(self.lb_title, 0, Qt.AlignHCenter)

        self.layout.addWidget(self.c_title)


    def __create_content(self):
        self.c_content = QFrame(self)

        self.ly_content = QVBoxLayout(self.c_content)
        self.ly_content.setSpacing(20)
#        self.ly_content.setContentsMargins(9, 9, 9, 9)

        if self.is_ai_result:
            for ai_name, ai_result in self.results.items():
                self.__create_ai_result(ai_name, ai_result)
        else:
            self.__create_single_result(self.results, self.ly_content)


        self.layout.addWidget(self.c_content)


    def __create_ai_result(self, ai_name, ai_result):
        c_ai_result = QFrame(self.c_content)

        ly_ai_result = QVBoxLayout(c_ai_result)
        ly_ai_result.setSpacing(12)
        ly_ai_result.setContentsMargins(0, 0, 0, 0)

        # title
        lb_ai_result_title = Label(c_ai_result)
        lb_ai_result_title.setText(ai_name)
        ly_ai_result.addWidget(lb_ai_result_title)

        # content
        self.__create_single_result(ai_result, ly_ai_result)

        self.ly_content.addWidget(c_ai_result)

    def __create_single_result(self, result, parent_layout):
        c_single_content = QFrame(self)

        ly_single_content = QFormLayout(c_single_content)
#        ly_single_content.setVerticalSpacing(9)
        ly_single_content.setContentsMargins(0, 0, 0, 0)

        count = 0
        for name, value in result.items():
            lb_result_title = Label(c_single_content)
            lb_result_title.setText(name, colon=True, format=True)
            ly_single_content.setWidget(count, QFormLayout.LabelRole, lb_result_title)

            if type(value) in (tuple, list):
                value = " ".join(value)
            elif type(value) in (int, float):
                value = str(value)

            lb_result_content = Label(c_single_content)
            lb_result_content.setText(value)
            ly_single_content.setWidget(count, QFormLayout.FieldRole, lb_result_content)

            count = count +1

        parent_layout.addWidget(c_single_content)

