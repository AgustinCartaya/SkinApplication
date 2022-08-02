from PySide6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout,
        QLineEdit, QGridLayout, QSpacerItem, QSizePolicy)

#from PySide6.QtWidgets import QApplication

from PySide6.QtCore import QCoreApplication, Qt, QSize

from .button import Button
from .label import Label
from .line_edit import LineEdit

import src.util.data_cleaner as data_cleaner

class Pagination(QFrame):

    def __init__(self, parent, min=(3,4), max=(4,5), min_sep = 5, min_element_size = (50,50), forced_empty_spaces = False):
        QFrame.__init__(self, parent)

        # No usado por el momento
        self.min_rows = min[0]
        self.min_cols = min[1]

        self.max_rows = max[0]
        self.max_cols = max[1]

        self.nb_rows = self.min_rows
        self.nb_cols = self.min_cols

        self.min_sep = min_sep

        self.min_card_width = min_element_size[0]
        self.min_card_height = min_element_size[1]

        self.forced_empty_spaces = forced_empty_spaces
        # fin no usado

        self.nb_cards = 0
        self.pointer = 0
        self.nb_max_pages = 0

        self.__create()

#        cards = []
#        for i in range(25):
#            cards.append("C"+str(i))
#        self.add_cards(cards)

    def __create(self):
        self.__crete_cards_container()
        self.__create_controls()

        layout = QVBoxLayout(self)
        layout.addWidget(self.c_cards)
        layout.addWidget(self.c_controllers, 0, Qt.AlignHCenter)

    def __crete_cards_container(self):
        self.c_cards = QFrame(self)
        self.c_cards_layout = QGridLayout(self.c_cards)

    def __create_controls(self):
        self.c_controllers = QFrame(self)
        self.c_controllers.setMaximumSize(QSize(16777215, 35))
#        self.c_controllers.setFrameShape(QFrame.StyledPanel)
#        self.c_controllers.setFrameShadow(QFrame.Raised)

        self.c_controllers_layout = QHBoxLayout(self.c_controllers)
        self.c_controllers_layout.setContentsMargins(-1, 0, -1, 0)

        self.bt_back_page = Button(self.c_controllers)
        self.bt_back_page.setMinimumSize(QSize(28, 28))
        self.bt_back_page.setMaximumSize(QSize(28, 28))
        self.bt_back_page.set_icon(Button.IC_LEFT)
        self.c_controllers_layout.addWidget(self.bt_back_page)
        self.bt_back_page.clicked.connect(self.back_page)

        self.i_actual_page = LineEdit(self.c_controllers)
        self.i_actual_page.setMaximumSize(QSize(40, 16777215))
        self.c_controllers_layout.addWidget(self.i_actual_page)
        self.i_actual_page.returnPressed.connect(self.change_page_manually)
        self.i_actual_page.setValidator(data_cleaner.create_text_validator(data_cleaner.regex_not_null_4_number))

        self.lb_number_of_pages = Label(self.c_controllers)
        self.lb_number_of_pages.setText(QCoreApplication.translate("pagination", u"of ...", None))
        self.c_controllers_layout.addWidget(self.lb_number_of_pages)

        self.bt_next_page = Button(self.c_controllers)
        self.bt_next_page.setMinimumSize(QSize(28, 28))
        self.bt_next_page.setMaximumSize(QSize(28, 28))
        self.bt_next_page.set_icon(Button.IC_RIGHT)
        self.c_controllers_layout.addWidget(self.bt_next_page)
        self.bt_next_page.clicked.connect(self.next_page)

    def add_cards(self, cards):
        self.cards = cards
        self.nb_cards = len(cards)
        if self.nb_cards == 0:
            self.nb_max_pages = 1
        else :
            self.nb_max_pages = (self.nb_cards-1)//(self.nb_rows * self.nb_cols) + 1

        self.lb_number_of_pages.setText(QCoreApplication.translate("pagination", u"of " + str(self.nb_max_pages), None))
        self.go_to_page(self.pointer + 1)

    def __paint_cards(self):

        for i in reversed(range(self.c_cards_layout.count())):
            self.c_cards_layout.itemAt(i).widget().setParent(None)

        index_card = self.pointer * self.nb_rows * self.nb_cols

#        i = 0
#        j = 0
#        while (i < self.nb_rows and index_card < self.nb_cards):
#            while (j < self.nb_cols and index_card < self.nb_cards):
##                bt = CardButton(self.c_cards)
##                text = self.cards[index_card]
##                if len(text) > 10:
##                    bt.setText(text[:10] + "...")
##                else:
##                    bt.setText(text)
##                bt.setMinimumSize(QSize(100, 100))
##               pushButton.setMaximumSize(QSize(150, 150))

#                self.c_cards_layout.addWidget(self.cards[index_card], i, j, 1, 1)

#                j = j+1
#                index_card = index_card+1
#            j = 0
#            i = i+1

        for i in range(self.nb_rows):
            for j in range(self.nb_cols):
                if index_card < self.nb_cards:
                    self.c_cards_layout.addWidget(self.cards[index_card], i, j, 1, 1)
                    index_card = index_card+1
                else:

                    if self.forced_empty_spaces:
                        fr = QFrame(self)
                        ly = QHBoxLayout(fr)
                        spacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Expanding)
                        ly.addItem(spacer)
                        self.c_cards_layout.addWidget(fr, i, j, 1, 1)

                    else:
                        self.c_cards_layout.addWidget(Label(self), i, j, 1, 1)


        self.i_actual_page.setText(str(self.pointer+1))
        self.c_cards_layout.update()

    def next_page(self):
        self.go_to_page(self.pointer + 2)

    def back_page(self):
        self.go_to_page(self.pointer)

    def change_page_manually(self):
        self.go_to_page(int(self.i_actual_page.text()))

    def go_to_page(self, page):
        if page <= 0:
            page = 1
        elif page > self.nb_max_pages:
            page = self.nb_max_pages
        self.pointer = page - 1
        self.__paint_cards()

