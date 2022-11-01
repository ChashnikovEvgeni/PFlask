
CREATE TABLE IF NOT EXISTS City (
id integer PRIMARY KEY AUTOINCREMENT,
maxID integer DEFAULT(0)
);



CREATE TABLE IF NOT EXISTS Citizen (
id integer PRIMARY KEY,
type VARCHAR(50) DEFAULT 'Житель',
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50),
age integer NOT NULL CHECK (age > '-1'),
city_id INTEGER,
FOREIGN KEY (city_id) REFERENCES City (id)
);


CREATE TABLE IF NOT EXISTS Soldier (
id integer PRIMARY KEY,
type VARCHAR(50) DEFAULT 'Солдат',
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50),
age integer NOT NULL CHECK (age > '-1'),
military_unit TEXT,
rank TEXT,
city_id INTEGER,
FOREIGN KEY (city_id) REFERENCES City(id)
);


CREATE TABLE IF NOT EXISTS Doctor (
id integer PRIMARY KEY,
type VARCHAR(50) DEFAULT 'Доктор',
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50),
age integer NOT NULL CHECK (age > '-1'),
hospital  TEXT,
specialization TEXT,
city_id INTEGER,
FOREIGN KEY (city_id) REFERENCES City(id)
);