from flask import Flask, request, redirect, render_template
import cgi
import os
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/validate-user")
def display_signup_form():
    return render_template('signup.html')

@app.route("/validate-user", methods=['POST'])
def validate_user():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''


    if ' ' in username or len(username) < 3 or len(username) > 20 or username is None:
        username_error = "Username must be 3 - 20 Characters and contain no Spaces."      
        username = ''
    else: 
        username = username

    if ' ' in password or len(password) < 3 or len(password) > 20 or password is None:
        password_error = "Password must be 3 - 20 Characters and contain no Spaces."      
        password = ''
    else: 
        password = password

    if ' ' in verify_password or len(verify_password) < 3 or len(verify_password) > 20 or verify_password is None or verify_password != password:
        verify_password_error = "Passwords Don't Match."      
        verify_password = ''
    else: 
        verify_password = verify_password

    email_requirement = re.compile(r"^[\S]+@[\S]+.[\S]+$")
    if email_requirement.match(email) == None or len(email) < 3 or len(email) > 20:
        email_error = "Please enter a valid email!"
    else:
        email = email

    if not username_error and not password_error and not verify_password_error and not email_error:
        username = username
        
        return redirect("/valid-user?username={0}".format(username))
    else:
        return render_template('signup.html',
        username_error = username_error,
        password_error = password_error,
        verify_password_error = verify_password_error,
        email_error = email_error,
        username = username,
        password = password,
        verify_password = verify_password,
        email = email)

@app.route("/valid-user")
def valid_user():
    username = request.args.get('username')
    return "<h1>Thank you for signing up, {0}!</h1>".format(username)


app.run()