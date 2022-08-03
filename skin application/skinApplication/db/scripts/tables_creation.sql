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

CREATE TABLE SKIN_LESIONS (
    number INTEGER NOT NULL,
    id_patient TEXT NOT NULL,
    caracteristics TEXT NOT NULL,
    ai_results TEXT NOT NULL,
    UNIQUE(number, id_patient)
);

INSERT INTO DOCTORS (id, first_name, last_name, password, email ) VALUES (NULL, 'Agustin', 'Cartaya', 'Ag.1', 'ag@gmail.com');

INSERT INTO PATIENTS (id, first_name, last_name, birth_date, gender, medical_information) VALUES ("AG3526CA", "Agustin", "Cartaya", '10-11-2000', 1, '{"eye_color":"Hazel","hair_color":"Blonde"}');
INSERT INTO PATIENTS (id, first_name, last_name, birth_date, gender, medical_information) VALUES ("PI3526RD", "Pierre", "Bernard", '21-02-1970', 1, '{"eye_color":"Hazel","hair_color":"Blonde"}');
INSERT INTO PATIENTS (id, first_name, last_name, birth_date, gender, medical_information) VALUES ("PH3526IN", "Philippe", "Martin" , '23-07-1974', 1, '{"eye_color":"Hazel","hair_color":"Blonde"}');
INSERT INTO PATIENTS (id, first_name, last_name, birth_date, gender, medical_information) VALUES ("AL9626AS", "Alain", "Thomas", '30-06-1963', 1, '{"eye_color":"Hazel","hair_color":"Blonde"}');
INSERT INTO PATIENTS (id, first_name, last_name, birth_date, gender, medical_information) VALUES ("NA3528IT", "Nathalie", "Petit", '22-07-1981', 0, '{"eye_color":"Hazel","hair_color":"Blonde"}');
INSERT INTO PATIENTS (id, first_name, last_name, birth_date, gender, medical_information) VALUES ("MO3526RT", "Monique", "Robert", '28-12-1967', 0, '{"eye_color":"Hazel","hair_color":"Blonde"}');
INSERT INTO PATIENTS (id, first_name, last_name, birth_date, gender, medical_information) VALUES ("SY5426RD", "Sylvie", "Richard", '06-11-1955', 0, '{"eye_color":"Hazel","hair_color":"Blonde"}');
INSERT INTO PATIENTS (id, first_name, last_name, birth_date, gender, medical_information) VALUES ("FR9876ND", "Francoise", "Durand", '08-09-1949', 0, '{"eye_color":"Hazel","hair_color":"Blonde"}');
INSERT INTO PATIENTS (id, first_name, last_name, birth_date, gender, medical_information) VALUES ("CH3526IS", "Christophe", "Dubois", '10-10-1983', 1, '{"eye_color":"Hazel","hair_color":"Blonde"}');

INSERT INTO PATIENTS (id, first_name, last_name, birth_date, gender, medical_information) VALUES ("JA1226YA", "Jacques", "Cartaya", '11-01-2007', 1, '{"eye_color":"Hazel","hair_color":"Blonde"}');
INSERT INTO PATIENTS (id, first_name, last_name, birth_date, gender, medical_information) VALUES ("MA4726RD", "Martine", "Bernard", '08-03-1778', 0, '{"eye_color":"Hazel","hair_color":"Blonde"}');
INSERT INTO PATIENTS (id, first_name, last_name, birth_date, gender, medical_information) VALUES ("LA8726IN", "Laurent", "Martin" , '05-04-1985', 1, '{"eye_color":"Hazel","hair_color":"Blonde"}');
INSERT INTO PATIENTS (id, first_name, last_name, birth_date, gender, medical_information) VALUES ("FR3626AS", "Frederic", "Thomas", '17-05-1988', 1, '{"eye_color":"Hazel","hair_color":"Blonde"}');
INSERT INTO PATIENTS (id, first_name, last_name, birth_date, gender, medical_information) VALUES ("ST9786IT", "Stephane", "Petit", '26-09-1995', 0, '{"eye_color":"Hazel","hair_color":"Blonde"}');
INSERT INTO PATIENTS (id, first_name, last_name, birth_date, gender, medical_information) VALUES ("SE5226EN", "Sebastien", "Robert", '27-12-1991', 1, '{"eye_color":"Hazel","hair_color":"Blonde"}');
INSERT INTO PATIENTS (id, first_name, last_name, birth_date, gender, medical_information) VALUES ("JU3529EN", "Julien", "Richard", '04-04-1976', 1, '{"eye_color":"Hazel","hair_color":"Blonde"}');
INSERT INTO PATIENTS (id, first_name, last_name, birth_date, gender, medical_information) VALUES ("PA3524ND", "Pascal", "Durand", '03-03-1975', 1, '{"eye_color":"Hazel","hair_color":"Blonde"}');
INSERT INTO PATIENTS (id, first_name, last_name, birth_date, gender, medical_information) VALUES ("TH3590IS", "Thierry", "Dubois", '10-11-1974', 1, '{"eye_color":"Hazel","hair_color":"Blonde"}');



INSERT INTO SKIN_LESIONS (number, id_patient, caracteristics, ai_results) VALUES (0, "AG3526CA", '{"diameter":["3","cm"], "apparition_date":["4","Months"]}', '{"AI-01":{"Risk": "MALIGNANT", "Type":"Melanoma", "Accurance:":87}}');
INSERT INTO SKIN_LESIONS (number, id_patient, caracteristics, ai_results) VALUES (1, "AG3526CA", '{"diameter":["1","mm"], "apparition_date":["1","Years"]}', '{"AI-01":{"Risk": "BENIGN", "Type":"Mole", "Accurance:":83}, "AI-02":{"Risk": "BENIGN", "Type":"Mole", "Accurance:":87}, "AI-03":{"Risk": "BENIGN", "Type":"Mole", "Accurance:":90}}');
INSERT INTO SKIN_LESIONS (number, id_patient, caracteristics, ai_results) VALUES (0, "PI3526RD", '{"diameter":["10","cm"], "apparition_date":["3","Weeks"]}', '{}');
