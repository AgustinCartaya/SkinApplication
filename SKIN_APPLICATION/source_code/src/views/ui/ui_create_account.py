# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_create_account.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from .promoted.button import Button
from .promoted.label import Label
from .promoted.line_edit import LineEdit

class Ui_create_account(object):
    def setupUi(self, create_account):
        if not create_account.objectName():
            create_account.setObjectName(u"create_account")
        create_account.resize(800, 600)
        create_account.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(create_account)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.c_center = QFrame(create_account)
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

        self.ly_inputs = QVBoxLayout()
        self.ly_inputs.setSpacing(16)
        self.ly_inputs.setObjectName(u"ly_inputs")
        self.ly_upper = QVBoxLayout()
        self.ly_upper.setSpacing(16)
        self.ly_upper.setObjectName(u"ly_upper")
        self.ly_up = QHBoxLayout()
        self.ly_up.setSpacing(16)
        self.ly_up.setObjectName(u"ly_up")
        self.ly_first_name = QVBoxLayout()
        self.ly_first_name.setSpacing(2)
        self.ly_first_name.setObjectName(u"ly_first_name")
        self.ly_first_name.setContentsMargins(-1, 0, -1, -1)
        self.lb_first_name = QLabel(self.c_center)
        self.lb_first_name.setObjectName(u"lb_first_name")

        self.ly_first_name.addWidget(self.lb_first_name)

        self.i_first_name = LineEdit(self.c_center)
        self.i_first_name.setObjectName(u"i_first_name")

        self.ly_first_name.addWidget(self.i_first_name)


        self.ly_up.addLayout(self.ly_first_name)

        self.ly_last_name = QVBoxLayout()
        self.ly_last_name.setSpacing(2)
        self.ly_last_name.setObjectName(u"ly_last_name")
        self.ly_last_name.setContentsMargins(-1, 0, -1, -1)
        self.lb_last_name = QLabel(self.c_center)
        self.lb_last_name.setObjectName(u"lb_last_name")

        self.ly_last_name.addWidget(self.lb_last_name)

        self.i_last_name = LineEdit(self.c_center)
        self.i_last_name.setObjectName(u"i_last_name")

        self.ly_last_name.addWidget(self.i_last_name)


        self.ly_up.addLayout(self.ly_last_name)


        self.ly_upper.addLayout(self.ly_up)

        self.ly_down = QHBoxLayout()
        self.ly_down.setSpacing(16)
        self.ly_down.setObjectName(u"ly_down")
        self.ly_password = QVBoxLayout()
        self.ly_password.setSpacing(2)
        self.ly_password.setObjectName(u"ly_password")
        self.ly_password.setContentsMargins(-1, 0, -1, -1)
        self.lb_password = QLabel(self.c_center)
        self.lb_password.setObjectName(u"lb_password")

        self.ly_password.addWidget(self.lb_password)

        self.i_password = LineEdit(self.c_center)
        self.i_password.setObjectName(u"i_password")

        self.ly_password.addWidget(self.i_password)


        self.ly_down.addLayout(self.ly_password)

        self.ly_repeat_password = QVBoxLayout()
        self.ly_repeat_password.setSpacing(2)
        self.ly_repeat_password.setObjectName(u"ly_repeat_password")
        self.ly_repeat_password.setContentsMargins(-1, 0, -1, -1)
        self.lb_repeat_password = QLabel(self.c_center)
        self.lb_repeat_password.setObjectName(u"lb_repeat_password")

        self.ly_repeat_password.addWidget(self.lb_repeat_password)

        self.i_repeat_password = LineEdit(self.c_center)
        self.i_repeat_password.setObjectName(u"i_repeat_password")

        self.ly_repeat_password.addWidget(self.i_repeat_password)


        self.ly_down.addLayout(self.ly_repeat_password)


        self.ly_upper.addLayout(self.ly_down)


        self.ly_inputs.addLayout(self.ly_upper)

        self.ly_email = QVBoxLayout()
        self.ly_email.setSpacing(2)
        self.ly_email.setObjectName(u"ly_email")
        self.ly_email.setContentsMargins(0, 0, -1, -1)
        self.lb_email = QLabel(self.c_center)
        self.lb_email.setObjectName(u"lb_email")

        self.ly_email.addWidget(self.lb_email)

        self.i_email = LineEdit(self.c_center)
        self.i_email.setObjectName(u"i_email")

        self.ly_email.addWidget(self.i_email)


        self.ly_inputs.addLayout(self.ly_email)

        self.bt_login = Button(self.c_center)
        self.bt_login.setObjectName(u"bt_login")

        self.ly_inputs.addWidget(self.bt_login, 0, Qt.AlignLeft)


        self.verticalLayout_2.addLayout(self.ly_inputs)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.bt_create = Button(self.c_center)
        self.bt_create.setObjectName(u"bt_create")

        self.verticalLayout_2.addWidget(self.bt_create, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.c_center, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(create_account)

        QMetaObject.connectSlotsByName(create_account)
    # setupUi

    def retranslateUi(self, create_account):
        create_account.setWindowTitle(QCoreApplication.translate("create_account", u"Loggin", None))
        self.lb_title.setText(QCoreApplication.translate("create_account", u"Create account", None))
        self.lb_first_name.setText(QCoreApplication.translate("create_account", u"First name", None))
        self.lb_last_name.setText(QCoreApplication.translate("create_account", u"Last name", None))
        self.lb_password.setText(QCoreApplication.translate("create_account", u"Password", None))
        self.lb_repeat_password.setText(QCoreApplication.translate("create_account", u"Repeat password", None))
        self.lb_email.setText(QCoreApplication.translate("create_account", u"E-mail", None))
        self.bt_login.setText(QCoreApplication.translate("create_account", u"Go to login", None))
        self.bt_create.setText(QCoreApplication.translate("create_account", u"Create", None))
    # retranslateUi

