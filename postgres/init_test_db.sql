-- --------------------------------------------
-- Create the tables (user)
-- --------------------------------------------
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users
(
    id      serial NOT NULL,
    name    varchar(100) NOT NULL,
    age     integer NOT NULL,
    country varchar(100) NOT NULL,
    CONSTRAINT users_pkey PRIMARY KEY (id)
);

-- Populate table users
INSERT INTO users (name, age, country) values('John Doe', 33, 'Canada');
INSERT INTO users (name, age, country) values('Jane Doe', 42, 'USA');
INSERT INTO users (name, age, country) values('Next Client', 21, 'Germany');
INSERT INTO users (name, age, country) values('Previous Client', 23, 'Sweden');
INSERT INTO users (name, age, country) values('Super Client', 29, 'Finland');
