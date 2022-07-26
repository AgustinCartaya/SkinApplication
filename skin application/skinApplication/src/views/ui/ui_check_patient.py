# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_check_patient.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from .promoted.button import Button
from .promoted.label import Label
from .promoted.navigator_button import NavigatorButton

class Ui_check_patient(object):
    def setupUi(self, check_patient):
        if not check_patient.objectName():
            check_patient.setObjectName(u"check_patient")
        check_patient.resize(1200, 800)
        check_patient.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(check_patient)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(check_patient)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 60))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bt_back = NavigatorButton(self.frame_6)
        self.bt_back.setObjectName(u"bt_back")

        self.horizontalLayout.addWidget(self.bt_back)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lb_title = Label(self.frame_6)
        self.lb_title.setObjectName(u"lb_title")

        self.horizontalLayout.addWidget(self.lb_title)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.bt_add_new_skin_part = NavigatorButton(self.frame_6)
        self.bt_add_new_skin_part.setObjectName(u"bt_add_new_skin_part")

        self.horizontalLayout.addWidget(self.bt_add_new_skin_part)

        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(3, 3)

        self.verticalLayout_2.addWidget(self.frame_6)

        self.c_center = QFrame(check_patient)
        self.c_center.setObjectName(u"c_center")
        self.c_center.setFrameShape(QFrame.StyledPanel)
        self.c_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.c_center)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 18, 0)
        self.c_patient_information = QFrame(self.c_center)
        self.c_patient_information.setObjectName(u"c_patient_information")
        self.c_patient_information.setMinimumSize(QSize(280, 0))
        self.c_patient_information.setMaximumSize(QSize(280, 16777215))
        self.c_patient_information.setFrameShape(QFrame.StyledPanel)
        self.c_patient_information.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.c_patient_information)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 18)
        self.lb_patient_information = Label(self.c_patient_information)
        self.lb_patient_information.setObjectName(u"lb_patient_information")
        self.lb_patient_information.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.lb_patient_information, 0, Qt.AlignHCenter)

        self.scrollArea = QScrollArea(self.c_patient_information)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.c_basic_information_scroll_area = QWidget()
        self.c_basic_information_scroll_area.setObjectName(u"c_basic_information_scroll_area")
        self.c_basic_information_scroll_area.setGeometry(QRect(0, 0, 258, 335))
        self.verticalLayout_5 = QVBoxLayout(self.c_basic_information_scroll_area)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.c_basic_information = QFrame(self.c_basic_information_scroll_area)
        self.c_basic_information.setObjectName(u"c_basic_information")
        self.c_basic_information.setFrameShape(QFrame.StyledPanel)
        self.c_basic_information.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.c_basic_information)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lb_basic_information = Label(self.c_basic_information)
        self.lb_basic_information.setObjectName(u"lb_basic_information")
        self.lb_basic_information.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_7.addWidget(self.lb_basic_information)

        self.c_bi_content = QFrame(self.c_basic_information)
        self.c_bi_content.setObjectName(u"c_bi_content")
        self.c_bi_content.setFrameShape(QFrame.StyledPanel)
        self.c_bi_content.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.c_bi_content)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(16)
        self.lb_first_name = Label(self.c_bi_content)
        self.lb_first_name.setObjectName(u"lb_first_name")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lb_first_name)

        self.i_first_name = Label(self.c_bi_content)
        self.i_first_name.setObjectName(u"i_first_name")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.i_first_name)

        self.lb_last_name = Label(self.c_bi_content)
        self.lb_last_name.setObjectName(u"lb_last_name")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lb_last_name)

        self.i_last_name = Label(self.c_bi_content)
        self.i_last_name.setObjectName(u"i_last_name")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.i_last_name)

        self.lb_gender = Label(self.c_bi_content)
        self.lb_gender.setObjectName(u"lb_gender")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lb_gender)

        self.i_gender = Label(self.c_bi_content)
        self.i_gender.setObjectName(u"i_gender")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.i_gender)

        self.leb_age = Label(self.c_bi_content)
        self.leb_age.setObjectName(u"leb_age")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.leb_age)

        self.i_age = Label(self.c_bi_content)
        self.i_age.setObjectName(u"i_age")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.i_age)


        self.verticalLayout_7.addWidget(self.c_bi_content)


        self.verticalLayout_5.addWidget(self.c_basic_information)

        self.c_medical_information = QFrame(self.c_basic_information_scroll_area)
        self.c_medical_information.setObjectName(u"c_medical_information")
        self.c_medical_information.setFrameShape(QFrame.StyledPanel)
        self.c_medical_information.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.c_medical_information)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lb_medical_information = Label(self.c_medical_information)
        self.lb_medical_information.setObjectName(u"lb_medical_information")
        self.lb_medical_information.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_8.addWidget(self.lb_medical_information)

        self.c_mi_content = QFrame(self.c_medical_information)
        self.c_mi_content.setObjectName(u"c_mi_content")
        self.c_mi_content.setFrameShape(QFrame.StyledPanel)
        self.c_mi_content.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.c_mi_content)


        self.verticalLayout_5.addWidget(self.c_medical_information)

        self.scrollArea.setWidget(self.c_basic_information_scroll_area)

        self.verticalLayout.addWidget(self.scrollArea)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.bt_edit_patient_info = Button(self.c_patient_information)
        self.bt_edit_patient_info.setObjectName(u"bt_edit_patient_info")

        self.verticalLayout.addWidget(self.bt_edit_patient_info, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.c_patient_information)

        self.frame = QFrame(self.c_center)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = Label(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter)

        self.scrollArea_2 = QScrollArea(self.frame)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.c_skin_parts_scroll_area = QWidget()
        self.c_skin_parts_scroll_area.setObjectName(u"c_skin_parts_scroll_area")
        self.c_skin_parts_scroll_area.setGeometry(QRect(0, 0, 872, 702))
        self.verticalLayout_6 = QVBoxLayout(self.c_skin_parts_scroll_area)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.c_skin_lesions = QFrame(self.c_skin_parts_scroll_area)
        self.c_skin_lesions.setObjectName(u"c_skin_lesions")
        self.c_skin_lesions.setFrameShape(QFrame.StyledPanel)
        self.c_skin_lesions.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.c_skin_lesions)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.scrollArea_2.setWidget(self.c_skin_parts_scroll_area)

        self.verticalLayout_3.addWidget(self.scrollArea_2)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.c_center)


        self.retranslateUi(check_patient)

        QMetaObject.connectSlotsByName(check_patient)
    # setupUi

    def retranslateUi(self, check_patient):
        check_patient.setWindowTitle(QCoreApplication.translate("check_patient", u"Loggin", None))
        self.bt_back.setText(QCoreApplication.translate("check_patient", u"Back", None))
        self.lb_title.setText(QCoreApplication.translate("check_patient", u"Check patient", None))
        self.bt_add_new_skin_part.setText(QCoreApplication.translate("check_patient", u"Add skin part", None))
        self.lb_patient_information.setText(QCoreApplication.translate("check_patient", u"Patient information", None))
        self.lb_basic_information.setText(QCoreApplication.translate("check_patient", u"Basic information", None))
        self.lb_first_name.setText(QCoreApplication.translate("check_patient", u"First name :", None))
        self.i_first_name.setText(QCoreApplication.translate("check_patient", u"...", None))
        self.lb_last_name.setText(QCoreApplication.translate("check_patient", u"Last name :", None))
        self.i_last_name.setText(QCoreApplication.translate("check_patient", u"...", None))
        self.lb_gender.setText(QCoreApplication.translate("check_patient", u"Gender :", None))
        self.i_gender.setText(QCoreApplication.translate("check_patient", u"...", None))
        self.leb_age.setText(QCoreApplication.translate("check_patient", u"Age :", None))
        self.i_age.setText(QCoreApplication.translate("check_patient", u"...", None))
        self.lb_medical_information.setText(QCoreApplication.translate("check_patient", u"Madical information", None))
        self.bt_edit_patient_info.setText(QCoreApplication.translate("check_patient", u"Edit patient information", None))
        self.label.setText(QCoreApplication.translate("check_patient", u"Parts of the sking under study", None))
    # retranslateUi

