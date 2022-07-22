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
        self.center_container = QFrame(create_account)
        self.center_container.setObjectName(u"center_container")
        self.center_container.setFrameShape(QFrame.StyledPanel)
        self.center_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.center_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, -1)
        self.lb_title = Label(self.center_container)
        self.lb_title.setObjectName(u"lb_title")

        self.verticalLayout_2.addWidget(self.lb_title, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.frame_2 = QFrame(self.center_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.inputs_container = QFrame(self.frame_2)
        self.inputs_container.setObjectName(u"inputs_container")
        self.inputs_container.setFrameShape(QFrame.StyledPanel)
        self.inputs_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.inputs_container)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_side_container = QFrame(self.inputs_container)
        self.left_side_container.setObjectName(u"left_side_container")
        self.left_side_container.setMinimumSize(QSize(250, 0))
        self.left_side_container.setMaximumSize(QSize(250, 300))
        self.left_side_container.setFrameShape(QFrame.StyledPanel)
        self.left_side_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_side_container)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.lb_first_name = QLabel(self.left_side_container)
        self.lb_first_name.setObjectName(u"lb_first_name")

        self.verticalLayout_3.addWidget(self.lb_first_name)

        self.i_first_name = LineEdit(self.left_side_container)
        self.i_first_name.setObjectName(u"i_first_name")

        self.verticalLayout_3.addWidget(self.i_first_name)

        self.lb_password = QLabel(self.left_side_container)
        self.lb_password.setObjectName(u"lb_password")

        self.verticalLayout_3.addWidget(self.lb_password)

        self.i_password = LineEdit(self.left_side_container)
        self.i_password.setObjectName(u"i_password")

        self.verticalLayout_3.addWidget(self.i_password)


        self.horizontalLayout.addWidget(self.left_side_container)

        self.right_side_container = QFrame(self.inputs_container)
        self.right_side_container.setObjectName(u"right_side_container")
        self.right_side_container.setMinimumSize(QSize(250, 0))
        self.right_side_container.setMaximumSize(QSize(250, 300))
        self.right_side_container.setFrameShape(QFrame.StyledPanel)
        self.right_side_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.right_side_container)
        self.verticalLayout_6.setSpacing(9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.lb_last_name = QLabel(self.right_side_container)
        self.lb_last_name.setObjectName(u"lb_last_name")

        self.verticalLayout_6.addWidget(self.lb_last_name)

        self.i_last_name = LineEdit(self.right_side_container)
        self.i_last_name.setObjectName(u"i_last_name")

        self.verticalLayout_6.addWidget(self.i_last_name)

        self.lb_repeat_password = QLabel(self.right_side_container)
        self.lb_repeat_password.setObjectName(u"lb_repeat_password")

        self.verticalLayout_6.addWidget(self.lb_repeat_password)

        self.i_repeat_password = LineEdit(self.right_side_container)
        self.i_repeat_password.setObjectName(u"i_repeat_password")

        self.verticalLayout_6.addWidget(self.i_repeat_password)


        self.horizontalLayout.addWidget(self.right_side_container)


        self.verticalLayout_5.addWidget(self.inputs_container)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lb_email = QLabel(self.frame)
        self.lb_email.setObjectName(u"lb_email")

        self.verticalLayout_4.addWidget(self.lb_email)

        self.i_email = LineEdit(self.frame)
        self.i_email.setObjectName(u"i_email")

        self.verticalLayout_4.addWidget(self.i_email)


        self.verticalLayout_5.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.bt_create = Button(self.center_container)
        self.bt_create.setObjectName(u"bt_create")

        self.verticalLayout_2.addWidget(self.bt_create, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.center_container, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(create_account)

        QMetaObject.connectSlotsByName(create_account)
    # setupUi

    def retranslateUi(self, create_account):
        create_account.setWindowTitle(QCoreApplication.translate("create_account", u"Loggin", None))
        self.lb_title.setText(QCoreApplication.translate("create_account", u"Create account", None))
        self.lb_first_name.setText(QCoreApplication.translate("create_account", u"First name", None))
        self.lb_password.setText(QCoreApplication.translate("create_account", u"Password", None))
        self.lb_last_name.setText(QCoreApplication.translate("create_account", u"Last name", None))
        self.lb_repeat_password.setText(QCoreApplication.translate("create_account", u"Repeat password", None))
        self.lb_email.setText(QCoreApplication.translate("create_account", u"E-mail", None))
        self.bt_create.setText(QCoreApplication.translate("create_account", u"Create", None))
    # retranslateUi

