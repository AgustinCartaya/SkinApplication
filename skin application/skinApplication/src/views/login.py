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
        
    mySignam = Signal(str,str,str)
    def connect_ui_signals(self):
        #ui signals
        self.ui.bt_login.clicked.connect(self.login)
        # created signals
        self.mySignam.connect(self.MW.change_view)

    def charge_doctors_name(self):
        dc = Doctor()
        names = dc.obtain_doctors_name()
        self.ui.i_name.setText(names[0][0])

    # connecting click to the main window
    def login(self):
        dc = Doctor()
        dc.get_doctor_by_last_name_and_password(self.ui.i_name.text(),self.ui.i_password.text())
        print(dc.email)
        # self.mySignam.emit(cfg.LOGIN_VIEW, cfg.PATIENTS_VIEW, None)

