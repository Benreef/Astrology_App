from db.db import sql

def find_user_image(user_id):
    return sql('SELECT * FROM astro WHERE user_id=%s ORDER BY id', [user_id])

def find_image_id(id):
    image = sql('SELECT * FROM astro WHERE id=%s', [id])
    return image[0]

def create_image(title, explanation, url, date, user_id):
    sql(f'INSERT INTO astro(title, explanation, url, date, user_id) VALUES (%s, %s, %s, %s, %s) RETURNING *', [title, explanation, url, date, user_id])

def update_image(id, title, explanation, url, date):
    print(id)
    print(title)
    print(explanation)
    print(url)
    print(date)
    sql('UPDATE astro SET title=%s, explanation=%s, url=%s, date=%s WHERE id=%s RETURNING *',[title, explanation, url, date, id])

def delete_image(id):
    sql('DELETE FROM astro WHERE id=%s RETURNING *', [id])

# def user_favourite(user_id, image_id):
#     sql('INSERT INTO user_fav(user_id, image_id) VALUES (%s, %s)', [user_id, image_id])


# # def user_favourite(title, explanation, url, date, user_id, image_id):
# #    return sql('INSERT INTO user_fav(title, explanation, url, date, user_id, image_id) VALUES (%s, %s, %s, %s, %s, %s)', [title, explanation, url, date, user_id, image_id])


def like_image(title, explanation, url, date, user_id):
    sql('INSERT INTO image_likes(title, explanation, url, date, user_id) VALUES(%s, %s, %s, %s, %s) RETURNING *', [title, explanation, url, date, user_id])

def find_user_fav(user_id):
    fav_image = sql('SELECT * FROM image_likes WHERE user_id = %s ORDER BY id', [user_id])
    return fav_image
