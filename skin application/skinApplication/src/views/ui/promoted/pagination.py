from PySide6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout,
        QLineEdit,QGridLayout, QLabel)

#from PySide6.QtWidgets import QApplication

from PySide6.QtCore import QCoreApplication, Qt, QSize

from .button import Button
from .card_button import CardButton
from .line_edit import LineEdit

class Pagination(QFrame):

    def __init__(self, *args, **kwards):
        QFrame.__init__(self, *args, **kwards)

        # No usado por el momento
        self.min_rows = 3
        self.min_cols = 4

        self.max_rows = 4
        self.max_cols = 5

        self.nb_rows = self.min_rows
        self.nb_cols = self.min_cols

        self.min_sep = 5

        self.min_card_width = 50
        self.min_card_height = 50
        # fin no usado

        self.nb_cards = 0
        self.pointer = 0
        self.nb_max_pages = 0

        self.__create()

        cards = []
        for i in range(25):
            cards.append("C"+str(i))
        self.add_cards(cards)

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
        self.i_actual_page.textChanged.connect(self.change_manual_page)

        self.lb_number_of_pages = QLabel(self.c_controllers)
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
        self.nb_max_pages = (self.nb_cards-1)//(self.nb_rows * self.nb_cols) + 1
        self.lb_number_of_pages.setText(QCoreApplication.translate("pagination", u"of " + str(self.nb_max_pages), None))
        self.__paint_cards()

    def __paint_cards(self):

        for i in reversed(range(self.c_cards_layout.count())):
            self.c_cards_layout.itemAt(i).widget().setParent(None)

        index_card = self.pointer * self.nb_rows * self.nb_cols
        i = 0
        j = 0

        while i < self.nb_rows and index_card < self.nb_cards:
            while j < self.nb_cols and index_card < self.nb_cards:
                bt = CardButton(self.c_cards)
                text = self.cards[index_card]
                if len(text) > 10:
                    bt.setText(text[:10] + "...")
                else:
                    bt.setText(text)
                bt.setMinimumSize(QSize(100, 100))
#               pushButton.setMaximumSize(QSize(150, 150))

                self.c_cards_layout.addWidget(bt, i, j, 1, 1)

                j = j+1
                index_card = index_card+1
            j = 0
            i = i+1
        self.i_actual_page.setText(str(self.pointer+1))
        self.c_cards_layout.update()


    def next_page(self):
        if (self.pointer + 1)  < self.nb_max_pages:
            self.pointer = self.pointer + 1
        self.__paint_cards()

    def back_page(self):
        if (self.pointer - 1)  >= 0:
            self.pointer = self.pointer - 1
        self.__paint_cards()

    def change_manual_page(self):
        if int(self.i_actual_page.text()) <= 0:
            self.i_actual_page.setText("1")
        elif int(self.i_actual_page.text()) > self.nb_max_pages:
            self.i_actual_page.setText(str(self.nb_max_pages))
        else:
            self.pointer = int(self.i_actual_page.text()) - 1
            self.__paint_cards()

