from .promoted_container import *

class Pagination(PromotedContainer):

    s_card_size_changed = Signal(int, int)
    def __init__(self, parent, min=(1,1), max=(10,10), sep = (6,6), min_element_size = (50,50)):
        super().__init__(parent)

        self.min_rows = min[0]
        self.min_cols = min[1]

        self.max_rows = max[0]
        self.max_cols = max[1]

        self.nb_rows = self.min_rows
        self.nb_cols = self.min_cols

        self.v_sep = sep[0]
        self.h_sep = sep[1]

        self.min_card_width = min_element_size[0]
        self.min_card_height = min_element_size[1]

        self.nb_cards = 0
        self.pointer = 0
        self.nb_max_pages = 0

        self._pre_charge()

    def initialize(self):
        pass

    def _pre_charge(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.__crete_cards_container()
        self.__create_controllers()

    def __crete_cards_container(self):
        self.c_cards = QFrame(self)
        self.ly_cards = QGridLayout(self.c_cards)
        self.ly_cards.setContentsMargins(0, 0, 0, 0)
        self.ly_cards.setHorizontalSpacing(self.h_sep)
        self.ly_cards.setVerticalSpacing(self.v_sep)

        self.layout.addWidget(self.c_cards)

    def __create_controllers(self):
        self.c_controllers = QFrame(self)
        self.c_controllers.setMaximumSize(QSize(16777215, 35))

        self.ly_controllers = QHBoxLayout(self.c_controllers)
        self.ly_controllers.setContentsMargins(0, 0, 0, 0)

#        self.ly_controllers.addWidget(Label(self.c_controllers))
        self.label_3 = Label(self.c_controllers)
        self.ly_controllers.addWidget(self.label_3)

        self.__create_pagination_controllers()
        self.__create_size_controllers()

        self.ly_controllers.setStretch(0, 1)
        self.ly_controllers.setStretch(1, 1)
        self.ly_controllers.setStretch(2, 1)

        self.layout.addWidget(self.c_controllers)

    def __create_pagination_controllers(self):

        self.c_pagination_controllers = QFrame(self.c_controllers)

        self.ly_pagination_controllers = QHBoxLayout(self.c_pagination_controllers)
        self.ly_pagination_controllers.setContentsMargins(0, 0, 0, 0)

        self.bt_back_page = Button(self.c_pagination_controllers)
        self.bt_back_page.setMinimumSize(QSize(28, 28))
        self.bt_back_page.setMaximumSize(QSize(28, 28))
        self.bt_back_page.setText("<")
#        self.bt_back_page.set_icon(Button.IC_LEFT)
        self.ly_pagination_controllers.addWidget(self.bt_back_page)
        self.bt_back_page.clicked.connect(self.back_page)

        self.i_actual_page = LineEdit(self.c_pagination_controllers)
        self.i_actual_page.setMaximumSize(QSize(40, 16777215))
        self.i_actual_page.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ly_pagination_controllers.addWidget(self.i_actual_page)
        self.i_actual_page.returnPressed.connect(self.__change_page_manually)
        self.i_actual_page.setValidator(data_cleaner.create_text_validator(data_cleaner.regex_not_null_4_number))

        lb_of = Label(self.c_pagination_controllers)
        lb_of.setText("of")
        self.ly_pagination_controllers.addWidget(lb_of)

        self.lb_number_of_pages = Label(self.c_pagination_controllers)
#        self.lb_number_of_pages.setText("Of ...")
        self.ly_pagination_controllers.addWidget(self.lb_number_of_pages)

        self.bt_next_page = Button(self.c_pagination_controllers)
        self.bt_next_page.setMinimumSize(QSize(28, 28))
        self.bt_next_page.setMaximumSize(QSize(28, 28))
        self.bt_next_page.setText(">")

        self.ly_pagination_controllers.addWidget(self.bt_next_page)
        self.bt_next_page.clicked.connect(self.next_page)

        self.ly_controllers.addWidget(self.c_pagination_controllers, 0, Qt.AlignHCenter)

    def __create_size_controllers(self):
        self.c_size_controllers = QFrame(self.c_controllers)

        self.ly_size_controllers = QHBoxLayout(self.c_size_controllers)
        self.ly_size_controllers.setContentsMargins(0, 0, 0, 0)

        self.i_nb_rows = LineEdit(self.c_size_controllers)
        self.i_nb_rows.setMaximumSize(QSize(40, 16777215))
        self.i_nb_rows.setText(str(self.nb_rows))
        self.i_nb_rows.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ly_size_controllers.addWidget(self.i_nb_rows)
        self.i_nb_rows.returnPressed.connect(self.__change_size)
        self.i_nb_rows.setValidator(data_cleaner.create_text_validator(data_cleaner.regex_not_null_4_number))

        self.lb_x_size = Label(self.c_size_controllers)
        self.lb_x_size.setText("x")
        self.ly_size_controllers.addWidget(self.lb_x_size)

        self.i_nb_cols = LineEdit(self.c_size_controllers)
        self.i_nb_cols.setMaximumSize(QSize(40, 16777215))
        self.i_nb_cols.setText(str(self.nb_cols))
        self.ly_size_controllers.addWidget(self.i_nb_cols)
        self.i_nb_cols.returnPressed.connect(self.__change_size)
        self.i_nb_cols.setValidator(data_cleaner.create_text_validator(data_cleaner.regex_not_null_4_number))

        self.ly_controllers.addWidget(self.c_size_controllers, 0, Qt.AlignRight)

    def __refresh_controllers(self):
        if self.nb_cards == 0:
            self.nb_max_pages = 1
        else :
            self.nb_max_pages = (self.nb_cards-1)//(self.nb_rows * self.nb_cols) + 1

        if self.nb_max_pages == 1:
            self.c_pagination_controllers.hide()
        else:
            self.c_pagination_controllers.show()

        self.lb_number_of_pages.setText(self.nb_max_pages)
        self.i_nb_rows.setText(str(self.nb_rows))
        self.i_nb_cols.setText(str(self.nb_cols))

    def __paint_cards(self):
        for i in reversed(range(self.ly_cards.count())):
            self.ly_cards.itemAt(i).widget().setParent(None)

        index_card = self.pointer * self.nb_rows * self.nb_cols

        for i in range(self.nb_rows):
            for j in range(self.nb_cols):
                if index_card < self.nb_cards:
                    self.ly_cards.addWidget(self.cards[index_card], i, j, 1, 1)
                    index_card = index_card+1
                else:
                    self.ly_cards.addWidget(Label(self), i, j, 1, 1)

        self.i_actual_page.setText(str(self.pointer+1))
        self.c_cards.update()
        self.__calc_elem_size()

    def __calc_elem_size(self):
        w = int((self.c_cards.size().width() - self.v_sep * (self.nb_cols - 1))/self.nb_cols)
        h = int((self.c_cards.size().height() - self.h_sep * (self.nb_rows - 1))/self.nb_rows)

        if w > 0 and h > 0:
            for i in reversed(range(self.ly_cards.count())):
                self.ly_cards.itemAt(i).widget().resize(QSize(w,h))

        self.s_card_size_changed.emit(w,h)

    @Slot()
    def __change_page_manually(self):
        self.go_to_page(int(self.i_actual_page.text()))

    @Slot()
    def __change_size(self):
        self.nb_rows = util.get_in_range_value(int(self.i_nb_rows.text()), self.min_rows, self.max_rows)
        self.nb_cols = util.get_in_range_value(int(self.i_nb_cols.text()), self.min_cols, self.max_cols)

        self.__refresh_controllers()
        self.go_to_page(1)

    @Slot()
    def next_page(self):
        self.go_to_page(self.pointer + 2)

    @Slot()
    def back_page(self):
        self.go_to_page(self.pointer)

    def go_to_page(self, page):
        if page <= 0:
            page = 1
        elif page > self.nb_max_pages:
            page = self.nb_max_pages
        self.pointer = page - 1
        self.__paint_cards()

    def set_cards_sep(self, v_sep, h_sep):
        self.v_sep = v_sep
        self.h_sep = h_sep
        self.ly_cards.setHorizontalSpacing(self.h_sep)
        self.ly_cards.setVerticalSpacing(self.v_sep)
        self.__calc_elem_size()

    def set_grid_cards_size(self, nb_rows, nb_cols):
        self.nb_rows = util.get_in_range_value(int(nb_rows), self.min_rows, self.max_rows)
        self.nb_cols = util.get_in_range_value(int(nb_cols), self.min_cols, self.max_cols)

        self.__refresh_controllers()
        self.go_to_page(1)

    def add_cards(self, cards):
        self.cards = cards
        self.nb_cards = len(cards)

        self.__refresh_controllers()
        self.go_to_page(self.pointer + 1)

    def hide_size_controllers(self, hide=True):
        if hide == True:
            self.c_size_controllers.hide()
        else:
            self.c_size_controllers.show()

    def add_card_size_changed_receaver(self, receaver):
        self.s_card_size_changed.connect(receaver)

    def resizeEvent(self, event):
        self.__calc_elem_size()
