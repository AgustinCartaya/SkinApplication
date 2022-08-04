# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_upsert_skin_lesion.ui'
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

from .promoted.label import Label
from .promoted.navigator_button import NavigatorButton

class Ui_upsert_skin_lesion(object):
    def setupUi(self, upsert_skin_lesion):
        if not upsert_skin_lesion.objectName():
            upsert_skin_lesion.setObjectName(u"upsert_skin_lesion")
        upsert_skin_lesion.resize(1200, 800)
        upsert_skin_lesion.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(upsert_skin_lesion)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ly_navigator = QHBoxLayout()
        self.ly_navigator.setSpacing(0)
        self.ly_navigator.setObjectName(u"ly_navigator")
        self.ly_navigator.setContentsMargins(-1, 0, 0, -1)
        self.bt_back = NavigatorButton(upsert_skin_lesion)
        self.bt_back.setObjectName(u"bt_back")

        self.ly_navigator.addWidget(self.bt_back)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ly_navigator.addItem(self.horizontalSpacer)

        self.lb_title = Label(upsert_skin_lesion)
        self.lb_title.setObjectName(u"lb_title")

        self.ly_navigator.addWidget(self.lb_title)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ly_navigator.addItem(self.horizontalSpacer_2)

        self.bt_complete = NavigatorButton(upsert_skin_lesion)
        self.bt_complete.setObjectName(u"bt_complete")

        self.ly_navigator.addWidget(self.bt_complete)


        self.verticalLayout_2.addLayout(self.ly_navigator)

        self.ly_center = QHBoxLayout()
        self.ly_center.setSpacing(30)
        self.ly_center.setObjectName(u"ly_center")
        self.ly_center.setContentsMargins(-1, 20, -1, -1)
        self.ly_left = QVBoxLayout()
        self.ly_left.setObjectName(u"ly_left")
        self.c_body2d = QFrame(upsert_skin_lesion)
        self.c_body2d.setObjectName(u"c_body2d")
        self.c_body2d.setFrameShape(QFrame.StyledPanel)
        self.c_body2d.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.c_body2d)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_4 = QLabel(self.c_body2d)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_16.addWidget(self.label_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.ly_left.addWidget(self.c_body2d)


        self.ly_center.addLayout(self.ly_left)

        self.ly_right = QVBoxLayout()
        self.ly_right.setSpacing(20)
        self.ly_right.setObjectName(u"ly_right")
        self.ly_right.setContentsMargins(-1, -1, 20, -1)
        self.ly_skin_lesion_content = QHBoxLayout()
        self.ly_skin_lesion_content.setSpacing(20)
        self.ly_skin_lesion_content.setObjectName(u"ly_skin_lesion_content")
        self.ly_characteristics = QVBoxLayout()
        self.ly_characteristics.setSpacing(16)
        self.ly_characteristics.setObjectName(u"ly_characteristics")
        self.lb_characteristics = Label(upsert_skin_lesion)
        self.lb_characteristics.setObjectName(u"lb_characteristics")
        self.lb_characteristics.setMaximumSize(QSize(16777215, 20))

        self.ly_characteristics.addWidget(self.lb_characteristics, 0, Qt.AlignHCenter)

        self.sc_characteristics = QScrollArea(upsert_skin_lesion)
        self.sc_characteristics.setObjectName(u"sc_characteristics")
        self.sc_characteristics.setWidgetResizable(True)
        self.c_characteristics_content = QWidget()
        self.c_characteristics_content.setObjectName(u"c_characteristics_content")
        self.c_characteristics_content.setGeometry(QRect(0, 0, 364, 332))
        self.verticalLayout_30 = QVBoxLayout(self.c_characteristics_content)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.ly_characteristics_content = QVBoxLayout()
        self.ly_characteristics_content.setObjectName(u"ly_characteristics_content")

        self.verticalLayout_30.addLayout(self.ly_characteristics_content)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_3)

        self.sc_characteristics.setWidget(self.c_characteristics_content)

        self.ly_characteristics.addWidget(self.sc_characteristics)


        self.ly_skin_lesion_content.addLayout(self.ly_characteristics)

        self.ly_images = QVBoxLayout()
        self.ly_images.setSpacing(16)
        self.ly_images.setObjectName(u"ly_images")
        self.lb_add_images = Label(upsert_skin_lesion)
        self.lb_add_images.setObjectName(u"lb_add_images")
        self.lb_add_images.setMaximumSize(QSize(16777215, 20))

        self.ly_images.addWidget(self.lb_add_images, 0, Qt.AlignHCenter)

        self.sc_images = QScrollArea(upsert_skin_lesion)
        self.sc_images.setObjectName(u"sc_images")
        self.sc_images.setWidgetResizable(True)
        self.c_images_content = QWidget()
        self.c_images_content.setObjectName(u"c_images_content")
        self.c_images_content.setGeometry(QRect(0, 0, 364, 332))
        self.verticalLayout_10 = QVBoxLayout(self.c_images_content)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.ly_images_type_content = QVBoxLayout()
        self.ly_images_type_content.setObjectName(u"ly_images_type_content")

        self.verticalLayout_10.addLayout(self.ly_images_type_content)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.sc_images.setWidget(self.c_images_content)

        self.ly_images.addWidget(self.sc_images)


        self.ly_skin_lesion_content.addLayout(self.ly_images)


        self.ly_right.addLayout(self.ly_skin_lesion_content)

        self.c_ai_results = QFrame(upsert_skin_lesion)
        self.c_ai_results.setObjectName(u"c_ai_results")
        self.c_ai_results.setFrameShape(QFrame.StyledPanel)
        self.c_ai_results.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.c_ai_results)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_lauch_ai = Label(self.c_ai_results)
        self.lb_lauch_ai.setObjectName(u"lb_lauch_ai")
        self.lb_lauch_ai.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout.addWidget(self.lb_lauch_ai, 0, Qt.AlignHCenter)

        self.ly_ai_results = QVBoxLayout()
        self.ly_ai_results.setObjectName(u"ly_ai_results")
        self.ly_ai_results.setContentsMargins(-1, -1, -1, 10)

        self.verticalLayout.addLayout(self.ly_ai_results)


        self.ly_right.addWidget(self.c_ai_results)

        self.ly_right.setStretch(0, 1)
        self.ly_right.setStretch(1, 1)

        self.ly_center.addLayout(self.ly_right)

        self.ly_center.setStretch(0, 1)
        self.ly_center.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.ly_center)


        self.retranslateUi(upsert_skin_lesion)

        QMetaObject.connectSlotsByName(upsert_skin_lesion)
    # setupUi

    def retranslateUi(self, upsert_skin_lesion):
        upsert_skin_lesion.setWindowTitle(QCoreApplication.translate("upsert_skin_lesion", u"Loggin", None))
        self.bt_back.setText(QCoreApplication.translate("upsert_skin_lesion", u"Back", None))
        self.lb_title.setText(QCoreApplication.translate("upsert_skin_lesion", u"Add skin lesion", None))
        self.bt_complete.setText(QCoreApplication.translate("upsert_skin_lesion", u"Completed", None))
        self.label_4.setText(QCoreApplication.translate("upsert_skin_lesion", u"Indisponible", None))
        self.lb_characteristics.setText(QCoreApplication.translate("upsert_skin_lesion", u"Characteristics", None))
        self.lb_add_images.setText(QCoreApplication.translate("upsert_skin_lesion", u"Add images", None))
        self.lb_lauch_ai.setText(QCoreApplication.translate("upsert_skin_lesion", u"Launch AI", None))
    # retranslateUi

