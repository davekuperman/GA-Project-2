-- createdb frelper
-- psql frelper

-- DROP TABLE IF EXISTS shippers
-- DROP TABLE IF EXISTS carriers

-- CREATE TABLE shippers(
--     id SERIAL PRIMARY KEY,
--     firstName VARCHAR (50) NOT NULL,
--     lastName VARCHAR (50) NOT NULL,
--     email TEXT NOT NULL,
--     phoneNumber TEXT NOT NULL,
--     companyName TEXT NOT NULL,
--     password_hash TEXT NOT NULL

-- );

-- CREATE TABLE carriers(
--     id SERIAL PRIMARY KEY,
--     firstName VARCHAR (50) NOT NULL,
--     lastName VARCHAR (50) NOT NULL,
--     email TEXT NOT NULL,
--     phoneNumber TEXT NOT NULL,
--     companyName TEXT NOT NULL,
--     password_hash TEXT NOT NULL

-- );

-- CREATE TABLE jobs (
--     id SERIAL PRIMARY KEY,
--     shipper_id INTEGER REFERENCES shippers(id),
--     type TEXT NOT NULL,
--     weight FLOAT NOT NULL,
--     pick_up TEXT NOT NULL,
--     drop_off TEXT NOT NULL,
--     suburb TEXT NOT NULL,
--     state TEXT NOT NULL
-- );

-- -- ALTER TABLE carriers ADD profile_pic TEXT;