CREATE DATABASE astrology_app;
\c astrology_app

CREATE TABLE astro (
    id SERIAL PRIMARY KEY,
    name TEXT,
    image_url TEXT, 
    title TEXT,
    explanation TEXT,
    mass REAL,
    moon_count INTEGER,
    date DATE,
    url TEXT
);

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT
    password_digest TEXT
);



ALTER TABLE users ADD COLUMN password_digest TEXT;