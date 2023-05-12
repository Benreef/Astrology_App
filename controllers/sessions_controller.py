from flask import render_template, request, redirect, session
from models.users import find_user_by_email
import bcrypt

def login():
    return render_template('sessions/login.html')

def create():
    email = request.form.get('email')
    password = request.form.get('password')
    user = find_user_by_email(email)
    if user == None:
        return redirect('/sessions/login')
    valid_password = bcrypt.checkpw(password.encode(), user['password_digest'].encode())
    if valid_password:
        session['user_id'] = user['id'] # this logs the user in
        return redirect('/image')
    else: 
        return redirect('/sessions/login')
    
def delete():
    session.clear() #logs the user out
    return redirect('/')