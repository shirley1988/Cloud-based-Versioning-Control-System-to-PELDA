from flask import Flask, render_template, send_from_directory, redirect, url_for, request, session, json
from flask_cors import CORS
import string
import pymysql
import subprocess
import bcrypt
from praat import app

database_host = 'peldaw2018.mysql.database.azure.com'
database_user = 'myadmin@peldaw2018'
database_password = '1988@Idaho'
database_db = 'peldaw'

conn = pymysql.connect(user = database_user, 
        password = database_password, 
        database = database_db, 
        host = database_host)

@app.route('/')
def index():
	if 'username' in session:
		return app.send_static_file("index.html")
	return render_template('home.html')

@app.route('/logout')
def logout():
    if 'username' in session:
        session['username'] = None
    return render_template('home.html')

@app.route('/login',methods=['POST'])
def login():
    cursor = conn.cursor()
    username = request.form['username']
    cursor.execute("SELECT * FROM user WHERE username = %s;", username)
    users = cursor.fetchall()
    print(users)

    if users:
        #hash_password = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
        if username == users[0][0]:
            session['username'] = username
            conn.commit()
            #return app.send_static_file("index.html")
            return redirect(url_for('index'))

    conn.commit()
    return 'Invalid username/password combination'

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        cursor = conn.cursor()
        username = request.form['username']
        cursor.execute("SELECT * FROM user WHERE username = %s;", username)
        users = cursor.fetchall()
        print(users)
        print(len(users))

        if len(users) == 0:
            hash_password = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            cursor.execute("INSERT INTO user (username, password) VALUES (%s, %s);", (username, hash_password))
            session['username'] = username
            conn.commit()
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('register.html')


@app.route('/praatapidocs')
def Praatapidocs():
   return app.send_static_file("praatapidocs.html")

@app.route('/elanapidocs')
def ELANapidocs():
   return app.send_static_file("elanapidocs.html")

@app.route('/js/<jsfile>')
def getJS(jsfile):
   return send_from_directory("static/js/", jsfile)

@app.route('/css/<cssfile>')
def getCSS(cssfile):
   return send_from_directory("static/css/", cssfile)

@app.route('/img/<imgfile>')
def getImage(imgfile):
   return send_from_directory("static/img/", imgfile)

