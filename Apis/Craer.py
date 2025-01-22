import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL, MySQLdb

load_dotenv()

app = Flask(__name__, template_folder="templates")

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
app.config['MYSQL_CURSORCLASS'] = os.getenv('MYSQL_CURSORCLASS')

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Obtener los datos del formulario
        username = request.form['username']
        password = request.form['password']

        # Conectar a la base de datos
        cur = mysql.connection.cursor()

        # Insertar los datos en la tabla (asegúrate de tener una tabla 'users' en tu base de datos)
        try:
            cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            mysql.connection.commit()  # Guardar los cambios
            cur.close()
            return redirect('/')  # Redirigir a la página de inicio después del registro
        except MySQLdb.Error as e:
            return f"Error al registrar el usuario: {e}"

    return render_template('register.html')
