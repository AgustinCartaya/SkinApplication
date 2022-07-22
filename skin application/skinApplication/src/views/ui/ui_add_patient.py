# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_add_patient.ui'
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

class Ui_add_patient(object):
    def setupUi(self, add_patient):
        if not add_patient.objectName():
            add_patient.setObjectName(u"add_patient")
        add_patient.resize(800, 600)
        add_patient.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(add_patient)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 7)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.c_center = QFrame(add_patient)
        self.c_center.setObjectName(u"c_center")
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

        self.c_inputs = QFrame(self.c_center)
        self.c_inputs.setObjectName(u"c_inputs")
        self.c_inputs.setFrameShape(QFrame.StyledPanel)
        self.c_inputs.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.c_inputs)
        self.horizontalLayout.setSpacing(16)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.c_left_side = QFrame(self.c_inputs)
        self.c_left_side.setObjectName(u"c_left_side")
        self.c_left_side.setMinimumSize(QSize(250, 0))
        self.c_left_side.setMaximumSize(QSize(250, 300))
        self.c_left_side.setFrameShape(QFrame.StyledPanel)
        self.c_left_side.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.c_left_side)
        self.verticalLayout_3.setSpacing(16)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.c_first_name = QFrame(self.c_left_side)
        self.c_first_name.setObjectName(u"c_first_name")
        self.c_first_name.setFrameShape(QFrame.StyledPanel)
        self.c_first_name.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.c_first_name)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lb_first_name = QLabel(self.c_first_name)
        self.lb_first_name.setObjectName(u"lb_first_name")

        self.verticalLayout_5.addWidget(self.lb_first_name)

        self.i_first_name = LineEdit(self.c_first_name)
        self.i_first_name.setObjectName(u"i_first_name")

        self.verticalLayout_5.addWidget(self.i_first_name)


        self.verticalLayout_3.addWidget(self.c_first_name)

        self.c_birth_date = QFrame(self.c_left_side)
        self.c_birth_date.setObjectName(u"c_birth_date")
        self.c_birth_date.setFrameShape(QFrame.StyledPanel)
        self.c_birth_date.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.c_birth_date)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lb_birth_date = QLabel(self.c_birth_date)
        self.lb_birth_date.setObjectName(u"lb_birth_date")

        self.verticalLayout_4.addWidget(self.lb_birth_date)

        self.i_birth_date = QDateEdit(self.c_birth_date)
        self.i_birth_date.setObjectName(u"i_birth_date")

        self.verticalLayout_4.addWidget(self.i_birth_date)


        self.verticalLayout_3.addWidget(self.c_birth_date)


        self.horizontalLayout.addWidget(self.c_left_side)

        self.right_side_container = QFrame(self.c_inputs)
        self.right_side_container.setObjectName(u"right_side_container")
        self.right_side_container.setMinimumSize(QSize(250, 0))
        self.right_side_container.setMaximumSize(QSize(250, 300))
        self.right_side_container.setFrameShape(QFrame.StyledPanel)
        self.right_side_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.right_side_container)
        self.verticalLayout_6.setSpacing(16)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.c_last_name = QFrame(self.right_side_container)
        self.c_last_name.setObjectName(u"c_last_name")
        self.c_last_name.setFrameShape(QFrame.StyledPanel)
        self.c_last_name.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.c_last_name)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lb_last_name = QLabel(self.c_last_name)
        self.lb_last_name.setObjectName(u"lb_last_name")

        self.verticalLayout_7.addWidget(self.lb_last_name)

        self.i_last_name = LineEdit(self.c_last_name)
        self.i_last_name.setObjectName(u"i_last_name")

        self.verticalLayout_7.addWidget(self.i_last_name)


        self.verticalLayout_6.addWidget(self.c_last_name)

        self.c_gender = QFrame(self.right_side_container)
        self.c_gender.setObjectName(u"c_gender")
        self.c_gender.setFrameShape(QFrame.StyledPanel)
        self.c_gender.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.c_gender)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lb_gender = QLabel(self.c_gender)
        self.lb_gender.setObjectName(u"lb_gender")

        self.verticalLayout_8.addWidget(self.lb_gender)

        self.c_gender_rb = QFrame(self.c_gender)
        self.c_gender_rb.setObjectName(u"c_gender_rb")
        self.c_gender_rb.setFrameShape(QFrame.StyledPanel)
        self.c_gender_rb.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.c_gender_rb)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.i_gender_f = QRadioButton(self.c_gender_rb)
        self.i_gender_f.setObjectName(u"i_gender_f")

        self.horizontalLayout_2.addWidget(self.i_gender_f)

        self.i_gender_m = QRadioButton(self.c_gender_rb)
        self.i_gender_m.setObjectName(u"i_gender_m")

        self.horizontalLayout_2.addWidget(self.i_gender_m)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_8.addWidget(self.c_gender_rb)


        self.verticalLayout_6.addWidget(self.c_gender)


        self.horizontalLayout.addWidget(self.right_side_container)


        self.verticalLayout_2.addWidget(self.c_inputs)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.c_buttons = QFrame(self.c_center)
        self.c_buttons.setObjectName(u"c_buttons")
        self.c_buttons.setFrameShape(QFrame.StyledPanel)
        self.c_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.c_buttons)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.bt_cancel = Button(self.c_buttons)
        self.bt_cancel.setObjectName(u"bt_cancel")

        self.horizontalLayout_3.addWidget(self.bt_cancel)

        self.bt_add = Button(self.c_buttons)
        self.bt_add.setObjectName(u"bt_add")

        self.horizontalLayout_3.addWidget(self.bt_add)


        self.verticalLayout_2.addWidget(self.c_buttons, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.c_center, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.c_rb_views = QFrame(add_patient)
        self.c_rb_views.setObjectName(u"c_rb_views")
        self.c_rb_views.setFrameShape(QFrame.StyledPanel)
        self.c_rb_views.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.c_rb_views)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.i_add_patient_view = QRadioButton(self.c_rb_views)
        self.i_add_patient_view.setObjectName(u"i_add_patient_view")
        self.i_add_patient_view.setChecked(True)

        self.horizontalLayout_4.addWidget(self.i_add_patient_view)

        self.i_add_patient_p2_view = QRadioButton(self.c_rb_views)
        self.i_add_patient_p2_view.setObjectName(u"i_add_patient_p2_view")

        self.horizontalLayout_4.addWidget(self.i_add_patient_p2_view)


        self.verticalLayout.addWidget(self.c_rb_views, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(add_patient)

        QMetaObject.connectSlotsByName(add_patient)
    # setupUi

    def retranslateUi(self, add_patient):
        add_patient.setWindowTitle(QCoreApplication.translate("add_patient", u"Loggin", None))
        self.lb_title.setText(QCoreApplication.translate("add_patient", u"Add patient", None))
        self.lb_first_name.setText(QCoreApplication.translate("add_patient", u"First name", None))
        self.lb_birth_date.setText(QCoreApplication.translate("add_patient", u"Date of birth", None))
        self.i_birth_date.setDisplayFormat(QCoreApplication.translate("add_patient", u"d/M/yyyy", None))
        self.lb_last_name.setText(QCoreApplication.translate("add_patient", u"Last name", None))
        self.lb_gender.setText(QCoreApplication.translate("add_patient", u"Gender", None))
        self.i_gender_f.setText(QCoreApplication.translate("add_patient", u"Female", None))
        self.i_gender_m.setText(QCoreApplication.translate("add_patient", u"Male", None))
        self.bt_cancel.setText(QCoreApplication.translate("add_patient", u"Cancel", None))
        self.bt_add.setText(QCoreApplication.translate("add_patient", u"Next", None))
        self.i_add_patient_view.setText("")
        self.i_add_patient_p2_view.setText("")
    # retranslateUi

