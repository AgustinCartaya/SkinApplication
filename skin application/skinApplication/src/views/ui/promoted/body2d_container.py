from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt, QSize
from .label import Label
from .button import Button
from .body2d import Body2D

from PySide6.QtCore import Signal, Slot


class Body2DContainer(QFrame):

#    s_edit_items = Signal(str)
    def __init__(self, parent):
        QFrame.__init__(self, parent)
        self.imgs = []
        self.actual_image = 0

        self.__create()

    def __create(self):
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(12)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.__create_body2d_container()
        self.__create_controls()

    def __create_body2d_container(self):
        self.body2d = Body2D(self)
        self.layout.addWidget(self.body2d)

    def __create_controls(self):
        c_controllers = QFrame(self)
        c_controllers.setMaximumSize(QSize(16777215, 30))
        self.layout.addWidget(c_controllers)

        ly_controllers = QHBoxLayout(c_controllers)
        ly_controllers.setContentsMargins(0, 0, 0, 0)

        self.bt_turn_body = Button(c_controllers)
        self.bt_turn_body.setText("Turn body")
        self.bt_turn_body.clicked.connect(self.__turn_image)

#        self.bt_turn_body.setToolTip('This is a tooltip for the QPushButton widget')

        ly_controllers.addWidget(self.bt_turn_body,  0, Qt.AlignHCenter)

#    def draw_body2d(self, img):


    def set_images(self, imgs, actual_image=0, rel_point = []):
        self.imgs = imgs
        self.actual_image = actual_image
        self.body2d.set_image(self.imgs[self.actual_image])
        if len(rel_point) == 2:
            self.body2d.set_relative_point(rel_point[0], rel_point[1])

    @Slot()
    def __turn_image(self):
        self.actual_image = (self.actual_image + 1) % len(self.imgs)
        self.body2d.set_image(self.imgs[self.actual_image])

    def get_point_info(self):
        if self.body2d.get_relative_point() is not None:
            return (self.actual_image, list(self.body2d.get_relative_point()))
        return None


