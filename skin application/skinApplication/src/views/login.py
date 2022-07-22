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

        
    s_change_view = Signal(str,str,str)
    def connect_ui_signals(self):
        #ui signals
        self.ui.bt_login.clicked.connect(self.login)
        self.ui.i_password.returnPressed.connect(self.ui.bt_login.click)

        # created signals
        self.s_change_view.connect(self.MW.change_view)

    def charge_doctors_name(self):
        dc = Doctor()
        names = dc.obtain_doctors_name()
        self.ui.i_name.setText(names[0][0])

    # connecting click to the main window
    def login(self):
        dc = Doctor()
        try:
            dc.get_doctor_by_last_name_and_password(self.ui.i_name.text(),self.ui.i_password.text())
            self.s_change_view.emit(cfg.LOGIN_VIEW, cfg.PATIENTS_VIEW, None)
        except ValueError as err:
            print(err.args)





