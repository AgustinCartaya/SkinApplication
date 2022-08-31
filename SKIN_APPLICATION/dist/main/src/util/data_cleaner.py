# @autor: Agustin CARTAYA

# this file contains all the methods necessary
# for the verification of text strings
import re 
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression

# regular expressions
regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
regex_name = "^([a-zA-Z]|-|')*$"
regex_letters = "[a-zA-Z]*"
regex_number = "[0-9]*"
regex_not_null_number = "[1-9][0-9]*"
regex_not_null_4_number = "[1-9][0-9]{0,3}"
regex_age = "(|[1-9][0-9]{0,2})"
regex_range = "(|[1-9][0-9]{0,2} ?- ?[1-9][0-9]{0,2}|[1-9][0-9]{0,2}(\+|\-))"
regex_letter_space = "^([A-Za-z]| )*$"
regex_letter_number_space = "^([A-Za-z]| |[0-9])*$"
regex_no_dangerous = "^[^=;]*$"


# normalize a name
def normalize_name(text):
    return text.strip().upper()


# normalize an email
def normalize_email(text):
    return text.strip().lower()


# normalize a password
def normalize_password(text):
    return text.strip()


# check if a string contains only letters
def is_only_text(text):
    return text.isalpha()


# check if a string is an name
def is_name(text):
    regex = regex_name
    if re.search(regex,text):
        return True
    else:
        return False


# check if a string is an email
def is_email(text):
    regex = regex_email
    if re.search(regex,text):   
        return True 
    else:   
        return False


# check if a string is a password
# a password must contain
# 1 lower case letter
# 1 upper case letter
# 1 digit
# 1 of the following special characters (@ $ _ .)
def is_password(text):
    l, u, p, d = 0, 0, 0, 0

    if (len(text) >= 4):
        for i in text:
    
            # counting lowercase alphabets
            if (i.islower()):
                l+=1           
    
            # counting uppercase alphabets
            if (i.isupper()):
                u+=1           
    
            # counting digits
            if (i.isdigit()):
                d+=1           
    
            # counting the mentioned special characters
            if(i=='@'or i=='$' or i=='_' or i=='.'):
                p+=1          
    if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(text)):
        return True
    else:
        return False


# returns a QRegularExpression object
# with the regular expression passed by parameter
def create_text_validator(regex_text):
    regex = QRegularExpression(regex_text)
    return QRegularExpressionValidator(regex)
