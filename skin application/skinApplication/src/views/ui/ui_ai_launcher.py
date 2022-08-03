# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_ai_launcher.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from .promoted.label import Label
from .promoted.navigator_button import NavigatorButton

class Ui_ai_launcher(object):
    def setupUi(self, ai_launcher):
        if not ai_launcher.objectName():
            ai_launcher.setObjectName(u"ai_launcher")
        ai_launcher.resize(1200, 800)
        ai_launcher.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(ai_launcher)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ly_navigator = QHBoxLayout()
        self.ly_navigator.setSpacing(0)
        self.ly_navigator.setObjectName(u"ly_navigator")
        self.ly_navigator.setContentsMargins(-1, 0, 0, -1)
        self.bt_back = NavigatorButton(ai_launcher)
        self.bt_back.setObjectName(u"bt_back")

        self.ly_navigator.addWidget(self.bt_back)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ly_navigator.addItem(self.horizontalSpacer)

        self.lb_title = Label(ai_launcher)
        self.lb_title.setObjectName(u"lb_title")

        self.ly_navigator.addWidget(self.lb_title)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ly_navigator.addItem(self.horizontalSpacer_2)

        self.bt_complete = NavigatorButton(ai_launcher)
        self.bt_complete.setObjectName(u"bt_complete")

        self.ly_navigator.addWidget(self.bt_complete)


        self.verticalLayout_2.addLayout(self.ly_navigator)

        self.ly_center = QHBoxLayout()
        self.ly_center.setSpacing(30)
        self.ly_center.setObjectName(u"ly_center")
        self.ly_center.setContentsMargins(-1, 20, -1, -1)
        self.ly_left = QVBoxLayout()
        self.ly_left.setObjectName(u"ly_left")
        self.c_body2d = QFrame(ai_launcher)
        self.c_body2d.setObjectName(u"c_body2d")
        self.c_body2d.setFrameShape(QFrame.StyledPanel)
        self.c_body2d.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.c_body2d)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_4 = QLabel(self.c_body2d)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_16.addWidget(self.label_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.ly_left.addWidget(self.c_body2d)


        self.ly_center.addLayout(self.ly_left)

        self.ly_right = QVBoxLayout()
        self.ly_right.setSpacing(20)
        self.ly_right.setObjectName(u"ly_right")
        self.ly_right.setContentsMargins(-1, -1, 20, -1)
        self.ly_skin_lesion_content = QHBoxLayout()
        self.ly_skin_lesion_content.setSpacing(20)
        self.ly_skin_lesion_content.setObjectName(u"ly_skin_lesion_content")
        self.ly_caracteristics = QVBoxLayout()
        self.ly_caracteristics.setSpacing(16)
        self.ly_caracteristics.setObjectName(u"ly_caracteristics")
        self.lb_caracteristics = Label(ai_launcher)
        self.lb_caracteristics.setObjectName(u"lb_caracteristics")
        self.lb_caracteristics.setMaximumSize(QSize(16777215, 20))

        self.ly_caracteristics.addWidget(self.lb_caracteristics, 0, Qt.AlignHCenter)

        self.sc_caracteristics = QScrollArea(ai_launcher)
        self.sc_caracteristics.setObjectName(u"sc_caracteristics")
        self.sc_caracteristics.setWidgetResizable(True)
        self.c_caracteristics_content = QWidget()
        self.c_caracteristics_content.setObjectName(u"c_caracteristics_content")
        self.c_caracteristics_content.setGeometry(QRect(0, 0, 364, 332))
        self.verticalLayout_30 = QVBoxLayout(self.c_caracteristics_content)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.ly_caracteristics_content = QVBoxLayout()
        self.ly_caracteristics_content.setObjectName(u"ly_caracteristics_content")

        self.verticalLayout_30.addLayout(self.ly_caracteristics_content)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_3)

        self.sc_caracteristics.setWidget(self.c_caracteristics_content)

        self.ly_caracteristics.addWidget(self.sc_caracteristics)


        self.ly_skin_lesion_content.addLayout(self.ly_caracteristics)

        self.ly_images = QVBoxLayout()
        self.ly_images.setSpacing(16)
        self.ly_images.setObjectName(u"ly_images")
        self.lb_add_images = Label(ai_launcher)
        self.lb_add_images.setObjectName(u"lb_add_images")
        self.lb_add_images.setMaximumSize(QSize(16777215, 20))

        self.ly_images.addWidget(self.lb_add_images, 0, Qt.AlignHCenter)

        self.sc_images = QScrollArea(ai_launcher)
        self.sc_images.setObjectName(u"sc_images")
        self.sc_images.setWidgetResizable(True)
        self.c_images_content = QWidget()
        self.c_images_content.setObjectName(u"c_images_content")
        self.c_images_content.setGeometry(QRect(0, 0, 364, 332))
        self.verticalLayout_10 = QVBoxLayout(self.c_images_content)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.ly_images_type_content = QVBoxLayout()
        self.ly_images_type_content.setObjectName(u"ly_images_type_content")

        self.verticalLayout_10.addLayout(self.ly_images_type_content)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.sc_images.setWidget(self.c_images_content)

        self.ly_images.addWidget(self.sc_images)


        self.ly_skin_lesion_content.addLayout(self.ly_images)


        self.ly_right.addLayout(self.ly_skin_lesion_content)

        self.c_ai_results = QFrame(ai_launcher)
        self.c_ai_results.setObjectName(u"c_ai_results")
        self.c_ai_results.setFrameShape(QFrame.StyledPanel)
        self.c_ai_results.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.c_ai_results)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_lauch_ai = Label(self.c_ai_results)
        self.lb_lauch_ai.setObjectName(u"lb_lauch_ai")
        self.lb_lauch_ai.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout.addWidget(self.lb_lauch_ai, 0, Qt.AlignHCenter)

        self.ly_ai_results = QVBoxLayout()
        self.ly_ai_results.setObjectName(u"ly_ai_results")
        self.ly_ai_results.setContentsMargins(-1, -1, -1, 10)
        self.frame = QFrame(self.c_ai_results)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_2)

        self.c_controllers = QFrame(self.frame)
        self.c_controllers.setObjectName(u"c_controllers")
        self.c_controllers.setMaximumSize(QSize(16777215, 35))
        self.c_controllers.setFrameShape(QFrame.StyledPanel)
        self.c_controllers.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.c_controllers)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.c_controllers)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.c_pages_controller = QFrame(self.c_controllers)
        self.c_pages_controller.setObjectName(u"c_pages_controller")
        self.c_pages_controller.setFrameShape(QFrame.StyledPanel)
        self.c_pages_controller.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.c_pages_controller)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.i_back = QPushButton(self.c_pages_controller)
        self.i_back.setObjectName(u"i_back")
        self.i_back.setMaximumSize(QSize(28, 28))

        self.horizontalLayout_2.addWidget(self.i_back)

        self.i_actual_page = QLineEdit(self.c_pages_controller)
        self.i_actual_page.setObjectName(u"i_actual_page")
        self.i_actual_page.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_2.addWidget(self.i_actual_page)

        self.label = QLabel(self.c_pages_controller)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_2.addWidget(self.label)

        self.i_next = QPushButton(self.c_pages_controller)
        self.i_next.setObjectName(u"i_next")
        self.i_next.setMaximumSize(QSize(28, 28))

        self.horizontalLayout_2.addWidget(self.i_next)


        self.horizontalLayout.addWidget(self.c_pages_controller, 0, Qt.AlignHCenter)

        self.c_size_controller = QFrame(self.c_controllers)
        self.c_size_controller.setObjectName(u"c_size_controller")
        self.c_size_controller.setFrameShape(QFrame.StyledPanel)
        self.c_size_controller.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.c_size_controller)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.i_nb_rows = QLineEdit(self.c_size_controller)
        self.i_nb_rows.setObjectName(u"i_nb_rows")
        self.i_nb_rows.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.i_nb_rows)

        self.label_2 = QLabel(self.c_size_controller)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.i_nb_cols = QLineEdit(self.c_size_controller)
        self.i_nb_cols.setObjectName(u"i_nb_cols")
        self.i_nb_cols.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.i_nb_cols)


        self.horizontalLayout.addWidget(self.c_size_controller, 0, Qt.AlignRight)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout_3.addWidget(self.c_controllers)


        self.ly_ai_results.addWidget(self.frame)


        self.verticalLayout.addLayout(self.ly_ai_results)


        self.ly_right.addWidget(self.c_ai_results)

        self.ly_right.setStretch(0, 1)
        self.ly_right.setStretch(1, 1)

        self.ly_center.addLayout(self.ly_right)

        self.ly_center.setStretch(0, 1)
        self.ly_center.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.ly_center)


        self.retranslateUi(ai_launcher)

        QMetaObject.connectSlotsByName(ai_launcher)
    # setupUi

    def retranslateUi(self, ai_launcher):
        ai_launcher.setWindowTitle(QCoreApplication.translate("ai_launcher", u"Loggin", None))
        self.bt_back.setText(QCoreApplication.translate("ai_launcher", u"Back", None))
        self.lb_title.setText(QCoreApplication.translate("ai_launcher", u"Ai launcher", None))
        self.bt_complete.setText(QCoreApplication.translate("ai_launcher", u"Learn more", None))
        self.label_4.setText(QCoreApplication.translate("ai_launcher", u"Indisponible", None))
        self.lb_caracteristics.setText(QCoreApplication.translate("ai_launcher", u"Caracteristics", None))
        self.lb_add_images.setText(QCoreApplication.translate("ai_launcher", u"Add images", None))
        self.lb_lauch_ai.setText(QCoreApplication.translate("ai_launcher", u"Launch AI", None))
        self.label_3.setText("")
        self.i_back.setText(QCoreApplication.translate("ai_launcher", u"<", None))
        self.label.setText(QCoreApplication.translate("ai_launcher", u"of 2", None))
        self.i_next.setText(QCoreApplication.translate("ai_launcher", u">", None))
        self.label_2.setText(QCoreApplication.translate("ai_launcher", u"X", None))
    # retranslateUi

