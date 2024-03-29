# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_upsert_patient_preview.ui'
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

class Ui_upsert_patient_preview(object):
    def setupUi(self, upsert_patient_preview):
        if not upsert_patient_preview.objectName():
            upsert_patient_preview.setObjectName(u"upsert_patient_preview")
        upsert_patient_preview.setEnabled(True)
        upsert_patient_preview.resize(800, 600)
        upsert_patient_preview.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(upsert_patient_preview)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.c_navigator = QFrame(upsert_patient_preview)
        self.c_navigator.setObjectName(u"c_navigator")
        self.c_navigator.setFrameShape(QFrame.StyledPanel)
        self.c_navigator.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.c_navigator)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.c_navigator, 0, Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, -1, -1)
        self.bt_cancel = NavigatorButton(upsert_patient_preview)
        self.bt_cancel.setObjectName(u"bt_cancel")

        self.horizontalLayout_6.addWidget(self.bt_cancel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.c_center = QFrame(upsert_patient_preview)
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
        self.c_patient_information_preview = QWidget()
        self.c_patient_information_preview.setObjectName(u"c_patient_information_preview")
        self.c_patient_information_preview.setGeometry(QRect(0, 0, 496, 349))
        self.verticalLayout_3 = QVBoxLayout(self.c_patient_information_preview)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ly_patient_information_preview = QVBoxLayout()
        self.ly_patient_information_preview.setSpacing(30)
        self.ly_patient_information_preview.setObjectName(u"ly_patient_information_preview")
        self.ly_patient_information_preview.setContentsMargins(-1, -1, 9, -1)
        self.ly_basic_information = QVBoxLayout()
        self.ly_basic_information.setObjectName(u"ly_basic_information")
        self.ly_basic_information.setContentsMargins(-1, 0, -1, -1)
        self.lb_basic_information_title = Label(self.c_patient_information_preview)
        self.lb_basic_information_title.setObjectName(u"lb_basic_information_title")

        self.ly_basic_information.addWidget(self.lb_basic_information_title)

        self.ly_bi_content = QHBoxLayout()
        self.ly_bi_content.setSpacing(16)
        self.ly_bi_content.setObjectName(u"ly_bi_content")
        self.ly_bi_content.setContentsMargins(9, 0, -1, -1)
        self.ly_bi_left = QVBoxLayout()
        self.ly_bi_left.setSpacing(16)
        self.ly_bi_left.setObjectName(u"ly_bi_left")
        self.ly_bi_left.setContentsMargins(-1, 0, -1, -1)
        self.ly_first_name = QVBoxLayout()
        self.ly_first_name.setSpacing(4)
        self.ly_first_name.setObjectName(u"ly_first_name")
        self.ly_first_name.setContentsMargins(-1, 0, -1, -1)
        self.lb_first_name = Label(self.c_patient_information_preview)
        self.lb_first_name.setObjectName(u"lb_first_name")

        self.ly_first_name.addWidget(self.lb_first_name)

        self.i_first_name = Label(self.c_patient_information_preview)
        self.i_first_name.setObjectName(u"i_first_name")

        self.ly_first_name.addWidget(self.i_first_name)


        self.ly_bi_left.addLayout(self.ly_first_name)

        self.ly_birth_date = QVBoxLayout()
        self.ly_birth_date.setSpacing(4)
        self.ly_birth_date.setObjectName(u"ly_birth_date")
        self.ly_birth_date.setContentsMargins(-1, 0, -1, -1)
        self.lb_birth_date = Label(self.c_patient_information_preview)
        self.lb_birth_date.setObjectName(u"lb_birth_date")

        self.ly_birth_date.addWidget(self.lb_birth_date)

        self.i_birth_date = Label(self.c_patient_information_preview)
        self.i_birth_date.setObjectName(u"i_birth_date")

        self.ly_birth_date.addWidget(self.i_birth_date)


        self.ly_bi_left.addLayout(self.ly_birth_date)


        self.ly_bi_content.addLayout(self.ly_bi_left)

        self.ly_bi_right = QVBoxLayout()
        self.ly_bi_right.setSpacing(16)
        self.ly_bi_right.setObjectName(u"ly_bi_right")
        self.ly_bi_right.setContentsMargins(-1, 0, -1, -1)
        self.ly_last_name = QVBoxLayout()
        self.ly_last_name.setSpacing(4)
        self.ly_last_name.setObjectName(u"ly_last_name")
        self.lb_last_name = Label(self.c_patient_information_preview)
        self.lb_last_name.setObjectName(u"lb_last_name")

        self.ly_last_name.addWidget(self.lb_last_name)

        self.i_last_name = Label(self.c_patient_information_preview)
        self.i_last_name.setObjectName(u"i_last_name")

        self.ly_last_name.addWidget(self.i_last_name)


        self.ly_bi_right.addLayout(self.ly_last_name)

        self.ly_gender = QVBoxLayout()
        self.ly_gender.setSpacing(4)
        self.ly_gender.setObjectName(u"ly_gender")
        self.ly_gender.setContentsMargins(-1, 0, -1, -1)
        self.lb_gender = Label(self.c_patient_information_preview)
        self.lb_gender.setObjectName(u"lb_gender")

        self.ly_gender.addWidget(self.lb_gender)

        self.i_gender = Label(self.c_patient_information_preview)
        self.i_gender.setObjectName(u"i_gender")

        self.ly_gender.addWidget(self.i_gender)


        self.ly_bi_right.addLayout(self.ly_gender)


        self.ly_bi_content.addLayout(self.ly_bi_right)


        self.ly_basic_information.addLayout(self.ly_bi_content)


        self.ly_patient_information_preview.addLayout(self.ly_basic_information)

        self.c_problem = QFrame(self.c_patient_information_preview)
        self.c_problem.setObjectName(u"c_problem")
        self.c_problem.setFrameShape(QFrame.StyledPanel)
        self.c_problem.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.c_problem)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ly_medical_information = QVBoxLayout()
        self.ly_medical_information.setSpacing(16)
        self.ly_medical_information.setObjectName(u"ly_medical_information")
        self.ly_medical_information.setContentsMargins(-1, 0, -1, -1)
        self.lb_medical_information_title = Label(self.c_problem)
        self.lb_medical_information_title.setObjectName(u"lb_medical_information_title")

        self.ly_medical_information.addWidget(self.lb_medical_information_title)

        self.ly_mi_content = QVBoxLayout()
        self.ly_mi_content.setSpacing(16)
        self.ly_mi_content.setObjectName(u"ly_mi_content")
        self.ly_mi_content.setContentsMargins(9, -1, -1, -1)

        self.ly_medical_information.addLayout(self.ly_mi_content)


        self.verticalLayout_4.addLayout(self.ly_medical_information)


        self.ly_patient_information_preview.addWidget(self.c_problem)


        self.verticalLayout_3.addLayout(self.ly_patient_information_preview)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.scrollArea.setWidget(self.c_patient_information_preview)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.ly_buttons = QHBoxLayout()
        self.ly_buttons.setObjectName(u"ly_buttons")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ly_buttons.addItem(self.horizontalSpacer)

        self.bt_back = Button(self.c_center)
        self.bt_back.setObjectName(u"bt_back")

        self.ly_buttons.addWidget(self.bt_back)

        self.bt_upsert = Button(self.c_center)
        self.bt_upsert.setObjectName(u"bt_upsert")

        self.ly_buttons.addWidget(self.bt_upsert)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ly_buttons.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.ly_buttons)


        self.verticalLayout.addWidget(self.c_center, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.c_rb_upsert_patient_views = QFrame(upsert_patient_preview)
        self.c_rb_upsert_patient_views.setObjectName(u"c_rb_upsert_patient_views")
        self.c_rb_upsert_patient_views.setFrameShape(QFrame.StyledPanel)
        self.c_rb_upsert_patient_views.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.c_rb_upsert_patient_views)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 16)
        self.i_upsert_patient_view = QRadioButton(self.c_rb_upsert_patient_views)
        self.i_upsert_patient_view.setObjectName(u"i_upsert_patient_view")

        self.horizontalLayout_2.addWidget(self.i_upsert_patient_view)

        self.i_upsert_patient_mi_view = QRadioButton(self.c_rb_upsert_patient_views)
        self.i_upsert_patient_mi_view.setObjectName(u"i_upsert_patient_mi_view")

        self.horizontalLayout_2.addWidget(self.i_upsert_patient_mi_view)

        self.i_upsert_patient_preview_view = QRadioButton(self.c_rb_upsert_patient_views)
        self.i_upsert_patient_preview_view.setObjectName(u"i_upsert_patient_preview_view")
        self.i_upsert_patient_preview_view.setChecked(True)

        self.horizontalLayout_2.addWidget(self.i_upsert_patient_preview_view)


        self.verticalLayout.addWidget(self.c_rb_upsert_patient_views, 0, Qt.AlignHCenter)


        self.retranslateUi(upsert_patient_preview)

        QMetaObject.connectSlotsByName(upsert_patient_preview)
    # setupUi

    def retranslateUi(self, upsert_patient_preview):
        upsert_patient_preview.setWindowTitle(QCoreApplication.translate("upsert_patient_preview", u"Loggin", None))
        self.bt_cancel.setText(QCoreApplication.translate("upsert_patient_preview", u"Cancel", None))
        self.lb_title.setText(QCoreApplication.translate("upsert_patient_preview", u"Patient preview", None))
        self.lb_basic_information_title.setText(QCoreApplication.translate("upsert_patient_preview", u"Basic information", None))
        self.lb_first_name.setText(QCoreApplication.translate("upsert_patient_preview", u"First name :", None))
        self.i_first_name.setText(QCoreApplication.translate("upsert_patient_preview", u"...", None))
        self.lb_birth_date.setText(QCoreApplication.translate("upsert_patient_preview", u"Date of birth :", None))
        self.i_birth_date.setText(QCoreApplication.translate("upsert_patient_preview", u"...", None))
        self.lb_last_name.setText(QCoreApplication.translate("upsert_patient_preview", u"Last name :", None))
        self.i_last_name.setText(QCoreApplication.translate("upsert_patient_preview", u"...", None))
        self.lb_gender.setText(QCoreApplication.translate("upsert_patient_preview", u"Gender :", None))
        self.i_gender.setText(QCoreApplication.translate("upsert_patient_preview", u"...", None))
        self.lb_medical_information_title.setText(QCoreApplication.translate("upsert_patient_preview", u"Medical information", None))
        self.bt_back.setText(QCoreApplication.translate("upsert_patient_preview", u"Back", None))
        self.bt_upsert.setText(QCoreApplication.translate("upsert_patient_preview", u"Add", None))
        self.i_upsert_patient_view.setText("")
        self.i_upsert_patient_mi_view.setText("")
        self.i_upsert_patient_preview_view.setText("")
    # retranslateUi

