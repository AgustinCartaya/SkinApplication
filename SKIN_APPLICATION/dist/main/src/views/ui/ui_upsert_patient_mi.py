# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_upsert_patient_mi.ui'
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
from .promoted.variable_inputs_container import VariableInputsContainer

class Ui_upsert_patient_mi(object):
    def setupUi(self, upsert_patient_mi):
        if not upsert_patient_mi.objectName():
            upsert_patient_mi.setObjectName(u"upsert_patient_mi")
        upsert_patient_mi.setEnabled(True)
        upsert_patient_mi.resize(800, 600)
        upsert_patient_mi.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(upsert_patient_mi)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ly_navigator = QHBoxLayout()
        self.ly_navigator.setSpacing(0)
        self.ly_navigator.setObjectName(u"ly_navigator")
        self.ly_navigator.setContentsMargins(-1, 0, -1, -1)
        self.bt_cancel = NavigatorButton(upsert_patient_mi)
        self.bt_cancel.setObjectName(u"bt_cancel")

        self.ly_navigator.addWidget(self.bt_cancel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ly_navigator.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.ly_navigator)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.c_center = QFrame(upsert_patient_mi)
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
        self.c_medical_information = QWidget()
        self.c_medical_information.setObjectName(u"c_medical_information")
        self.c_medical_information.setGeometry(QRect(0, 0, 496, 334))
        self.verticalLayout_3 = QVBoxLayout(self.c_medical_information)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ly_medical_information = QVBoxLayout()
        self.ly_medical_information.setSpacing(30)
        self.ly_medical_information.setObjectName(u"ly_medical_information")
        self.c_mi = VariableInputsContainer(self.c_medical_information)
        self.c_mi.setObjectName(u"c_mi")
        self.c_mi.setFrameShape(QFrame.StyledPanel)
        self.c_mi.setFrameShadow(QFrame.Raised)

        self.ly_medical_information.addWidget(self.c_mi)

        self.bt_create_new_mi = Button(self.c_medical_information)
        self.bt_create_new_mi.setObjectName(u"bt_create_new_mi")

        self.ly_medical_information.addWidget(self.bt_create_new_mi, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.ly_medical_information)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.scrollArea.setWidget(self.c_medical_information)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.bt_back = Button(self.c_center)
        self.bt_back.setObjectName(u"bt_back")

        self.horizontalLayout_2.addWidget(self.bt_back)

        self.bt_next = Button(self.c_center)
        self.bt_next.setObjectName(u"bt_next")

        self.horizontalLayout_2.addWidget(self.bt_next)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.c_buttons = QFrame(self.c_center)
        self.c_buttons.setObjectName(u"c_buttons")
        self.c_buttons.setFrameShape(QFrame.StyledPanel)
        self.c_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.c_buttons)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.c_buttons, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.c_center, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.c_rb_views = QFrame(upsert_patient_mi)
        self.c_rb_views.setObjectName(u"c_rb_views")
        self.c_rb_views.setFrameShape(QFrame.StyledPanel)
        self.c_rb_views.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.c_rb_views)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 16)
        self.i_upsert_patient_view = QRadioButton(self.c_rb_views)
        self.i_upsert_patient_view.setObjectName(u"i_upsert_patient_view")

        self.horizontalLayout_4.addWidget(self.i_upsert_patient_view)

        self.i_upsert_patient_mi_view = QRadioButton(self.c_rb_views)
        self.i_upsert_patient_mi_view.setObjectName(u"i_upsert_patient_mi_view")
        self.i_upsert_patient_mi_view.setChecked(True)

        self.horizontalLayout_4.addWidget(self.i_upsert_patient_mi_view)

        self.i_upsert_patient_preview_view = QRadioButton(self.c_rb_views)
        self.i_upsert_patient_preview_view.setObjectName(u"i_upsert_patient_preview_view")

        self.horizontalLayout_4.addWidget(self.i_upsert_patient_preview_view)


        self.verticalLayout.addWidget(self.c_rb_views, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(upsert_patient_mi)

        QMetaObject.connectSlotsByName(upsert_patient_mi)
    # setupUi

    def retranslateUi(self, upsert_patient_mi):
        upsert_patient_mi.setWindowTitle(QCoreApplication.translate("upsert_patient_mi", u"Loggin", None))
        self.bt_cancel.setText(QCoreApplication.translate("upsert_patient_mi", u"Cancel", None))
        self.lb_title.setText(QCoreApplication.translate("upsert_patient_mi", u"Medical information", None))
        self.bt_create_new_mi.setText(QCoreApplication.translate("upsert_patient_mi", u"Create new medical information type", None))
        self.bt_back.setText(QCoreApplication.translate("upsert_patient_mi", u"Back", None))
        self.bt_next.setText(QCoreApplication.translate("upsert_patient_mi", u"Next", None))
        self.i_upsert_patient_view.setText("")
        self.i_upsert_patient_mi_view.setText("")
        self.i_upsert_patient_preview_view.setText("")
    # retranslateUi

