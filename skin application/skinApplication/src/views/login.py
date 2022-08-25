from .view_object import *
from .ui.ui_login import Ui_login

from src.objects.doctor import Doctor

class LoginView(ViewObject):
    def __init__(self,mw):
        super().__init__(mw)
        self.load_ui()
        self.connect_ui_signals()
        self.charge_doctors_name()


    def load_ui(self):
        self.ui = Ui_login()
        self.ui.setupUi(self)

        self.ui.i_password.setFocus()

        # labels
        self.ui.lb_title.set_title(1)

        # create other account
        self.ui.bt_create_account.hide()

    def connect_ui_signals(self):
        #ui signals
        self.ui.bt_login.clicked.connect(self.login)
        self.ui.i_password.returnPressed.connect(self.ui.bt_login.click)

        self.ui.bt_create_account.clicked.connect(self.create_account)

    def charge_doctors_name(self):
        dc = Doctor()
        names = dc.obtain_doctors_name()
        self.ui.i_name.addItems(names)

    @Slot()
    def login(self):
        try:
            doctor = Doctor.get_doctor(self.ui.i_name.currentText(),self.ui.i_password.text())
            self.GLOBAL["doctor"] = doctor
            self.s_change_view.emit(cfg.LOGIN_VIEW, cfg.PATIENTS_VIEW, None)
        except ValueError as err:
            self.show_message(err.args[0], cfg.MSG_ERROR)
            print(err.args)


    @Slot()
    def create_account(self):
        self.s_change_view.emit(cfg.LOGIN_VIEW, cfg.CREATE_ACCOUNT_VIEW, None)
