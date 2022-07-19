# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_account.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(600, 400)
        Widget.setStyleSheet(u"background-color: rgb(170, 0, 0);")
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignTop)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setEnabled(True)
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget_8 = QWidget(self.widget_5)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_4 = QVBoxLayout(self.widget_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_7 = QWidget(self.widget_8)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_6 = QVBoxLayout(self.widget_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.widget_7)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.i_first_name = QLineEdit(self.widget_7)
        self.i_first_name.setObjectName(u"i_first_name")

        self.verticalLayout_6.addWidget(self.i_first_name)


        self.verticalLayout_4.addWidget(self.widget_7)

        self.widget_10 = QWidget(self.widget_8)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_5 = QVBoxLayout(self.widget_10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.widget_10)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.i_password = QLineEdit(self.widget_10)
        self.i_password.setObjectName(u"i_password")

        self.verticalLayout_5.addWidget(self.i_password)


        self.verticalLayout_4.addWidget(self.widget_10)


        self.horizontalLayout_5.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_5)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_7 = QVBoxLayout(self.widget_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_11 = QWidget(self.widget_9)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_8 = QVBoxLayout(self.widget_11)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(self.widget_11)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_8.addWidget(self.label_6)

        self.i_last_name = QLineEdit(self.widget_11)
        self.i_last_name.setObjectName(u"i_last_name")

        self.verticalLayout_8.addWidget(self.i_last_name)


        self.verticalLayout_7.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget_9)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_9 = QVBoxLayout(self.widget_12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_7 = QLabel(self.widget_12)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_9.addWidget(self.label_7)

        self.i_repeat_password = QLineEdit(self.widget_12)
        self.i_repeat_password.setObjectName(u"i_repeat_password")

        self.verticalLayout_9.addWidget(self.i_repeat_password)


        self.verticalLayout_7.addWidget(self.widget_12)


        self.horizontalLayout_5.addWidget(self.widget_9)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_3 = QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbEmail = QLabel(self.widget_6)
        self.lbEmail.setObjectName(u"lbEmail")

        self.verticalLayout_3.addWidget(self.lbEmail)

        self.i_email = QLineEdit(self.widget_6)
        self.i_email.setObjectName(u"i_email")

        self.verticalLayout_3.addWidget(self.i_email)


        self.verticalLayout_2.addWidget(self.widget_6)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bt_create = QPushButton(self.widget_4)
        self.bt_create.setObjectName(u"bt_create")

        self.horizontalLayout_3.addWidget(self.bt_create)


        self.verticalLayout.addWidget(self.widget_4, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Create account", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"First name", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Password", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Last name", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Pasword", None))
        self.lbEmail.setText(QCoreApplication.translate("Widget", u"Email", None))
        self.bt_create.setText(QCoreApplication.translate("Widget", u"Create", None))
    # retranslateUi

