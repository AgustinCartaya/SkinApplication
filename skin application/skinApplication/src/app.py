from PySide6.QtWidgets import QApplication
import src.config as cfg
from src.main_window import MainWindow

from src.db_controllers.db_controller import DBController

def first_time():
    # check the existence of the database and the existence of at least 
    # one element in the DOCTOR table 
    dbc = DBController()
    dbc.db.verify_db_existence()
    return dbc.count_all(cfg.TABLE_DOCTORS) == 0

def run():
    app = QApplication([])

    mainWindow = MainWindow()
    # mainWindow.change_view(None, cfg.ADD_PATIENT_VIEW, [])
    # first_time()
    if first_time():
        mainWindow.change_view(None, cfg.CREATE_ACCOUNT_VIEW, [])
    else:
        mainWindow.change_view(None, cfg.LOGIN_VIEW, [])

    mainWindow.show()
    app.exec()


