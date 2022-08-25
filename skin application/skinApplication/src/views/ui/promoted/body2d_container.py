from .promoted_container import *

from .body2d import Body2D


class Body2DContainer(PromotedContainer):

    def __init__(self, parent):
        super().__init__(parent)
        self.imgs = []
        self.actual_image = 0

        self._pre_charge()

    def initialize(self):
        pass

    def _pre_charge(self):
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(12)
        self.layout.setContentsMargins(0, 0, 0, 36)

        self.__create_up_controllers()
        self.__create_body2d_container()
        self.__create_down_controllers()

    def __create_body2d_container(self):
        self.body2d = Body2D(self)
        self.layout.addWidget(self.body2d)

    def __create_up_controllers(self):
        c_up_controllers = QFrame(self)
        c_up_controllers.setMaximumSize(QSize(16777215, 35))
        self.layout.addWidget(c_up_controllers)

        ly_up_controllers = QHBoxLayout(c_up_controllers)
        ly_up_controllers.setContentsMargins(0, 0, 0, 0)

        self.bt_clear_point = Button(c_up_controllers)
        self.bt_clear_point.setText("Clear point")
        ly_up_controllers.addWidget(self.bt_clear_point,0, Qt.AlignRight)
        self.bt_clear_point.clicked.connect(self.__clear_point)

    def __create_down_controllers(self):
        c_down_controllers = QFrame(self)
        c_down_controllers.setMaximumSize(QSize(16777215, 35))
        self.layout.addWidget(c_down_controllers)

        ly_down_controllers = QHBoxLayout(c_down_controllers)
        ly_down_controllers.setContentsMargins(0, 0, 0, 0)

        self.bt_turn_body_left = Button(c_down_controllers)
        self.bt_turn_body_left.setText("<")
        ly_down_controllers.addWidget(self.bt_turn_body_left, 0, Qt.AlignCenter)
        self.bt_turn_body_left.clicked.connect(lambda: (self.__turn_image(-1)))

        self.bt_turn_body_right = Button(c_down_controllers)
        self.bt_turn_body_right.setText(">")
        ly_down_controllers.addWidget(self.bt_turn_body_right,0, Qt.AlignCenter)
        self.bt_turn_body_right.clicked.connect(lambda: (self.__turn_image(1)))

    @Slot()
    def __turn_image(self, to=1):
        self.actual_image = self.actual_image + to
        if self.actual_image < 0 :
            self.actual_image = len(self.imgs) -1
        elif self.actual_image == len(self.imgs):
            self.actual_image = 0

        self.body2d.set_image(self.imgs[self.actual_image])

    @Slot()
    def __clear_point(self):
        self.body2d.clear_point()

    def set_images(self, imgs, actual_image=0, rel_point_x=-1, rel_point_y=-1):
        self.imgs = imgs
        self.actual_image = actual_image
        self.body2d.set_image(self.imgs[self.actual_image])
        if rel_point_x > -1 and rel_point_y > -1:
            self.body2d.set_relative_point(rel_point_x, rel_point_y)

    def get_point_info(self):
        if self.body2d.get_relative_point() is not None:
            return ([self.actual_image] + list(self.body2d.get_relative_point()))
        return []

