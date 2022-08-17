# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_upsert_patient.ui'
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
    QLabel, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from .promoted.button import Button
from .promoted.label import Label
from .promoted.line_edit import LineEdit
from .promoted.navigator_button import NavigatorButton

class Ui_upsert_patient(object):
    def setupUi(self, upsert_patient):
        if not upsert_patient.objectName():
            upsert_patient.setObjectName(u"upsert_patient")
        upsert_patient.resize(800, 600)
        upsert_patient.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(upsert_patient)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ly_navigator = QHBoxLayout()
        self.ly_navigator.setObjectName(u"ly_navigator")
        self.ly_navigator.setContentsMargins(-1, 0, -1, -1)
        self.bt_cancel = NavigatorButton(upsert_patient)
        self.bt_cancel.setObjectName(u"bt_cancel")

        self.ly_navigator.addWidget(self.bt_cancel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ly_navigator.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.ly_navigator)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.c_center = QFrame(upsert_patient)
        self.c_center.setObjectName(u"c_center")
        self.c_center.setMinimumSize(QSize(500, 0))
        self.c_center.setFrameShape(QFrame.StyledPanel)
        self.c_center.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.c_center)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lb_title = Label(self.c_center)
        self.lb_title.setObjectName(u"lb_title")

        self.verticalLayout_2.addWidget(self.lb_title, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.ly_inputs = QHBoxLayout()
        self.ly_inputs.setSpacing(16)
        self.ly_inputs.setObjectName(u"ly_inputs")
        self.ly_inputs.setContentsMargins(0, 0, -1, -1)
        self.ly_left_side = QVBoxLayout()
        self.ly_left_side.setSpacing(16)
        self.ly_left_side.setObjectName(u"ly_left_side")
        self.ly_left_side.setContentsMargins(-1, 0, -1, -1)
        self.ly_first_name = QVBoxLayout()
        self.ly_first_name.setSpacing(4)
        self.ly_first_name.setObjectName(u"ly_first_name")
        self.ly_first_name.setContentsMargins(-1, 0, -1, -1)
        self.lb_first_name = QLabel(self.c_center)
        self.lb_first_name.setObjectName(u"lb_first_name")

        self.ly_first_name.addWidget(self.lb_first_name)

        self.i_first_name = LineEdit(self.c_center)
        self.i_first_name.setObjectName(u"i_first_name")

        self.ly_first_name.addWidget(self.i_first_name)


        self.ly_left_side.addLayout(self.ly_first_name)

        self.ly_birth_date = QVBoxLayout()
        self.ly_birth_date.setSpacing(4)
        self.ly_birth_date.setObjectName(u"ly_birth_date")
        self.ly_birth_date.setContentsMargins(-1, 0, -1, -1)
        self.lb_birth_date = QLabel(self.c_center)
        self.lb_birth_date.setObjectName(u"lb_birth_date")

        self.ly_birth_date.addWidget(self.lb_birth_date)

        self.i_birth_date = QDateEdit(self.c_center)
        self.i_birth_date.setObjectName(u"i_birth_date")
        self.i_birth_date.setMinimumDate(QDate(1892, 1, 1))

        self.ly_birth_date.addWidget(self.i_birth_date)


        self.ly_left_side.addLayout(self.ly_birth_date)


        self.ly_inputs.addLayout(self.ly_left_side)

        self.ly_right_side = QVBoxLayout()
        self.ly_right_side.setSpacing(16)
        self.ly_right_side.setObjectName(u"ly_right_side")
        self.ly_right_side.setContentsMargins(-1, 0, -1, -1)
        self.c_last_name = QVBoxLayout()
        self.c_last_name.setSpacing(4)
        self.c_last_name.setObjectName(u"c_last_name")
        self.lb_last_name = QLabel(self.c_center)
        self.lb_last_name.setObjectName(u"lb_last_name")

        self.c_last_name.addWidget(self.lb_last_name)

        self.i_last_name = LineEdit(self.c_center)
        self.i_last_name.setObjectName(u"i_last_name")

        self.c_last_name.addWidget(self.i_last_name)


        self.ly_right_side.addLayout(self.c_last_name)

        self.ly_gender = QVBoxLayout()
        self.ly_gender.setSpacing(4)
        self.ly_gender.setObjectName(u"ly_gender")
        self.lb_gender = QLabel(self.c_center)
        self.lb_gender.setObjectName(u"lb_gender")

        self.ly_gender.addWidget(self.lb_gender)

        self.ly_gender_rb = QHBoxLayout()
        self.ly_gender_rb.setObjectName(u"ly_gender_rb")
        self.i_gender_m = QRadioButton(self.c_center)
        self.i_gender_m.setObjectName(u"i_gender_m")

        self.ly_gender_rb.addWidget(self.i_gender_m)

        self.i_gender_f = QRadioButton(self.c_center)
        self.i_gender_f.setObjectName(u"i_gender_f")

        self.ly_gender_rb.addWidget(self.i_gender_f)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ly_gender_rb.addItem(self.horizontalSpacer)


        self.ly_gender.addLayout(self.ly_gender_rb)


        self.ly_right_side.addLayout(self.ly_gender)


        self.ly_inputs.addLayout(self.ly_right_side)


        self.verticalLayout_2.addLayout(self.ly_inputs)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.bt_next = Button(self.c_center)
        self.bt_next.setObjectName(u"bt_next")

        self.verticalLayout_2.addWidget(self.bt_next, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.c_center, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.c_rb_upsert_patient_views = QFrame(upsert_patient)
        self.c_rb_upsert_patient_views.setObjectName(u"c_rb_upsert_patient_views")
        self.c_rb_upsert_patient_views.setFrameShape(QFrame.StyledPanel)
        self.c_rb_upsert_patient_views.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.c_rb_upsert_patient_views)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 16)
        self.i_upsert_patient_view = QRadioButton(self.c_rb_upsert_patient_views)
        self.i_upsert_patient_view.setObjectName(u"i_upsert_patient_view")
        self.i_upsert_patient_view.setChecked(True)

        self.horizontalLayout_2.addWidget(self.i_upsert_patient_view)

        self.i_upsert_patient_mi_view = QRadioButton(self.c_rb_upsert_patient_views)
        self.i_upsert_patient_mi_view.setObjectName(u"i_upsert_patient_mi_view")

        self.horizontalLayout_2.addWidget(self.i_upsert_patient_mi_view)

        self.i_upsert_patient_preview_view = QRadioButton(self.c_rb_upsert_patient_views)
        self.i_upsert_patient_preview_view.setObjectName(u"i_upsert_patient_preview_view")

        self.horizontalLayout_2.addWidget(self.i_upsert_patient_preview_view)


        self.verticalLayout.addWidget(self.c_rb_upsert_patient_views, 0, Qt.AlignHCenter)


        self.retranslateUi(upsert_patient)

        QMetaObject.connectSlotsByName(upsert_patient)
    # setupUi

    def retranslateUi(self, upsert_patient):
        upsert_patient.setWindowTitle(QCoreApplication.translate("upsert_patient", u"Loggin", None))
        self.bt_cancel.setText(QCoreApplication.translate("upsert_patient", u"Cancel", None))
        self.lb_title.setText(QCoreApplication.translate("upsert_patient", u"Add patient", None))
        self.lb_first_name.setText(QCoreApplication.translate("upsert_patient", u"First name", None))
        self.lb_birth_date.setText(QCoreApplication.translate("upsert_patient", u"Date of birth", None))
        self.i_birth_date.setDisplayFormat(QCoreApplication.translate("upsert_patient", u"dd-MM-yyyy", None))
        self.lb_last_name.setText(QCoreApplication.translate("upsert_patient", u"Last name", None))
        self.lb_gender.setText(QCoreApplication.translate("upsert_patient", u"Gender", None))
        self.i_gender_m.setText(QCoreApplication.translate("upsert_patient", u"Male", None))
        self.i_gender_f.setText(QCoreApplication.translate("upsert_patient", u"Female", None))
        self.bt_next.setText(QCoreApplication.translate("upsert_patient", u"Next", None))
        self.i_upsert_patient_view.setText("")
        self.i_upsert_patient_mi_view.setText("")
        self.i_upsert_patient_preview_view.setText("")
    # retranslateUi

