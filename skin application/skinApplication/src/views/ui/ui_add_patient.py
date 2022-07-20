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
from .promoted.line_edit import LineEdit

class Ui_add_patient(object):
    def setupUi(self, add_patient):
        if not add_patient.objectName():
            add_patient.setObjectName(u"add_patient")
        add_patient.resize(800, 600)
        add_patient.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(add_patient)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 7)
        self.center_container = QFrame(add_patient)
        self.center_container.setObjectName(u"center_container")
        self.center_container.setFrameShape(QFrame.StyledPanel)
        self.center_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.center_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lb_title = QLabel(self.center_container)
        self.lb_title.setObjectName(u"lb_title")

        self.verticalLayout_2.addWidget(self.lb_title, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.inputs_container = QFrame(self.center_container)
        self.inputs_container.setObjectName(u"inputs_container")
        self.inputs_container.setFrameShape(QFrame.StyledPanel)
        self.inputs_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.inputs_container)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.left_side_container = QFrame(self.inputs_container)
        self.left_side_container.setObjectName(u"left_side_container")
        self.left_side_container.setMinimumSize(QSize(250, 0))
        self.left_side_container.setMaximumSize(QSize(250, 300))
        self.left_side_container.setFrameShape(QFrame.StyledPanel)
        self.left_side_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_side_container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lb_first_name = QLabel(self.left_side_container)
        self.lb_first_name.setObjectName(u"lb_first_name")

        self.verticalLayout_3.addWidget(self.lb_first_name)

        self.i_first_name = LineEdit(self.left_side_container)
        self.i_first_name.setObjectName(u"i_first_name")

        self.verticalLayout_3.addWidget(self.i_first_name)

        self.lb_birth_date = QLabel(self.left_side_container)
        self.lb_birth_date.setObjectName(u"lb_birth_date")

        self.verticalLayout_3.addWidget(self.lb_birth_date)

        self.i_birth_date = QDateEdit(self.left_side_container)
        self.i_birth_date.setObjectName(u"i_birth_date")

        self.verticalLayout_3.addWidget(self.i_birth_date)


        self.horizontalLayout.addWidget(self.left_side_container)

        self.right_side_container = QFrame(self.inputs_container)
        self.right_side_container.setObjectName(u"right_side_container")
        self.right_side_container.setMinimumSize(QSize(250, 0))
        self.right_side_container.setMaximumSize(QSize(250, 300))
        self.right_side_container.setFrameShape(QFrame.StyledPanel)
        self.right_side_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.right_side_container)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lb_last_name = QLabel(self.right_side_container)
        self.lb_last_name.setObjectName(u"lb_last_name")

        self.verticalLayout_6.addWidget(self.lb_last_name)

        self.i_last_name = LineEdit(self.right_side_container)
        self.i_last_name.setObjectName(u"i_last_name")

        self.verticalLayout_6.addWidget(self.i_last_name)

        self.lb_gender = QLabel(self.right_side_container)
        self.lb_gender.setObjectName(u"lb_gender")

        self.verticalLayout_6.addWidget(self.lb_gender)

        self.frame = QFrame(self.right_side_container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.i_gender_f = QRadioButton(self.frame)
        self.i_gender_f.setObjectName(u"i_gender_f")

        self.horizontalLayout_2.addWidget(self.i_gender_f)

        self.i_gender_m = QRadioButton(self.frame)
        self.i_gender_m.setObjectName(u"i_gender_m")

        self.horizontalLayout_2.addWidget(self.i_gender_m)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_6.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.right_side_container)


        self.verticalLayout_2.addWidget(self.inputs_container)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_2 = QFrame(self.center_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bt_cancel = Button(self.frame_2)
        self.bt_cancel.setObjectName(u"bt_cancel")

        self.horizontalLayout_3.addWidget(self.bt_cancel)

        self.bt_add = Button(self.frame_2)
        self.bt_add.setObjectName(u"bt_add")

        self.horizontalLayout_3.addWidget(self.bt_add)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.center_container, 0, Qt.AlignHCenter|Qt.AlignVCenter)


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
        self.bt_add.setText(QCoreApplication.translate("add_patient", u"Add", None))
    # retranslateUi

