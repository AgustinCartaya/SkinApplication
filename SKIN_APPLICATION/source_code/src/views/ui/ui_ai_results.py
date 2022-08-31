# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_ai_results.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from .promoted.label import Label
from .promoted.navigator_button import NavigatorButton

class Ui_ai_results(object):
    def setupUi(self, ai_results):
        if not ai_results.objectName():
            ai_results.setObjectName(u"ai_results")
        ai_results.resize(1200, 800)
        ai_results.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(ai_results)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.ly_navigator = QHBoxLayout()
        self.ly_navigator.setSpacing(0)
        self.ly_navigator.setObjectName(u"ly_navigator")
        self.ly_navigator.setContentsMargins(-1, 0, 0, -1)
        self.bt_back = NavigatorButton(ai_results)
        self.bt_back.setObjectName(u"bt_back")

        self.ly_navigator.addWidget(self.bt_back, 0, Qt.AlignLeft)

        self.c_title = QFrame(ai_results)
        self.c_title.setObjectName(u"c_title")
        self.c_title.setFrameShape(QFrame.StyledPanel)
        self.c_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.c_title)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_title = Label(self.c_title)
        self.lb_title.setObjectName(u"lb_title")

        self.horizontalLayout.addWidget(self.lb_title)

        self.lb_ai_name = Label(self.c_title)
        self.lb_ai_name.setObjectName(u"lb_ai_name")

        self.horizontalLayout.addWidget(self.lb_ai_name)


        self.ly_navigator.addWidget(self.c_title)

        self.bt_relaunch = NavigatorButton(ai_results)
        self.bt_relaunch.setObjectName(u"bt_relaunch")

        self.ly_navigator.addWidget(self.bt_relaunch, 0, Qt.AlignRight)

        self.ly_navigator.setStretch(0, 1)
        self.ly_navigator.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.ly_navigator)

        self.ly_center = QHBoxLayout()
        self.ly_center.setObjectName(u"ly_center")
        self.ly_center.setContentsMargins(20, -1, 20, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ly_center.addItem(self.horizontalSpacer)

        self.ly_results = QVBoxLayout()
        self.ly_results.setObjectName(u"ly_results")
        self.ly_results.setContentsMargins(-1, 20, -1, -1)
        self.lb_results = Label(ai_results)
        self.lb_results.setObjectName(u"lb_results")

        self.ly_results.addWidget(self.lb_results, 0, Qt.AlignHCenter)

        self.sc_results = QScrollArea(ai_results)
        self.sc_results.setObjectName(u"sc_results")
        self.sc_results.setWidgetResizable(True)
        self.c_results = QWidget()
        self.c_results.setObjectName(u"c_results")
        self.c_results.setGeometry(QRect(0, 0, 488, 698))
        self.verticalLayout_3 = QVBoxLayout(self.c_results)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ly_results_content = QVBoxLayout()
        self.ly_results_content.setObjectName(u"ly_results_content")

        self.verticalLayout_3.addLayout(self.ly_results_content)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.sc_results.setWidget(self.c_results)

        self.ly_results.addWidget(self.sc_results)


        self.ly_center.addLayout(self.ly_results)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ly_center.addItem(self.horizontalSpacer_2)

        self.ly_center.setStretch(0, 2)
        self.ly_center.setStretch(1, 3)
        self.ly_center.setStretch(2, 2)

        self.verticalLayout_2.addLayout(self.ly_center)


        self.retranslateUi(ai_results)

        QMetaObject.connectSlotsByName(ai_results)
    # setupUi

    def retranslateUi(self, ai_results):
        ai_results.setWindowTitle(QCoreApplication.translate("ai_results", u"Loggin", None))
        self.bt_back.setText(QCoreApplication.translate("ai_results", u"Back", None))
        self.lb_title.setText(QCoreApplication.translate("ai_results", u"Results", None))
        self.lb_ai_name.setText(QCoreApplication.translate("ai_results", u"AI-01", None))
        self.bt_relaunch.setText(QCoreApplication.translate("ai_results", u"Re launch", None))
        self.lb_results.setText(QCoreApplication.translate("ai_results", u"Results", None))
    # retranslateUi

