# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_images.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QFrame,
    QHBoxLayout, QLabel, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from .promoted.check_button import CheckButton
from .promoted.label import Label
from .promoted.navigator_button import NavigatorButton
from .promoted.pagination import Pagination

class Ui_images(object):
    def setupUi(self, images):
        if not images.objectName():
            images.setObjectName(u"images")
        images.resize(1200, 800)
        images.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(images)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ly_navigator = QHBoxLayout()
        self.ly_navigator.setSpacing(0)
        self.ly_navigator.setObjectName(u"ly_navigator")
        self.ly_navigator.setContentsMargins(-1, 0, -1, -1)
        self.bt_back = NavigatorButton(images)
        self.bt_back.setObjectName(u"bt_back")

        self.ly_navigator.addWidget(self.bt_back, 0, Qt.AlignLeft)

        self.lb_title = Label(images)
        self.lb_title.setObjectName(u"lb_title")

        self.ly_navigator.addWidget(self.lb_title, 0, Qt.AlignHCenter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ly_navigator.addItem(self.horizontalSpacer)

        self.ly_navigator.setStretch(0, 1)
        self.ly_navigator.setStretch(1, 1)
        self.ly_navigator.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.ly_navigator)

        self.ly_center = QHBoxLayout()
        self.ly_center.setSpacing(30)
        self.ly_center.setObjectName(u"ly_center")
        self.ly_center.setContentsMargins(0, 30, 0, 0)
        self.c_filters = QFrame(images)
        self.c_filters.setObjectName(u"c_filters")
        self.c_filters.setMinimumSize(QSize(300, 0))
        self.c_filters.setMaximumSize(QSize(330, 16777215))
        self.c_filters.setFrameShape(QFrame.StyledPanel)
        self.c_filters.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.c_filters)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(20, -1, -1, -1)
        self.frame_3 = QFrame(self.c_filters)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_3)
        self.verticalLayout_11.setSpacing(20)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 40)
        self.lb_filters_title = Label(self.frame_3)
        self.lb_filters_title.setObjectName(u"lb_filters_title")
        self.lb_filters_title.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_11.addWidget(self.lb_filters_title, 0, Qt.AlignHCenter)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(12)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, -1, -1, -1)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dateEdit = QDateEdit(self.frame_3)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(110, 0))
        self.dateEdit.setMaximumSize(QSize(130, 16777215))

        self.horizontalLayout.addWidget(self.dateEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(9, -1, -1, -1)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_7.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dateEdit_2 = QDateEdit(self.frame_3)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setMinimumSize(QSize(110, 0))
        self.dateEdit_2.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_2.addWidget(self.dateEdit_2)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.dateEdit_3 = QDateEdit(self.frame_3)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        self.dateEdit_3.setMinimumSize(QSize(110, 0))
        self.dateEdit_3.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_2.addWidget(self.dateEdit_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.verticalLayout_5)

        self.ly_filter_diagnostic_attributes = QVBoxLayout()
        self.ly_filter_diagnostic_attributes.setSpacing(9)
        self.ly_filter_diagnostic_attributes.setObjectName(u"ly_filter_diagnostic_attributes")
        self.lb_filter_diagnostic_attributes = QLabel(self.frame_3)
        self.lb_filter_diagnostic_attributes.setObjectName(u"lb_filter_diagnostic_attributes")
        self.lb_filter_diagnostic_attributes.setMaximumSize(QSize(16777215, 20))

        self.ly_filter_diagnostic_attributes.addWidget(self.lb_filter_diagnostic_attributes)

        self.ly_filter_diagnostic_attributes_content = QVBoxLayout()
        self.ly_filter_diagnostic_attributes_content.setSpacing(4)
        self.ly_filter_diagnostic_attributes_content.setObjectName(u"ly_filter_diagnostic_attributes_content")
        self.ly_filter_diagnostic_attributes_content.setContentsMargins(9, -1, -1, -1)
        self.i_bening = QCheckBox(self.frame_3)
        self.i_bening.setObjectName(u"i_bening")

        self.ly_filter_diagnostic_attributes_content.addWidget(self.i_bening)

        self.i_malignant = QCheckBox(self.frame_3)
        self.i_malignant.setObjectName(u"i_malignant")

        self.ly_filter_diagnostic_attributes_content.addWidget(self.i_malignant)

        self.i_indeterminate = QCheckBox(self.frame_3)
        self.i_indeterminate.setObjectName(u"i_indeterminate")

        self.ly_filter_diagnostic_attributes_content.addWidget(self.i_indeterminate)


        self.ly_filter_diagnostic_attributes.addLayout(self.ly_filter_diagnostic_attributes_content)


        self.verticalLayout_8.addLayout(self.ly_filter_diagnostic_attributes)


        self.verticalLayout_11.addLayout(self.verticalLayout_8)


        self.verticalLayout_10.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.c_filters)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label, 0, Qt.AlignHCenter)

        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.c_filters_content = QWidget()
        self.c_filters_content.setObjectName(u"c_filters_content")
        self.c_filters_content.setGeometry(QRect(0, 0, 303, 370))
        self.verticalLayout_3 = QVBoxLayout(self.c_filters_content)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(16, 0, 0, -1)
        self.ly_filters = QVBoxLayout()
        self.ly_filters.setSpacing(20)
        self.ly_filters.setObjectName(u"ly_filters")

        self.verticalLayout_3.addLayout(self.ly_filters)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.c_filters_content)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.verticalLayout_10.addWidget(self.frame_2)


        self.verticalLayout_18.addLayout(self.verticalLayout_10)


        self.ly_center.addWidget(self.c_filters)

        self.ly_right = QVBoxLayout()
        self.ly_right.setObjectName(u"ly_right")
        self.ly_right.setContentsMargins(-1, -1, 20, 20)
        self.frame = QFrame(images)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 60))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_organizer_titles = QLabel(self.frame)
        self.lb_organizer_titles.setObjectName(u"lb_organizer_titles")
        self.lb_organizer_titles.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.lb_organizer_titles, 0, Qt.AlignHCenter)

        self.frame_12 = QFrame(self.frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 80))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.bt_sorter_asc = CheckButton(self.frame_12)
        self.bt_sorter_asc.setObjectName(u"bt_sorter_asc")
        self.bt_sorter_asc.setMinimumSize(QSize(40, 25))
        self.bt_sorter_asc.setMaximumSize(QSize(40, 25))

        self.horizontalLayout_3.addWidget(self.bt_sorter_asc)

        self.bt_sorter_dsc = CheckButton(self.frame_12)
        self.bt_sorter_dsc.setObjectName(u"bt_sorter_dsc")
        self.bt_sorter_dsc.setMinimumSize(QSize(40, 25))
        self.bt_sorter_dsc.setMaximumSize(QSize(40, 25))

        self.horizontalLayout_3.addWidget(self.bt_sorter_dsc)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.bt_sorter_id = CheckButton(self.frame_12)
        self.bt_sorter_id.setObjectName(u"bt_sorter_id")
        self.bt_sorter_id.setMinimumSize(QSize(40, 25))
        self.bt_sorter_id.setMaximumSize(QSize(40, 25))

        self.horizontalLayout_3.addWidget(self.bt_sorter_id)

        self.bt_sorter_name = CheckButton(self.frame_12)
        self.bt_sorter_name.setObjectName(u"bt_sorter_name")
        self.bt_sorter_name.setMinimumSize(QSize(50, 25))
        self.bt_sorter_name.setMaximumSize(QSize(50, 25))

        self.horizontalLayout_3.addWidget(self.bt_sorter_name)


        self.verticalLayout.addWidget(self.frame_12, 0, Qt.AlignHCenter)


        self.ly_right.addWidget(self.frame)

        self.c_pagination = Pagination(images)
        self.c_pagination.setObjectName(u"c_pagination")
        self.c_pagination.setFrameShape(QFrame.StyledPanel)
        self.c_pagination.setFrameShadow(QFrame.Raised)

        self.ly_right.addWidget(self.c_pagination)


        self.ly_center.addLayout(self.ly_right)


        self.verticalLayout_2.addLayout(self.ly_center)


        self.retranslateUi(images)

        QMetaObject.connectSlotsByName(images)
    # setupUi

    def retranslateUi(self, images):
        images.setWindowTitle(QCoreApplication.translate("images", u"Loggin", None))
        self.bt_back.setText(QCoreApplication.translate("images", u"Back", None))
        self.lb_title.setText(QCoreApplication.translate("images", u"Images", None))
        self.lb_filters_title.setText(QCoreApplication.translate("images", u"Filters", None))
        self.label_2.setText(QCoreApplication.translate("images", u"DATE", None))
        self.label_3.setText(QCoreApplication.translate("images", u"Precice", None))
        self.label_4.setText(QCoreApplication.translate("images", u"Range", None))
        self.label_5.setText(QCoreApplication.translate("images", u"to", None))
        self.lb_filter_diagnostic_attributes.setText(QCoreApplication.translate("images", u"DIAGNOSTIC ATTRIBUTES", None))
        self.i_bening.setText(QCoreApplication.translate("images", u"Photo (120 / 300)", None))
        self.i_malignant.setText(QCoreApplication.translate("images", u"Dermatology (150 / 300)", None))
        self.i_indeterminate.setText(QCoreApplication.translate("images", u"Microscopy (30 / 300)", None))
        self.label.setText(QCoreApplication.translate("images", u"Description", None))
        self.lb_organizer_titles.setText(QCoreApplication.translate("images", u"Organizer", None))
        self.bt_sorter_asc.setText(QCoreApplication.translate("images", u"A-z", None))
        self.bt_sorter_dsc.setText(QCoreApplication.translate("images", u"z-A", None))
        self.bt_sorter_id.setText(QCoreApplication.translate("images", u"Date", None))
        self.bt_sorter_name.setText(QCoreApplication.translate("images", u"Name", None))
    # retranslateUi

