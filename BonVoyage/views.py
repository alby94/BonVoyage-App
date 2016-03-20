# -*- coding: utf-8 -*-

DEBUG = True
MYSQL_DATABASE_USER = 'root1'
MYSQL_DATABASE_PASSWORD = 'root1'
MYSQL_DATABASE_DB = 'webapp'
MYSQL_DATABASE_HOST = 'localhost'

from flask import Flask, render_template,request,session, redirect, url_for, escape
from flaskext.mysql import MySQL
import MySQLdb
import urllib2,cookielib,sys
from getpass import getpass

mysql = MySQL()
app = Flask(__name__,static_folder = "static")
app.config.from_object(__name__)
mysql.init_app(app)

user1=' '

@app.route('/', methods=['POST', 'GET'])
def index():
    error= None
    if request.method == 'POST':
        cursor = mysql.connect().cursor()
        password=request.form['password']
        name=request.form['name']
        cursor.execute("SELECT * from Users where Password='" + password + "'AND Username='" + name + "'")
        data = cursor.fetchone()
        if data is None:
            return render_template('index.html',error=error)
        else:
             session['password'] = request.form['password']
             cursor.execute("SELECT * from Users where Password='" + password + "'AND Username='" + name + "'")
             data = cursor.fetchone()
    	     name=data[0]
    	     global user1
    	     user1 = name
             cursor.close()
             return render_template('pages/index_2.html',name=name)
	     print user1
    else:
        return render_template('index.html')
app.secret_key = '\xe1\x03\xcb\xf9^\xb8k\xb2\xcc\xd3\xbe\x9a\x01\x841\xf2t\xb6&MB\xac\xbb\xad'

@app.route('/credit', methods=['POST', 'GET'])
def credit():
	print user1
	if 'password' in session:
		 db= MySQLdb.connect("localhost","root1","root1","webapp")
		 cursor1 = db.cursor()
		 cursor1.execute("select * from Credit where Username='" + user1 + "'")
		 row1 = cursor1.fetchone()
	         cred=row1[1]
		 cursor1.close()
		 db.close()

		 return render_template('pages/index_4.html',name=user1, cred=cred)

@app.route('/map', methods=['POST', 'GET'])
def ref():
    return render_template('pages/index_3.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
