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

    mySignam = Signal(str,str,str)
    def connect_ui_signals(self):
        #ui signals
        self.ui.bt_create.clicked.connect(self.create_account)
        # created signals
        self.mySignam.connect(self.MW.change_view)

    # connecting click to the main window
    def create_account(self):
        try:  
            doctor = Doctor(self.ui.i_first_name.text(),
                self.ui.i_last_name.text(),
                self.ui.i_password.text(),
                self.ui.i_email.text())
            doctor.save_data()
            self.mySignam.emit(cfg.CREATE_ACCOUNT_VIEW, cfg.PATIENTS_VIEW, None)
        except ValueError as err:
            print(err.args)

    def fill_default_test(self):
        self.ui.i_first_name.setText('Agustin')
        self.ui.i_last_name.setText('Cartaya')
        self.ui.i_password.setText('Ag.1')
        self.ui.i_email.setText('ag@gmail.com')

#    def load_ui(self):
#        loader = QUiLoader()
#        ui_path = os.fspath(Path(__file__).resolve().parent / "ui/create_account.ui")
#        ui_file = QFile(ui_path)
#        ui_file.open(QFile.ReadOnly)
#        loader.load(ui_file, self)
#        ui_file.close()
