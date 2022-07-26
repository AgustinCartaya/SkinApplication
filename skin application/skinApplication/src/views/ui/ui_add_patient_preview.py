# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_add_patient_preview.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from .promoted.button import Button
from .promoted.label import Label
from .promoted.navigator_button import NavigatorButton

class Ui_add_patient_preview(object):
    def setupUi(self, add_patient_preview):
        if not add_patient_preview.objectName():
            add_patient_preview.setObjectName(u"add_patient_preview")
        add_patient_preview.setEnabled(True)
        add_patient_preview.resize(800, 600)
        add_patient_preview.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(add_patient_preview)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 7)
        self.c_navigator = QFrame(add_patient_preview)
        self.c_navigator.setObjectName(u"c_navigator")
        self.c_navigator.setFrameShape(QFrame.StyledPanel)
        self.c_navigator.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.c_navigator)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bt_cancel = NavigatorButton(self.c_navigator)
        self.bt_cancel.setObjectName(u"bt_cancel")

        self.horizontalLayout.addWidget(self.bt_cancel)


        self.verticalLayout.addWidget(self.c_navigator, 0, Qt.AlignLeft|Qt.AlignTop)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.c_center = QFrame(add_patient_preview)
        self.c_center.setObjectName(u"c_center")
        self.c_center.setMinimumSize(QSize(500, 450))
        self.c_center.setFrameShape(QFrame.StyledPanel)
        self.c_center.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.c_center)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lb_title = Label(self.c_center)
        self.lb_title.setObjectName(u"lb_title")

        self.verticalLayout_2.addWidget(self.lb_title, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.scrollArea = QScrollArea(self.c_center)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 496, 318))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.c_up_basic_information = QFrame(self.scrollAreaWidgetContents)
        self.c_up_basic_information.setObjectName(u"c_up_basic_information")
        self.c_up_basic_information.setFrameShape(QFrame.StyledPanel)
        self.c_up_basic_information.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.c_up_basic_information)
        self.verticalLayout_10.setSpacing(16)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lb_basic_information_title = Label(self.c_up_basic_information)
        self.lb_basic_information_title.setObjectName(u"lb_basic_information_title")
        self.lb_basic_information_title.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_10.addWidget(self.lb_basic_information_title)

        self.c_basic_information = QFrame(self.c_up_basic_information)
        self.c_basic_information.setObjectName(u"c_basic_information")
        self.c_basic_information.setFrameShape(QFrame.StyledPanel)
        self.c_basic_information.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.c_basic_information)
        self.horizontalLayout_2.setSpacing(16)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 0, 0, 0)
        self.c_left_basic_information = QFrame(self.c_basic_information)
        self.c_left_basic_information.setObjectName(u"c_left_basic_information")
        self.c_left_basic_information.setFrameShape(QFrame.StyledPanel)
        self.c_left_basic_information.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.c_left_basic_information)
        self.verticalLayout_5.setSpacing(16)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.c_first_name = QFrame(self.c_left_basic_information)
        self.c_first_name.setObjectName(u"c_first_name")
        self.c_first_name.setFrameShape(QFrame.StyledPanel)
        self.c_first_name.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.c_first_name)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lb_first_name = Label(self.c_first_name)
        self.lb_first_name.setObjectName(u"lb_first_name")

        self.verticalLayout_9.addWidget(self.lb_first_name)

        self.i_first_name = Label(self.c_first_name)
        self.i_first_name.setObjectName(u"i_first_name")

        self.verticalLayout_9.addWidget(self.i_first_name, 0, Qt.AlignLeft)


        self.verticalLayout_5.addWidget(self.c_first_name)

        self.c_birth_date = QFrame(self.c_left_basic_information)
        self.c_birth_date.setObjectName(u"c_birth_date")
        self.c_birth_date.setFrameShape(QFrame.StyledPanel)
        self.c_birth_date.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.c_birth_date)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lb_birth_date = Label(self.c_birth_date)
        self.lb_birth_date.setObjectName(u"lb_birth_date")

        self.verticalLayout_8.addWidget(self.lb_birth_date)

        self.i_birth_date = Label(self.c_birth_date)
        self.i_birth_date.setObjectName(u"i_birth_date")

        self.verticalLayout_8.addWidget(self.i_birth_date, 0, Qt.AlignLeft)


        self.verticalLayout_5.addWidget(self.c_birth_date)


        self.horizontalLayout_2.addWidget(self.c_left_basic_information)

        self.c_right_basic_information = QFrame(self.c_basic_information)
        self.c_right_basic_information.setObjectName(u"c_right_basic_information")
        self.c_right_basic_information.setFrameShape(QFrame.StyledPanel)
        self.c_right_basic_information.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.c_right_basic_information)
        self.verticalLayout_4.setSpacing(16)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.c_last_name = QFrame(self.c_right_basic_information)
        self.c_last_name.setObjectName(u"c_last_name")
        self.c_last_name.setFrameShape(QFrame.StyledPanel)
        self.c_last_name.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.c_last_name)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lb_last_name = Label(self.c_last_name)
        self.lb_last_name.setObjectName(u"lb_last_name")

        self.verticalLayout_6.addWidget(self.lb_last_name)

        self.i_last_name = Label(self.c_last_name)
        self.i_last_name.setObjectName(u"i_last_name")

        self.verticalLayout_6.addWidget(self.i_last_name, 0, Qt.AlignLeft)


        self.verticalLayout_4.addWidget(self.c_last_name)

        self.c_gender = QFrame(self.c_right_basic_information)
        self.c_gender.setObjectName(u"c_gender")
        self.c_gender.setFrameShape(QFrame.StyledPanel)
        self.c_gender.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.c_gender)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lb_gender = Label(self.c_gender)
        self.lb_gender.setObjectName(u"lb_gender")

        self.verticalLayout_7.addWidget(self.lb_gender)

        self.i_gender = Label(self.c_gender)
        self.i_gender.setObjectName(u"i_gender")

        self.verticalLayout_7.addWidget(self.i_gender, 0, Qt.AlignLeft)


        self.verticalLayout_4.addWidget(self.c_gender)


        self.horizontalLayout_2.addWidget(self.c_right_basic_information)


        self.verticalLayout_10.addWidget(self.c_basic_information)


        self.verticalLayout_3.addWidget(self.c_up_basic_information)

        self.c_down_medical_information = QFrame(self.scrollAreaWidgetContents)
        self.c_down_medical_information.setObjectName(u"c_down_medical_information")
        self.c_down_medical_information.setFrameShape(QFrame.StyledPanel)
        self.c_down_medical_information.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.c_down_medical_information)
        self.verticalLayout_11.setSpacing(16)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 10)
        self.lb_medical_information_title = Label(self.c_down_medical_information)
        self.lb_medical_information_title.setObjectName(u"lb_medical_information_title")
        self.lb_medical_information_title.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_11.addWidget(self.lb_medical_information_title)

        self.c_medical_information_margin = QFrame(self.c_down_medical_information)
        self.c_medical_information_margin.setObjectName(u"c_medical_information_margin")
        self.c_medical_information_margin.setFrameShape(QFrame.StyledPanel)
        self.c_medical_information_margin.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.c_medical_information_margin)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, 0, 0)
        self.c_medical_information = QFrame(self.c_medical_information_margin)
        self.c_medical_information.setObjectName(u"c_medical_information")
        self.c_medical_information.setFrameShape(QFrame.StyledPanel)
        self.c_medical_information.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.c_medical_information)


        self.verticalLayout_11.addWidget(self.c_medical_information_margin)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_5)


        self.verticalLayout_3.addWidget(self.c_down_medical_information)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.c_buttons = QFrame(self.c_center)
        self.c_buttons.setObjectName(u"c_buttons")
        self.c_buttons.setFrameShape(QFrame.StyledPanel)
        self.c_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.c_buttons)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.bt_back = Button(self.c_buttons)
        self.bt_back.setObjectName(u"bt_back")

        self.horizontalLayout_3.addWidget(self.bt_back)

        self.bt_add = Button(self.c_buttons)
        self.bt_add.setObjectName(u"bt_add")

        self.horizontalLayout_3.addWidget(self.bt_add)


        self.verticalLayout_2.addWidget(self.c_buttons, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.c_center, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.c_rb_views = QFrame(add_patient_preview)
        self.c_rb_views.setObjectName(u"c_rb_views")
        self.c_rb_views.setFrameShape(QFrame.StyledPanel)
        self.c_rb_views.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.c_rb_views)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.i_add_patient_view = QRadioButton(self.c_rb_views)
        self.i_add_patient_view.setObjectName(u"i_add_patient_view")

        self.horizontalLayout_4.addWidget(self.i_add_patient_view)

        self.i_add_patient_mi_view = QRadioButton(self.c_rb_views)
        self.i_add_patient_mi_view.setObjectName(u"i_add_patient_mi_view")
        self.i_add_patient_mi_view.setChecked(False)

        self.horizontalLayout_4.addWidget(self.i_add_patient_mi_view)

        self.i_add_patient_preview_view = QRadioButton(self.c_rb_views)
        self.i_add_patient_preview_view.setObjectName(u"i_add_patient_preview_view")
        self.i_add_patient_preview_view.setChecked(True)

        self.horizontalLayout_4.addWidget(self.i_add_patient_preview_view)


        self.verticalLayout.addWidget(self.c_rb_views, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(add_patient_preview)

        QMetaObject.connectSlotsByName(add_patient_preview)
    # setupUi

    def retranslateUi(self, add_patient_preview):
        add_patient_preview.setWindowTitle(QCoreApplication.translate("add_patient_preview", u"Loggin", None))
        self.bt_cancel.setText(QCoreApplication.translate("add_patient_preview", u"Cancel", None))
        self.lb_title.setText(QCoreApplication.translate("add_patient_preview", u"Patient preview", None))
        self.lb_basic_information_title.setText(QCoreApplication.translate("add_patient_preview", u"Basic information", None))
        self.lb_first_name.setText(QCoreApplication.translate("add_patient_preview", u"First name :", None))
        self.i_first_name.setText(QCoreApplication.translate("add_patient_preview", u"...", None))
        self.lb_birth_date.setText(QCoreApplication.translate("add_patient_preview", u"Date of birth :", None))
        self.i_birth_date.setText(QCoreApplication.translate("add_patient_preview", u"...", None))
        self.lb_last_name.setText(QCoreApplication.translate("add_patient_preview", u"Last name :", None))
        self.i_last_name.setText(QCoreApplication.translate("add_patient_preview", u"...", None))
        self.lb_gender.setText(QCoreApplication.translate("add_patient_preview", u"Gender :", None))
        self.i_gender.setText(QCoreApplication.translate("add_patient_preview", u"...", None))
        self.lb_medical_information_title.setText(QCoreApplication.translate("add_patient_preview", u"Medical information", None))
        self.bt_back.setText(QCoreApplication.translate("add_patient_preview", u"Back", None))
        self.bt_add.setText(QCoreApplication.translate("add_patient_preview", u"Add", None))
        self.i_add_patient_view.setText("")
        self.i_add_patient_mi_view.setText("")
        self.i_add_patient_preview_view.setText("")
    # retranslateUi

