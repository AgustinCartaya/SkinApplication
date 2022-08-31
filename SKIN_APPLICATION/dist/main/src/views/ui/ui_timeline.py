# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_timeline.ui'
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

from .promoted.info_line import InfoLine
from .promoted.label import Label
from .promoted.navigator_button import NavigatorButton
from .promoted.skin_lesion_preview_info import SkinLesionPreviewInfo
from .promoted.timeline_points_container import TimelinePointsContainer

class Ui_timeline(object):
    def setupUi(self, timeline):
        if not timeline.objectName():
            timeline.setObjectName(u"timeline")
        timeline.resize(1200, 800)
        timeline.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(timeline)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.ly_navigator = QHBoxLayout()
        self.ly_navigator.setSpacing(0)
        self.ly_navigator.setObjectName(u"ly_navigator")
        self.ly_navigator.setContentsMargins(-1, 0, 0, -1)
        self.bt_back = NavigatorButton(timeline)
        self.bt_back.setObjectName(u"bt_back")

        self.ly_navigator.addWidget(self.bt_back, 0, Qt.AlignLeft)

        self.lb_title = Label(timeline)
        self.lb_title.setObjectName(u"lb_title")

        self.ly_navigator.addWidget(self.lb_title, 0, Qt.AlignHCenter)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ly_navigator.addItem(self.horizontalSpacer_5)

        self.ly_navigator.setStretch(0, 1)
        self.ly_navigator.setStretch(1, 1)
        self.ly_navigator.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.ly_navigator)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 20)
        self.frame = QFrame(timeline)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(60)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.c_patient_info_line = InfoLine(self.frame)
        self.c_patient_info_line.setObjectName(u"c_patient_info_line")
        self.c_patient_info_line.setFrameShape(QFrame.StyledPanel)
        self.c_patient_info_line.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.c_patient_info_line, 0, Qt.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(timeline)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.c_timeline_points = TimelinePointsContainer(self.frame_2)
        self.c_timeline_points.setObjectName(u"c_timeline_points")
        self.c_timeline_points.setFrameShape(QFrame.StyledPanel)
        self.c_timeline_points.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.c_timeline_points)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.frame_2)

        self.c_skl_info_container = QFrame(timeline)
        self.c_skl_info_container.setObjectName(u"c_skl_info_container")
        self.c_skl_info_container.setFrameShape(QFrame.StyledPanel)
        self.c_skl_info_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.c_skl_info_container)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.c_skl_characteristics = SkinLesionPreviewInfo(self.c_skl_info_container)
        self.c_skl_characteristics.setObjectName(u"c_skl_characteristics")
        self.c_skl_characteristics.setFrameShape(QFrame.StyledPanel)
        self.c_skl_characteristics.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.c_skl_characteristics)

        self.c_ai_results = SkinLesionPreviewInfo(self.c_skl_info_container)
        self.c_ai_results.setObjectName(u"c_ai_results")
        self.c_ai_results.setFrameShape(QFrame.StyledPanel)
        self.c_ai_results.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.c_ai_results)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 6)
        self.horizontalLayout_9.setStretch(2, 6)
        self.horizontalLayout_9.setStretch(3, 1)

        self.verticalLayout.addWidget(self.c_skl_info_container)

        self.frame_4 = QFrame(timeline)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, 20, -1)
        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_8.addWidget(self.label_13, 0, Qt.AlignHCenter)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)

        self.sc_images = QScrollArea(self.frame_4)
        self.sc_images.setObjectName(u"sc_images")
        self.sc_images.setWidgetResizable(True)
        self.c_images = QWidget()
        self.c_images.setObjectName(u"c_images")
        self.c_images.setGeometry(QRect(0, 0, 991, 257))
        self.verticalLayout_14 = QVBoxLayout(self.c_images)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.ly_images = QVBoxLayout()
        self.ly_images.setSpacing(30)
        self.ly_images.setObjectName(u"ly_images")

        self.verticalLayout_14.addLayout(self.ly_images)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer)

        self.sc_images.setWidget(self.c_images)

        self.horizontalLayout_2.addWidget(self.sc_images)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 14)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_8.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.frame_4)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 6)
        self.verticalLayout.setStretch(3, 8)

        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(timeline)

        QMetaObject.connectSlotsByName(timeline)
    # setupUi

    def retranslateUi(self, timeline):
        timeline.setWindowTitle(QCoreApplication.translate("timeline", u"Loggin", None))
        self.bt_back.setText(QCoreApplication.translate("timeline", u"Back", None))
        self.lb_title.setText(QCoreApplication.translate("timeline", u"Timeline", None))
        self.label_13.setText(QCoreApplication.translate("timeline", u"Images", None))
    # retranslateUi

