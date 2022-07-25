# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_check_patient.ui'
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

class Ui_check_patient(object):
    def setupUi(self, check_patient):
        if not check_patient.objectName():
            check_patient.setObjectName(u"check_patient")
        check_patient.resize(1200, 800)
        check_patient.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(check_patient)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(check_patient)
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

        self.bt_add_new_skin_part = NavigatorButton(self.frame_6)
        self.bt_add_new_skin_part.setObjectName(u"bt_add_new_skin_part")

        self.horizontalLayout.addWidget(self.bt_add_new_skin_part)

        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(3, 3)

        self.verticalLayout_2.addWidget(self.frame_6)

        self.c_center = QFrame(check_patient)
        self.c_center.setObjectName(u"c_center")
        self.c_center.setFrameShape(QFrame.StyledPanel)
        self.c_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.c_center)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 18, 0)
        self.c_patient_information = QFrame(self.c_center)
        self.c_patient_information.setObjectName(u"c_patient_information")
        self.c_patient_information.setMinimumSize(QSize(280, 0))
        self.c_patient_information.setMaximumSize(QSize(280, 16777215))
        self.c_patient_information.setFrameShape(QFrame.StyledPanel)
        self.c_patient_information.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.c_patient_information)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_patient_information = Label(self.c_patient_information)
        self.lb_patient_information.setObjectName(u"lb_patient_information")
        self.lb_patient_information.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.lb_patient_information, 0, Qt.AlignHCenter)

        self.scrollArea = QScrollArea(self.c_patient_information)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.c_basic_information_scroll_area = QWidget()
        self.c_basic_information_scroll_area.setObjectName(u"c_basic_information_scroll_area")
        self.c_basic_information_scroll_area.setGeometry(QRect(0, 0, 258, 344))
        self.verticalLayout_5 = QVBoxLayout(self.c_basic_information_scroll_area)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.c_basic_information = QFrame(self.c_basic_information_scroll_area)
        self.c_basic_information.setObjectName(u"c_basic_information")
        self.c_basic_information.setFrameShape(QFrame.StyledPanel)
        self.c_basic_information.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.c_basic_information)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lb_basic_information = Label(self.c_basic_information)
        self.lb_basic_information.setObjectName(u"lb_basic_information")
        self.lb_basic_information.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_7.addWidget(self.lb_basic_information)

        self.c_bi_content = QFrame(self.c_basic_information)
        self.c_bi_content.setObjectName(u"c_bi_content")
        self.c_bi_content.setFrameShape(QFrame.StyledPanel)
        self.c_bi_content.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.c_bi_content)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(16)
        self.lb_first_name = Label(self.c_bi_content)
        self.lb_first_name.setObjectName(u"lb_first_name")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lb_first_name)

        self.i_first_name = Label(self.c_bi_content)
        self.i_first_name.setObjectName(u"i_first_name")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.i_first_name)

        self.lb_last_name = Label(self.c_bi_content)
        self.lb_last_name.setObjectName(u"lb_last_name")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lb_last_name)

        self.i_last_name = Label(self.c_bi_content)
        self.i_last_name.setObjectName(u"i_last_name")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.i_last_name)

        self.lb_gender = Label(self.c_bi_content)
        self.lb_gender.setObjectName(u"lb_gender")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lb_gender)

        self.i_gender = Label(self.c_bi_content)
        self.i_gender.setObjectName(u"i_gender")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.i_gender)

        self.leb_age = Label(self.c_bi_content)
        self.leb_age.setObjectName(u"leb_age")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.leb_age)

        self.i_age = Label(self.c_bi_content)
        self.i_age.setObjectName(u"i_age")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.i_age)


        self.verticalLayout_7.addWidget(self.c_bi_content)


        self.verticalLayout_5.addWidget(self.c_basic_information)

        self.c_medical_information = QFrame(self.c_basic_information_scroll_area)
        self.c_medical_information.setObjectName(u"c_medical_information")
        self.c_medical_information.setFrameShape(QFrame.StyledPanel)
        self.c_medical_information.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.c_medical_information)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lb_medical_information = Label(self.c_medical_information)
        self.lb_medical_information.setObjectName(u"lb_medical_information")
        self.lb_medical_information.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_8.addWidget(self.lb_medical_information)

        self.c_mi_content = QFrame(self.c_medical_information)
        self.c_mi_content.setObjectName(u"c_mi_content")
        self.c_mi_content.setFrameShape(QFrame.StyledPanel)
        self.c_mi_content.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.c_mi_content)


        self.verticalLayout_5.addWidget(self.c_medical_information)

        self.scrollArea.setWidget(self.c_basic_information_scroll_area)

        self.verticalLayout.addWidget(self.scrollArea)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_2 = Button(self.c_patient_information)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.c_patient_information)

        self.frame = QFrame(self.c_center)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = Label(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter)

        self.scrollArea_2 = QScrollArea(self.frame)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.c_skin_parts_scroll_area = QWidget()
        self.c_skin_parts_scroll_area.setObjectName(u"c_skin_parts_scroll_area")
        self.c_skin_parts_scroll_area.setGeometry(QRect(0, 0, 872, 708))
        self.verticalLayout_6 = QVBoxLayout(self.c_skin_parts_scroll_area)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.c_skin_parts = QFrame(self.c_skin_parts_scroll_area)
        self.c_skin_parts.setObjectName(u"c_skin_parts")
        self.c_skin_parts.setFrameShape(QFrame.StyledPanel)
        self.c_skin_parts.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.c_skin_parts)
        self.verticalLayout_4.setSpacing(30)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.c_skin_part_to_duplicate = QFrame(self.c_skin_parts)
        self.c_skin_part_to_duplicate.setObjectName(u"c_skin_part_to_duplicate")
        self.c_skin_part_to_duplicate.setFrameShape(QFrame.StyledPanel)
        self.c_skin_part_to_duplicate.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.c_skin_part_to_duplicate)
        self.verticalLayout_14.setSpacing(16)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.c_skin_part_to_duplicate)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setSpacing(16)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.c_n1 = QFrame(self.frame_2)
        self.c_n1.setObjectName(u"c_n1")
        self.c_n1.setFrameShape(QFrame.StyledPanel)
        self.c_n1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.c_n1)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.c_image = QFrame(self.c_n1)
        self.c_image.setObjectName(u"c_image")
        self.c_image.setFrameShape(QFrame.StyledPanel)
        self.c_image.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.c_image)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lb_image = QLabel(self.c_image)
        self.lb_image.setObjectName(u"lb_image")
        self.lb_image.setMaximumSize(QSize(150, 150))
        self.lb_image.setPixmap(QPixmap(u"assets/img/Screenshot 2022-07-25 180616.png"))
        self.lb_image.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.lb_image)


        self.verticalLayout_10.addWidget(self.c_image)


        self.horizontalLayout_7.addWidget(self.c_n1)

        self.c_n2 = QFrame(self.frame_2)
        self.c_n2.setObjectName(u"c_n2")
        self.c_n2.setFrameShape(QFrame.StyledPanel)
        self.c_n2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.c_n2)
        self.horizontalLayout_4.setSpacing(16)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.c_annotations = QFrame(self.c_n2)
        self.c_annotations.setObjectName(u"c_annotations")
        self.c_annotations.setFrameShape(QFrame.StyledPanel)
        self.c_annotations.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.c_annotations)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.c_annotation_title = QFrame(self.c_annotations)
        self.c_annotation_title.setObjectName(u"c_annotation_title")
        self.c_annotation_title.setMaximumSize(QSize(16777215, 20))
        self.c_annotation_title.setFrameShape(QFrame.StyledPanel)
        self.c_annotation_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.c_annotation_title)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lb_annotations = QLabel(self.c_annotation_title)
        self.lb_annotations.setObjectName(u"lb_annotations")
        self.lb_annotations.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_6.addWidget(self.lb_annotations, 0, Qt.AlignHCenter)


        self.verticalLayout_12.addWidget(self.c_annotation_title)

        self.c_annotation_content = QFrame(self.c_annotations)
        self.c_annotation_content.setObjectName(u"c_annotation_content")
        self.c_annotation_content.setFrameShape(QFrame.StyledPanel)
        self.c_annotation_content.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.c_annotation_content)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(12)
        self.formLayout.setContentsMargins(9, 0, 9, 0)
        self.lb_annotation_risk = QLabel(self.c_annotation_content)
        self.lb_annotation_risk.setObjectName(u"lb_annotation_risk")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lb_annotation_risk)

        self.label_7 = QLabel(self.c_annotation_content)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_7)

        self.lb_annotation_type = QLabel(self.c_annotation_content)
        self.lb_annotation_type.setObjectName(u"lb_annotation_type")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lb_annotation_type)

        self.label_8 = QLabel(self.c_annotation_content)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_8)

        self.lb_annotation_notes = QLabel(self.c_annotation_content)
        self.lb_annotation_notes.setObjectName(u"lb_annotation_notes")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lb_annotation_notes)

        self.label_9 = QLabel(self.c_annotation_content)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_9)


        self.verticalLayout_12.addWidget(self.c_annotation_content)

        self.lb_read_more_annotations = QLabel(self.c_annotations)
        self.lb_read_more_annotations.setObjectName(u"lb_read_more_annotations")

        self.verticalLayout_12.addWidget(self.lb_read_more_annotations, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.horizontalLayout_4.addWidget(self.c_annotations)

        self.c_ai_results = QFrame(self.c_n2)
        self.c_ai_results.setObjectName(u"c_ai_results")
        self.c_ai_results.setFrameShape(QFrame.StyledPanel)
        self.c_ai_results.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.c_ai_results)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_3 = QLabel(self.c_ai_results)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_11.addWidget(self.label_3, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.c_ai_content = QFrame(self.c_ai_results)
        self.c_ai_content.setObjectName(u"c_ai_content")
        self.c_ai_content.setFrameShape(QFrame.StyledPanel)
        self.c_ai_content.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.c_ai_content)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setVerticalSpacing(12)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lb_ai_type_ai = QLabel(self.c_ai_content)
        self.lb_ai_type_ai.setObjectName(u"lb_ai_type_ai")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.lb_ai_type_ai)

        self.label_13 = QLabel(self.c_ai_content)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.label_13)

        self.lb_ai_risk = QLabel(self.c_ai_content)
        self.lb_ai_risk.setObjectName(u"lb_ai_risk")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.lb_ai_risk)

        self.label_14 = QLabel(self.c_ai_content)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.label_14)

        self.lb_ai_accurance = QLabel(self.c_ai_content)
        self.lb_ai_accurance.setObjectName(u"lb_ai_accurance")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.lb_ai_accurance)

        self.label_15 = QLabel(self.c_ai_content)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.label_15)

        self.lb_ai_type = QLabel(self.c_ai_content)
        self.lb_ai_type.setObjectName(u"lb_ai_type")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.lb_ai_type)

        self.label_4 = QLabel(self.c_ai_content)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.label_4)


        self.verticalLayout_11.addWidget(self.c_ai_content)

        self.lb_read_more_ai_results = QLabel(self.c_ai_results)
        self.lb_read_more_ai_results.setObjectName(u"lb_read_more_ai_results")

        self.verticalLayout_11.addWidget(self.lb_read_more_ai_results, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.horizontalLayout_4.addWidget(self.c_ai_results)


        self.horizontalLayout_7.addWidget(self.c_n2)

        self.c_n3 = QFrame(self.frame_2)
        self.c_n3.setObjectName(u"c_n3")
        self.c_n3.setFrameShape(QFrame.StyledPanel)
        self.c_n3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.c_n3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.c_buttons = QFrame(self.c_n3)
        self.c_buttons.setObjectName(u"c_buttons")
        self.c_buttons.setFrameShape(QFrame.StyledPanel)
        self.c_buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.c_buttons)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.bt_see_time_line = Button(self.c_buttons)
        self.bt_see_time_line.setObjectName(u"bt_see_time_line")
        self.bt_see_time_line.setMinimumSize(QSize(100, 0))
        self.bt_see_time_line.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_13.addWidget(self.bt_see_time_line)

        self.bt_see_images = Button(self.c_buttons)
        self.bt_see_images.setObjectName(u"bt_see_images")
        self.bt_see_images.setMinimumSize(QSize(100, 0))
        self.bt_see_images.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_13.addWidget(self.bt_see_images)

        self.bt_more_options = Button(self.c_buttons)
        self.bt_more_options.setObjectName(u"bt_more_options")
        self.bt_more_options.setMinimumSize(QSize(100, 0))
        self.bt_more_options.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_13.addWidget(self.bt_more_options)


        self.verticalLayout_9.addWidget(self.c_buttons)

        self.vs_buttons = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_9.addItem(self.vs_buttons)


        self.horizontalLayout_7.addWidget(self.c_n3)

        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 6)
        self.horizontalLayout_7.setStretch(2, 1)

        self.verticalLayout_14.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.c_skin_part_to_duplicate)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 10, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.bt_update = Button(self.frame_3)
        self.bt_update.setObjectName(u"bt_update")

        self.horizontalLayout_3.addWidget(self.bt_update)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 10)
        self.horizontalLayout_3.setStretch(2, 3)

        self.verticalLayout_14.addWidget(self.frame_3)


        self.verticalLayout_4.addWidget(self.c_skin_part_to_duplicate)


        self.verticalLayout_6.addWidget(self.c_skin_parts)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.scrollArea_2.setWidget(self.c_skin_parts_scroll_area)

        self.verticalLayout_3.addWidget(self.scrollArea_2)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.c_center)


        self.retranslateUi(check_patient)

        QMetaObject.connectSlotsByName(check_patient)
    # setupUi

    def retranslateUi(self, check_patient):
        check_patient.setWindowTitle(QCoreApplication.translate("check_patient", u"Loggin", None))
        self.bt_back.setText(QCoreApplication.translate("check_patient", u"Back", None))
        self.lb_title.setText(QCoreApplication.translate("check_patient", u"Check patient", None))
        self.bt_add_new_skin_part.setText(QCoreApplication.translate("check_patient", u"Add skin part", None))
        self.lb_patient_information.setText(QCoreApplication.translate("check_patient", u"Patient information", None))
        self.lb_basic_information.setText(QCoreApplication.translate("check_patient", u"Basic information", None))
        self.lb_first_name.setText(QCoreApplication.translate("check_patient", u"First name :", None))
        self.i_first_name.setText(QCoreApplication.translate("check_patient", u"...", None))
        self.lb_last_name.setText(QCoreApplication.translate("check_patient", u"Last name :", None))
        self.i_last_name.setText(QCoreApplication.translate("check_patient", u"...", None))
        self.lb_gender.setText(QCoreApplication.translate("check_patient", u"Gender :", None))
        self.i_gender.setText(QCoreApplication.translate("check_patient", u"...", None))
        self.leb_age.setText(QCoreApplication.translate("check_patient", u"Age :", None))
        self.i_age.setText(QCoreApplication.translate("check_patient", u"...", None))
        self.lb_medical_information.setText(QCoreApplication.translate("check_patient", u"Madical information", None))
        self.pushButton_2.setText(QCoreApplication.translate("check_patient", u"Edit patient information", None))
        self.label.setText(QCoreApplication.translate("check_patient", u"Parts of the sking under study", None))
        self.lb_image.setText("")
        self.lb_annotations.setText(QCoreApplication.translate("check_patient", u"Annotations", None))
        self.lb_annotation_risk.setText(QCoreApplication.translate("check_patient", u"Risk", None))
        self.label_7.setText(QCoreApplication.translate("check_patient", u"BENIGN", None))
        self.lb_annotation_type.setText(QCoreApplication.translate("check_patient", u"Type", None))
        self.label_8.setText(QCoreApplication.translate("check_patient", u"Mole", None))
        self.lb_annotation_notes.setText(QCoreApplication.translate("check_patient", u"Notes", None))
        self.label_9.setText(QCoreApplication.translate("check_patient", u"...", None))
        self.lb_read_more_annotations.setText(QCoreApplication.translate("check_patient", u"Read more", None))
        self.label_3.setText(QCoreApplication.translate("check_patient", u"AI results", None))
        self.lb_ai_type_ai.setText(QCoreApplication.translate("check_patient", u"IA:", None))
        self.label_13.setText(QCoreApplication.translate("check_patient", u"IA - 1", None))
        self.lb_ai_risk.setText(QCoreApplication.translate("check_patient", u"Risk", None))
        self.label_14.setText(QCoreApplication.translate("check_patient", u"BENIGN", None))
        self.lb_ai_accurance.setText(QCoreApplication.translate("check_patient", u"Accurance", None))
        self.label_15.setText(QCoreApplication.translate("check_patient", u"93 %", None))
        self.lb_ai_type.setText(QCoreApplication.translate("check_patient", u"Type", None))
        self.label_4.setText(QCoreApplication.translate("check_patient", u"Mole", None))
        self.lb_read_more_ai_results.setText(QCoreApplication.translate("check_patient", u"Read more", None))
        self.bt_see_time_line.setText(QCoreApplication.translate("check_patient", u"Time line", None))
        self.bt_see_images.setText(QCoreApplication.translate("check_patient", u"Images", None))
        self.bt_more_options.setText(QCoreApplication.translate("check_patient", u"More", None))
        self.bt_update.setText(QCoreApplication.translate("check_patient", u"Update", None))
    # retranslateUi

