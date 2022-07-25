from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)


from .button import Button
from .annotation_preview import AnnotationPreview

from .line_edit import LineEdit

import src.util.data_cleaner as data_cleaner


class SkinPartPreview(QFrame):

    def __init__(self, *args, **kwards):
        QFrame.__init__(self, *args, **kwards)

        self.__create()


    def __create(self):
        self.layout = QHBoxLayout(self)
        self.layout.setSpacing(16)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.__create_c_n1()
        self.__create_c_n2()
        self.__create_c_n3()

    def __create_c_n1(self):
        # c_n1 frame
        self.c_n1 = QFrame(self)

        self.c_n1_layout = QVBoxLayout(self.c_n1)
        self.c_n1_layout.setContentsMargins(0, 0, 0, 0)

        # image
        self.c_image = QFrame(self.c_n1)

        self.c_image_layout = QHBoxLayout(self.c_image)
        self.c_image_layout.setContentsMargins(0, 0, 0, 0)

        self.lb_image = QLabel(self.c_image)
        self.lb_image.setMaximumSize(QSize(150, 150))
        self.lb_image.setPixmap(QPixmap("assets/img/Screenshot 2022-07-25 180616.png"))
        self.lb_image.setScaledContents(True)

        self.c_image_layout.addWidget(self.lb_image)
        self.c_n1_layout.addWidget(self.c_image)

        # button
        self.bt_update = Button(self.c_n1)
        self.bt_update.setText("Update")
        self.bt_update.setMaximumSize(QSize(160, 16777215))

        self.c_n1_layout.addWidget(self.bt_update, 0, Qt.AlignHCenter)


        self.layout.addWidget(self.c_n1)


    def __create_c_n2(self):
        # c_n2 frame
        self.c_n2 = QFrame(self)

        self.c_n2_layout = QHBoxLayout(self.c_n2)
        self.c_n2_layout.setSpacing(16)
        self.c_n2_layout.setContentsMargins(0, 0, 0, 0)

        # Anotations
        ann_dc = {"Risk":"BENIGN", "Type":"Mole", "Notes":"..."}
        ai_r_dc = {"AI":"AI - 1", "Risk":"BENIGN", "Type":"Mole", "Accurance":"93%"}

        annotations = AnnotationPreview(ann_dc, "Annotations", "Read more")
        ai_results = AnnotationPreview(ai_r_dc, "AI results", "Read more")

        self.c_n2_layout.addWidget(annotations)
        self.c_n2_layout.addWidget(ai_results)

        self.layout.addWidget(self.c_n2)


    def __create_c_n3(self):
        self.c_n3 = QFrame(self)

        self.c_n3_layout = QVBoxLayout(self.c_n3)
        self.c_n3_layout.setContentsMargins(0, 0, 0, 0)

        self.c_buttons = QFrame(self.c_n3)

        self.c_buttons_layout = QVBoxLayout(self.c_buttons)
        self.c_buttons_layout.setContentsMargins(0, 0, 0, 0)

        # bt see time line
        self.bt_see_time_line = Button(self.c_buttons)
        self.bt_see_time_line.setText("Time line")
        self.bt_see_time_line.setMinimumSize(QSize(100, 0))
        self.bt_see_time_line.setMaximumSize(QSize(100, 16777215))

        self.c_buttons_layout.addWidget(self.bt_see_time_line)

        # bt see imgaes
        self.bt_see_images = Button(self.c_buttons)
        self.bt_see_images.setText("Images")
        self.bt_see_images.setMinimumSize(QSize(100, 0))
        self.bt_see_images.setMaximumSize(QSize(100, 16777215))

        self.c_buttons_layout.addWidget(self.bt_see_images)

        # bt more
        self.bt_more_options = Button(self.c_buttons)
        self.bt_more_options.setText("More")
        self.bt_more_options.setMinimumSize(QSize(100, 0))
        self.bt_more_options.setMaximumSize(QSize(100, 16777215))

        self.c_buttons_layout.addWidget(self.bt_more_options)


        self.c_n3_layout.addWidget(self.c_buttons)

        # spacer
        self.vs_buttons = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.c_n3_layout.addItem(self.vs_buttons)


        self.layout.addWidget(self.c_n3)

        self.layout.setStretch(0, 2)
        self.layout.setStretch(1, 6)
        self.layout.setStretch(2, 1)




