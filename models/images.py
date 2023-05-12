from db.db import sql

def find_user_image(user_id):
    return sql('SELECT * FROM astro WHERE user_id=%s ORDER BY id', [user_id])

def create_image(title, explanation, url, date, user_id):
    sql(f'INSERT INTO astro(title, explanation, url, date, user_id) VALUES (%s, %s, %s, %s, %s) RETURNING *', [title, explanation, url, date, user_id])

def update_image(title, explanation, url, date):
    sql(f'UPDATE astro(title, explanation, url, date) VALUES(%s, %s, %s, %s) RETURNING *',[title, explanation, url, date])