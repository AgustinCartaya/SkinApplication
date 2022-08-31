# @autor: Agustin CARTAYA

# this file is responsible for filtering all the texts displayed on the screen
# it does not filter the text created in the ui
# use in the future to make translations
from src.objects.variable_input import VariableInput
import src.util.util as util

# method that filters all strings
def f(text, translate=True, colon=False, format=False, parenthesis=False, before=None, scale_input=None, upper=False):
    if type(text) in (list, tuple):
        text = " ".join(text)
    elif type(text) in (int, float):
        # scaled values
        if scale_input is not None:
            text = VariableInput.get_scalized_str(scale_input[0], text, scale_input[1])
        else:
            text = str(text)
    elif type(text) is bool:
        if text:
            text = "Yes"
        else:
            text = "No"

    # formatting
    if format:
        text = util.file_name_to_title(text)

    # parenthesis
    if parenthesis:
        text = "(" + text + ")"

    # colon
    if colon:
        text = text + " :"

    # before
    if before:
        text = before + text

    return text
