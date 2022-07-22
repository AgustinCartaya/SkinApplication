# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_add_patient_p2.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from .promoted.button import Button
from .promoted.label import Label
from .promoted.navigator_button import NavigatorButton

class Ui_add_patient_p2(object):
    def setupUi(self, add_patient_p2):
        if not add_patient_p2.objectName():
            add_patient_p2.setObjectName(u"add_patient_p2")
        add_patient_p2.resize(800, 600)
        add_patient_p2.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(add_patient_p2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 7)
        self.frame_5 = QFrame(add_patient_p2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bt_back = NavigatorButton(self.frame_5)
        self.bt_back.setObjectName(u"bt_back")

        self.horizontalLayout.addWidget(self.bt_back)


        self.verticalLayout.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.c_center = QFrame(add_patient_p2)
        self.c_center.setObjectName(u"c_center")
        self.c_center.setMinimumSize(QSize(400, 0))
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
        self.verticalLayout_3 = QVBoxLayout(self.c_inputs)
        self.verticalLayout_3.setSpacing(16)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.c_hair_color = QFrame(self.c_inputs)
        self.c_hair_color.setObjectName(u"c_hair_color")
        self.c_hair_color.setFrameShape(QFrame.StyledPanel)
        self.c_hair_color.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.c_hair_color)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lb_hair_color = QLabel(self.c_hair_color)
        self.lb_hair_color.setObjectName(u"lb_hair_color")

        self.verticalLayout_5.addWidget(self.lb_hair_color)

        self.i_hair_color = QComboBox(self.c_hair_color)
        self.i_hair_color.setObjectName(u"i_hair_color")

        self.verticalLayout_5.addWidget(self.i_hair_color)


        self.verticalLayout_3.addWidget(self.c_hair_color)

        self.c_eye_color = QFrame(self.c_inputs)
        self.c_eye_color.setObjectName(u"c_eye_color")
        self.c_eye_color.setFrameShape(QFrame.StyledPanel)
        self.c_eye_color.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.c_eye_color)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lb_eye_color = QLabel(self.c_eye_color)
        self.lb_eye_color.setObjectName(u"lb_eye_color")

        self.verticalLayout_4.addWidget(self.lb_eye_color)

        self.i_eye_color = QComboBox(self.c_eye_color)
        self.i_eye_color.setObjectName(u"i_eye_color")

        self.verticalLayout_4.addWidget(self.i_eye_color)


        self.verticalLayout_3.addWidget(self.c_eye_color)


        self.verticalLayout_2.addWidget(self.c_inputs)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

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

        self.frame_3 = QFrame(add_patient_p2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.i_add_patient_view = QRadioButton(self.frame_3)
        self.i_add_patient_view.setObjectName(u"i_add_patient_view")

        self.horizontalLayout_4.addWidget(self.i_add_patient_view)

        self.i_add_patient_p2_view = QRadioButton(self.frame_3)
        self.i_add_patient_p2_view.setObjectName(u"i_add_patient_p2_view")
        self.i_add_patient_p2_view.setChecked(True)

        self.horizontalLayout_4.addWidget(self.i_add_patient_p2_view)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(add_patient_p2)

        QMetaObject.connectSlotsByName(add_patient_p2)
    # setupUi

    def retranslateUi(self, add_patient_p2):
        add_patient_p2.setWindowTitle(QCoreApplication.translate("add_patient_p2", u"Loggin", None))
        self.bt_back.setText(QCoreApplication.translate("add_patient_p2", u"Back", None))
        self.lb_title.setText(QCoreApplication.translate("add_patient_p2", u"Add patient", None))
        self.lb_hair_color.setText(QCoreApplication.translate("add_patient_p2", u"Hair color", None))
        self.lb_eye_color.setText(QCoreApplication.translate("add_patient_p2", u"Eye color", None))
        self.bt_cancel.setText(QCoreApplication.translate("add_patient_p2", u"Cancel", None))
        self.bt_add.setText(QCoreApplication.translate("add_patient_p2", u"Next", None))
        self.i_add_patient_view.setText("")
        self.i_add_patient_p2_view.setText("")
    # retranslateUi

