import os
from dotenv import load_dotenv

from flask import Flask
from flask import render_template, redirect, request, Response, session
from flask_mysqldb import MySQL , MySQLdb


load_dotenv()

app = Flask(__name__,template_folder="template")

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
app.config['MYSQL_CURSORCLASS'] = os.getenv('MYSQL_CURSORCLASS')

mysql=MySQL(app)

@app.route('/')
def home():
    return render_template('login.html')

if __name__=='__main__':     
    app.secret_key = os.getenv('SECRET_KEY')
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)

