# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_patients.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_patients(object):
    def setupUi(self, patients):
        if not patients.objectName():
            patients.setObjectName(u"patients")
        patients.resize(1200, 800)
        patients.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(patients)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_6 = QFrame(patients)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 60))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.frame_6)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton_2 = QPushButton(self.frame_6)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_5 = QFrame(patients)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(300, 0))
        self.frame_2.setMaximumSize(QSize(360, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_7.addWidget(self.label_5, 0, Qt.AlignLeft)

        self.frame_14 = QFrame(self.frame_3)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_14)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 0, 0, 0)
        self.label_6 = QLabel(self.frame_14)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_8.addWidget(self.label_6)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.checkBox = QCheckBox(self.frame_16)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_6.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.frame_16)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_6.addWidget(self.checkBox_2)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)


        self.verticalLayout_8.addWidget(self.frame_16)


        self.verticalLayout_7.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 0, 0, 0)
        self.label_9 = QLabel(self.frame_15)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_9.addWidget(self.label_9)

        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_18)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 0, 0, 0)
        self.label_7 = QLabel(self.frame_18)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_10.addWidget(self.label_7)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, 0, 0)
        self.lineEdit_3 = QLineEdit(self.frame_20)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_8.addWidget(self.lineEdit_3)


        self.verticalLayout_10.addWidget(self.frame_20, 0, Qt.AlignLeft)


        self.verticalLayout_9.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_15)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_19)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 0, 0, 0)
        self.label_8 = QLabel(self.frame_19)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_11.addWidget(self.label_8)

        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_21)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_21)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_24 = QPushButton(self.frame_17)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setMinimumSize(QSize(90, 20))
        self.pushButton_24.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_7.addWidget(self.pushButton_24)

        self.pushButton_25 = QPushButton(self.frame_17)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setMinimumSize(QSize(90, 20))
        self.pushButton_25.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_7.addWidget(self.pushButton_25)

        self.pushButton_26 = QPushButton(self.frame_17)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMinimumSize(QSize(90, 20))
        self.pushButton_26.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_7.addWidget(self.pushButton_26)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)


        self.verticalLayout_12.addWidget(self.frame_17)

        self.lineEdit_4 = QLineEdit(self.frame_21)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_12.addWidget(self.lineEdit_4)


        self.verticalLayout_11.addWidget(self.frame_21)


        self.verticalLayout_9.addWidget(self.frame_19)


        self.verticalLayout_7.addWidget(self.frame_15)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, -1, 0, -1)
        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_14.addWidget(self.label_10)

        self.frame_22 = QFrame(self.frame_4)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_22)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.checkBox_3 = QCheckBox(self.frame_22)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_13.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.frame_22)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_13.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.frame_22)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout_13.addWidget(self.checkBox_5)


        self.verticalLayout_14.addWidget(self.frame_22)


        self.verticalLayout.addWidget(self.frame_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(self.frame_5)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 150))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 40))
        self.frame_9.setMaximumSize(QSize(16777215, 40))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_9 = QPushButton(self.frame_9)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_9)

        self.lineEdit = QLineEdit(self.frame_9)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(300, 0))
        self.lineEdit.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_4.addWidget(self.lineEdit)


        self.verticalLayout_4.addWidget(self.frame_9, 0, Qt.AlignHCenter)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 100))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 20))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_11)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_11)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_6.addWidget(self.label_3)


        self.verticalLayout_5.addWidget(self.frame_11, 0, Qt.AlignHCenter)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 80))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.pushButton_6 = QPushButton(self.frame_12)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(30, 30))
        self.pushButton_6.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.frame_12)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(30, 30))
        self.pushButton_5.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_5)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.pushButton_8 = QPushButton(self.frame_12)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(30, 30))
        self.pushButton_8.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.frame_12)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(30, 30))
        self.pushButton_7.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_7)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.pushButton_3 = QPushButton(self.frame_12)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(30, 30))
        self.pushButton_3.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_12)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(30, 30))
        self.pushButton_4.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addWidget(self.frame_12)


        self.verticalLayout_4.addWidget(self.frame_10)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_11 = QPushButton(self.frame_8)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(100, 100))
        self.pushButton_11.setMaximumSize(QSize(150, 150))

        self.gridLayout.addWidget(self.pushButton_11, 2, 3, 1, 1)

        self.pushButton_13 = QPushButton(self.frame_8)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(100, 100))
        self.pushButton_13.setMaximumSize(QSize(150, 150))

        self.gridLayout.addWidget(self.pushButton_13, 0, 3, 1, 1)

        self.pushButton_16 = QPushButton(self.frame_8)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(100, 100))
        self.pushButton_16.setMaximumSize(QSize(150, 150))

        self.gridLayout.addWidget(self.pushButton_16, 0, 1, 1, 1)

        self.pushButton_10 = QPushButton(self.frame_8)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(100, 100))
        self.pushButton_10.setMaximumSize(QSize(150, 150))

        self.gridLayout.addWidget(self.pushButton_10, 2, 2, 1, 1)

        self.pushButton_12 = QPushButton(self.frame_8)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(100, 100))
        self.pushButton_12.setMaximumSize(QSize(150, 150))

        self.gridLayout.addWidget(self.pushButton_12, 0, 2, 1, 1)

        self.pushButton_14 = QPushButton(self.frame_8)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(100, 100))
        self.pushButton_14.setMaximumSize(QSize(150, 150))

        self.gridLayout.addWidget(self.pushButton_14, 1, 2, 1, 1)

        self.pushButton_15 = QPushButton(self.frame_8)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(100, 100))
        self.pushButton_15.setMaximumSize(QSize(150, 150))

        self.gridLayout.addWidget(self.pushButton_15, 1, 3, 1, 1)

        self.pushButton_17 = QPushButton(self.frame_8)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(100, 100))
        self.pushButton_17.setMaximumSize(QSize(150, 150))

        self.gridLayout.addWidget(self.pushButton_17, 0, 0, 1, 1)

        self.pushButton_18 = QPushButton(self.frame_8)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(100, 100))
        self.pushButton_18.setMaximumSize(QSize(150, 150))

        self.gridLayout.addWidget(self.pushButton_18, 1, 0, 1, 1)

        self.pushButton_19 = QPushButton(self.frame_8)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(100, 100))
        self.pushButton_19.setMaximumSize(QSize(150, 150))

        self.gridLayout.addWidget(self.pushButton_19, 1, 1, 1, 1)

        self.pushButton_20 = QPushButton(self.frame_8)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(100, 100))
        self.pushButton_20.setMaximumSize(QSize(150, 150))

        self.gridLayout.addWidget(self.pushButton_20, 2, 0, 1, 1)

        self.pushButton_21 = QPushButton(self.frame_8)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(100, 100))
        self.pushButton_21.setMaximumSize(QSize(150, 150))

        self.gridLayout.addWidget(self.pushButton_21, 2, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnMinimumWidth(0, 1)
        self.gridLayout.setColumnMinimumWidth(1, 1)
        self.gridLayout.setColumnMinimumWidth(2, 1)
        self.gridLayout.setColumnMinimumWidth(3, 1)
        self.gridLayout.setRowMinimumHeight(0, 1)
        self.gridLayout.setRowMinimumHeight(1, 1)
        self.gridLayout.setRowMinimumHeight(2, 1)

        self.verticalLayout_3.addWidget(self.frame_8)

        self.frame_13 = QFrame(self.frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 35))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_22 = QPushButton(self.frame_13)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(30, 30))
        self.pushButton_22.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.pushButton_22)

        self.lineEdit_2 = QLineEdit(self.frame_13)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_5.addWidget(self.lineEdit_2)

        self.label_4 = QLabel(self.frame_13)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.pushButton_23 = QPushButton(self.frame_13)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMinimumSize(QSize(30, 30))
        self.pushButton_23.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.pushButton_23)


        self.verticalLayout_3.addWidget(self.frame_13, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.retranslateUi(patients)

        QMetaObject.connectSlotsByName(patients)
    # setupUi

    def retranslateUi(self, patients):
        patients.setWindowTitle(QCoreApplication.translate("patients", u"Loggin", None))
        self.pushButton.setText(QCoreApplication.translate("patients", u"Back", None))
        self.label_2.setText(QCoreApplication.translate("patients", u"List of patients", None))
        self.pushButton_2.setText(QCoreApplication.translate("patients", u"Add new patient", None))
        self.label.setText(QCoreApplication.translate("patients", u"Filters", None))
        self.label_5.setText(QCoreApplication.translate("patients", u"CLINICAL ATTRIBUTES", None))
        self.label_6.setText(QCoreApplication.translate("patients", u"Gender", None))
        self.checkBox.setText(QCoreApplication.translate("patients", u"Female", None))
        self.checkBox_2.setText(QCoreApplication.translate("patients", u"Male", None))
        self.label_9.setText(QCoreApplication.translate("patients", u"Age", None))
        self.label_7.setText(QCoreApplication.translate("patients", u"Precise", None))
        self.label_8.setText(QCoreApplication.translate("patients", u"Rangue", None))
        self.pushButton_24.setText(QCoreApplication.translate("patients", u"0 - 20", None))
        self.pushButton_25.setText(QCoreApplication.translate("patients", u"20 - 50", None))
        self.pushButton_26.setText(QCoreApplication.translate("patients", u"50 +", None))
        self.label_10.setText(QCoreApplication.translate("patients", u"DIAGNOSTIC ATTRIBUTES", None))
        self.checkBox_3.setText(QCoreApplication.translate("patients", u"Bening (120 / 300)", None))
        self.checkBox_4.setText(QCoreApplication.translate("patients", u"Malignant (150 / 300)", None))
        self.checkBox_5.setText(QCoreApplication.translate("patients", u"Indeterminate (30 / 300)", None))
        self.pushButton_9.setText(QCoreApplication.translate("patients", u"MM", None))
        self.label_3.setText(QCoreApplication.translate("patients", u"Organizer", None))
        self.pushButton_6.setText(QCoreApplication.translate("patients", u"MM", None))
        self.pushButton_5.setText(QCoreApplication.translate("patients", u"MM", None))
        self.pushButton_8.setText(QCoreApplication.translate("patients", u"MM", None))
        self.pushButton_7.setText(QCoreApplication.translate("patients", u"MM", None))
        self.pushButton_3.setText(QCoreApplication.translate("patients", u"MM", None))
        self.pushButton_4.setText(QCoreApplication.translate("patients", u"MM", None))
        self.pushButton_11.setText(QCoreApplication.translate("patients", u"MM", None))
        self.pushButton_13.setText(QCoreApplication.translate("patients", u"MM", None))
        self.pushButton_16.setText(QCoreApplication.translate("patients", u"MM", None))
        self.pushButton_10.setText(QCoreApplication.translate("patients", u"MM", None))
        self.pushButton_12.setText(QCoreApplication.translate("patients", u"MM", None))
        self.pushButton_14.setText(QCoreApplication.translate("patients", u"MM", None))
        self.pushButton_15.setText(QCoreApplication.translate("patients", u"MM", None))
        self.pushButton_17.setText(QCoreApplication.translate("patients", u"MM", None))
        self.pushButton_18.setText(QCoreApplication.translate("patients", u"MM", None))
        self.pushButton_19.setText(QCoreApplication.translate("patients", u"MM", None))
        self.pushButton_20.setText(QCoreApplication.translate("patients", u"MM", None))
        self.pushButton_21.setText(QCoreApplication.translate("patients", u"MM", None))
        self.pushButton_22.setText(QCoreApplication.translate("patients", u"MM", None))
        self.label_4.setText(QCoreApplication.translate("patients", u"of 250", None))
        self.pushButton_23.setText(QCoreApplication.translate("patients", u"MM", None))
    # retranslateUi

