# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_ai_launcher.ui'
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
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from .promoted.button import Button
from .promoted.label import Label
from .promoted.navigator_button import NavigatorButton

class Ui_ai_launcher(object):
    def setupUi(self, ai_launcher):
        if not ai_launcher.objectName():
            ai_launcher.setObjectName(u"ai_launcher")
        ai_launcher.resize(1200, 800)
        ai_launcher.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(ai_launcher)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 20)
        self.ly_navigator = QHBoxLayout()
        self.ly_navigator.setSpacing(0)
        self.ly_navigator.setObjectName(u"ly_navigator")
        self.ly_navigator.setContentsMargins(-1, 0, 0, -1)
        self.bt_back = NavigatorButton(ai_launcher)
        self.bt_back.setObjectName(u"bt_back")

        self.ly_navigator.addWidget(self.bt_back)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ly_navigator.addItem(self.horizontalSpacer)

        self.lb_title = Label(ai_launcher)
        self.lb_title.setObjectName(u"lb_title")

        self.ly_navigator.addWidget(self.lb_title)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ly_navigator.addItem(self.horizontalSpacer_2)

        self.bt_learn_more = NavigatorButton(ai_launcher)
        self.bt_learn_more.setObjectName(u"bt_learn_more")

        self.ly_navigator.addWidget(self.bt_learn_more)


        self.verticalLayout_2.addLayout(self.ly_navigator)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 40, -1, 10)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(20)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label = Label(ai_launcher)
        self.label.setObjectName(u"label")

        self.verticalLayout_13.addWidget(self.label, 0, Qt.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.frame_2 = QFrame(ai_launcher)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = Label(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 402, 237))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(12)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_5 = QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(12)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton = Button(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(28, 28))

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.label_17 = Label(self.frame_5)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_5.addWidget(self.label_17)

        self.label_18 = Label(self.frame_5)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_5.addWidget(self.label_18)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_11.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(12)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = Button(self.frame_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(28, 28))

        self.horizontalLayout_6.addWidget(self.pushButton_2)

        self.label_19 = Label(self.frame_6)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_6.addWidget(self.label_19)

        self.label_20 = Label(self.frame_6)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_6.addWidget(self.label_20)

        self.horizontalSpacer_4 = QSpacerItem(373, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_11.addWidget(self.frame_6)


        self.verticalLayout_12.addLayout(self.verticalLayout_11)

        self.verticalSpacer_2 = QSpacerItem(20, 147, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scrollArea)


        self.horizontalLayout.addWidget(self.frame_2)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.frame = QFrame(ai_launcher)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.scrollArea_2 = QScrollArea(self.frame)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 402, 237))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_8 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setSpacing(12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = Button(self.frame_8)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(28, 28))

        self.horizontalLayout_8.addWidget(self.pushButton_3)

        self.label_21 = Label(self.frame_8)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_8.addWidget(self.label_21)

        self.label_22 = Label(self.frame_8)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_8.addWidget(self.label_22)

        self.horizontalSpacer_10 = QSpacerItem(228, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)


        self.verticalLayout_10.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setSpacing(12)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = Button(self.frame_9)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(28, 28))

        self.horizontalLayout_9.addWidget(self.pushButton_4)

        self.label_23 = Label(self.frame_9)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_9.addWidget(self.label_23)

        self.label_24 = Label(self.frame_9)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_9.addWidget(self.label_24)

        self.horizontalSpacer_11 = QSpacerItem(186, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)


        self.verticalLayout_10.addWidget(self.frame_9)


        self.verticalLayout_14.addLayout(self.verticalLayout_10)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_3)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_5.addWidget(self.scrollArea_2)


        self.horizontalLayout.addWidget(self.frame)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 6)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 6)
        self.horizontalLayout.setStretch(4, 2)

        self.verticalLayout_13.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.verticalLayout_13)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = Label(ai_launcher)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = Label(ai_launcher)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.label_6 = Label(ai_launcher)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.label_5 = Label(ai_launcher)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.label_8 = Label(ai_launcher)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_2.addWidget(self.label_8, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.frame_7 = QFrame(ai_launcher)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.frame_7)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 867, 209))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, 0, 0)
        self.frame_3 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 30))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_12 = Label(self.frame_3)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_3.addWidget(self.label_12)

        self.label_11 = Label(self.frame_3)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_3.addWidget(self.label_11, 0, Qt.AlignHCenter)

        self.label_9 = Label(self.frame_3)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_3.addWidget(self.label_9, 0, Qt.AlignHCenter)

        self.label_10 = Label(self.frame_3)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_3.addWidget(self.label_10, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 30))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_4.addWidget(self.label_13)

        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_4.addWidget(self.label_14, 0, Qt.AlignHCenter)

        self.label_15 = QLabel(self.frame_4)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_4.addWidget(self.label_15, 0, Qt.AlignHCenter)

        self.label_16 = QLabel(self.frame_4)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_4.addWidget(self.label_16, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.frame_4)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_9.addWidget(self.scrollArea_3)


        self.verticalLayout_3.addWidget(self.frame_7)


        self.horizontalLayout_7.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 6)
        self.horizontalLayout_7.setStretch(2, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_7)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.bt_launch = Button(ai_launcher)
        self.bt_launch.setObjectName(u"bt_launch")
        self.bt_launch.setMinimumSize(QSize(100, 0))

        self.verticalLayout.addWidget(self.bt_launch, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(ai_launcher)

        QMetaObject.connectSlotsByName(ai_launcher)
    # setupUi

    def retranslateUi(self, ai_launcher):
        ai_launcher.setWindowTitle(QCoreApplication.translate("ai_launcher", u"Loggin", None))
        self.bt_back.setText(QCoreApplication.translate("ai_launcher", u"Back", None))
        self.lb_title.setText(QCoreApplication.translate("ai_launcher", u"Ai launcher", None))
        self.bt_learn_more.setText(QCoreApplication.translate("ai_launcher", u"Learn more", None))
        self.label.setText(QCoreApplication.translate("ai_launcher", u"Required information", None))
        self.label_3.setText(QCoreApplication.translate("ai_launcher", u"Patient", None))
        self.pushButton.setText(QCoreApplication.translate("ai_launcher", u"M", None))
        self.label_17.setText(QCoreApplication.translate("ai_launcher", u"Eye color :", None))
        self.label_18.setText(QCoreApplication.translate("ai_launcher", u"Black", None))
        self.pushButton_2.setText(QCoreApplication.translate("ai_launcher", u"M", None))
        self.label_19.setText(QCoreApplication.translate("ai_launcher", u"Hair color :", None))
        self.label_20.setText(QCoreApplication.translate("ai_launcher", u"Withe", None))
        self.label_4.setText(QCoreApplication.translate("ai_launcher", u"Skin lesion", None))
        self.pushButton_3.setText(QCoreApplication.translate("ai_launcher", u"M", None))
        self.label_21.setText(QCoreApplication.translate("ai_launcher", u"Diameter :", None))
        self.label_22.setText(QCoreApplication.translate("ai_launcher", u"2 mm", None))
        self.pushButton_4.setText(QCoreApplication.translate("ai_launcher", u"M", None))
        self.label_23.setText(QCoreApplication.translate("ai_launcher", u"Apparition Date :", None))
        self.label_24.setText(QCoreApplication.translate("ai_launcher", u"1 Week", None))
        self.label_2.setText(QCoreApplication.translate("ai_launcher", u"Required images", None))
        self.label_7.setText(QCoreApplication.translate("ai_launcher", u"Name image", None))
        self.label_6.setText(QCoreApplication.translate("ai_launcher", u"Min required", None))
        self.label_5.setText(QCoreApplication.translate("ai_launcher", u"Max", None))
        self.label_8.setText(QCoreApplication.translate("ai_launcher", u"Selected", None))
        self.label_12.setText(QCoreApplication.translate("ai_launcher", u"Dermatoscopy", None))
        self.label_11.setText(QCoreApplication.translate("ai_launcher", u"2", None))
        self.label_9.setText(QCoreApplication.translate("ai_launcher", u"4", None))
        self.label_10.setText(QCoreApplication.translate("ai_launcher", u"1", None))
        self.label_13.setText(QCoreApplication.translate("ai_launcher", u"Microscopy", None))
        self.label_14.setText(QCoreApplication.translate("ai_launcher", u"5", None))
        self.label_15.setText(QCoreApplication.translate("ai_launcher", u"10", None))
        self.label_16.setText(QCoreApplication.translate("ai_launcher", u"3", None))
        self.bt_launch.setText(QCoreApplication.translate("ai_launcher", u"Launch", None))
    # retranslateUi

