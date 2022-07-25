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
    QLabel, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

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
        self.c_patient_information.setMinimumSize(QSize(300, 0))
        self.c_patient_information.setMaximumSize(QSize(330, 16777215))
        self.c_patient_information.setFrameShape(QFrame.StyledPanel)
        self.c_patient_information.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.c_patient_information)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_patient_information = Label(self.c_patient_information)
        self.lb_patient_information.setObjectName(u"lb_patient_information")
        self.lb_patient_information.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.lb_patient_information, 0, Qt.AlignHCenter)

        self.scrollArea = QScrollArea(self.c_patient_information)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 308, 339))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.c_basic_information = QFrame(self.scrollAreaWidgetContents)
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

        self.c_medical_information = QFrame(self.scrollAreaWidgetContents)
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

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_2 = Button(self.c_patient_information)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.c_patient_information)

        self.frame = QFrame(self.c_center)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = Label(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter)

        self.scrollArea_2 = QScrollArea(self.frame)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 822, 716))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.c_skin_parts = QFrame(self.scrollAreaWidgetContents_4)
        self.c_skin_parts.setObjectName(u"c_skin_parts")
        self.c_skin_parts.setFrameShape(QFrame.StyledPanel)
        self.c_skin_parts.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.c_skin_parts)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.c_skin_parts)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 100))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_10)

        self.pushButton_5 = Button(self.frame_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(160, 16777215))

        self.verticalLayout_10.addWidget(self.pushButton_5, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)


        self.horizontalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_8)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_12.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_11)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(12)
        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.label_7 = QLabel(self.frame_11)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_7)

        self.label_5 = QLabel(self.frame_11)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_8)

        self.label_6 = QLabel(self.frame_11)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.label_9 = QLabel(self.frame_11)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_9)


        self.verticalLayout_12.addWidget(self.frame_11)


        self.horizontalLayout_4.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_11.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.frame_12)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setVerticalSpacing(12)
        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_10)

        self.label_13 = QLabel(self.frame_12)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.label_13)

        self.label_11 = QLabel(self.frame_12)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_11)

        self.label_14 = QLabel(self.frame_12)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.label_14)

        self.label_12 = QLabel(self.frame_12)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_12)

        self.label_15 = QLabel(self.frame_12)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.label_15)


        self.verticalLayout_11.addWidget(self.frame_12)


        self.horizontalLayout_4.addWidget(self.frame_9)


        self.horizontalLayout_3.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.pushButton = Button(self.frame_7)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(120, 0))
        self.pushButton.setMaximumSize(QSize(120, 16777215))

        self.verticalLayout_9.addWidget(self.pushButton, 0, Qt.AlignLeft)

        self.pushButton_3 = Button(self.frame_7)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(120, 0))
        self.pushButton_3.setMaximumSize(QSize(120, 16777215))

        self.verticalLayout_9.addWidget(self.pushButton_3, 0, Qt.AlignLeft)

        self.pushButton_4 = Button(self.frame_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(120, 0))
        self.pushButton_4.setMaximumSize(QSize(120, 16777215))

        self.verticalLayout_9.addWidget(self.pushButton_4, 0, Qt.AlignLeft)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addWidget(self.frame_7)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 6)
        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.c_skin_parts)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_3)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)

        self.verticalLayout_6.addWidget(self.c_skin_parts)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)

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
        self.pushButton_2.setText(QCoreApplication.translate("check_patient", u"Edit patient information", None))
        self.label.setText(QCoreApplication.translate("check_patient", u"Parts of the sking under study", None))
        self.pushButton_5.setText(QCoreApplication.translate("check_patient", u"Update", None))
        self.label_2.setText(QCoreApplication.translate("check_patient", u"Annotations", None))
        self.label_4.setText(QCoreApplication.translate("check_patient", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("check_patient", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("check_patient", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("check_patient", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("check_patient", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("check_patient", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("check_patient", u"AI results", None))
        self.label_10.setText(QCoreApplication.translate("check_patient", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("check_patient", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("check_patient", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("check_patient", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("check_patient", u"TextLabel", None))
        self.label_15.setText(QCoreApplication.translate("check_patient", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("check_patient", u"See time line", None))
        self.pushButton_3.setText(QCoreApplication.translate("check_patient", u"See images", None))
        self.pushButton_4.setText(QCoreApplication.translate("check_patient", u"More options", None))
    # retranslateUi

