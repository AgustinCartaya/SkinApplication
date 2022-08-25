from .promoted_container import *

from PySide6.QtWidgets import QScrollArea, QWidget

class AIPreview(PromotedContainer):

    s_launch_ai = Signal(str)
    def __init__(self, parent):
        super().__init__(None)

        self.ai_name = ""
        self.ai_description = ""
        self.ai_results = ""

        self._pre_charge()

    def initialize(self, ai_name, ai_description, ai_results, ai_launch_receaver):
        self.ai_name = ai_name
        self.ai_description = ai_description
        self.ai_results = ai_results
        self.s_launch_ai.connect(ai_launch_receaver)

        self.__create_launch_button()
        self.__create_description()
        self.__create_results()

        if len(self.ai_results) > 0:
            self.__show_results()
        else:
            self.c_results.hide()

    def _pre_charge(self):
        self.setMinimumSize(QSize(200, 100))

        self.p_layout = QVBoxLayout(self)
        self.p_layout.setContentsMargins(0, 0, 0, 0)

        self.__create_scroll_area()

    def __create_scroll_area(self):
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.p_layout.addWidget(self.scroll_area)

        self.c_scroll_area = QWidget(self.scroll_area)
        self.scroll_area.setWidget(self.c_scroll_area)
        self.ly_scroll_area = QVBoxLayout(self.c_scroll_area)

        # content layout
        self.layout = QVBoxLayout()
        self.layout.setSpacing(20)
        self.ly_scroll_area.addLayout(self.layout)

        # spacer
        self.vs_description_down = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.ly_scroll_area.addItem(self.vs_description_down)

    def __create_launch_button(self):
        self.bt_lauch = Button(self)
        self.bt_lauch.setText(self.ai_name)
        self.layout.addWidget(self.bt_lauch, 0, Qt.AlignHCenter)
        self.bt_lauch.clicked.connect(self.__launch_ai)

    def __create_description(self):
        self.c_description = QFrame(self)

        self.ly_description = QVBoxLayout(self.c_description)
        self.ly_description.setSpacing(12)
        self.ly_description.setContentsMargins(0, 0, 0, 0)

        # title
        self.lb_description = Label(self.c_description)
        self.lb_description.setText("Description")
        self.lb_description.setMaximumSize(QSize(16777215, 20))
        self.ly_description.addWidget(self.lb_description, 0, Qt.AlignHCenter)

        # content
        self.i_description = Label(self.c_description)
        self.i_description.setAlignment(Qt.AlignCenter)
        self.i_description.setWordWrap(True)
        self.i_description.setText(self.ai_description)
        self.ly_description.addWidget(self.i_description, 0, Qt.AlignTop)

        # read more
        self.i_read_more = Button(self.c_description)
#        self.i_read_more.setMaximumSize(QSize(16777215, 20))
        self.i_read_more.setText("Read more")
        self.ly_description.addWidget(self.i_read_more, 0, Qt.AlignHCenter)

        self.layout.addWidget(self.c_description)

    def __create_results(self):
        self.c_results = QFrame(self)

        self.ly_results = QVBoxLayout(self.c_results)
        self.ly_results.setSpacing(16)
        self.ly_results.setContentsMargins(0, 0, 0, 0)

        # title
        self.lb_results = Label(self.c_results)
        self.lb_results.setText("Results")
        self.lb_results.setMaximumSize(QSize(16777215, 20))
        self.ly_results.addWidget(self.lb_results, 0, Qt.AlignHCenter)

        # content
        self.ly_form_results = QFormLayout()
        self.ly_form_results.setVerticalSpacing(12)
        self.ly_results.addLayout(self.ly_form_results)

        self.layout.addWidget(self.c_results)

    def __show_results(self):
        self.c_description.hide()
        self.c_results.show()
        count = 0

        for res_name, res_content in self.ai_results.items():
            # Result name
            lb_res_name = Label(self.c_results)
            lb_res_name.setText(res_name)
#            ly_res.addWidget(lb_res_name)
            self.ly_form_results.setWidget(count, QFormLayout.LabelRole, lb_res_name)

            # Result Content
            lb_res_content = Label(self.c_results)
            lb_res_content.setText(res_content)
            self.ly_form_results.setWidget(count, QFormLayout.FieldRole, lb_res_content)

            count = count +1

    @Slot()
    def __launch_ai(self):
        self.s_launch_ai.emit(self.ai_name)

    def add_results(self, results):
        self.ai_results = results
        self.__show_results()
