from PySide6.QtWidgets import QFrame
from PySide6.QtCore import Qt, QSize, QPoint
from PySide6.QtGui import QPixmap, QPainter, QPen, QCursor, QColor

class Body2D(QFrame):

#    s_edit_items = Signal(str)
    def __init__(self, parent):
        QFrame.__init__(self, parent)

        self.img = None
        self.pix_img = None
        self.skl_relative_point = None
        self.skl_precise_point = None

        self.point_radius = 2
        self.point_color = QColor(255,0,0)
        self.point_width = 10

    def paintEvent(self, paint_event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.pix_img)
#        print(self.rect())
        pen = QPen()
        pen.setColor(self.point_color)
        pen.setWidth(self.point_width)
        painter.setPen(pen)
        painter.setRenderHint(QPainter.Antialiasing, True)

        if self.skl_precise_point is not None:
            painter.drawEllipse(self.skl_precise_point, self.point_radius, self.point_radius);

    def set_image(self, img):
        self.img = img
        self.pix_img  = QPixmap(img.src)
        self.update()

    def mouseReleaseEvent(self, cursor_event):
        self.skl_precise_point = cursor_event.pos()
        self.calc_relative_point(self.skl_precise_point.x(), self.skl_precise_point.y())
        self.update()

    def resizeEvent(self, event):
        self.resize_container()

    def resize_container(self):
        (w,h) = self.img.get_resized_size(self.size().width(), self.size().height())
        self.resize(QSize(w,h))
        if self.skl_relative_point is not None:
            self.calc_precise_point(self.skl_relative_point[0], self.skl_relative_point[1])

    def calc_relative_point(self, w, h):
        self.skl_relative_point = (w/self.size().width(), h/self.size().height())

    def calc_precise_point(self, w, h):
        self.skl_precise_point = QPoint(w * self.size().width(), h * self.size().height())

    def set_relative_point(self, w, h):
        self.skl_relative_point = (w, h)
        self.calc_precise_point(w, h)

    def get_relative_point(self):
        return self.skl_relative_point

    def clear_point(self):
        self.skl_relative_point = None
        self.skl_precise_point = None
        self.update()
