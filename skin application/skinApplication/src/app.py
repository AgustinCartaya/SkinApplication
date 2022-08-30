from PySide6.QtWidgets import QApplication
import src.config as cfg
from src.main_window import MainWindow

from src.db_controllers.db_controller import DBController

import src.internal.ai_loader as ai_loader
import src.internal.boot_checker as boot_checker

#--------- pre compiler delete at the end --------
import src.views.ui.styles.raw.compile_styles as styles_compyler
styles_compyler.compile_styles()
#--------- fin pre compiler --------

GLOBAL = {}
def first_time():
    # check the existence of the database and the existence of at least 
    # one element in the DOCTOR table 
    dbc = DBController()
    dbc.db.verify_db_existence()
    return dbc.count_all(cfg.TABLE_DOCTORS) == 0

def run():
    boot_checker.check()
    app = QApplication()
#    QTextCodec.setCodecForTr(QTextCodec.codecForName("UTF-8"));

    ai_dict = ai_loader.load_ai()
    GLOBAL["ai_dict"] = ai_dict
    mainWindow = MainWindow(GLOBAL)

#    mainWindow.change_view(None, cfg.PATIENTS_VIEW, [])

    if first_time():
        mainWindow.change_view(None, cfg.CREATE_ACCOUNT_VIEW, [])
    else:
        mainWindow.change_view(None, cfg.LOGIN_VIEW, [])

    mainWindow.show()
    app.exec()


