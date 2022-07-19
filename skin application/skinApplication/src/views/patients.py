import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class Patients(QWidget):
    def __init__(self, mw):
        super(Patients, self).__init__()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()

        ui_path = os.fspath(Path(__file__).resolve().parent / "ui/patients.ui")
        ui_file = QFile(ui_path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

