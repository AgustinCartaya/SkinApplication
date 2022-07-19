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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

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
        self.center_container.setFrameShape(QFrame.StyledPanel)
        self.center_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.center_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lb_login = QLabel(self.center_container)
        self.lb_login.setObjectName(u"lb_login")

        self.verticalLayout_2.addWidget(self.lb_login, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.inputs_container = QFrame(self.center_container)
        self.inputs_container.setObjectName(u"inputs_container")
        self.inputs_container.setMinimumSize(QSize(300, 0))
        self.inputs_container.setMaximumSize(QSize(200, 300))
        self.inputs_container.setFrameShape(QFrame.StyledPanel)
        self.inputs_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.inputs_container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lb_email = QLabel(self.inputs_container)
        self.lb_email.setObjectName(u"lb_email")

        self.verticalLayout_3.addWidget(self.lb_email)

        self.i_name = QLineEdit(self.inputs_container)
        self.i_name.setObjectName(u"i_name")

        self.verticalLayout_3.addWidget(self.i_name)

        self.lb_password = QLabel(self.inputs_container)
        self.lb_password.setObjectName(u"lb_password")

        self.verticalLayout_3.addWidget(self.lb_password)

        self.i_password = QLineEdit(self.inputs_container)
        self.i_password.setObjectName(u"i_password")

        self.verticalLayout_3.addWidget(self.i_password)


        self.verticalLayout_2.addWidget(self.inputs_container)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.bt_login = QPushButton(self.center_container)
        self.bt_login.setObjectName(u"bt_login")

        self.verticalLayout_2.addWidget(self.bt_login, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.center_container, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Loggin", None))
        self.lb_login.setText(QCoreApplication.translate("login", u"Login", None))
        self.lb_email.setText(QCoreApplication.translate("login", u"Name", None))
        self.lb_password.setText(QCoreApplication.translate("login", u"Password", None))
        self.bt_login.setText(QCoreApplication.translate("login", u"Login", None))
    # retranslateUi

