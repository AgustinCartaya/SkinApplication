# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
        Widget.resize(350, 400)
        Widget.setStyleSheet(u"background-color: rgb(0,250, 0);")
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
        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_3 = QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbEmail = QLabel(self.widget_6)
        self.lbEmail.setObjectName(u"lbEmail")

        self.verticalLayout_3.addWidget(self.lbEmail)

        self.i_name = QLineEdit(self.widget_6)
        self.i_name.setObjectName(u"i_name")

        self.verticalLayout_3.addWidget(self.i_name)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.widget_61 = QWidget(self.widget_3)
        self.widget_61.setObjectName(u"widget_61")
        self.verticalLayout_31 = QVBoxLayout(self.widget_61)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.lbEmail1 = QLabel(self.widget_61)
        self.lbEmail1.setObjectName(u"lbEmail1")

        self.verticalLayout_31.addWidget(self.lbEmail1)

        self.i_password = QLineEdit(self.widget_61)
        self.i_password.setObjectName(u"i_password")

        self.verticalLayout_31.addWidget(self.i_password)


        self.verticalLayout_2.addWidget(self.widget_61)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bt_login = QPushButton(self.widget_4)
        self.bt_login.setObjectName(u"bt_login")

        self.horizontalLayout_3.addWidget(self.bt_login)


        self.verticalLayout.addWidget(self.widget_4, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Login", None))
        self.lbEmail.setText(QCoreApplication.translate("Widget", u"Name", None))
        self.lbEmail1.setText(QCoreApplication.translate("Widget", u"Password", None))
        self.bt_login.setText(QCoreApplication.translate("Widget", u"Login", None))
    # retranslateUi
