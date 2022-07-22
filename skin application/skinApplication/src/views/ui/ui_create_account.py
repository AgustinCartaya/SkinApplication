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
        self.verticalLayout_5 = QVBoxLayout(self.c_inputs)
        self.verticalLayout_5.setSpacing(16)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.c_inputs)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(16)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_side_container = QFrame(self.frame_2)
        self.left_side_container.setObjectName(u"left_side_container")
        self.left_side_container.setMinimumSize(QSize(250, 0))
        self.left_side_container.setMaximumSize(QSize(250, 300))
        self.left_side_container.setFrameShape(QFrame.StyledPanel)
        self.left_side_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_side_container)
        self.verticalLayout_3.setSpacing(16)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.c_first_name = QFrame(self.left_side_container)
        self.c_first_name.setObjectName(u"c_first_name")
        self.c_first_name.setFrameShape(QFrame.StyledPanel)
        self.c_first_name.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.c_first_name)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lb_first_name = QLabel(self.c_first_name)
        self.lb_first_name.setObjectName(u"lb_first_name")

        self.verticalLayout_8.addWidget(self.lb_first_name)

        self.i_first_name = LineEdit(self.c_first_name)
        self.i_first_name.setObjectName(u"i_first_name")

        self.verticalLayout_8.addWidget(self.i_first_name)


        self.verticalLayout_3.addWidget(self.c_first_name)

        self.c_password = QFrame(self.left_side_container)
        self.c_password.setObjectName(u"c_password")
        self.c_password.setFrameShape(QFrame.StyledPanel)
        self.c_password.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.c_password)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lb_password = QLabel(self.c_password)
        self.lb_password.setObjectName(u"lb_password")

        self.verticalLayout_7.addWidget(self.lb_password)

        self.i_password = LineEdit(self.c_password)
        self.i_password.setObjectName(u"i_password")

        self.verticalLayout_7.addWidget(self.i_password)


        self.verticalLayout_3.addWidget(self.c_password)


        self.horizontalLayout.addWidget(self.left_side_container)

        self.right_side_container = QFrame(self.frame_2)
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
        self.verticalLayout_9 = QVBoxLayout(self.c_last_name)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lb_last_name = QLabel(self.c_last_name)
        self.lb_last_name.setObjectName(u"lb_last_name")

        self.verticalLayout_9.addWidget(self.lb_last_name)

        self.i_last_name = LineEdit(self.c_last_name)
        self.i_last_name.setObjectName(u"i_last_name")

        self.verticalLayout_9.addWidget(self.i_last_name)


        self.verticalLayout_6.addWidget(self.c_last_name)

        self.c_repeat_password = QFrame(self.right_side_container)
        self.c_repeat_password.setObjectName(u"c_repeat_password")
        self.c_repeat_password.setFrameShape(QFrame.StyledPanel)
        self.c_repeat_password.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.c_repeat_password)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lb_repeat_password = QLabel(self.c_repeat_password)
        self.lb_repeat_password.setObjectName(u"lb_repeat_password")

        self.verticalLayout_10.addWidget(self.lb_repeat_password)

        self.i_repeat_password = LineEdit(self.c_repeat_password)
        self.i_repeat_password.setObjectName(u"i_repeat_password")

        self.verticalLayout_10.addWidget(self.i_repeat_password)


        self.verticalLayout_6.addWidget(self.c_repeat_password)


        self.horizontalLayout.addWidget(self.right_side_container)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.c_email = QFrame(self.c_inputs)
        self.c_email.setObjectName(u"c_email")
        self.c_email.setFrameShape(QFrame.StyledPanel)
        self.c_email.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.c_email)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lb_email = QLabel(self.c_email)
        self.lb_email.setObjectName(u"lb_email")

        self.verticalLayout_4.addWidget(self.lb_email)

        self.i_email = LineEdit(self.c_email)
        self.i_email.setObjectName(u"i_email")

        self.verticalLayout_4.addWidget(self.i_email)


        self.verticalLayout_5.addWidget(self.c_email)


        self.verticalLayout_2.addWidget(self.c_inputs)

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
        self.lb_password.setText(QCoreApplication.translate("create_account", u"Password", None))
        self.lb_last_name.setText(QCoreApplication.translate("create_account", u"Last name", None))
        self.lb_repeat_password.setText(QCoreApplication.translate("create_account", u"Repeat password", None))
        self.lb_email.setText(QCoreApplication.translate("create_account", u"E-mail", None))
        self.bt_create.setText(QCoreApplication.translate("create_account", u"Create", None))
    # retranslateUi

