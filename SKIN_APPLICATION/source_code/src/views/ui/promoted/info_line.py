from .promoted_container import *

class InfoLine(PromotedContainer):

    def __init__(self, parent):
        super().__init__(parent)
        self._pre_charge()

    def _pre_charge(self):
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(50)

    def initialize(self, info_list):
        for info in info_list:
            self.c_info = QFrame(self)
            self.ly_info = QHBoxLayout(self.c_info)

            self.lb_info_name = Label(self.c_info)
            self.lb_info_name.setText(tf.f(info[0], translate=False, format=True, colon=True))
            self.ly_info.addWidget(self.lb_info_name)

            self.i_info_content = Label(self.c_info)
            self.i_info_content.setText(tf.f(info[1], translate=False))
            self.ly_info.addWidget(self.i_info_content)

            self.layout.addWidget(self.c_info, 0, Qt.AlignHCenter)

