CREATE TABLE DOCTORS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    UNIQUE(first_name, last_name)
);

CREATE TABLE PATIENTS (
    id TEXT NOT NULL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    birth_date DATE NOT NULL,
    gender INTEGER NOT NULL,
    medical_information TEXT
);
