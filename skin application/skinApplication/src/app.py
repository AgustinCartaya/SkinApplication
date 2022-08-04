from PySide6.QtWidgets import QApplication
import src.config as cfg
import src.util.util as util
from src.main_window import MainWindow
#from PySide6.QtCore  import QTextCodec

from src.db_controllers.db_controller import DBController
from src.objects.ai import AI

import src.internal.ai_loader as ai_loader
import src.internal.boot_checker as boot_checker

#--------- pre compiler delete at the end --------
from src.views.ui.styles.raw.compile_styles import *
compile_styles()
#--------- fin pre compiler --------

def first_time():
    # check the existence of the database and the existence of at least 
    # one element in the DOCTOR table 
    dbc = DBController()
    dbc.db.verify_db_existence()
    return dbc.count_all(cfg.TABLE_DOCTORS) == 0


#def load_ai():
#    ai_dict = {}
#    for ai_name in util.get_dir_list(cfg.AI_PATH):
#        try:
#            ai_dict[ai_name] = AI(ai_name)
#        except RuntimeError as rr:
#            print(ai_name + " upload aborted")
#            print(rr.args)
#    return ai_dict

def run():
    boot_checker.check()
    app = QApplication([])
#    QTextCodec.setCodecForTr(QTextCodec.codecForName("UTF-8"));

    mainWindow = MainWindow(ai_loader.load_ai())

    first_time()
    mainWindow.change_view(None, cfg.PATIENTS_VIEW, [])

#    if first_time():
#        mainWindow.change_view(None, cfg.CREATE_ACCOUNT_VIEW, [])
#    else:
#        mainWindow.change_view(None, cfg.LOGIN_VIEW, [])

    mainWindow.show()
    app.exec()


