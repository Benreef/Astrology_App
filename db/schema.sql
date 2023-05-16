CREATE DATABASE astrology_app;
\c astrology_app

CREATE TABLE astro (
    id SERIAL PRIMARY KEY,
    title TEXT,
    explanation TEXT,
    url TEXT,
    date TEXT
);

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    password_digest TEXT
);


ALTER TABLE astro ADD COLUMN user_id INTEGER REFERENCES users(id);


CREATE TABLE image_likes(
    id SERIAL PRIMARY KEY,
    title TEXT,
    explanation TEXT,
    url TEXT,
    date TEXT,
    user_id INTEGER REFERENCES users(id)
);
