from datetime import datetime

from src.db_controllers.db_controller import DBController
import src.util.data_cleaner as dc
import src.config as cfg
import src.util.util as util

from abc import ABC, abstractmethod

class DataObject:

    @abstractmethod
    def initialize(self, *args):
        pass

    @abstractmethod
    def save_data(self):
        pass

    @abstractmethod
    def verify_data(self):
        pass

    def _verify(self, var, var_type, error_var_name, verify_empty = True):
        if verify_empty and len(var) == 0:
            raise ValueError('Data Object verification error', error_var_name, "EMPTY")

        var_type = var_type.upper()

        if var_type == "NAME":
            var = dc.normalize_name(var)
            if not dc.is_name(var):
                raise ValueError('Data Object verification error', error_var_name, "NOT_VALID")

        elif var_type == "EMAIL":
            var = dc.normalize_email(var)
            if not dc.is_email(var):
                raise ValueError('Data Object verification error', error_var_name, "NOT_VALID")

        elif var_type == "PASSWORD":
            var = dc.normalize_password(var)
            if not dc.is_password(var):
                raise ValueError('Data Object verification error', error_var_name, "NOT_VALID")

        return True
