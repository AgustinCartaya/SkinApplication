# @autor: Agustin CARTAYA

from PySide6.QtWidgets import QApplication
import src.internal.ai_loader as ai_loader
import src.internal.boot_checker as boot_checker
from src.db_controllers.db_controller import DBController
import src.config as cfg
from src.main_window import MainWindow

# --------- styles precompilation --------
# used for precompiling colors
import src.views.ui.styles.raw.compile_styles as styles_compyler
styles_compyler.compile_styles()
# --------- fin pre compiler --------

# global variable
# should be disponible in all the views
# contains the actual doctor and the ai
GLOBAL = {}


# check the existence of at least one doctor.
# used to show the creating_account_view
# the first time the application is opened
def first_time():

    dbc = DBController()
    return dbc.count_all(cfg.TABLE_DOCTORS) == 0


# start of the application
def run():
    # checking all the necessary directories and the data base
    boot_checker.check()

    # creating the application
    app = QApplication()

    # to accept UTF-8 encoding
#    QTextCodec.setCodecForTr(QTextCodec.codecForName("UTF-8"));

    # loading the AI
    ai_dict = ai_loader.load_ai()
    GLOBAL["ai_dict"] = ai_dict

    # creating the main window
    mainWindow = MainWindow(GLOBAL)

    # used during the development to enter directly into the patient view
#    mainWindow.change_view(None, cfg.PATIENTS_VIEW, [])

    # showing the first view
    # If there is no doctor in the database
    # the doctor creation view will be shown
    if first_time():
        mainWindow.change_view(None, cfg.CREATE_ACCOUNT_VIEW, [])
    else:
        mainWindow.change_view(None, cfg.LOGIN_VIEW, [])

    # showing the main windwow
    mainWindow.show()
    app.exec()


