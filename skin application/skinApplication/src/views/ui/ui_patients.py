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
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

from .promoted.button import Button
from .promoted.check_button import CheckButton
from .promoted.filter_variable_inputs_container import FilterVariableInputsContainer
from .promoted.filters_content import FiltersContent
from .promoted.filters_header import FiltersHeader
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
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ly_navigator = QHBoxLayout()
        self.ly_navigator.setSpacing(0)
        self.ly_navigator.setObjectName(u"ly_navigator")
        self.ly_navigator.setContentsMargins(-1, 0, -1, -1)
        self.bt_back = NavigatorButton(patients)
        self.bt_back.setObjectName(u"bt_back")

        self.ly_navigator.addWidget(self.bt_back, 0, Qt.AlignLeft)

        self.lb_title = Label(patients)
        self.lb_title.setObjectName(u"lb_title")

        self.ly_navigator.addWidget(self.lb_title, 0, Qt.AlignHCenter)

        self.bt_add_new_patient = NavigatorButton(patients)
        self.bt_add_new_patient.setObjectName(u"bt_add_new_patient")

        self.ly_navigator.addWidget(self.bt_add_new_patient, 0, Qt.AlignRight)

        self.ly_navigator.setStretch(0, 1)
        self.ly_navigator.setStretch(1, 1)
        self.ly_navigator.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.ly_navigator)

        self.ly_center = QHBoxLayout()
        self.ly_center.setSpacing(30)
        self.ly_center.setObjectName(u"ly_center")
        self.ly_center.setContentsMargins(0, 30, 0, 0)
        self.c_filters = QFrame(patients)
        self.c_filters.setObjectName(u"c_filters")
        self.c_filters.setMinimumSize(QSize(300, 0))
        self.c_filters.setMaximumSize(QSize(330, 16777215))
        self.c_filters.setFrameShape(QFrame.StyledPanel)
        self.c_filters.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.c_filters)
        self.verticalLayout_18.setSpacing(20)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.ly_filters_title = QHBoxLayout()
        self.ly_filters_title.setObjectName(u"ly_filters_title")
        self.spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ly_filters_title.addItem(self.spacer)

        self.lb_filters_title = Label(self.c_filters)
        self.lb_filters_title.setObjectName(u"lb_filters_title")
        self.lb_filters_title.setMaximumSize(QSize(16777215, 20))

        self.ly_filters_title.addWidget(self.lb_filters_title, 0, Qt.AlignHCenter)

        self.bt_reset_filters = Button(self.c_filters)
        self.bt_reset_filters.setObjectName(u"bt_reset_filters")

        self.ly_filters_title.addWidget(self.bt_reset_filters, 0, Qt.AlignRight)

        self.ly_filters_title.setStretch(0, 1)
        self.ly_filters_title.setStretch(1, 1)
        self.ly_filters_title.setStretch(2, 1)

        self.verticalLayout_18.addLayout(self.ly_filters_title)

        self.sc_filters = QScrollArea(self.c_filters)
        self.sc_filters.setObjectName(u"sc_filters")
        self.sc_filters.setWidgetResizable(True)
        self.c_filters_content = QWidget()
        self.c_filters_content.setObjectName(u"c_filters_content")
        self.c_filters_content.setGeometry(QRect(0, 0, 326, 699))
        self.verticalLayout_3 = QVBoxLayout(self.c_filters_content)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ly_filters = QVBoxLayout()
        self.ly_filters.setSpacing(9)
        self.ly_filters.setObjectName(u"ly_filters")
        self.ly_filters.setContentsMargins(-1, -1, -1, 20)
        self.ly_filter_basic_information = QVBoxLayout()
        self.ly_filter_basic_information.setSpacing(0)
        self.ly_filter_basic_information.setObjectName(u"ly_filter_basic_information")
        self.c_filter_bi_header = FiltersHeader(self.c_filters_content)
        self.c_filter_bi_header.setObjectName(u"c_filter_bi_header")
        self.c_filter_bi_header.setFrameShape(QFrame.StyledPanel)
        self.c_filter_bi_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.c_filter_bi_header)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lb_filter_clinical_attributes = Label(self.c_filter_bi_header)
        self.lb_filter_clinical_attributes.setObjectName(u"lb_filter_clinical_attributes")
        self.lb_filter_clinical_attributes.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_7.addWidget(self.lb_filter_clinical_attributes, 0, Qt.AlignLeft)


        self.ly_filter_basic_information.addWidget(self.c_filter_bi_header)

        self.c_filter_bi_content = FiltersContent(self.c_filters_content)
        self.c_filter_bi_content.setObjectName(u"c_filter_bi_content")
        self.c_filter_bi_content.setFrameShape(QFrame.StyledPanel)
        self.c_filter_bi_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.c_filter_bi_content)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ly_filter_gender = QVBoxLayout()
        self.ly_filter_gender.setSpacing(4)
        self.ly_filter_gender.setObjectName(u"ly_filter_gender")
        self.ly_filter_gender.setContentsMargins(9, -1, -1, -1)
        self.lb_filter_gender = Label(self.c_filter_bi_content)
        self.lb_filter_gender.setObjectName(u"lb_filter_gender")

        self.ly_filter_gender.addWidget(self.lb_filter_gender)

        self.ly_filter_gender_i = QHBoxLayout()
        self.ly_filter_gender_i.setObjectName(u"ly_filter_gender_i")
        self.ly_filter_gender_i.setContentsMargins(9, -1, -1, -1)
        self.i_male = QCheckBox(self.c_filter_bi_content)
        self.i_male.setObjectName(u"i_male")

        self.ly_filter_gender_i.addWidget(self.i_male)

        self.i_female = QCheckBox(self.c_filter_bi_content)
        self.i_female.setObjectName(u"i_female")

        self.ly_filter_gender_i.addWidget(self.i_female)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ly_filter_gender_i.addItem(self.horizontalSpacer_7)


        self.ly_filter_gender.addLayout(self.ly_filter_gender_i)


        self.verticalLayout.addLayout(self.ly_filter_gender)

        self.ly_filter_age = QVBoxLayout()
        self.ly_filter_age.setSpacing(9)
        self.ly_filter_age.setObjectName(u"ly_filter_age")
        self.ly_filter_age.setContentsMargins(9, -1, -1, 0)
        self.lb_filter_age = Label(self.c_filter_bi_content)
        self.lb_filter_age.setObjectName(u"lb_filter_age")

        self.ly_filter_age.addWidget(self.lb_filter_age)

        self.ly_filter_age_precise = QVBoxLayout()
        self.ly_filter_age_precise.setSpacing(0)
        self.ly_filter_age_precise.setObjectName(u"ly_filter_age_precise")
        self.ly_filter_age_precise.setContentsMargins(10, -1, -1, -1)
        self.c_filter_age_precise_header = FiltersHeader(self.c_filter_bi_content)
        self.c_filter_age_precise_header.setObjectName(u"c_filter_age_precise_header")
        self.c_filter_age_precise_header.setFrameShape(QFrame.StyledPanel)
        self.c_filter_age_precise_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.c_filter_age_precise_header)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.lb_filter_age_precise = Label(self.c_filter_age_precise_header)
        self.lb_filter_age_precise.setObjectName(u"lb_filter_age_precise")

        self.horizontalLayout_12.addWidget(self.lb_filter_age_precise)


        self.ly_filter_age_precise.addWidget(self.c_filter_age_precise_header)

        self.c_filter_age_precise_content = QFrame(self.c_filter_bi_content)
        self.c_filter_age_precise_content.setObjectName(u"c_filter_age_precise_content")
        self.c_filter_age_precise_content.setFrameShape(QFrame.StyledPanel)
        self.c_filter_age_precise_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.c_filter_age_precise_content)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.i_agre_precise = QSpinBox(self.c_filter_age_precise_content)
        self.i_agre_precise.setObjectName(u"i_agre_precise")
        self.i_agre_precise.setMaximumSize(QSize(80, 16777215))

        self.verticalLayout_7.addWidget(self.i_agre_precise)


        self.ly_filter_age_precise.addWidget(self.c_filter_age_precise_content)


        self.ly_filter_age.addLayout(self.ly_filter_age_precise)

        self.ly_filter_age_range = QVBoxLayout()
        self.ly_filter_age_range.setSpacing(0)
        self.ly_filter_age_range.setObjectName(u"ly_filter_age_range")
        self.ly_filter_age_range.setContentsMargins(9, -1, -1, -1)
        self.c_filter_age_range_header = FiltersHeader(self.c_filter_bi_content)
        self.c_filter_age_range_header.setObjectName(u"c_filter_age_range_header")
        self.c_filter_age_range_header.setFrameShape(QFrame.StyledPanel)
        self.c_filter_age_range_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.c_filter_age_range_header)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.lb_age_range = Label(self.c_filter_age_range_header)
        self.lb_age_range.setObjectName(u"lb_age_range")

        self.horizontalLayout_13.addWidget(self.lb_age_range)


        self.ly_filter_age_range.addWidget(self.c_filter_age_range_header)

        self.c_filter_age_range_content = QFrame(self.c_filter_bi_content)
        self.c_filter_age_range_content.setObjectName(u"c_filter_age_range_content")
        self.c_filter_age_range_content.setFrameShape(QFrame.StyledPanel)
        self.c_filter_age_range_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.c_filter_age_range_content)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.ly_filter_age_range_bt = QHBoxLayout()
        self.ly_filter_age_range_bt.setObjectName(u"ly_filter_age_range_bt")
        self.bt_age_range_1 = CheckButton(self.c_filter_age_range_content)
        self.bt_age_range_1.setObjectName(u"bt_age_range_1")
        self.bt_age_range_1.setMinimumSize(QSize(80, 20))
        self.bt_age_range_1.setMaximumSize(QSize(90, 16777215))

        self.ly_filter_age_range_bt.addWidget(self.bt_age_range_1)

        self.bt_age_range_2 = CheckButton(self.c_filter_age_range_content)
        self.bt_age_range_2.setObjectName(u"bt_age_range_2")
        self.bt_age_range_2.setMinimumSize(QSize(80, 20))
        self.bt_age_range_2.setMaximumSize(QSize(90, 16777215))

        self.ly_filter_age_range_bt.addWidget(self.bt_age_range_2)

        self.bt_age_range_3 = CheckButton(self.c_filter_age_range_content)
        self.bt_age_range_3.setObjectName(u"bt_age_range_3")
        self.bt_age_range_3.setMinimumSize(QSize(80, 20))
        self.bt_age_range_3.setMaximumSize(QSize(90, 16777215))

        self.ly_filter_age_range_bt.addWidget(self.bt_age_range_3)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ly_filter_age_range_bt.addItem(self.horizontalSpacer_8)


        self.verticalLayout_8.addLayout(self.ly_filter_age_range_bt)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.i_age_range_min = QSpinBox(self.c_filter_age_range_content)
        self.i_age_range_min.setObjectName(u"i_age_range_min")
        self.i_age_range_min.setMinimumSize(QSize(80, 0))
        self.i_age_range_min.setMaximumSize(QSize(80, 16777215))
        self.i_age_range_min.setMaximum(130)

        self.horizontalLayout_14.addWidget(self.i_age_range_min)

        self.lb_age_range_separator = QLabel(self.c_filter_age_range_content)
        self.lb_age_range_separator.setObjectName(u"lb_age_range_separator")

        self.horizontalLayout_14.addWidget(self.lb_age_range_separator, 0, Qt.AlignHCenter)

        self.i_age_range_max = QSpinBox(self.c_filter_age_range_content)
        self.i_age_range_max.setObjectName(u"i_age_range_max")
        self.i_age_range_max.setMinimumSize(QSize(80, 0))
        self.i_age_range_max.setMaximumSize(QSize(80, 16777215))
        self.i_age_range_max.setMaximum(130)

        self.horizontalLayout_14.addWidget(self.i_age_range_max)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_14)


        self.ly_filter_age_range.addWidget(self.c_filter_age_range_content)


        self.ly_filter_age.addLayout(self.ly_filter_age_range)


        self.verticalLayout.addLayout(self.ly_filter_age)


        self.ly_filter_basic_information.addWidget(self.c_filter_bi_content)


        self.ly_filters.addLayout(self.ly_filter_basic_information)

        self.ly_filter_medical_information = QVBoxLayout()
        self.ly_filter_medical_information.setSpacing(0)
        self.ly_filter_medical_information.setObjectName(u"ly_filter_medical_information")
        self.c_filter_mi_header = FiltersHeader(self.c_filters_content)
        self.c_filter_mi_header.setObjectName(u"c_filter_mi_header")
        self.c_filter_mi_header.setFrameShape(QFrame.StyledPanel)
        self.c_filter_mi_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.c_filter_mi_header)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lb_filter_mi = Label(self.c_filter_mi_header)
        self.lb_filter_mi.setObjectName(u"lb_filter_mi")

        self.horizontalLayout_9.addWidget(self.lb_filter_mi)


        self.ly_filter_medical_information.addWidget(self.c_filter_mi_header)

        self.c_filter_mi_content = FilterVariableInputsContainer(self.c_filters_content)
        self.c_filter_mi_content.setObjectName(u"c_filter_mi_content")
        self.c_filter_mi_content.setFrameShape(QFrame.StyledPanel)
        self.c_filter_mi_content.setFrameShadow(QFrame.Raised)

        self.ly_filter_medical_information.addWidget(self.c_filter_mi_content)


        self.ly_filters.addLayout(self.ly_filter_medical_information)

        self.ly_filter_ai_results = QVBoxLayout()
        self.ly_filter_ai_results.setSpacing(0)
        self.ly_filter_ai_results.setObjectName(u"ly_filter_ai_results")
        self.c_filter_ai_results_header = FiltersHeader(self.c_filters_content)
        self.c_filter_ai_results_header.setObjectName(u"c_filter_ai_results_header")
        self.c_filter_ai_results_header.setFrameShape(QFrame.StyledPanel)
        self.c_filter_ai_results_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.c_filter_ai_results_header)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lb_filter_diagnostic_attributes = Label(self.c_filter_ai_results_header)
        self.lb_filter_diagnostic_attributes.setObjectName(u"lb_filter_diagnostic_attributes")
        self.lb_filter_diagnostic_attributes.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_10.addWidget(self.lb_filter_diagnostic_attributes)


        self.ly_filter_ai_results.addWidget(self.c_filter_ai_results_header)

        self.c_filter_ai_results_content = FiltersContent(self.c_filters_content)
        self.c_filter_ai_results_content.setObjectName(u"c_filter_ai_results_content")
        self.c_filter_ai_results_content.setFrameShape(QFrame.StyledPanel)
        self.c_filter_ai_results_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.c_filter_ai_results_content)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.ly_filter_ai_results_content = QVBoxLayout()
        self.ly_filter_ai_results_content.setSpacing(4)
        self.ly_filter_ai_results_content.setObjectName(u"ly_filter_ai_results_content")
        self.ly_filter_ai_results_content.setContentsMargins(9, -1, -1, -1)
        self.i_air_benign = QCheckBox(self.c_filter_ai_results_content)
        self.i_air_benign.setObjectName(u"i_air_benign")

        self.ly_filter_ai_results_content.addWidget(self.i_air_benign)

        self.i_air_malignant = QCheckBox(self.c_filter_ai_results_content)
        self.i_air_malignant.setObjectName(u"i_air_malignant")

        self.ly_filter_ai_results_content.addWidget(self.i_air_malignant)

        self.i_air_indeterminate = QCheckBox(self.c_filter_ai_results_content)
        self.i_air_indeterminate.setObjectName(u"i_air_indeterminate")

        self.ly_filter_ai_results_content.addWidget(self.i_air_indeterminate)


        self.verticalLayout_6.addLayout(self.ly_filter_ai_results_content)


        self.ly_filter_ai_results.addWidget(self.c_filter_ai_results_content)


        self.ly_filters.addLayout(self.ly_filter_ai_results)

        self.ly_filter_skin_lesion_characteristics = QVBoxLayout()
        self.ly_filter_skin_lesion_characteristics.setSpacing(0)
        self.ly_filter_skin_lesion_characteristics.setObjectName(u"ly_filter_skin_lesion_characteristics")
        self.c_filter_skl_charac_header = FiltersHeader(self.c_filters_content)
        self.c_filter_skl_charac_header.setObjectName(u"c_filter_skl_charac_header")
        self.c_filter_skl_charac_header.setFrameShape(QFrame.StyledPanel)
        self.c_filter_skl_charac_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.c_filter_skl_charac_header)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label = Label(self.c_filter_skl_charac_header)
        self.label.setObjectName(u"label")

        self.horizontalLayout_11.addWidget(self.label)


        self.ly_filter_skin_lesion_characteristics.addWidget(self.c_filter_skl_charac_header)

        self.c_filter_skl_charac_content = FilterVariableInputsContainer(self.c_filters_content)
        self.c_filter_skl_charac_content.setObjectName(u"c_filter_skl_charac_content")
        self.c_filter_skl_charac_content.setFrameShape(QFrame.StyledPanel)
        self.c_filter_skl_charac_content.setFrameShadow(QFrame.Raised)

        self.ly_filter_skin_lesion_characteristics.addWidget(self.c_filter_skl_charac_content)


        self.ly_filters.addLayout(self.ly_filter_skin_lesion_characteristics)


        self.verticalLayout_3.addLayout(self.ly_filters)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.sc_filters.setWidget(self.c_filters_content)

        self.verticalLayout_18.addWidget(self.sc_filters)


        self.ly_center.addWidget(self.c_filters)

        self.ly_right = QVBoxLayout()
        self.ly_right.setSpacing(2)
        self.ly_right.setObjectName(u"ly_right")
        self.ly_right.setContentsMargins(-1, -1, 20, 20)
        self.c_sorter = QFrame(patients)
        self.c_sorter.setObjectName(u"c_sorter")
        self.c_sorter.setMaximumSize(QSize(16777215, 100))
        self.c_sorter.setFrameShape(QFrame.StyledPanel)
        self.c_sorter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.c_sorter)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.c_search = SearchLine(self.c_sorter)
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

        self.ly_sorter_buttons = QVBoxLayout()
        self.ly_sorter_buttons.setObjectName(u"ly_sorter_buttons")
        self.lb_organizer_titles = Label(self.c_sorter)
        self.lb_organizer_titles.setObjectName(u"lb_organizer_titles")
        self.lb_organizer_titles.setMaximumSize(QSize(16777215, 20))

        self.ly_sorter_buttons.addWidget(self.lb_organizer_titles, 0, Qt.AlignHCenter)

        self.c_sorter_buttons = QFrame(self.c_sorter)
        self.c_sorter_buttons.setObjectName(u"c_sorter_buttons")
        self.c_sorter_buttons.setMaximumSize(QSize(16777215, 80))
        self.c_sorter_buttons.setFrameShape(QFrame.StyledPanel)
        self.c_sorter_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.c_sorter_buttons)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.hs_sorter_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.hs_sorter_1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.c_sorter_mosaico = QFrame(self.c_sorter_buttons)
        self.c_sorter_mosaico.setObjectName(u"c_sorter_mosaico")
        self.c_sorter_mosaico.setFrameShape(QFrame.StyledPanel)
        self.c_sorter_mosaico.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.c_sorter_mosaico)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bt_sorter_mosaico = CheckButton(self.c_sorter_mosaico)
        self.bt_sorter_mosaico.setObjectName(u"bt_sorter_mosaico")
        self.bt_sorter_mosaico.setMinimumSize(QSize(25, 25))
        self.bt_sorter_mosaico.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.bt_sorter_mosaico)

        self.bt_sorter_list = CheckButton(self.c_sorter_mosaico)
        self.bt_sorter_list.setObjectName(u"bt_sorter_list")
        self.bt_sorter_list.setMinimumSize(QSize(25, 25))
        self.bt_sorter_list.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.bt_sorter_list)


        self.horizontalLayout.addWidget(self.c_sorter_mosaico, 0, Qt.AlignHCenter)

        self.c_sorter_asc = QFrame(self.c_sorter_buttons)
        self.c_sorter_asc.setObjectName(u"c_sorter_asc")
        self.c_sorter_asc.setFrameShape(QFrame.StyledPanel)
        self.c_sorter_asc.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.c_sorter_asc)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.bt_sorter_asc = CheckButton(self.c_sorter_asc)
        self.bt_sorter_asc.setObjectName(u"bt_sorter_asc")
        self.bt_sorter_asc.setMinimumSize(QSize(40, 25))
        self.bt_sorter_asc.setMaximumSize(QSize(40, 25))

        self.horizontalLayout_5.addWidget(self.bt_sorter_asc)

        self.bt_sorter_dsc = CheckButton(self.c_sorter_asc)
        self.bt_sorter_dsc.setObjectName(u"bt_sorter_dsc")
        self.bt_sorter_dsc.setMinimumSize(QSize(40, 25))
        self.bt_sorter_dsc.setMaximumSize(QSize(40, 25))

        self.horizontalLayout_5.addWidget(self.bt_sorter_dsc)


        self.horizontalLayout.addWidget(self.c_sorter_asc, 0, Qt.AlignHCenter)

        self.c_sorter_id = QFrame(self.c_sorter_buttons)
        self.c_sorter_id.setObjectName(u"c_sorter_id")
        self.c_sorter_id.setFrameShape(QFrame.StyledPanel)
        self.c_sorter_id.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.c_sorter_id)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.bt_sorter_id = CheckButton(self.c_sorter_id)
        self.bt_sorter_id.setObjectName(u"bt_sorter_id")
        self.bt_sorter_id.setMinimumSize(QSize(40, 25))
        self.bt_sorter_id.setMaximumSize(QSize(40, 25))

        self.horizontalLayout_6.addWidget(self.bt_sorter_id)

        self.bt_sorter_name = CheckButton(self.c_sorter_id)
        self.bt_sorter_name.setObjectName(u"bt_sorter_name")
        self.bt_sorter_name.setMinimumSize(QSize(50, 25))
        self.bt_sorter_name.setMaximumSize(QSize(50, 25))

        self.horizontalLayout_6.addWidget(self.bt_sorter_name)


        self.horizontalLayout.addWidget(self.c_sorter_id, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.hs_sorter_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.hs_sorter_4)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_3.setStretch(2, 1)

        self.ly_sorter_buttons.addWidget(self.c_sorter_buttons)


        self.verticalLayout_4.addLayout(self.ly_sorter_buttons)


        self.ly_right.addWidget(self.c_sorter)

        self.c_number_of_patients = QFrame(patients)
        self.c_number_of_patients.setObjectName(u"c_number_of_patients")
        self.c_number_of_patients.setMaximumSize(QSize(16777215, 16))
        self.c_number_of_patients.setFrameShape(QFrame.StyledPanel)
        self.c_number_of_patients.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.c_number_of_patients)
        self.horizontalLayout_8.setSpacing(4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 4, 0)
        self.horizontalSpacer = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.lb_number_of_patients = Label(self.c_number_of_patients)
        self.lb_number_of_patients.setObjectName(u"lb_number_of_patients")
        self.lb_number_of_patients.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout_8.addWidget(self.lb_number_of_patients)

        self.i_number_of_patients = Label(self.c_number_of_patients)
        self.i_number_of_patients.setObjectName(u"i_number_of_patients")
        self.i_number_of_patients.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout_8.addWidget(self.i_number_of_patients)


        self.ly_right.addWidget(self.c_number_of_patients)

        self.c_pagination = Pagination(patients)
        self.c_pagination.setObjectName(u"c_pagination")
        self.c_pagination.setFrameShape(QFrame.StyledPanel)
        self.c_pagination.setFrameShadow(QFrame.Raised)

        self.ly_right.addWidget(self.c_pagination)


        self.ly_center.addLayout(self.ly_right)


        self.verticalLayout_2.addLayout(self.ly_center)


        self.retranslateUi(patients)

        QMetaObject.connectSlotsByName(patients)
    # setupUi

    def retranslateUi(self, patients):
        patients.setWindowTitle(QCoreApplication.translate("patients", u"Loggin", None))
        self.bt_back.setText(QCoreApplication.translate("patients", u"Back", None))
        self.lb_title.setText(QCoreApplication.translate("patients", u"List of patients", None))
        self.bt_add_new_patient.setText(QCoreApplication.translate("patients", u"Add new patient", None))
        self.lb_filters_title.setText(QCoreApplication.translate("patients", u"Filters", None))
        self.bt_reset_filters.setText(QCoreApplication.translate("patients", u"Reset", None))
        self.lb_filter_clinical_attributes.setText(QCoreApplication.translate("patients", u"BASIC INFORMATION", None))
        self.lb_filter_gender.setText(QCoreApplication.translate("patients", u"Gender", None))
        self.i_male.setText(QCoreApplication.translate("patients", u"Male", None))
        self.i_female.setText(QCoreApplication.translate("patients", u"Female", None))
        self.lb_filter_age.setText(QCoreApplication.translate("patients", u"Age", None))
        self.lb_filter_age_precise.setText(QCoreApplication.translate("patients", u"Precise", None))
        self.lb_age_range.setText(QCoreApplication.translate("patients", u"Range", None))
        self.bt_age_range_1.setText(QCoreApplication.translate("patients", u"0 - 20", None))
        self.bt_age_range_2.setText(QCoreApplication.translate("patients", u"20 - 50", None))
        self.bt_age_range_3.setText(QCoreApplication.translate("patients", u"50 +", None))
        self.lb_age_range_separator.setText(QCoreApplication.translate("patients", u"-", None))
        self.lb_filter_mi.setText(QCoreApplication.translate("patients", u"MEDICAL INFORMATION", None))
        self.lb_filter_diagnostic_attributes.setText(QCoreApplication.translate("patients", u"AI RESULTS", None))
        self.i_air_benign.setText(QCoreApplication.translate("patients", u"Benign", None))
        self.i_air_malignant.setText(QCoreApplication.translate("patients", u"Malignant", None))
        self.i_air_indeterminate.setText(QCoreApplication.translate("patients", u"Indeterminate", None))
        self.label.setText(QCoreApplication.translate("patients", u"SKIN LESION CHARACTERISTICS", None))
        self.bt_search.setText("")
        self.i_search.setPlaceholderText(QCoreApplication.translate("patients", u"E.g: AG4432YA", None))
        self.lb_organizer_titles.setText(QCoreApplication.translate("patients", u"Organizer", None))
        self.bt_sorter_mosaico.setText("")
        self.bt_sorter_list.setText("")
        self.bt_sorter_asc.setText(QCoreApplication.translate("patients", u"A-z", None))
        self.bt_sorter_dsc.setText(QCoreApplication.translate("patients", u"z-A", None))
        self.bt_sorter_id.setText(QCoreApplication.translate("patients", u"ID", None))
        self.bt_sorter_name.setText(QCoreApplication.translate("patients", u"Name", None))
        self.lb_number_of_patients.setText(QCoreApplication.translate("patients", u"Number of patients :", None))
        self.i_number_of_patients.setText(QCoreApplication.translate("patients", u"...", None))
    # retranslateUi

