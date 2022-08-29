# This Python file uses the following encoding: utf-8
from .data_object import *

class VariableInput(DataObject):

    scales={
    "length":[["um","mm","cm","dm","m","Dm","Hm","Km"],[1,1000,10000,100000,1000000,10000000,100000000,1000000000]],
    "time":[["seconds","minutes","hours"],[1,60,3600]],
    "volume":[["mm3","cm3","dm3","m3"],[1,1000,1000000,1000000000]],
    "weight":[["mg","cg","dg","g","Dg","Hg","Kg"],[1,10,100,1000,10000,100000,1000000]]
    }

    VIRTUAL_INPUT = "VIRTUAL_INPUT"
    MI_INPUT = "MI_INPUT"
    SKL_INPUT = "SKL_INPUT"

    TYPE_OPTIONS = "options"
    TYPE_INT = "int"
    TYPE_FLOAT = "float"
    TYPE_TEXT = "text"
    TYPE_BOOL = "bool"
    TYPE_DATE = "date"

    OWNER_AI = "ai"
    OWNER_DOCTOR = "doctor"
    OWNER_VIRTUAL = "virtual"

    BOOL_YES = "Yes"
    BOOL_NO = "No"

    def __init__(self, id, family, owner, input_type, name, items=None, scale=None):
        self.id = id
        self.family = family
        self.owner = owner
        self.type = input_type
        self.name = name

        if input_type == self.TYPE_BOOL:
            items = [self.BOOL_YES, self.BOOL_NO]
        else:
            if items is not None and type(items) == str:
                self.items = items.split(",")
            else:
                self.items = items
        self.scale = scale

        # for virtual inputs type options
        self.action_values = self.items

    def __save_data(self):
        try:
            dbc = DBController()
            items = self.items
            if items is not None:
                items = ",".join(items)

            dbc.insert(cfg.TABLE_VARIABLE_INPUTS, (
                                                    self.id,
                                                    self.family,
                                                    self.owner,
                                                    self.type,
                                                    self.name,
                                                    items,
                                                    self.scale))
        except ValueError as err:
            print(err.args)

    # update
    def update(self):
        try:
            dbc = DBController()
            items = self.items
            if items is not None:
                items = ",".join(items)
            dbc.update(cfg.TABLE_VARIABLE_INPUTS, (self.name, self.type, items, self.scale), (self.id, self.family))
        except ValueError as err:
            print(err.args)

    # update
    def delete(self):
        try:
            dbc = DBController()
            dbc.delete(cfg.TABLE_VARIABLE_INPUTS,(self.id, self.family))
        except ValueError as err:
            print(err.args)

    # creation
    def create(self):
        if self.id is None:
            self.id = self.generate_id()
        self.__save_data()
        return self.id

    def generate_id(self):
        vi_number = self.count_available_variable_inputs(self.family, self.OWNER_DOCTOR)
        return self.family + "_" + str(vi_number)

    def set_items(self, items, action_values=None):
        if self.type == self.TYPE_OPTIONS:
            self.items = items
            if action_values is not None and len(items) == len(action_values):
                self.action_values = action_values

    def get_scale_units(self):
        if self.has_scale():
            return self.scales[self.scale][0]

    def get_scalized_str(self, value):
        if self.has_scale():
            scalized = self.to_sub_unit(self.scale, value)
            return " ".join([str(scalized[0]), scalized[1]])
        else:
            return str(value)


    def accept_range(self):
        return (self.is_numeric() or self.type == self.TYPE_DATE)

    def is_numeric(self):
        return self.type in (self.TYPE_INT, self.TYPE_FLOAT)

    def has_scale(self):
        return self.scale is not None

    def is_editable(self):
        return self.owner != self.OWNER_AI

    # class methods
    @classmethod
    def count_available_variable_inputs(cls, family, owner):
        dbc = DBController()
        return dbc.count_all(cfg.TABLE_VARIABLE_INPUTS, (family,owner))

    @classmethod
    def get_variable_input(cls, id, family):
        dbc = DBController()
        vi = dbc.secure_select(cfg.TABLE_VARIABLE_INPUTS, (id,), False)
        return VariableInput(vi[0], vi[1], vi[2], vi[3], vi[4], vi[5], vi[6])

    @classmethod
    def get_available_variable_inputs(cls, family, owner=None):
        dbc = DBController()
        if owner is None:
            conditions = (family,)
        else:
            conditions = (family,owner)

        vi_list = []
        for vi in dbc.secure_select(cfg.TABLE_VARIABLE_INPUTS, conditions):
            vi_list.append(VariableInput(vi[0], vi[1], vi[2], vi[3], vi[4], vi[5], vi[6]))

        return vi_list

    @classmethod
    def get_available_variable_input_names(cls, family, owner=None):
        return [vi.name for vi in cls.get_available_variable_inputs(family, owner)]


    # ai creation
    @classmethod
    def get_accepted_types(cls):
        return [cls.TYPE_OPTIONS, cls.TYPE_INT,
                cls.TYPE_FLOAT, cls.TYPE_TEXT,
                cls.TYPE_BOOL, cls.TYPE_DATE]

    @classmethod
    def numeric_input(cls):
        return (cls.TYPE_FLOAT, cls.TYPE_INT)

    @classmethod
    def create_ai_variable_input(cls, data, family, ai_name, file_name):
        if "id" not in data:
            raise ValueError("%s WITHOUT ID (AI: %s FILE: %s)" % (family,ai_name,file_name) )

        if "name" not in data:
            raise ValueError("%s WITHOUT NAME (AI: %s FILE: %s)" % (family,ai_name,file_name) )

        if "type" not in data:
            raise ValueError("%s WITHOUT TYPE (AI: %s FILE: %s)" % (family,ai_name,file_name) )

        if data["type"] not in cls.get_accepted_types():
            raise ValueError("%s TYPE NOT ACCEPTED (AI: %s FILE: %s)\n ACCEPTED VALUES: %s" % (family, ai_name, file_name, ", ".join(cls.get_accepted_types()) ) )

        if "items" in data and type(data["items"]) != list:
            raise ValueError("%s ITEMS SHOULD BE TYPE LIST (AI: %s FILE: %s)" % (family,ai_name,file_name) )

        if "items" in data and data["type"] != cls.TYPE_OPTIONS:
            raise ValueError("ONLY INPUT TYPE %s CAN HAVE ITEMS (AI: %s FILE: %s)" % (cls.TYPE_OPTIONS,ai_name,file_name) )

        if "scale" in data and type(data["scale"]) != str:
            raise ValueError("%s SCALE SHOULD BE TYPE STR (AI: %s FILE: %s)" % (family,ai_name,file_name) )

        if "scale" in data and data["type"] not in cls.numeric_input():
            raise ValueError("ONLY INPUTS TYPE %s CAN HAVE SACLE (AI: %s FILE: %s)" % ("or ".join(cls.numeric_input()) ,ai_name,file_name) )

        if "scale" in data and "items" in data:
            raise ValueError("%s CAN'T HAVE ITEMS AND SCALE (AI: %s FILE: %s)" % (family,ai_name,file_name) )

        dbc = DBController()
        if not dbc.secure_exists(cfg.TABLE_VARIABLE_INPUTS, (data["id"],family)):
            vi = VariableInput(data["id"], family, cls.OWNER_AI, data["type"], util.clean_title(data["name"]))
            if "items" in data:
                vi.items = data["items"]
            elif "scale" in data:
                vi.scale = data["scale"]

            vi.create()

        return data["name"]

    # scales
    @classmethod
    def get_available_scales(cls):
        return list(cls.scales.keys())

    @classmethod
    def get_available_scale_units(cls, scale):
        if scale in cls.scales:
            return cls.scales[scale][0]
        return None

    @classmethod
    def to_basic_unit(cls, scale, value, actual_unit):
        if scale in cls.scales:
            index = cls.scales[scale][0].index(actual_unit)
            return value * cls.scales[scale][1][index]
        return None

    @classmethod
    def to_sub_unit(cls, scale, value):
        if scale in cls.scales:
            index = 0
            sc_content = cls.scales[scale]
            sc_len = len(cls.scales[scale][0])
            while (index < sc_len and value % sc_content[1][index] == 0):
                index = index+1
            if index > 0:
                index = index -1
            return (value/sc_content[1][index], sc_content[0][index])
        return None

#    @classmethod
#    def get_scalized_str(cls, id, value):
#        vi = cls.get_variable_input(id)
#        if vi.scale is not None:
#            scalized = cls.to_sub_unit(vi.scale, value)
#            return " ".join([str(scalized[0]), scalized[1]])
#        else:
#            return str(value)
