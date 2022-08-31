CREATE TABLE DOCTORS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE PATIENTS (
    id TEXT NOT NULL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    birth_date DATE NOT NULL,
    gender INTEGER NOT NULL,
    medical_information TEXT,
    doctor_id INTEGER NOT NULL
);

CREATE TABLE SKIN_LESIONS (
    number INTEGER NOT NULL,
    id_patient TEXT NOT NULL,
    location TEXT NOT NULL,
    characteristics TEXT NOT NULL,
    ai_results TEXT NOT NULL,
    UNIQUE(number, id_patient)
);

CREATE TABLE VARIABLE_INPUTS (
    id TEXT NOT NULL,
    family TEXT NOT NULL,
    owner TEXT NOT NULL,
    type TEXT NOT NULL,
    name TEXT NOT NULL,
    items TEXT,
    scale TEXT,
    UNIQUE(id, family)
);