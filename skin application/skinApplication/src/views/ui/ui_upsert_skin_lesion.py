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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from .promoted.button import Button
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
        self.ly_caracteristics = QVBoxLayout()
        self.ly_caracteristics.setSpacing(16)
        self.ly_caracteristics.setObjectName(u"ly_caracteristics")
        self.lb_caracteristics = Label(upsert_skin_lesion)
        self.lb_caracteristics.setObjectName(u"lb_caracteristics")
        self.lb_caracteristics.setMaximumSize(QSize(16777215, 20))

        self.ly_caracteristics.addWidget(self.lb_caracteristics, 0, Qt.AlignHCenter)

        self.sc_caracteristics = QScrollArea(upsert_skin_lesion)
        self.sc_caracteristics.setObjectName(u"sc_caracteristics")
        self.sc_caracteristics.setWidgetResizable(True)
        self.c_caracteristics_content = QWidget()
        self.c_caracteristics_content.setObjectName(u"c_caracteristics_content")
        self.c_caracteristics_content.setGeometry(QRect(0, 0, 364, 332))
        self.verticalLayout_30 = QVBoxLayout(self.c_caracteristics_content)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.ly_caracteristics_content = QVBoxLayout()
        self.ly_caracteristics_content.setObjectName(u"ly_caracteristics_content")

        self.verticalLayout_30.addLayout(self.ly_caracteristics_content)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_3)

        self.sc_caracteristics.setWidget(self.c_caracteristics_content)

        self.ly_caracteristics.addWidget(self.sc_caracteristics)


        self.ly_skin_lesion_content.addLayout(self.ly_caracteristics)

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

        self.ly_ai_results = QVBoxLayout()
        self.ly_ai_results.setObjectName(u"ly_ai_results")
        self.ly_ai_results.setContentsMargins(-1, -1, -1, 10)
        self.lb_lauch_ai = Label(upsert_skin_lesion)
        self.lb_lauch_ai.setObjectName(u"lb_lauch_ai")
        self.lb_lauch_ai.setMaximumSize(QSize(16777215, 25))

        self.ly_ai_results.addWidget(self.lb_lauch_ai, 0, Qt.AlignHCenter)

        self.ly_ai_results_content = QHBoxLayout()
        self.ly_ai_results_content.setObjectName(u"ly_ai_results_content")
        self.ly_ai_results_content.setContentsMargins(-1, -1, 10, 10)
        self.c_ai_1 = QFrame(upsert_skin_lesion)
        self.c_ai_1.setObjectName(u"c_ai_1")
        self.c_ai_1.setFrameShape(QFrame.StyledPanel)
        self.c_ai_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.c_ai_1)
        self.verticalLayout_15.setSpacing(16)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.bt_lauch_ai_1 = Button(self.c_ai_1)
        self.bt_lauch_ai_1.setObjectName(u"bt_lauch_ai_1")

        self.verticalLayout_15.addWidget(self.bt_lauch_ai_1, 0, Qt.AlignHCenter)

        self.c_description_ai_1 = QFrame(self.c_ai_1)
        self.c_description_ai_1.setObjectName(u"c_description_ai_1")
        self.c_description_ai_1.setEnabled(True)
        self.c_description_ai_1.setFrameShape(QFrame.StyledPanel)
        self.c_description_ai_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.c_description_ai_1)
        self.verticalLayout_6.setSpacing(12)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lb_description_ai_1 = QLabel(self.c_description_ai_1)
        self.lb_description_ai_1.setObjectName(u"lb_description_ai_1")
        self.lb_description_ai_1.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_6.addWidget(self.lb_description_ai_1, 0, Qt.AlignHCenter)

        self.i_description_ai_1 = Label(self.c_description_ai_1)
        self.i_description_ai_1.setObjectName(u"i_description_ai_1")
        self.i_description_ai_1.setAlignment(Qt.AlignCenter)
        self.i_description_ai_1.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.i_description_ai_1, 0, Qt.AlignTop)

        self.i_read_more_ai_1 = Label(self.c_description_ai_1)
        self.i_read_more_ai_1.setObjectName(u"i_read_more_ai_1")
        self.i_read_more_ai_1.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_6.addWidget(self.i_read_more_ai_1, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addWidget(self.c_description_ai_1)

        self.c_results_ai_1 = QFrame(self.c_ai_1)
        self.c_results_ai_1.setObjectName(u"c_results_ai_1")
        self.c_results_ai_1.setFrameShape(QFrame.StyledPanel)
        self.c_results_ai_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.c_results_ai_1)
        self.verticalLayout_19.setSpacing(16)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.lb_results_ai_1 = QLabel(self.c_results_ai_1)
        self.lb_results_ai_1.setObjectName(u"lb_results_ai_1")
        self.lb_results_ai_1.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_19.addWidget(self.lb_results_ai_1, 0, Qt.AlignHCenter)

        self.scrollArea_4 = QScrollArea(self.c_results_ai_1)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 238, 147))
        self.verticalLayout_26 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_26.setSpacing(12)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.layout_results_ai_1 = QFormLayout()
        self.layout_results_ai_1.setObjectName(u"layout_results_ai_1")

        self.verticalLayout_26.addLayout(self.layout_results_ai_1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_19.addWidget(self.scrollArea_4)


        self.verticalLayout_15.addWidget(self.c_results_ai_1)


        self.ly_ai_results_content.addWidget(self.c_ai_1)

        self.c_ai_2 = QFrame(upsert_skin_lesion)
        self.c_ai_2.setObjectName(u"c_ai_2")
        self.c_ai_2.setFrameShape(QFrame.StyledPanel)
        self.c_ai_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.c_ai_2)
        self.verticalLayout_14.setSpacing(16)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.bt_lauch_ai_2 = Button(self.c_ai_2)
        self.bt_lauch_ai_2.setObjectName(u"bt_lauch_ai_2")

        self.verticalLayout_14.addWidget(self.bt_lauch_ai_2, 0, Qt.AlignHCenter)

        self.c_description_ai_2 = QFrame(self.c_ai_2)
        self.c_description_ai_2.setObjectName(u"c_description_ai_2")
        self.c_description_ai_2.setFrameShape(QFrame.StyledPanel)
        self.c_description_ai_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.c_description_ai_2)
        self.verticalLayout_27.setSpacing(12)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.lb_description_ai_2 = QLabel(self.c_description_ai_2)
        self.lb_description_ai_2.setObjectName(u"lb_description_ai_2")
        self.lb_description_ai_2.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_27.addWidget(self.lb_description_ai_2, 0, Qt.AlignHCenter)

        self.i_description_ai_2 = Label(self.c_description_ai_2)
        self.i_description_ai_2.setObjectName(u"i_description_ai_2")
        self.i_description_ai_2.setAlignment(Qt.AlignCenter)
        self.i_description_ai_2.setWordWrap(True)

        self.verticalLayout_27.addWidget(self.i_description_ai_2)

        self.i_read_more_ai_2 = QLabel(self.c_description_ai_2)
        self.i_read_more_ai_2.setObjectName(u"i_read_more_ai_2")
        self.i_read_more_ai_2.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_27.addWidget(self.i_read_more_ai_2, 0, Qt.AlignHCenter)


        self.verticalLayout_14.addWidget(self.c_description_ai_2)

        self.c_results_ai_2 = QFrame(self.c_ai_2)
        self.c_results_ai_2.setObjectName(u"c_results_ai_2")
        self.c_results_ai_2.setFrameShape(QFrame.StyledPanel)
        self.c_results_ai_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.c_results_ai_2)
        self.verticalLayout_20.setSpacing(16)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.lb_results_ai_2 = QLabel(self.c_results_ai_2)
        self.lb_results_ai_2.setObjectName(u"lb_results_ai_2")
        self.lb_results_ai_2.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_20.addWidget(self.lb_results_ai_2, 0, Qt.AlignHCenter)

        self.scrollArea_5 = QScrollArea(self.c_results_ai_2)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 239, 147))
        self.verticalLayout_28 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_28.setSpacing(12)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.layout_results_ai_2 = QFormLayout()
        self.layout_results_ai_2.setObjectName(u"layout_results_ai_2")
        self.layout_results_ai_2.setVerticalSpacing(12)
        self.layout_results_ai_2.setContentsMargins(0, -1, -1, -1)
        self.label_6 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_6.setObjectName(u"label_6")

        self.layout_results_ai_2.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.label_8 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_8.setObjectName(u"label_8")

        self.layout_results_ai_2.setWidget(0, QFormLayout.FieldRole, self.label_8)

        self.label_7 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_7.setObjectName(u"label_7")

        self.layout_results_ai_2.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.label_9 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_9.setObjectName(u"label_9")

        self.layout_results_ai_2.setWidget(1, QFormLayout.FieldRole, self.label_9)

        self.label_10 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_10.setObjectName(u"label_10")

        self.layout_results_ai_2.setWidget(2, QFormLayout.LabelRole, self.label_10)

        self.label_11 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_11.setObjectName(u"label_11")

        self.layout_results_ai_2.setWidget(2, QFormLayout.FieldRole, self.label_11)


        self.verticalLayout_28.addLayout(self.layout_results_ai_2)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_20.addWidget(self.scrollArea_5)


        self.verticalLayout_14.addWidget(self.c_results_ai_2)


        self.ly_ai_results_content.addWidget(self.c_ai_2)

        self.c_ai_3 = QFrame(upsert_skin_lesion)
        self.c_ai_3.setObjectName(u"c_ai_3")
        self.c_ai_3.setFrameShape(QFrame.StyledPanel)
        self.c_ai_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.c_ai_3)
        self.verticalLayout_13.setSpacing(16)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.bt_lauch_ai_3 = Button(self.c_ai_3)
        self.bt_lauch_ai_3.setObjectName(u"bt_lauch_ai_3")

        self.verticalLayout_13.addWidget(self.bt_lauch_ai_3, 0, Qt.AlignHCenter)

        self.c_description_ai_3 = QFrame(self.c_ai_3)
        self.c_description_ai_3.setObjectName(u"c_description_ai_3")
        self.c_description_ai_3.setFrameShape(QFrame.StyledPanel)
        self.c_description_ai_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.c_description_ai_3)
        self.verticalLayout_17.setSpacing(12)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.lb_description_ai_3 = QLabel(self.c_description_ai_3)
        self.lb_description_ai_3.setObjectName(u"lb_description_ai_3")
        self.lb_description_ai_3.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_17.addWidget(self.lb_description_ai_3, 0, Qt.AlignHCenter)

        self.i_description_ai_3 = Label(self.c_description_ai_3)
        self.i_description_ai_3.setObjectName(u"i_description_ai_3")
        self.i_description_ai_3.setAlignment(Qt.AlignCenter)
        self.i_description_ai_3.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.i_description_ai_3, 0, Qt.AlignTop)

        self.i_read_more_ai_3 = Label(self.c_description_ai_3)
        self.i_read_more_ai_3.setObjectName(u"i_read_more_ai_3")
        self.i_read_more_ai_3.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_17.addWidget(self.i_read_more_ai_3, 0, Qt.AlignHCenter)


        self.verticalLayout_13.addWidget(self.c_description_ai_3)

        self.lb_results_ai_4 = QFrame(self.c_ai_3)
        self.lb_results_ai_4.setObjectName(u"lb_results_ai_4")
        self.lb_results_ai_4.setFrameShape(QFrame.StyledPanel)
        self.lb_results_ai_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.lb_results_ai_4)
        self.verticalLayout_21.setSpacing(16)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.lb_results_ai_3 = QLabel(self.lb_results_ai_4)
        self.lb_results_ai_3.setObjectName(u"lb_results_ai_3")
        self.lb_results_ai_3.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_21.addWidget(self.lb_results_ai_3, 0, Qt.AlignHCenter)

        self.scrollArea_6 = QScrollArea(self.lb_results_ai_4)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 238, 147))
        self.verticalLayout_29 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_29.setSpacing(12)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.layout_results_ai_3 = QFormLayout()
        self.layout_results_ai_3.setObjectName(u"layout_results_ai_3")

        self.verticalLayout_29.addLayout(self.layout_results_ai_3)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_21.addWidget(self.scrollArea_6)


        self.verticalLayout_13.addWidget(self.lb_results_ai_4)


        self.ly_ai_results_content.addWidget(self.c_ai_3)


        self.ly_ai_results.addLayout(self.ly_ai_results_content)


        self.ly_right.addLayout(self.ly_ai_results)

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
        self.lb_caracteristics.setText(QCoreApplication.translate("upsert_skin_lesion", u"Caracteristics", None))
        self.lb_add_images.setText(QCoreApplication.translate("upsert_skin_lesion", u"Add images", None))
        self.lb_lauch_ai.setText(QCoreApplication.translate("upsert_skin_lesion", u"Launch AI", None))
        self.bt_lauch_ai_1.setText(QCoreApplication.translate("upsert_skin_lesion", u"AI - 1", None))
        self.lb_description_ai_1.setText(QCoreApplication.translate("upsert_skin_lesion", u"Description", None))
        self.i_description_ai_1.setText(QCoreApplication.translate("upsert_skin_lesion", u"There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour..", None))
        self.i_read_more_ai_1.setText(QCoreApplication.translate("upsert_skin_lesion", u"Read more", None))
        self.lb_results_ai_1.setText(QCoreApplication.translate("upsert_skin_lesion", u"Results", None))
        self.bt_lauch_ai_2.setText(QCoreApplication.translate("upsert_skin_lesion", u"AI - 2", None))
        self.lb_description_ai_2.setText(QCoreApplication.translate("upsert_skin_lesion", u"Results", None))
        self.i_description_ai_2.setText(QCoreApplication.translate("upsert_skin_lesion", u"There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour..", None))
        self.i_read_more_ai_2.setText(QCoreApplication.translate("upsert_skin_lesion", u"Read more", None))
        self.lb_results_ai_2.setText(QCoreApplication.translate("upsert_skin_lesion", u"Results", None))
        self.label_6.setText(QCoreApplication.translate("upsert_skin_lesion", u"Risk :", None))
        self.label_8.setText(QCoreApplication.translate("upsert_skin_lesion", u"MALIGNAT", None))
        self.label_7.setText(QCoreApplication.translate("upsert_skin_lesion", u"Type :", None))
        self.label_9.setText(QCoreApplication.translate("upsert_skin_lesion", u"Melanoma", None))
        self.label_10.setText(QCoreApplication.translate("upsert_skin_lesion", u"Accurance :", None))
        self.label_11.setText(QCoreApplication.translate("upsert_skin_lesion", u"87%", None))
        self.bt_lauch_ai_3.setText(QCoreApplication.translate("upsert_skin_lesion", u"AI - 3", None))
        self.lb_description_ai_3.setText(QCoreApplication.translate("upsert_skin_lesion", u"Description", None))
        self.i_description_ai_3.setText(QCoreApplication.translate("upsert_skin_lesion", u"There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour..", None))
        self.i_read_more_ai_3.setText(QCoreApplication.translate("upsert_skin_lesion", u"Read more", None))
        self.lb_results_ai_3.setText(QCoreApplication.translate("upsert_skin_lesion", u"Results", None))
    # retranslateUi

