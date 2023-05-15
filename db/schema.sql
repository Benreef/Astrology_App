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


CREATE TABLE user_fav(
    id SERIAL PRIMARY KEY,
    title TEXT,
    explanation TEXT,
    url TEXT,
    date TEXT,
    user_id INTEGER REFERENCES users(id),
    image_id INTEGER
);

CREATE TABLE photo_comments(
    id SERIAL PRIMARY KEY,
    comment TEXT,
    user_id INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE image_likes(
    id SERIAL PRIMARY KEY,
    title TEXT,
    explanation TEXT,
    url TEXT,
    date TEXT,
    user_id INTEGER REFERENCES users(id)
);
