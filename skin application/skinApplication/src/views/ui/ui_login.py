# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_login.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from .promoted.button import Button
from .promoted.label import Label
from .promoted.line_edit import LineEdit

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(800, 600)
        login.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(login)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.center_container = QFrame(login)
        self.center_container.setObjectName(u"center_container")
        self.center_container.setMinimumSize(QSize(300, 0))
        self.center_container.setFrameShape(QFrame.StyledPanel)
        self.center_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.center_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lb_title = Label(self.center_container)
        self.lb_title.setObjectName(u"lb_title")

        self.verticalLayout_2.addWidget(self.lb_title, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.ly_inputs = QVBoxLayout()
        self.ly_inputs.setSpacing(16)
        self.ly_inputs.setObjectName(u"ly_inputs")
        self.ly_inputs.setContentsMargins(-1, 0, -1, -1)
        self.ly_name = QVBoxLayout()
        self.ly_name.setSpacing(2)
        self.ly_name.setObjectName(u"ly_name")
        self.ly_name.setContentsMargins(-1, 0, -1, -1)
        self.lb_email = QLabel(self.center_container)
        self.lb_email.setObjectName(u"lb_email")

        self.ly_name.addWidget(self.lb_email)

        self.i_name = QComboBox(self.center_container)
        self.i_name.setObjectName(u"i_name")

        self.ly_name.addWidget(self.i_name)


        self.ly_inputs.addLayout(self.ly_name)

        self.ly_password = QVBoxLayout()
        self.ly_password.setSpacing(2)
        self.ly_password.setObjectName(u"ly_password")
        self.ly_password.setContentsMargins(-1, 0, -1, -1)
        self.lb_password = QLabel(self.center_container)
        self.lb_password.setObjectName(u"lb_password")

        self.ly_password.addWidget(self.lb_password)

        self.i_password = LineEdit(self.center_container)
        self.i_password.setObjectName(u"i_password")

        self.ly_password.addWidget(self.i_password)


        self.ly_inputs.addLayout(self.ly_password)


        self.verticalLayout_2.addLayout(self.ly_inputs)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.bt_login = Button(self.center_container)
        self.bt_login.setObjectName(u"bt_login")

        self.verticalLayout_2.addWidget(self.bt_login, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.center_container, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Loggin", None))
        self.lb_title.setText(QCoreApplication.translate("login", u"Login", None))
        self.lb_email.setText(QCoreApplication.translate("login", u"Name", None))
        self.lb_password.setText(QCoreApplication.translate("login", u"Password", None))
        self.bt_login.setText(QCoreApplication.translate("login", u"Login", None))
    # retranslateUi

