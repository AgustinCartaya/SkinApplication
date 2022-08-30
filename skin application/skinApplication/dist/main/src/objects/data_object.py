from datetime import datetime, timedelta

from src.db_controllers.db_controller import DBController
import src.util.data_cleaner as dc
import src.config as cfg
import src.internal.errors as err
import src.util.util as util
import json

from abc import ABC, abstractmethod

class DataObject:

    VAR_PASSWORD = "PASSWORD"
    VAR_EMAIL = "EMAIL"
    VAR_NAME = "NAME"

    @abstractmethod
    def initialize(self, *args):
        pass

    @abstractmethod
    def save_data(self):
        pass

    @abstractmethod
    def verify_data(self):
        pass

    @classmethod
    def _verify(cls, var, var_type, error_object, verify_empty = True):
        if verify_empty and len(var) == 0:
            raise ValueError(error_object, err.ET_EMPTY)

        var_type = var_type.upper()

        if var_type == cls.VAR_NAME:
            var = dc.normalize_name(var)
            if not dc.is_name(var):
                raise ValueError(error_object, err.ET_NOT_VALID)

        elif var_type == cls.VAR_EMAIL:
            var = dc.normalize_email(var)
            if not dc.is_email(var):
                raise ValueError(error_object, err.ET_NOT_VALID)

        elif var_type == cls.VAR_PASSWORD:
            var = dc.normalize_password(var)
            if not dc.is_password(var):
                raise ValueError(error_object, err.ET_NOT_VALID)

        return True
