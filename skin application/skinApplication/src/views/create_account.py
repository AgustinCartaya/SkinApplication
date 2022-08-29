from .view_object import *
from .ui.ui_create_account import Ui_create_account

from src.objects.doctor import Doctor

class CreateAccountView(ViewObject):    

    def __init__(self, mw):
        super().__init__(mw)
        self.load_ui()
        self.connect_ui_signals()

        #test
        self.fill_default_test()

    def load_ui(self):
        self.ui = Ui_create_account()
        self.ui.setupUi(self)

        self.ui.i_first_name.setValidator(self.create_text_validator(data_cleaner.regex_name))
        self.ui.i_last_name.setValidator(self.create_text_validator(data_cleaner.regex_name))
        self.ui.i_email.setValidator(self.create_text_validator(data_cleaner.regex_email))

        # labels
        self.ui.lb_title.set_title(1)


    def connect_ui_signals(self):
        #ui signals
        self.ui.bt_create.clicked.connect(self.create_account)

    # connecting click to the main window
    def create_account(self):
        self.reset_inputs_decorators()
        try:  
            # repeat password does not match
            if self.ui.i_password.text() != self.ui.i_repeat_password.text():
                raise ValueError(err.EO_DOCTOR_REPEAT_PASSWORD, err.ET_NOT_MATCH)

            doctor = Doctor(self.ui.i_first_name.text(),
                self.ui.i_last_name.text(),
                self.ui.i_password.text(),
                self.ui.i_email.text())
            doctor.create()
            self.s_change_view.emit(cfg.CREATE_ACCOUNT_VIEW, cfg.PATIENTS_VIEW, None)

        except ValueError as ve:
            err_msg = "ERROR"

            if ve.args[0] == err.EO_DOCTOR_FIRST_NAME:
                self.ui.i_first_name.set_decorator("error")
                err_msg = "Invalid first name"

            elif ve.args[0] == err.EO_DOCTOR_LAST_NAME:
                self.ui.i_last_name.set_decorator("error")
                err_msg = "Invalid last name"

            elif ve.args[0] == err.EO_DOCTOR_PASSWORD:
                self.ui.i_password.set_decorator("error")
                if ve.args[1] == err.ET_EMPTY:
                    err_msg = "Please fill the password"
                if ve.args[1] == err.ET_NOT_VALID:
                    # password should have at least:
                        # 1 lower case letter
                        # 1 upper case letter
                        # 1 digit
                        # 1 of the following special characters (@ $ _ .)
                    err_msg = "Invalid password"

            elif ve.args[0] == err.EO_DOCTOR_REPEAT_PASSWORD:
                self.ui.i_repeat_password.set_decorator("error")
                if ve.args[1] == err.ET_NOT_MATCH:
                    err_msg = "Repeat password does not match"

            elif ve.args[0] == err.EO_DOCTOR_EMAIL:
                self.ui.i_email.set_decorator("error")
                if ve.args[1] == err.ET_EMPTY:
                    err_msg = "Please fill the email"
                if ve.args[1] == err.ET_NOT_VALID:
                    err_msg = "Invalid email"

            self.show_message(err_msg, cfg.MSG_ERROR)
            print(ve.args)

    def reset_inputs_decorators(self):
        self.ui.i_first_name.set_decorator(None)
        self.ui.i_last_name.set_decorator(None)
        self.ui.i_password.set_decorator(None)
        self.ui.i_repeat_password.set_decorator(None)
        self.ui.i_email.set_decorator(None)


    def fill_default_test(self):
        self.ui.i_first_name.setText('Agustin')
        self.ui.i_last_name.setText('Cartaya')
        self.ui.i_password.setText('Ag.1')
        self.ui.i_email.setText('ag@gmail.com')


