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
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ly_navigator = QHBoxLayout()
        self.ly_navigator.setObjectName(u"ly_navigator")
        self.ly_navigator.setContentsMargins(-1, 0, -1, -1)
        self.bt_back = NavigatorButton(check_patient)
        self.bt_back.setObjectName(u"bt_back")

        self.ly_navigator.addWidget(self.bt_back, 0, Qt.AlignLeft)

        self.lb_title = Label(check_patient)
        self.lb_title.setObjectName(u"lb_title")

        self.ly_navigator.addWidget(self.lb_title, 0, Qt.AlignHCenter)

        self.bt_add_lesion = NavigatorButton(check_patient)
        self.bt_add_lesion.setObjectName(u"bt_add_lesion")

        self.ly_navigator.addWidget(self.bt_add_lesion, 0, Qt.AlignRight)

        self.ly_navigator.setStretch(0, 1)
        self.ly_navigator.setStretch(1, 1)
        self.ly_navigator.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.ly_navigator)

        self.ly_center = QHBoxLayout()
        self.ly_center.setSpacing(20)
        self.ly_center.setObjectName(u"ly_center")
        self.ly_center.setContentsMargins(-1, 20, -1, -1)
        self.c_patient_information = QFrame(check_patient)
        self.c_patient_information.setObjectName(u"c_patient_information")
        self.c_patient_information.setMinimumSize(QSize(280, 0))
        self.c_patient_information.setMaximumSize(QSize(280, 16777215))
        self.c_patient_information.setFrameShape(QFrame.StyledPanel)
        self.c_patient_information.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.c_patient_information)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_patient_information = Label(self.c_patient_information)
        self.lb_patient_information.setObjectName(u"lb_patient_information")
        self.lb_patient_information.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.lb_patient_information, 0, Qt.AlignHCenter)

        self.scrollArea = QScrollArea(self.c_patient_information)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.c_patient_information_content = QWidget()
        self.c_patient_information_content.setObjectName(u"c_patient_information_content")
        self.c_patient_information_content.setGeometry(QRect(0, 0, 276, 648))
        self.verticalLayout_5 = QVBoxLayout(self.c_patient_information_content)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(30, 0, 0, -1)
        self.ly_patient_information = QVBoxLayout()
        self.ly_patient_information.setSpacing(20)
        self.ly_patient_information.setObjectName(u"ly_patient_information")
        self.ly_patient_information.setContentsMargins(-1, 10, -1, -1)
        self.ly_id = QFormLayout()
        self.ly_id.setObjectName(u"ly_id")
        self.ly_id.setHorizontalSpacing(9)
        self.ly_id.setContentsMargins(-1, 0, -1, -1)
        self.lb_id = Label(self.c_patient_information_content)
        self.lb_id.setObjectName(u"lb_id")

        self.ly_id.setWidget(0, QFormLayout.LabelRole, self.lb_id)

        self.i_id = Label(self.c_patient_information_content)
        self.i_id.setObjectName(u"i_id")

        self.ly_id.setWidget(0, QFormLayout.FieldRole, self.i_id)


        self.ly_patient_information.addLayout(self.ly_id)

        self.ly_basic_information = QVBoxLayout()
        self.ly_basic_information.setSpacing(12)
        self.ly_basic_information.setObjectName(u"ly_basic_information")
        self.lb_basic_information = Label(self.c_patient_information_content)
        self.lb_basic_information.setObjectName(u"lb_basic_information")
        self.lb_basic_information.setMaximumSize(QSize(16777215, 20))

        self.ly_basic_information.addWidget(self.lb_basic_information)

        self.ly_bi_content = QFormLayout()
        self.ly_bi_content.setObjectName(u"ly_bi_content")
        self.ly_bi_content.setHorizontalSpacing(9)
        self.ly_bi_content.setVerticalSpacing(16)
        self.ly_bi_content.setContentsMargins(9, 0, 0, 0)
        self.lb_first_name = Label(self.c_patient_information_content)
        self.lb_first_name.setObjectName(u"lb_first_name")

        self.ly_bi_content.setWidget(0, QFormLayout.LabelRole, self.lb_first_name)

        self.i_first_name = Label(self.c_patient_information_content)
        self.i_first_name.setObjectName(u"i_first_name")

        self.ly_bi_content.setWidget(0, QFormLayout.FieldRole, self.i_first_name)

        self.lb_last_name = Label(self.c_patient_information_content)
        self.lb_last_name.setObjectName(u"lb_last_name")

        self.ly_bi_content.setWidget(1, QFormLayout.LabelRole, self.lb_last_name)

        self.i_last_name = Label(self.c_patient_information_content)
        self.i_last_name.setObjectName(u"i_last_name")

        self.ly_bi_content.setWidget(1, QFormLayout.FieldRole, self.i_last_name)

        self.lb_gender = Label(self.c_patient_information_content)
        self.lb_gender.setObjectName(u"lb_gender")

        self.ly_bi_content.setWidget(2, QFormLayout.LabelRole, self.lb_gender)

        self.i_gender = Label(self.c_patient_information_content)
        self.i_gender.setObjectName(u"i_gender")

        self.ly_bi_content.setWidget(2, QFormLayout.FieldRole, self.i_gender)

        self.leb_age = Label(self.c_patient_information_content)
        self.leb_age.setObjectName(u"leb_age")

        self.ly_bi_content.setWidget(3, QFormLayout.LabelRole, self.leb_age)

        self.i_age = Label(self.c_patient_information_content)
        self.i_age.setObjectName(u"i_age")

        self.ly_bi_content.setWidget(3, QFormLayout.FieldRole, self.i_age)


        self.ly_basic_information.addLayout(self.ly_bi_content)


        self.ly_patient_information.addLayout(self.ly_basic_information)

        self.ly_medical_information = QVBoxLayout()
        self.ly_medical_information.setSpacing(12)
        self.ly_medical_information.setObjectName(u"ly_medical_information")
        self.lb_medical_information = Label(self.c_patient_information_content)
        self.lb_medical_information.setObjectName(u"lb_medical_information")
        self.lb_medical_information.setMaximumSize(QSize(16777215, 20))

        self.ly_medical_information.addWidget(self.lb_medical_information)

        self.ly_mi_content = QFormLayout()
        self.ly_mi_content.setObjectName(u"ly_mi_content")
        self.ly_mi_content.setHorizontalSpacing(9)
        self.ly_mi_content.setVerticalSpacing(16)
        self.ly_mi_content.setContentsMargins(9, 9, 9, 9)

        self.ly_medical_information.addLayout(self.ly_mi_content)


        self.ly_patient_information.addLayout(self.ly_medical_information)


        self.verticalLayout_5.addLayout(self.ly_patient_information)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.c_patient_information_content)

        self.verticalLayout.addWidget(self.scrollArea)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 20)
        self.bt_edit_patient_info = Button(self.c_patient_information)
        self.bt_edit_patient_info.setObjectName(u"bt_edit_patient_info")

        self.verticalLayout_3.addWidget(self.bt_edit_patient_info, 0, Qt.AlignHCenter)


        self.verticalLayout.addLayout(self.verticalLayout_3)


        self.ly_center.addWidget(self.c_patient_information)

        self.ly_right = QVBoxLayout()
        self.ly_right.setObjectName(u"ly_right")
        self.ly_right.setContentsMargins(-1, -1, 20, 20)
        self.lb_title_2 = Label(check_patient)
        self.lb_title_2.setObjectName(u"lb_title_2")
        self.lb_title_2.setMaximumSize(QSize(16777215, 20))

        self.ly_right.addWidget(self.lb_title_2, 0, Qt.AlignHCenter)

        self.sc_skin_lesions_preview = QScrollArea(check_patient)
        self.sc_skin_lesions_preview.setObjectName(u"sc_skin_lesions_preview")
        self.sc_skin_lesions_preview.setWidgetResizable(True)
        self.c_skin_lesions_preview = QWidget()
        self.c_skin_lesions_preview.setObjectName(u"c_skin_lesions_preview")
        self.c_skin_lesions_preview.setGeometry(QRect(0, 0, 875, 708))
        self.verticalLayout_6 = QVBoxLayout(self.c_skin_lesions_preview)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.ly_skin_lesions_preview = QVBoxLayout()
        self.ly_skin_lesions_preview.setSpacing(40)
        self.ly_skin_lesions_preview.setObjectName(u"ly_skin_lesions_preview")

        self.verticalLayout_6.addLayout(self.ly_skin_lesions_preview)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.sc_skin_lesions_preview.setWidget(self.c_skin_lesions_preview)

        self.ly_right.addWidget(self.sc_skin_lesions_preview)


        self.ly_center.addLayout(self.ly_right)


        self.verticalLayout_2.addLayout(self.ly_center)


        self.retranslateUi(check_patient)

        QMetaObject.connectSlotsByName(check_patient)
    # setupUi

    def retranslateUi(self, check_patient):
        check_patient.setWindowTitle(QCoreApplication.translate("check_patient", u"Loggin", None))
        self.bt_back.setText(QCoreApplication.translate("check_patient", u"Back", None))
        self.lb_title.setText(QCoreApplication.translate("check_patient", u"Check patient", None))
        self.bt_add_lesion.setText(QCoreApplication.translate("check_patient", u"Add lesion", None))
        self.lb_patient_information.setText(QCoreApplication.translate("check_patient", u"Patient information", None))
        self.lb_id.setText(QCoreApplication.translate("check_patient", u"ID :", None))
        self.i_id.setText(QCoreApplication.translate("check_patient", u"...", None))
        self.lb_basic_information.setText(QCoreApplication.translate("check_patient", u"Basic information", None))
        self.lb_first_name.setText(QCoreApplication.translate("check_patient", u"First name :", None))
        self.i_first_name.setText(QCoreApplication.translate("check_patient", u"...", None))
        self.lb_last_name.setText(QCoreApplication.translate("check_patient", u"Last name :", None))
        self.i_last_name.setText(QCoreApplication.translate("check_patient", u"...", None))
        self.lb_gender.setText(QCoreApplication.translate("check_patient", u"Gender :", None))
        self.i_gender.setText(QCoreApplication.translate("check_patient", u"...", None))
        self.leb_age.setText(QCoreApplication.translate("check_patient", u"Age :", None))
        self.i_age.setText(QCoreApplication.translate("check_patient", u"...", None))
        self.lb_medical_information.setText(QCoreApplication.translate("check_patient", u"Medical information", None))
        self.bt_edit_patient_info.setText(QCoreApplication.translate("check_patient", u"Edit patient information", None))
        self.lb_title_2.setText(QCoreApplication.translate("check_patient", u"Parts of the sking under study", None))
    # retranslateUi

