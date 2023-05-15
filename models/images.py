from db.db import sql

def find_user_image(user_id):
    return sql('SELECT * FROM astro WHERE user_id=%s ORDER BY id', [user_id])

def find_image_id(id):
    image = sql('SELECT * FROM astro WHERE id=%s', [id])
    return image[0]

def create_image(title, explanation, url, date, user_id):
    sql(f'INSERT INTO astro(title, explanation, url, date, user_id) VALUES (%s, %s, %s, %s, %s) RETURNING *', [title, explanation, url, date, user_id])

def update_image(id, title, explanation, url, date):
    sql('UPDATE astro SET title=%s, explanation=%s, url=%s, date=%s WHERE id=%s RETURNING *',[title, explanation, url, date, id])

def delete_image(id):
    sql('DELETE FROM astro WHERE id=%s RETURNING *', [id])