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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QHBoxLayout,
    QLabel, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from .promoted.button import Button
from .promoted.check_button import CheckButton
from .promoted.filter_skl_img_container import FilterSklImgContainer
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

        self.bt_command = NavigatorButton(images)
        self.bt_command.setObjectName(u"bt_command")

        self.ly_navigator.addWidget(self.bt_command, 0, Qt.AlignRight)

        self.ly_navigator.setStretch(0, 1)
        self.ly_navigator.setStretch(1, 1)
        self.ly_navigator.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.ly_navigator)

        self.ly_center = QHBoxLayout()
        self.ly_center.setSpacing(30)
        self.ly_center.setObjectName(u"ly_center")
        self.ly_center.setContentsMargins(0, 30, 10, 0)
        self.c_left = QFrame(images)
        self.c_left.setObjectName(u"c_left")
        self.c_left.setMinimumSize(QSize(300, 0))
        self.c_left.setMaximumSize(QSize(330, 16777215))
        self.c_left.setFrameShape(QFrame.StyledPanel)
        self.c_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.c_left)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(20, -1, -1, 10)
        self.c_filters = QFrame(self.c_left)
        self.c_filters.setObjectName(u"c_filters")
        self.c_filters.setFrameShape(QFrame.StyledPanel)
        self.c_filters.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.c_filters)
        self.verticalLayout_11.setSpacing(20)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 40)
        self.lb_filters_title = Label(self.c_filters)
        self.lb_filters_title.setObjectName(u"lb_filters_title")
        self.lb_filters_title.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_11.addWidget(self.lb_filters_title, 0, Qt.AlignHCenter)

        self.ly_filters = QVBoxLayout()
        self.ly_filters.setSpacing(20)
        self.ly_filters.setObjectName(u"ly_filters")
        self.ly_filter_image_type = QVBoxLayout()
        self.ly_filter_image_type.setSpacing(9)
        self.ly_filter_image_type.setObjectName(u"ly_filter_image_type")
        self.lb_filter_image_type = Label(self.c_filters)
        self.lb_filter_image_type.setObjectName(u"lb_filter_image_type")
        self.lb_filter_image_type.setMaximumSize(QSize(16777215, 20))

        self.ly_filter_image_type.addWidget(self.lb_filter_image_type)

        self.c_filter_image_type = FilterSklImgContainer(self.c_filters)
        self.c_filter_image_type.setObjectName(u"c_filter_image_type")
        self.c_filter_image_type.setFrameShape(QFrame.StyledPanel)
        self.c_filter_image_type.setFrameShadow(QFrame.Raised)

        self.ly_filter_image_type.addWidget(self.c_filter_image_type)


        self.ly_filters.addLayout(self.ly_filter_image_type)

        self.c_filter_date = QFrame(self.c_filters)
        self.c_filter_date.setObjectName(u"c_filter_date")
        self.c_filter_date.setFrameShape(QFrame.StyledPanel)
        self.c_filter_date.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.c_filter_date)
        self.verticalLayout_5.setSpacing(12)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lb_filter_date = Label(self.c_filter_date)
        self.lb_filter_date.setObjectName(u"lb_filter_date")

        self.verticalLayout_5.addWidget(self.lb_filter_date)

        self.ly_filter_date_precise = QVBoxLayout()
        self.ly_filter_date_precise.setSpacing(4)
        self.ly_filter_date_precise.setObjectName(u"ly_filter_date_precise")
        self.ly_filter_date_precise.setContentsMargins(9, -1, -1, -1)
        self.lb_filter_date_precise = Label(self.c_filter_date)
        self.lb_filter_date_precise.setObjectName(u"lb_filter_date_precise")

        self.ly_filter_date_precise.addWidget(self.lb_filter_date_precise)

        self.ly_filter_date_precise_inputs = QHBoxLayout()
        self.ly_filter_date_precise_inputs.setObjectName(u"ly_filter_date_precise_inputs")
        self.i_date_precise = QDateEdit(self.c_filter_date)
        self.i_date_precise.setObjectName(u"i_date_precise")
        self.i_date_precise.setMinimumSize(QSize(110, 0))
        self.i_date_precise.setMaximumSize(QSize(130, 16777215))

        self.ly_filter_date_precise_inputs.addWidget(self.i_date_precise)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ly_filter_date_precise_inputs.addItem(self.horizontalSpacer_2)


        self.ly_filter_date_precise.addLayout(self.ly_filter_date_precise_inputs)


        self.verticalLayout_5.addLayout(self.ly_filter_date_precise)

        self.ly_filter_date_range = QVBoxLayout()
        self.ly_filter_date_range.setSpacing(4)
        self.ly_filter_date_range.setObjectName(u"ly_filter_date_range")
        self.ly_filter_date_range.setContentsMargins(9, -1, -1, -1)
        self.lb_filter_date_range = Label(self.c_filter_date)
        self.lb_filter_date_range.setObjectName(u"lb_filter_date_range")

        self.ly_filter_date_range.addWidget(self.lb_filter_date_range)

        self.ly_filter_date_range_inputs = QHBoxLayout()
        self.ly_filter_date_range_inputs.setObjectName(u"ly_filter_date_range_inputs")
        self.i_date_range_min = QDateEdit(self.c_filter_date)
        self.i_date_range_min.setObjectName(u"i_date_range_min")
        self.i_date_range_min.setMinimumSize(QSize(110, 0))
        self.i_date_range_min.setMaximumSize(QSize(110, 16777215))

        self.ly_filter_date_range_inputs.addWidget(self.i_date_range_min)

        self.lb_date_range_to = QLabel(self.c_filter_date)
        self.lb_date_range_to.setObjectName(u"lb_date_range_to")

        self.ly_filter_date_range_inputs.addWidget(self.lb_date_range_to, 0, Qt.AlignHCenter)

        self.i_date_range_max = QDateEdit(self.c_filter_date)
        self.i_date_range_max.setObjectName(u"i_date_range_max")
        self.i_date_range_max.setMinimumSize(QSize(110, 0))
        self.i_date_range_max.setMaximumSize(QSize(110, 16777215))

        self.ly_filter_date_range_inputs.addWidget(self.i_date_range_max)

        self.spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ly_filter_date_range_inputs.addItem(self.spacer)


        self.ly_filter_date_range.addLayout(self.ly_filter_date_range_inputs)


        self.verticalLayout_5.addLayout(self.ly_filter_date_range)


        self.ly_filters.addWidget(self.c_filter_date)


        self.verticalLayout_11.addLayout(self.ly_filters)


        self.verticalLayout_10.addWidget(self.c_filters)

        self.c_description = QFrame(self.c_left)
        self.c_description.setObjectName(u"c_description")
        self.c_description.setFrameShape(QFrame.StyledPanel)
        self.c_description.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.c_description)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lb_description = Label(self.c_description)
        self.lb_description.setObjectName(u"lb_description")

        self.verticalLayout_4.addWidget(self.lb_description, 0, Qt.AlignHCenter)

        self.sc_description_content = QScrollArea(self.c_description)
        self.sc_description_content.setObjectName(u"sc_description_content")
        self.sc_description_content.setWidgetResizable(True)
        self.c_description_content = QWidget()
        self.c_description_content.setObjectName(u"c_description_content")
        self.c_description_content.setGeometry(QRect(0, 0, 303, 349))
        self.verticalLayout_3 = QVBoxLayout(self.c_description_content)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(16, 0, 0, -1)
        self.ly_description_content = QVBoxLayout()
        self.ly_description_content.setObjectName(u"ly_description_content")

        self.verticalLayout_3.addLayout(self.ly_description_content)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.sc_description_content.setWidget(self.c_description_content)

        self.verticalLayout_4.addWidget(self.sc_description_content)


        self.verticalLayout_10.addWidget(self.c_description)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.ly_bt = QHBoxLayout()
        self.ly_bt.setObjectName(u"ly_bt")
        self.ly_bt.setContentsMargins(9, -1, 9, -1)
        self.bt_delete_image = Button(self.c_left)
        self.bt_delete_image.setObjectName(u"bt_delete_image")

        self.ly_bt.addWidget(self.bt_delete_image, 0, Qt.AlignHCenter)

        self.bt_clear_selection = Button(self.c_left)
        self.bt_clear_selection.setObjectName(u"bt_clear_selection")

        self.ly_bt.addWidget(self.bt_clear_selection, 0, Qt.AlignHCenter)


        self.verticalLayout_10.addLayout(self.ly_bt)


        self.verticalLayout_18.addLayout(self.verticalLayout_10)


        self.ly_center.addWidget(self.c_left)

        self.ly_right = QVBoxLayout()
        self.ly_right.setObjectName(u"ly_right")
        self.ly_right.setContentsMargins(-1, -1, 20, 20)
        self.c_organizer = QFrame(images)
        self.c_organizer.setObjectName(u"c_organizer")
        self.c_organizer.setMaximumSize(QSize(16777215, 60))
        self.c_organizer.setFrameShape(QFrame.StyledPanel)
        self.c_organizer.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.c_organizer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_organizer_titles = Label(self.c_organizer)
        self.lb_organizer_titles.setObjectName(u"lb_organizer_titles")
        self.lb_organizer_titles.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.lb_organizer_titles, 0, Qt.AlignHCenter)

        self.ly_organizer_controllers = QFrame(self.c_organizer)
        self.ly_organizer_controllers.setObjectName(u"ly_organizer_controllers")
        self.ly_organizer_controllers.setMaximumSize(QSize(16777215, 80))
        self.ly_organizer_controllers.setFrameShape(QFrame.StyledPanel)
        self.ly_organizer_controllers.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.ly_organizer_controllers)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 10, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.c_sorter_asc = QFrame(self.ly_organizer_controllers)
        self.c_sorter_asc.setObjectName(u"c_sorter_asc")
        self.c_sorter_asc.setFrameShape(QFrame.StyledPanel)
        self.c_sorter_asc.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.c_sorter_asc)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bt_sorter_dsc = CheckButton(self.c_sorter_asc)
        self.bt_sorter_dsc.setObjectName(u"bt_sorter_dsc")
        self.bt_sorter_dsc.setMinimumSize(QSize(40, 25))
        self.bt_sorter_dsc.setMaximumSize(QSize(40, 25))

        self.horizontalLayout_2.addWidget(self.bt_sorter_dsc)

        self.bt_sorter_asc = CheckButton(self.c_sorter_asc)
        self.bt_sorter_asc.setObjectName(u"bt_sorter_asc")
        self.bt_sorter_asc.setMinimumSize(QSize(40, 25))
        self.bt_sorter_asc.setMaximumSize(QSize(40, 25))

        self.horizontalLayout_2.addWidget(self.bt_sorter_asc)


        self.horizontalLayout.addWidget(self.c_sorter_asc, 0, Qt.AlignHCenter)

        self.c_sorter_name = QFrame(self.ly_organizer_controllers)
        self.c_sorter_name.setObjectName(u"c_sorter_name")
        self.c_sorter_name.setFrameShape(QFrame.StyledPanel)
        self.c_sorter_name.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.c_sorter_name)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.bt_sorter_name = CheckButton(self.c_sorter_name)
        self.bt_sorter_name.setObjectName(u"bt_sorter_name")
        self.bt_sorter_name.setMinimumSize(QSize(50, 25))
        self.bt_sorter_name.setMaximumSize(QSize(50, 25))

        self.horizontalLayout_4.addWidget(self.bt_sorter_name)

        self.bt_sorter_date = CheckButton(self.c_sorter_name)
        self.bt_sorter_date.setObjectName(u"bt_sorter_date")
        self.bt_sorter_date.setMinimumSize(QSize(40, 25))
        self.bt_sorter_date.setMaximumSize(QSize(40, 25))

        self.horizontalLayout_4.addWidget(self.bt_sorter_date)


        self.horizontalLayout.addWidget(self.c_sorter_name, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout.addWidget(self.ly_organizer_controllers)


        self.ly_right.addWidget(self.c_organizer)

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
        self.bt_command.setText(QCoreApplication.translate("images", u"View", None))
        self.lb_filters_title.setText(QCoreApplication.translate("images", u"Filters", None))
        self.lb_filter_image_type.setText(QCoreApplication.translate("images", u"Image type", None))
        self.lb_filter_date.setText(QCoreApplication.translate("images", u"Date", None))
        self.lb_filter_date_precise.setText(QCoreApplication.translate("images", u"Precise", None))
        self.lb_filter_date_range.setText(QCoreApplication.translate("images", u"Range", None))
        self.lb_date_range_to.setText(QCoreApplication.translate("images", u"to", None))
        self.lb_description.setText(QCoreApplication.translate("images", u"Description", None))
        self.bt_delete_image.setText(QCoreApplication.translate("images", u"Delete image", None))
        self.bt_clear_selection.setText(QCoreApplication.translate("images", u"Clear selection", None))
        self.lb_organizer_titles.setText(QCoreApplication.translate("images", u"Organizer", None))
        self.bt_sorter_dsc.setText(QCoreApplication.translate("images", u"z-A", None))
        self.bt_sorter_asc.setText(QCoreApplication.translate("images", u"A-z", None))
        self.bt_sorter_name.setText(QCoreApplication.translate("images", u"Name", None))
        self.bt_sorter_date.setText(QCoreApplication.translate("images", u"Date", None))
    # retranslateUi

