# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(300, 0))
        self.frame_2.setMaximumSize(QSize(200, 300))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_3.addWidget(self.lineEdit)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_3.addWidget(self.lineEdit_2)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

