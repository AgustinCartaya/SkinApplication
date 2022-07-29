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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from .promoted.button import Button
from .promoted.check_button import CheckButton
from .promoted.label import Label
from .promoted.line_edit import LineEdit
from .promoted.navigator_button import NavigatorButton

class Ui_upsert_skin_lesion(object):
    def setupUi(self, upsert_skin_lesion):
        if not upsert_skin_lesion.objectName():
            upsert_skin_lesion.setObjectName(u"upsert_skin_lesion")
        upsert_skin_lesion.resize(1200, 800)
        upsert_skin_lesion.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(upsert_skin_lesion)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(upsert_skin_lesion)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 60))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bt_back = NavigatorButton(self.frame_6)
        self.bt_back.setObjectName(u"bt_back")

        self.horizontalLayout.addWidget(self.bt_back)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lb_title = Label(self.frame_6)
        self.lb_title.setObjectName(u"lb_title")

        self.horizontalLayout.addWidget(self.lb_title)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.bt_upsert = NavigatorButton(self.frame_6)
        self.bt_upsert.setObjectName(u"bt_upsert")

        self.horizontalLayout.addWidget(self.bt_upsert)

        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(3, 3)

        self.verticalLayout_2.addWidget(self.frame_6)

        self.c_center = QFrame(upsert_skin_lesion)
        self.c_center.setObjectName(u"c_center")
        self.c_center.setFrameShape(QFrame.StyledPanel)
        self.c_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.c_center)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 18, 0)
        self.c_left = QFrame(self.c_center)
        self.c_left.setObjectName(u"c_left")
        self.c_left.setFrameShape(QFrame.StyledPanel)
        self.c_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.c_left)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.c_body2d = QFrame(self.c_left)
        self.c_body2d.setObjectName(u"c_body2d")
        self.c_body2d.setFrameShape(QFrame.StyledPanel)
        self.c_body2d.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.c_body2d)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_4 = QLabel(self.c_body2d)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_16.addWidget(self.label_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.c_body2d)


        self.horizontalLayout_2.addWidget(self.c_left)

        self.c_right = QFrame(self.c_center)
        self.c_right.setObjectName(u"c_right")
        self.c_right.setFrameShape(QFrame.StyledPanel)
        self.c_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.c_right)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.c_up = QFrame(self.c_right)
        self.c_up.setObjectName(u"c_up")
        self.c_up.setFrameShape(QFrame.StyledPanel)
        self.c_up.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.c_up)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 30, 0)
        self.c_up_left = QFrame(self.c_up)
        self.c_up_left.setObjectName(u"c_up_left")
        self.c_up_left.setMaximumSize(QSize(500, 16777215))
        self.c_up_left.setFrameShape(QFrame.StyledPanel)
        self.c_up_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.c_up_left)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lb_caracteristics = Label(self.c_up_left)
        self.lb_caracteristics.setObjectName(u"lb_caracteristics")
        self.lb_caracteristics.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.lb_caracteristics, 0, Qt.AlignHCenter)

        self.scrollArea = QScrollArea(self.c_up_left)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -60, 391, 400))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setSpacing(40)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.layout_caracteristics = QVBoxLayout()
        self.layout_caracteristics.setSpacing(16)
        self.layout_caracteristics.setObjectName(u"layout_caracteristics")
        self.layout_caracteristics.setContentsMargins(-1, 0, -1, -1)
        self.c_diameter = QFrame(self.scrollAreaWidgetContents)
        self.c_diameter.setObjectName(u"c_diameter")
        self.c_diameter.setFrameShape(QFrame.StyledPanel)
        self.c_diameter.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.c_diameter)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_20 = Label(self.c_diameter)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_5.addWidget(self.label_20)

        self.doubleSpinBox = QDoubleSpinBox(self.c_diameter)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.horizontalLayout_5.addWidget(self.doubleSpinBox)

        self.comboBox = QComboBox(self.c_diameter)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_5.addWidget(self.comboBox)

        self.pushButton_4 = Button(self.c_diameter)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.pushButton_4)


        self.layout_caracteristics.addWidget(self.c_diameter)

        self.c_apparition = QFrame(self.scrollAreaWidgetContents)
        self.c_apparition.setObjectName(u"c_apparition")
        self.c_apparition.setFrameShape(QFrame.StyledPanel)
        self.c_apparition.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.c_apparition)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_21 = Label(self.c_apparition)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_6.addWidget(self.label_21)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.c_apparition)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.horizontalLayout_6.addWidget(self.doubleSpinBox_2)

        self.comboBox_2 = QComboBox(self.c_apparition)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_6.addWidget(self.comboBox_2)

        self.pushButton_5 = Button(self.c_apparition)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.pushButton_5)


        self.layout_caracteristics.addWidget(self.c_apparition)


        self.verticalLayout_8.addLayout(self.layout_caracteristics)

        self.c_create_new_caracteristic = QFrame(self.scrollAreaWidgetContents)
        self.c_create_new_caracteristic.setObjectName(u"c_create_new_caracteristic")
        self.c_create_new_caracteristic.setFrameShape(QFrame.StyledPanel)
        self.c_create_new_caracteristic.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.c_create_new_caracteristic)
        self.verticalLayout_11.setSpacing(20)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.bt_create_new_caracteristic = Button(self.c_create_new_caracteristic)
        self.bt_create_new_caracteristic.setObjectName(u"bt_create_new_caracteristic")

        self.verticalLayout_11.addWidget(self.bt_create_new_caracteristic, 0, Qt.AlignHCenter)

        self.c_new_caracteristic_content = QFrame(self.c_create_new_caracteristic)
        self.c_new_caracteristic_content.setObjectName(u"c_new_caracteristic_content")
        self.c_new_caracteristic_content.setFrameShape(QFrame.StyledPanel)
        self.c_new_caracteristic_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.c_new_caracteristic_content)
        self.verticalLayout_12.setSpacing(16)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.c_new_caracteristic_content)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.bt_values = CheckButton(self.frame_8)
        self.bt_values.setObjectName(u"bt_values")

        self.horizontalLayout_8.addWidget(self.bt_values)

        self.bt_number = CheckButton(self.frame_8)
        self.bt_number.setObjectName(u"bt_number")

        self.horizontalLayout_8.addWidget(self.bt_number)

        self.bt_text = CheckButton(self.frame_8)
        self.bt_text.setObjectName(u"bt_text")

        self.horizontalLayout_8.addWidget(self.bt_text)


        self.verticalLayout_12.addWidget(self.frame_8, 0, Qt.AlignHCenter)

        self.frame_9 = QFrame(self.c_new_caracteristic_content)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_9)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.lb_name_new_caracteristic = Label(self.frame_9)
        self.lb_name_new_caracteristic.setObjectName(u"lb_name_new_caracteristic")

        self.verticalLayout_22.addWidget(self.lb_name_new_caracteristic)

        self.i_name_new_caracteristic = LineEdit(self.frame_9)
        self.i_name_new_caracteristic.setObjectName(u"i_name_new_caracteristic")

        self.verticalLayout_22.addWidget(self.i_name_new_caracteristic)


        self.verticalLayout_12.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.c_new_caracteristic_content)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_10)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.lb_values_new_caracteristic = Label(self.frame_10)
        self.lb_values_new_caracteristic.setObjectName(u"lb_values_new_caracteristic")

        self.verticalLayout_23.addWidget(self.lb_values_new_caracteristic)

        self.i_values_new_caracteristic = LineEdit(self.frame_10)
        self.i_values_new_caracteristic.setObjectName(u"i_values_new_caracteristic")

        self.verticalLayout_23.addWidget(self.i_values_new_caracteristic)


        self.verticalLayout_12.addWidget(self.frame_10)

        self.frame_7 = QFrame(self.c_new_caracteristic_content)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.bt_cancel_new_caracteristic = Button(self.frame_7)
        self.bt_cancel_new_caracteristic.setObjectName(u"bt_cancel_new_caracteristic")

        self.horizontalLayout_12.addWidget(self.bt_cancel_new_caracteristic)

        self.bt_add_new_caracteristic = Button(self.frame_7)
        self.bt_add_new_caracteristic.setObjectName(u"bt_add_new_caracteristic")

        self.horizontalLayout_12.addWidget(self.bt_add_new_caracteristic)


        self.verticalLayout_12.addWidget(self.frame_7, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.c_new_caracteristic_content)


        self.verticalLayout_8.addWidget(self.c_create_new_caracteristic)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.horizontalLayout_3.addWidget(self.c_up_left)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.c_up_right = QFrame(self.c_up)
        self.c_up_right.setObjectName(u"c_up_right")
        self.c_up_right.setMaximumSize(QSize(270, 16777215))
        self.c_up_right.setFrameShape(QFrame.StyledPanel)
        self.c_up_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.c_up_right)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lb_add_images = Label(self.c_up_right)
        self.lb_add_images.setObjectName(u"lb_add_images")
        self.lb_add_images.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_5.addWidget(self.lb_add_images, 0, Qt.AlignHCenter)

        self.scrollArea_3 = QScrollArea(self.c_up_right)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 266, 346))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_10.setSpacing(30)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.layout_image_type = QVBoxLayout()
        self.layout_image_type.setSpacing(0)
        self.layout_image_type.setObjectName(u"layout_image_type")
        self.layout_image_type.setContentsMargins(0, 0, 0, 0)
        self.c_medical_image = QFrame(self.scrollAreaWidgetContents_3)
        self.c_medical_image.setObjectName(u"c_medical_image")
        self.c_medical_image.setFrameShape(QFrame.StyledPanel)
        self.c_medical_image.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.c_medical_image)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.c_medical_image)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(125, 0))
        self.label_17.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_7.addWidget(self.label_17)

        self.label_22 = QLabel(self.c_medical_image)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_7.addWidget(self.label_22)

        self.label_23 = QLabel(self.c_medical_image)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_7.addWidget(self.label_23)


        self.layout_image_type.addWidget(self.c_medical_image)

        self.c_dermatoscopy = QFrame(self.scrollAreaWidgetContents_3)
        self.c_dermatoscopy.setObjectName(u"c_dermatoscopy")
        self.c_dermatoscopy.setFrameShape(QFrame.StyledPanel)
        self.c_dermatoscopy.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.c_dermatoscopy)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.c_dermatoscopy)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(125, 0))
        self.label_24.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_9.addWidget(self.label_24)

        self.label_25 = QLabel(self.c_dermatoscopy)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_9.addWidget(self.label_25)

        self.label_26 = QLabel(self.c_dermatoscopy)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_9.addWidget(self.label_26)


        self.layout_image_type.addWidget(self.c_dermatoscopy)

        self.c_microscopy = QFrame(self.scrollAreaWidgetContents_3)
        self.c_microscopy.setObjectName(u"c_microscopy")
        self.c_microscopy.setFrameShape(QFrame.StyledPanel)
        self.c_microscopy.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.c_microscopy)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.c_microscopy)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(125, 0))
        self.label_27.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_10.addWidget(self.label_27)

        self.label_28 = QLabel(self.c_microscopy)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_10.addWidget(self.label_28)

        self.label_29 = QLabel(self.c_microscopy)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_10.addWidget(self.label_29)


        self.layout_image_type.addWidget(self.c_microscopy)


        self.verticalLayout_10.addLayout(self.layout_image_type)

        self.c_create_new_image_type = QFrame(self.scrollAreaWidgetContents_3)
        self.c_create_new_image_type.setObjectName(u"c_create_new_image_type")
        self.c_create_new_image_type.setFrameShape(QFrame.StyledPanel)
        self.c_create_new_image_type.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.c_create_new_image_type)
        self.verticalLayout_24.setSpacing(12)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(-1, 0, -1, 0)
        self.bt_create_new_image_type = Button(self.c_create_new_image_type)
        self.bt_create_new_image_type.setObjectName(u"bt_create_new_image_type")

        self.verticalLayout_24.addWidget(self.bt_create_new_image_type)

        self.c_new_image_type_content = QFrame(self.c_create_new_image_type)
        self.c_new_image_type_content.setObjectName(u"c_new_image_type_content")
        self.c_new_image_type_content.setFrameShape(QFrame.StyledPanel)
        self.c_new_image_type_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.c_new_image_type_content)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.lb_new_image_type_name = Label(self.c_new_image_type_content)
        self.lb_new_image_type_name.setObjectName(u"lb_new_image_type_name")

        self.verticalLayout_25.addWidget(self.lb_new_image_type_name)

        self.i_new_image_type_name = LineEdit(self.c_new_image_type_content)
        self.i_new_image_type_name.setObjectName(u"i_new_image_type_name")

        self.verticalLayout_25.addWidget(self.i_new_image_type_name)

        self.frame_5 = QFrame(self.c_new_image_type_content)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.bt_cancel_new_image_type = Button(self.frame_5)
        self.bt_cancel_new_image_type.setObjectName(u"bt_cancel_new_image_type")

        self.horizontalLayout_11.addWidget(self.bt_cancel_new_image_type)

        self.bt_add_new_image_type = Button(self.frame_5)
        self.bt_add_new_image_type.setObjectName(u"bt_add_new_image_type")

        self.horizontalLayout_11.addWidget(self.bt_add_new_image_type)


        self.verticalLayout_25.addWidget(self.frame_5, 0, Qt.AlignHCenter)


        self.verticalLayout_24.addWidget(self.c_new_image_type_content)


        self.verticalLayout_10.addWidget(self.c_create_new_image_type)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_5.addWidget(self.scrollArea_3)


        self.horizontalLayout_3.addWidget(self.c_up_right)


        self.verticalLayout_3.addWidget(self.c_up)

        self.c_bottom = QFrame(self.c_right)
        self.c_bottom.setObjectName(u"c_bottom")
        self.c_bottom.setFrameShape(QFrame.StyledPanel)
        self.c_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.c_bottom)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lb_lauch_ai = Label(self.c_bottom)
        self.lb_lauch_ai.setObjectName(u"lb_lauch_ai")
        self.lb_lauch_ai.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_7.addWidget(self.lb_lauch_ai, 0, Qt.AlignHCenter)

        self.c_ai_result = QFrame(self.c_bottom)
        self.c_ai_result.setObjectName(u"c_ai_result")
        self.c_ai_result.setFrameShape(QFrame.StyledPanel)
        self.c_ai_result.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.c_ai_result)
        self.horizontalLayout_4.setSpacing(30)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.c_ai_1 = QFrame(self.c_ai_result)
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
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 233, 168))
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


        self.horizontalLayout_4.addWidget(self.c_ai_1)

        self.c_ai_2 = QFrame(self.c_ai_result)
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
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 233, 168))
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


        self.horizontalLayout_4.addWidget(self.c_ai_2)

        self.c_ai_3 = QFrame(self.c_ai_result)
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
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 233, 168))
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


        self.horizontalLayout_4.addWidget(self.c_ai_3)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)

        self.verticalLayout_7.addWidget(self.c_ai_result)


        self.verticalLayout_3.addWidget(self.c_bottom)


        self.horizontalLayout_2.addWidget(self.c_right)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 4)

        self.verticalLayout_2.addWidget(self.c_center)


        self.retranslateUi(upsert_skin_lesion)

        QMetaObject.connectSlotsByName(upsert_skin_lesion)
    # setupUi

    def retranslateUi(self, upsert_skin_lesion):
        upsert_skin_lesion.setWindowTitle(QCoreApplication.translate("upsert_skin_lesion", u"Loggin", None))
        self.bt_back.setText(QCoreApplication.translate("upsert_skin_lesion", u"Back", None))
        self.lb_title.setText(QCoreApplication.translate("upsert_skin_lesion", u"Add skin lesion", None))
        self.bt_upsert.setText(QCoreApplication.translate("upsert_skin_lesion", u"Completed", None))
        self.label_4.setText(QCoreApplication.translate("upsert_skin_lesion", u"Indisponible", None))
        self.lb_caracteristics.setText(QCoreApplication.translate("upsert_skin_lesion", u"Caracteristics", None))
        self.label_20.setText(QCoreApplication.translate("upsert_skin_lesion", u"Diameter : ", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("upsert_skin_lesion", u"cm", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("upsert_skin_lesion", u"mm", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("upsert_skin_lesion", u"nm", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("upsert_skin_lesion", u"um", None))

        self.pushButton_4.setText(QCoreApplication.translate("upsert_skin_lesion", u"+", None))
        self.label_21.setText(QCoreApplication.translate("upsert_skin_lesion", u"Apparition :", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("upsert_skin_lesion", u"Years", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("upsert_skin_lesion", u"Months", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("upsert_skin_lesion", u"Weeks", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("upsert_skin_lesion", u"Days", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("upsert_skin_lesion", u"Hours", None))

        self.pushButton_5.setText(QCoreApplication.translate("upsert_skin_lesion", u"+", None))
        self.bt_create_new_caracteristic.setText(QCoreApplication.translate("upsert_skin_lesion", u"Create new caracteristic", None))
        self.bt_values.setText(QCoreApplication.translate("upsert_skin_lesion", u"Values", None))
        self.bt_number.setText(QCoreApplication.translate("upsert_skin_lesion", u"Number", None))
        self.bt_text.setText(QCoreApplication.translate("upsert_skin_lesion", u"Text", None))
        self.lb_name_new_caracteristic.setText(QCoreApplication.translate("upsert_skin_lesion", u"Name :", None))
        self.lb_values_new_caracteristic.setText(QCoreApplication.translate("upsert_skin_lesion", u"Values :", None))
        self.bt_cancel_new_caracteristic.setText(QCoreApplication.translate("upsert_skin_lesion", u"Cancel", None))
        self.bt_add_new_caracteristic.setText(QCoreApplication.translate("upsert_skin_lesion", u"Add", None))
        self.lb_add_images.setText(QCoreApplication.translate("upsert_skin_lesion", u"Add images", None))
        self.label_17.setText(QCoreApplication.translate("upsert_skin_lesion", u"Medical image", None))
        self.label_22.setText(QCoreApplication.translate("upsert_skin_lesion", u"(2)", None))
        self.label_23.setText(QCoreApplication.translate("upsert_skin_lesion", u"+ 1", None))
        self.label_24.setText(QCoreApplication.translate("upsert_skin_lesion", u"Dermatoscopy", None))
        self.label_25.setText(QCoreApplication.translate("upsert_skin_lesion", u"(999)", None))
        self.label_26.setText(QCoreApplication.translate("upsert_skin_lesion", u"+999", None))
        self.label_27.setText(QCoreApplication.translate("upsert_skin_lesion", u"Microscopy", None))
        self.label_28.setText(QCoreApplication.translate("upsert_skin_lesion", u"(999)", None))
        self.label_29.setText(QCoreApplication.translate("upsert_skin_lesion", u"+999", None))
        self.bt_create_new_image_type.setText(QCoreApplication.translate("upsert_skin_lesion", u"Create new image type", None))
        self.lb_new_image_type_name.setText(QCoreApplication.translate("upsert_skin_lesion", u"Name", None))
        self.bt_cancel_new_image_type.setText(QCoreApplication.translate("upsert_skin_lesion", u"Cancel", None))
        self.bt_add_new_image_type.setText(QCoreApplication.translate("upsert_skin_lesion", u"Add", None))
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

