import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from delete_user import delete_user  # Importar la lógica de eliminación

load_dotenv()

app = Flask(__name__)

# Configuración de la base de datos
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
app.config['MYSQL_CURSORCLASS'] = os.getenv('MYSQL_CURSORCLASS')

mysql = MySQL(app)

# Ruta para registrar un nuevo usuario
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']

    # Conectar a la base de datos
    cur = mysql.connection.cursor()
    try:
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        mysql.connection.commit()  # Guardar los cambios
        cur.close()
        return jsonify({"message": "Usuario registrado exitosamente"}), 201
    except Exception as e:
        return jsonify({"error": f"Error al registrar el usuario: {e}"}), 500

# Ruta para eliminar un usuario
@app.route('/api/delete/<int:id>', methods=['DELETE'])
def delete(id):
    return delete_user(id)  # Llamamos a la función de eliminación

if __name__ == '__main__':
    app.secret_key = os.getenv('SECRET_KEY')
    app.run(debug=True, host='0.0.0.0', port=5000)
