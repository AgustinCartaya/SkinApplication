# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_image_viewer.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_image_viewer(object):
    def setupUi(self, image_viewer):
        if not image_viewer.objectName():
            image_viewer.setObjectName(u"image_viewer")
        image_viewer.resize(800, 600)
        image_viewer.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(image_viewer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.sc_image = QScrollArea(image_viewer)
        self.sc_image.setObjectName(u"sc_image")
        self.sc_image.setWidgetResizable(True)
        self.c_image_content = QWidget()
        self.c_image_content.setObjectName(u"c_image_content")
        self.c_image_content.setGeometry(QRect(0, 0, 798, 598))
        self.verticalLayout_2 = QVBoxLayout(self.c_image_content)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lb_image = QLabel(self.c_image_content)
        self.lb_image.setObjectName(u"lb_image")

        self.verticalLayout_2.addWidget(self.lb_image)

        self.sc_image.setWidget(self.c_image_content)

        self.verticalLayout.addWidget(self.sc_image)


        self.retranslateUi(image_viewer)

        QMetaObject.connectSlotsByName(image_viewer)
    # setupUi

    def retranslateUi(self, image_viewer):
        image_viewer.setWindowTitle(QCoreApplication.translate("image_viewer", u"Loggin", None))
        self.lb_image.setText("")
    # retranslateUi

