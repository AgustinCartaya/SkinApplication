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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from .promoted.check_button import CheckButton
from .promoted.label import Label
from .promoted.line_edit import LineEdit
from .promoted.navigator_button import NavigatorButton
from .promoted.pagination import Pagination
from .promoted.search_line import SearchLine

class Ui_patients(object):
    def setupUi(self, patients):
        if not patients.objectName():
            patients.setObjectName(u"patients")
        patients.resize(1200, 800)
        patients.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(patients)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(patients)
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

        self.bt_add_new_patient = NavigatorButton(self.frame_6)
        self.bt_add_new_patient.setObjectName(u"bt_add_new_patient")

        self.horizontalLayout.addWidget(self.bt_add_new_patient)

        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(3, 3)

        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_5 = QFrame(patients)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 18, 0)
        self.frame_filters = QFrame(self.frame_5)
        self.frame_filters.setObjectName(u"frame_filters")
        self.frame_filters.setMinimumSize(QSize(300, 0))
        self.frame_filters.setMaximumSize(QSize(330, 16777215))
        self.frame_filters.setFrameShape(QFrame.StyledPanel)
        self.frame_filters.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_filters)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_filters_title = Label(self.frame_filters)
        self.lb_filters_title.setObjectName(u"lb_filters_title")
        self.lb_filters_title.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.lb_filters_title, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.frame_filters)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.lb_filter_clinical_attributes = QLabel(self.frame_3)
        self.lb_filter_clinical_attributes.setObjectName(u"lb_filter_clinical_attributes")
        self.lb_filter_clinical_attributes.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_7.addWidget(self.lb_filter_clinical_attributes, 0, Qt.AlignLeft)

        self.frame_14 = QFrame(self.frame_3)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_14)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 0, 0, 0)
        self.lb_filter_gender = QLabel(self.frame_14)
        self.lb_filter_gender.setObjectName(u"lb_filter_gender")

        self.verticalLayout_8.addWidget(self.lb_filter_gender)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.i_female = QCheckBox(self.frame_16)
        self.i_female.setObjectName(u"i_female")

        self.horizontalLayout_6.addWidget(self.i_female)

        self.i_male = QCheckBox(self.frame_16)
        self.i_male.setObjectName(u"i_male")

        self.horizontalLayout_6.addWidget(self.i_male)

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
        self.lb_filter_age = QLabel(self.frame_15)
        self.lb_filter_age.setObjectName(u"lb_filter_age")

        self.verticalLayout_9.addWidget(self.lb_filter_age)

        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_18)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 0, 0, 0)
        self.lb_filter_age_precise = QLabel(self.frame_18)
        self.lb_filter_age_precise.setObjectName(u"lb_filter_age_precise")

        self.verticalLayout_10.addWidget(self.lb_filter_age_precise)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, 0, 0)
        self.i_agre_precise = LineEdit(self.frame_20)
        self.i_agre_precise.setObjectName(u"i_agre_precise")
        self.i_agre_precise.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_8.addWidget(self.i_agre_precise)


        self.verticalLayout_10.addWidget(self.frame_20, 0, Qt.AlignLeft)


        self.verticalLayout_9.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_15)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_19)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 0, 0, 0)
        self.lb_age_rangue = QLabel(self.frame_19)
        self.lb_age_rangue.setObjectName(u"lb_age_rangue")

        self.verticalLayout_11.addWidget(self.lb_age_rangue)

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
        self.bt_age_rangue_1 = CheckButton(self.frame_17)
        self.bt_age_rangue_1.setObjectName(u"bt_age_rangue_1")
        self.bt_age_rangue_1.setMinimumSize(QSize(80, 20))
        self.bt_age_rangue_1.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_7.addWidget(self.bt_age_rangue_1)

        self.bt_age_rangue_2 = CheckButton(self.frame_17)
        self.bt_age_rangue_2.setObjectName(u"bt_age_rangue_2")
        self.bt_age_rangue_2.setMinimumSize(QSize(80, 20))
        self.bt_age_rangue_2.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_7.addWidget(self.bt_age_rangue_2)

        self.bt_age_rangue_3 = CheckButton(self.frame_17)
        self.bt_age_rangue_3.setObjectName(u"bt_age_rangue_3")
        self.bt_age_rangue_3.setMinimumSize(QSize(80, 20))
        self.bt_age_rangue_3.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_7.addWidget(self.bt_age_rangue_3)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)


        self.verticalLayout_12.addWidget(self.frame_17)

        self.i_age_rangue = LineEdit(self.frame_21)
        self.i_age_rangue.setObjectName(u"i_age_rangue")
        self.i_age_rangue.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_12.addWidget(self.i_age_rangue)


        self.verticalLayout_11.addWidget(self.frame_21)


        self.verticalLayout_9.addWidget(self.frame_19)


        self.verticalLayout_7.addWidget(self.frame_15)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_filters)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, -1, 0, -1)
        self.lb_filter_diagnostic_attributes = QLabel(self.frame_4)
        self.lb_filter_diagnostic_attributes.setObjectName(u"lb_filter_diagnostic_attributes")
        self.lb_filter_diagnostic_attributes.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_14.addWidget(self.lb_filter_diagnostic_attributes)

        self.frame_22 = QFrame(self.frame_4)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_22)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.i_bening = QCheckBox(self.frame_22)
        self.i_bening.setObjectName(u"i_bening")

        self.verticalLayout_13.addWidget(self.i_bening)

        self.i_malignant = QCheckBox(self.frame_22)
        self.i_malignant.setObjectName(u"i_malignant")

        self.verticalLayout_13.addWidget(self.i_malignant)

        self.i_indeterminate = QCheckBox(self.frame_22)
        self.i_indeterminate.setObjectName(u"i_indeterminate")

        self.verticalLayout_13.addWidget(self.i_indeterminate)


        self.verticalLayout_14.addWidget(self.frame_22)


        self.verticalLayout.addWidget(self.frame_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.frame_filters)

        self.frame = QFrame(self.frame_5)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 120))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.c_search = SearchLine(self.frame_7)
        self.c_search.setObjectName(u"c_search")
        self.c_search.setMinimumSize(QSize(0, 30))
        self.c_search.setFrameShape(QFrame.StyledPanel)
        self.c_search.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.c_search)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.bt_search = QPushButton(self.c_search)
        self.bt_search.setObjectName(u"bt_search")
        self.bt_search.setMinimumSize(QSize(20, 20))
        self.bt_search.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_4.addWidget(self.bt_search)

        self.i_search = LineEdit(self.c_search)
        self.i_search.setObjectName(u"i_search")
        self.i_search.setMinimumSize(QSize(300, 0))
        self.i_search.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_4.addWidget(self.i_search)


        self.verticalLayout_4.addWidget(self.c_search, 0, Qt.AlignHCenter)

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
        self.lb_organizer_titles = QLabel(self.frame_11)
        self.lb_organizer_titles.setObjectName(u"lb_organizer_titles")
        self.lb_organizer_titles.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_6.addWidget(self.lb_organizer_titles)


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

        self.bt_sorter_mosaico = CheckButton(self.frame_12)
        self.bt_sorter_mosaico.setObjectName(u"bt_sorter_mosaico")
        self.bt_sorter_mosaico.setMinimumSize(QSize(25, 25))
        self.bt_sorter_mosaico.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.bt_sorter_mosaico)

        self.bt_sorter_list = CheckButton(self.frame_12)
        self.bt_sorter_list.setObjectName(u"bt_sorter_list")
        self.bt_sorter_list.setMinimumSize(QSize(25, 25))
        self.bt_sorter_list.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.bt_sorter_list)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.bt_sorter_asc = CheckButton(self.frame_12)
        self.bt_sorter_asc.setObjectName(u"bt_sorter_asc")
        self.bt_sorter_asc.setMinimumSize(QSize(40, 25))
        self.bt_sorter_asc.setMaximumSize(QSize(40, 25))

        self.horizontalLayout_3.addWidget(self.bt_sorter_asc)

        self.bt_sorter_dsc = CheckButton(self.frame_12)
        self.bt_sorter_dsc.setObjectName(u"bt_sorter_dsc")
        self.bt_sorter_dsc.setMinimumSize(QSize(40, 25))
        self.bt_sorter_dsc.setMaximumSize(QSize(40, 25))

        self.horizontalLayout_3.addWidget(self.bt_sorter_dsc)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.bt_sorter_id = CheckButton(self.frame_12)
        self.bt_sorter_id.setObjectName(u"bt_sorter_id")
        self.bt_sorter_id.setMinimumSize(QSize(40, 25))
        self.bt_sorter_id.setMaximumSize(QSize(40, 25))

        self.horizontalLayout_3.addWidget(self.bt_sorter_id)

        self.bt_sorter_name = CheckButton(self.frame_12)
        self.bt_sorter_name.setObjectName(u"bt_sorter_name")
        self.bt_sorter_name.setMinimumSize(QSize(50, 25))
        self.bt_sorter_name.setMaximumSize(QSize(50, 25))

        self.horizontalLayout_3.addWidget(self.bt_sorter_name)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_3.setStretch(0, 4)
        self.horizontalLayout_3.setStretch(3, 2)
        self.horizontalLayout_3.setStretch(6, 2)
        self.horizontalLayout_3.setStretch(9, 3)

        self.verticalLayout_5.addWidget(self.frame_12)


        self.verticalLayout_4.addWidget(self.frame_10)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.c_pagination = Pagination(self.frame)
        self.c_pagination.setObjectName(u"c_pagination")
        self.c_pagination.setFrameShape(QFrame.StyledPanel)
        self.c_pagination.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.c_pagination)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.retranslateUi(patients)

        QMetaObject.connectSlotsByName(patients)
    # setupUi

    def retranslateUi(self, patients):
        patients.setWindowTitle(QCoreApplication.translate("patients", u"Loggin", None))
        self.bt_back.setText(QCoreApplication.translate("patients", u"Back", None))
        self.lb_title.setText(QCoreApplication.translate("patients", u"List of patients", None))
        self.bt_add_new_patient.setText(QCoreApplication.translate("patients", u"Add new patient", None))
        self.lb_filters_title.setText(QCoreApplication.translate("patients", u"Filters", None))
        self.lb_filter_clinical_attributes.setText(QCoreApplication.translate("patients", u"CLINICAL ATTRIBUTES", None))
        self.lb_filter_gender.setText(QCoreApplication.translate("patients", u"Gender", None))
        self.i_female.setText(QCoreApplication.translate("patients", u"Female", None))
        self.i_male.setText(QCoreApplication.translate("patients", u"Male", None))
        self.lb_filter_age.setText(QCoreApplication.translate("patients", u"Age", None))
        self.lb_filter_age_precise.setText(QCoreApplication.translate("patients", u"Precise", None))
        self.i_agre_precise.setPlaceholderText(QCoreApplication.translate("patients", u"E.g: 43", None))
        self.lb_age_rangue.setText(QCoreApplication.translate("patients", u"Rangue", None))
        self.bt_age_rangue_1.setText(QCoreApplication.translate("patients", u"0 - 20", None))
        self.bt_age_rangue_2.setText(QCoreApplication.translate("patients", u"20 - 50", None))
        self.bt_age_rangue_3.setText(QCoreApplication.translate("patients", u"50 +", None))
        self.i_age_rangue.setPlaceholderText(QCoreApplication.translate("patients", u"E.g: 17 - 32", None))
        self.lb_filter_diagnostic_attributes.setText(QCoreApplication.translate("patients", u"DIAGNOSTIC ATTRIBUTES", None))
        self.i_bening.setText(QCoreApplication.translate("patients", u"Bening (120 / 300)", None))
        self.i_malignant.setText(QCoreApplication.translate("patients", u"Malignant (150 / 300)", None))
        self.i_indeterminate.setText(QCoreApplication.translate("patients", u"Indeterminate (30 / 300)", None))
        self.bt_search.setText("")
        self.i_search.setPlaceholderText(QCoreApplication.translate("patients", u"E.g: AG4432YA", None))
        self.lb_organizer_titles.setText(QCoreApplication.translate("patients", u"Organizer", None))
        self.bt_sorter_mosaico.setText("")
        self.bt_sorter_list.setText("")
        self.bt_sorter_asc.setText(QCoreApplication.translate("patients", u"A-z", None))
        self.bt_sorter_dsc.setText(QCoreApplication.translate("patients", u"z-A", None))
        self.bt_sorter_id.setText(QCoreApplication.translate("patients", u"ID", None))
        self.bt_sorter_name.setText(QCoreApplication.translate("patients", u"Name", None))
    # retranslateUi

