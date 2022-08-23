import src.util.util as util
import src.config as cfg

scales={
"length":[["um","mm","cm","dm","m","Dm","Hm","Km"],[1,1000,10000,100000,1000000,10000000,100000000,1000000000]],
"time":[["seconds","minutes","hours"],[1,60,3600]],
"volume":[["mm3","cm3","dm3","m3"],[1,1000,1000000,1000000000]],
"weight":[["mg","cg","dg","g","Dg","Hg","Kg"],[1,10,100,1000,10000,100000,1000000]]
}
MI_INPUT = "MI_INPUT"
SKL_INPUT = "SKL_INPUT"

INPUT_OPTIONS = "options"
INPUT_INT = "int"
INPUT_FLOAT = "float"
INPUT_TEXT = "text"
INPUT_BOOL = "bool"
INPUT_DATE = "date"


def get_availables_ai_variable_inputs(input_type):
    if input_type == MI_INPUT:
        return util.get_file_list(cfg.FILES_AI_MEDICAL_INFORMATION_PATH)
    elif input_type == SKL_INPUT:
        return util.get_file_list(cfg.FILES_AI_SKIN_LESION_CHARACTERISTICS_PATH)

def get_availables_created_variable_inputs(input_type):
    if input_type == MI_INPUT:
        return util.get_file_list(cfg.FILES_CREATED_MEDICAL_INFORMATION_PATH)
    elif input_type == SKL_INPUT:
        return util.get_file_list(cfg.FILES_CREATED_SKIN_LESION_CHARACTERISTICS_PATH)

def get_availables_variable_inputs(input_type):
    return get_availables_ai_variable_inputs(input_type) + get_availables_created_variable_inputs(input_type)

def get_availables_variable_input_names(input_type):
    return [i.split(".")[0] for i in get_availables_variable_inputs(input_type)]

def create_new_variable_input(input_type, name, type, content):
    file_content = ""
    if len(content) > 0:
        file_content = '\n'.join(content)
    if input_type == MI_INPUT:
        util.create_file(file_content, cfg.FILES_CREATED_MEDICAL_INFORMATION_PATH, name + "." + type)
    elif input_type == SKL_INPUT:
        util.create_file(file_content, cfg.FILES_CREATED_SKIN_LESION_CHARACTERISTICS_PATH, name + "." + type)

def get_variable_input_content(input_type, file_name):
    if input_type == MI_INPUT:
        if util.is_file(cfg.FILES_AI_MEDICAL_INFORMATION_PATH, file_name):
            return util.read_file_list(cfg.FILES_AI_MEDICAL_INFORMATION_PATH, file_name)
        elif util.is_file(cfg.FILES_CREATED_MEDICAL_INFORMATION_PATH, file_name):
            return util.read_file_list(cfg.FILES_CREATED_MEDICAL_INFORMATION_PATH, file_name)

    elif input_type == SKL_INPUT:
        if util.is_file(cfg.FILES_AI_SKIN_LESION_CHARACTERISTICS_PATH, file_name):
            return util.read_file_list(cfg.FILES_AI_SKIN_LESION_CHARACTERISTICS_PATH, file_name)
        elif util.is_file(cfg.FILES_CREATED_SKIN_LESION_CHARACTERISTICS_PATH, file_name):
            return util.read_file_list(cfg.FILES_CREATED_SKIN_LESION_CHARACTERISTICS_PATH, file_name)

def get_availables_scales():
    return list(scales.keys())


def get_scale_units(scale):
    if scale in scales:
        return scales[scale][0]
    return None


def to_basic_unit(scale, value, actual_unit):
    if scale in scales:
        index = scales[scale][0].index(actual_unit)
        return value * scales[scale][1][index]
    return None


def to_sub_unit(scale, value):
    if scale in scales:
        index = 0
        sc_content = scales[scale]
        sc_len = len(scales[scale][0])
        while (index < sc_len and value % sc_content[1][index] == 0):
            index = index+1
        if index > 0:
            index = index -1
        return (value/sc_content[1][index], sc_content[0][index])
    return None


def get_scalized_str(file_name, value, input_type):
    # AI
    if input_type == MI_INPUT:
        path = cfg.FILES_AI_MEDICAL_INFORMATION_PATH
    elif input_type == SKL_INPUT:
        path = cfg.FILES_AI_SKIN_LESION_CHARACTERISTICS_PATH
    else:
        return str(value)

    for f_name in util.get_file_list(path):
        if file_name in f_name:
            scale = util.read_file(path, f_name).strip()
            if len(scale) > 0:
                scalized = to_sub_unit(scale, value)
                return " ".join([str(scalized[0]), scalized[1]])

    # created
    if input_type == MI_INPUT:
        path = cfg.FILES_CREATED_MEDICAL_INFORMATION_PATH
    elif input_type == SKL_INPUT:
        path = cfg.FILES_CREATED_SKIN_LESION_CHARACTERISTICS_PATH
    else:
        return str(value)

    for f_name in util.get_file_list(path):
        if file_name in f_name:
            scale = util.read_file(path, f_name).strip()
            if len(scale) > 0:
                scalized = to_sub_unit(scale, value)
                return " ".join([str(scalized[0]), scalized[1]])
    # not found
    return str(value)


def trailing_zeros(longint):
    manipulandum = str(longint)
    return len(manipulandum)-len(manipulandum.rstrip('0'))
