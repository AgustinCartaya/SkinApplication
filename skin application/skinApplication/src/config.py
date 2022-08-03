import os

# project location
PROJECT_FOLDER = os.sep.join(__file__.split(os.sep)[:-2])

# system folder separator
_S = os.sep

# data base
DB_PATH = PROJECT_FOLDER + _S + "db"
DB_NAME = "skin_application.sqlite"
DB_PATH_NAME = DB_PATH + _S + DB_NAME
DB_SCRIPT_PATH = DB_PATH + _S + "scripts"
DB_SCRIPT_NAME = "tables_creation.sql"
DB_SCRIPT_PATH_NAME = DB_SCRIPT_PATH + _S + DB_SCRIPT_NAME
TABLE_DOCTORS = "DOCTORS"
TABLE_PATIENTS = "PATIENTS"
TABLE_SKIN_LESIONS = "SKIN_LESIONS"
COLUMN_DOCTORS_FIRST_NAME = "first_name"
COLUMN_DOCTORS_LAST_NAME = "last_name"
COLUMN_DOCTORS_PASSWORD = "password"

# assets
ASSETS_PATH = PROJECT_FOLDER + _S + "assets"
FILES_PATH = ASSETS_PATH + _S + "files"
FILES_MEDICAL_INFORMATION_PATH = FILES_PATH + _S + "medical_information"
FILES_SKIN_LESION_CARACTERISTICS_PATH = FILES_PATH + _S + "skin_lesion_caracteristics"
FILES_IMAGES_TYPE_PATH = FILES_PATH + _S + "images_type"

# Artificial inteligence
AI_PATH = PROJECT_FOLDER + _S + "ai"
AI_INFO_FOLDER_NAME = "info"
AI_DESCRIPTION_FILE_NAME = "description"

# patients data
PATIENTS_DATA_PATH = PROJECT_FOLDER + _S + "patients_data"
SKL_IMAGES_FOLDER_NAME = "images"
SKL_AI_RESULTS_FOLDER_NAME = "ai_results"
SKL_TIMELINE_FOLDER_NAME = "timeline"

# skin lession folder sufix
SKL_FOLDER_SUFIX = "skin_lesion_"

# views
CREATE_ACCOUNT_VIEW = "CREATE_ACCOUNT_VIEW"
LOGIN_VIEW = "LOGIN_VIEW"
PATIENTS_VIEW = "PATIENTS_VIEW"
UPSERT_PATIENT_VIEW = "UPSERT_PATIENT_VIEW"
UPSERT_PATIENT_MI_VIEW = "UPSERT_PATIENT_MI_VIEW"
UPSERT_PATIENT_PREVIEW_VIEW = "UPSERT_PATIENT_PREVIEW_VIEW"
UPSERT_SKIN_LESION_VIEW = "UPSERT_SKIN_LESION_VIEW"
CHECK_PATIENT_VIEW = "CHECK_PATIENT_VIEW"
AI_LAUNCHER_VIEW = "AI_LAUNCHER_VIEW"

# styles
STYLES_PATH = PROJECT_FOLDER + "/src/views/ui/styles"
GLOBAL_STYLES_NAME = "global.css"
GLOBAL_STYLES_PATH_NAME = STYLES_PATH + _S + GLOBAL_STYLES_NAME

