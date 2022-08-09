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
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from .promoted.button import Button
from .promoted.label import Label
from .promoted.navigator_button import NavigatorButton
from .promoted.required_elements_container import RequiredElementsContainer
from .promoted.required_skl_img_container import RequiredSklImgContainer

class Ui_ai_launcher(object):
    def setupUi(self, ai_launcher):
        if not ai_launcher.objectName():
            ai_launcher.setObjectName(u"ai_launcher")
        ai_launcher.resize(1200, 800)
        ai_launcher.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(ai_launcher)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ly_navigator = QHBoxLayout()
        self.ly_navigator.setSpacing(0)
        self.ly_navigator.setObjectName(u"ly_navigator")
        self.ly_navigator.setContentsMargins(-1, 0, 0, -1)
        self.bt_back = NavigatorButton(ai_launcher)
        self.bt_back.setObjectName(u"bt_back")

        self.ly_navigator.addWidget(self.bt_back, 0, Qt.AlignLeft)

        self.lb_title = Label(ai_launcher)
        self.lb_title.setObjectName(u"lb_title")

        self.ly_navigator.addWidget(self.lb_title, 0, Qt.AlignHCenter)

        self.bt_learn_more = NavigatorButton(ai_launcher)
        self.bt_learn_more.setObjectName(u"bt_learn_more")

        self.ly_navigator.addWidget(self.bt_learn_more, 0, Qt.AlignRight)

        self.ly_navigator.setStretch(0, 1)
        self.ly_navigator.setStretch(1, 1)
        self.ly_navigator.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.ly_navigator)

        self.ly_center = QVBoxLayout()
        self.ly_center.setObjectName(u"ly_center")
        self.ly_center.setContentsMargins(-1, -1, -1, 30)
        self.ly_center_content = QVBoxLayout()
        self.ly_center_content.setSpacing(30)
        self.ly_center_content.setObjectName(u"ly_center_content")
        self.ly_required_information = QVBoxLayout()
        self.ly_required_information.setSpacing(20)
        self.ly_required_information.setObjectName(u"ly_required_information")
        self.lb_required_information = Label(ai_launcher)
        self.lb_required_information.setObjectName(u"lb_required_information")

        self.ly_required_information.addWidget(self.lb_required_information, 0, Qt.AlignHCenter)

        self.ly_required_information_content = QHBoxLayout()
        self.ly_required_information_content.setObjectName(u"ly_required_information_content")
        self.ly_required_information_content.setContentsMargins(10, -1, 10, -1)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ly_required_information_content.addItem(self.horizontalSpacer_5)

        self.c_patient_required_info = QFrame(ai_launcher)
        self.c_patient_required_info.setObjectName(u"c_patient_required_info")
        self.c_patient_required_info.setFrameShape(QFrame.StyledPanel)
        self.c_patient_required_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.c_patient_required_info)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lb_patient_required_info = Label(self.c_patient_required_info)
        self.lb_patient_required_info.setObjectName(u"lb_patient_required_info")

        self.verticalLayout_6.addWidget(self.lb_patient_required_info, 0, Qt.AlignHCenter)

        self.sc_patient_required_info = QScrollArea(self.c_patient_required_info)
        self.sc_patient_required_info.setObjectName(u"sc_patient_required_info")
        self.sc_patient_required_info.setWidgetResizable(True)
        self.c_patient_required_info_content = QWidget()
        self.c_patient_required_info_content.setObjectName(u"c_patient_required_info_content")
        self.c_patient_required_info_content.setGeometry(QRect(0, 0, 402, 260))
        self.verticalLayout_12 = QVBoxLayout(self.c_patient_required_info_content)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.c_patient_required_info_list = RequiredElementsContainer(self.c_patient_required_info_content)
        self.c_patient_required_info_list.setObjectName(u"c_patient_required_info_list")
        self.c_patient_required_info_list.setFrameShape(QFrame.StyledPanel)
        self.c_patient_required_info_list.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.c_patient_required_info_list)

        self.verticalSpacer_2 = QSpacerItem(20, 147, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.sc_patient_required_info.setWidget(self.c_patient_required_info_content)

        self.verticalLayout_6.addWidget(self.sc_patient_required_info)


        self.ly_required_information_content.addWidget(self.c_patient_required_info)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.ly_required_information_content.addItem(self.horizontalSpacer_7)

        self.c_skl_required_info = QFrame(ai_launcher)
        self.c_skl_required_info.setObjectName(u"c_skl_required_info")
        self.c_skl_required_info.setFrameShape(QFrame.StyledPanel)
        self.c_skl_required_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.c_skl_required_info)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lb_skl_required_info = QLabel(self.c_skl_required_info)
        self.lb_skl_required_info.setObjectName(u"lb_skl_required_info")

        self.verticalLayout_5.addWidget(self.lb_skl_required_info, 0, Qt.AlignHCenter)

        self.sc_skl_required_info_content = QScrollArea(self.c_skl_required_info)
        self.sc_skl_required_info_content.setObjectName(u"sc_skl_required_info_content")
        self.sc_skl_required_info_content.setWidgetResizable(True)
        self.c_skl_required_info_content = QWidget()
        self.c_skl_required_info_content.setObjectName(u"c_skl_required_info_content")
        self.c_skl_required_info_content.setGeometry(QRect(0, 0, 402, 260))
        self.verticalLayout_14 = QVBoxLayout(self.c_skl_required_info_content)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.c_skl_required_info_list = RequiredElementsContainer(self.c_skl_required_info_content)
        self.c_skl_required_info_list.setObjectName(u"c_skl_required_info_list")
        self.c_skl_required_info_list.setFrameShape(QFrame.StyledPanel)
        self.c_skl_required_info_list.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.c_skl_required_info_list)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_3)

        self.sc_skl_required_info_content.setWidget(self.c_skl_required_info_content)

        self.verticalLayout_5.addWidget(self.sc_skl_required_info_content)


        self.ly_required_information_content.addWidget(self.c_skl_required_info)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ly_required_information_content.addItem(self.horizontalSpacer_6)

        self.ly_required_information_content.setStretch(0, 2)
        self.ly_required_information_content.setStretch(1, 6)
        self.ly_required_information_content.setStretch(2, 1)
        self.ly_required_information_content.setStretch(3, 6)
        self.ly_required_information_content.setStretch(4, 2)

        self.ly_required_information.addLayout(self.ly_required_information_content)


        self.ly_center_content.addLayout(self.ly_required_information)

        self.ly_required_images = QVBoxLayout()
        self.ly_required_images.setSpacing(20)
        self.ly_required_images.setObjectName(u"ly_required_images")
        self.lb_required_images = Label(ai_launcher)
        self.lb_required_images.setObjectName(u"lb_required_images")

        self.ly_required_images.addWidget(self.lb_required_images, 0, Qt.AlignHCenter)

        self.ly_required_images_content = QHBoxLayout()
        self.ly_required_images_content.setObjectName(u"ly_required_images_content")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ly_required_images_content.addItem(self.horizontalSpacer_8)

        self.ly_required_images_table = QVBoxLayout()
        self.ly_required_images_table.setSpacing(20)
        self.ly_required_images_table.setObjectName(u"ly_required_images_table")
        self.ly_required_images_ttitles = QHBoxLayout()
        self.ly_required_images_ttitles.setObjectName(u"ly_required_images_ttitles")
        self.ly_required_images_ttitles.setContentsMargins(9, -1, -1, -1)
        self.lb_image_name = Label(ai_launcher)
        self.lb_image_name.setObjectName(u"lb_image_name")

        self.ly_required_images_ttitles.addWidget(self.lb_image_name)

        self.lb_min_images = Label(ai_launcher)
        self.lb_min_images.setObjectName(u"lb_min_images")

        self.ly_required_images_ttitles.addWidget(self.lb_min_images, 0, Qt.AlignHCenter)

        self.lb_max_images = Label(ai_launcher)
        self.lb_max_images.setObjectName(u"lb_max_images")

        self.ly_required_images_ttitles.addWidget(self.lb_max_images, 0, Qt.AlignHCenter)

        self.lb_selected_images = Label(ai_launcher)
        self.lb_selected_images.setObjectName(u"lb_selected_images")

        self.ly_required_images_ttitles.addWidget(self.lb_selected_images, 0, Qt.AlignHCenter)


        self.ly_required_images_table.addLayout(self.ly_required_images_ttitles)

        self.sc_required_images_table = QScrollArea(ai_launcher)
        self.sc_required_images_table.setObjectName(u"sc_required_images_table")
        self.sc_required_images_table.setWidgetResizable(True)
        self.c_required_images_table = QWidget()
        self.c_required_images_table.setObjectName(u"c_required_images_table")
        self.c_required_images_table.setGeometry(QRect(0, 0, 881, 257))
        self.verticalLayout_8 = QVBoxLayout(self.c_required_images_table)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.c_required_skl_imgs = RequiredSklImgContainer(self.c_required_images_table)
        self.c_required_skl_imgs.setObjectName(u"c_required_skl_imgs")
        self.c_required_skl_imgs.setFrameShape(QFrame.StyledPanel)
        self.c_required_skl_imgs.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.c_required_skl_imgs)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.sc_required_images_table.setWidget(self.c_required_images_table)

        self.ly_required_images_table.addWidget(self.sc_required_images_table)


        self.ly_required_images_content.addLayout(self.ly_required_images_table)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ly_required_images_content.addItem(self.horizontalSpacer_9)

        self.ly_required_images_content.setStretch(0, 1)
        self.ly_required_images_content.setStretch(1, 6)
        self.ly_required_images_content.setStretch(2, 1)

        self.ly_required_images.addLayout(self.ly_required_images_content)


        self.ly_center_content.addLayout(self.ly_required_images)

        self.ly_center_content.setStretch(0, 1)
        self.ly_center_content.setStretch(1, 1)

        self.ly_center.addLayout(self.ly_center_content)

        self.bt_launch = Button(ai_launcher)
        self.bt_launch.setObjectName(u"bt_launch")
        self.bt_launch.setEnabled(False)
        self.bt_launch.setMinimumSize(QSize(100, 0))

        self.ly_center.addWidget(self.bt_launch, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addLayout(self.ly_center)


        self.retranslateUi(ai_launcher)

        QMetaObject.connectSlotsByName(ai_launcher)
    # setupUi

    def retranslateUi(self, ai_launcher):
        ai_launcher.setWindowTitle(QCoreApplication.translate("ai_launcher", u"Loggin", None))
        self.bt_back.setText(QCoreApplication.translate("ai_launcher", u"Back", None))
        self.lb_title.setText(QCoreApplication.translate("ai_launcher", u"Ai launcher", None))
        self.bt_learn_more.setText(QCoreApplication.translate("ai_launcher", u"Learn more", None))
        self.lb_required_information.setText(QCoreApplication.translate("ai_launcher", u"Required information", None))
        self.lb_patient_required_info.setText(QCoreApplication.translate("ai_launcher", u"Patient", None))
        self.lb_skl_required_info.setText(QCoreApplication.translate("ai_launcher", u"Skin lesion", None))
        self.lb_required_images.setText(QCoreApplication.translate("ai_launcher", u"Required images", None))
        self.lb_image_name.setText(QCoreApplication.translate("ai_launcher", u"Image Name", None))
        self.lb_min_images.setText(QCoreApplication.translate("ai_launcher", u"Min", None))
        self.lb_max_images.setText(QCoreApplication.translate("ai_launcher", u"Max", None))
        self.lb_selected_images.setText(QCoreApplication.translate("ai_launcher", u"Selected", None))
        self.bt_launch.setText(QCoreApplication.translate("ai_launcher", u"Launch", None))
    # retranslateUi

