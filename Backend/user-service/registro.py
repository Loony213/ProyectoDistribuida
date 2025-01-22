from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# Configuración de la base de datos
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

mysql = MySQL(app)

# Ruta para registrar un nuevo usuario
@app.route('/api/users', methods=['POST'])
def register_user():
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
@app.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    # Conectar a la base de datos
    cur = mysql.connection.cursor()
    try:
        cur.execute("DELETE FROM users WHERE id = %s", (id,))
        mysql.connection.commit()  # Guardar los cambios
        cur.close()
        return jsonify({"message": "Usuario eliminado exitosamente"}), 200
    except Exception as e:
        return jsonify({"error": f"Error al eliminar el usuario: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5002)  # Servicio de usuario en el puerto 5002
