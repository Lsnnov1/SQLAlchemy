DROP DATABASE firstdb;
CREATE DATABASE firstdb;
\c firstdb;

CREATE TABLE women (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
);

CREATE TABLE men (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
);

INSERT INTO women(name, age)VALUES ('woman1', 20), ('woman2', 25), ('woman3', 30);
INSERT INTO men(name, age) VALUES ('man1', 22), ('man2', 27), ('man3', 32);