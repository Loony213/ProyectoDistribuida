from flask import jsonify
from app import mysql
from MySQLdb import Error

def delete_user(id):
    # Conectar a la base de datos
    cur = mysql.connection.cursor()

    # Ejecutar la consulta SQL para eliminar al usuario
    try:
        cur.execute("DELETE FROM users WHERE id = %s", (id,))
        mysql.connection.commit()  # Guardar los cambios
        cur.close()

        # Retornar un mensaje de éxito en formato JSON
        return jsonify({"message": "Usuario eliminado exitosamente"}), 200
    except Error as e:
        # En caso de error, retornar el mensaje de error
        return jsonify({"error": f"Error al eliminar el usuario: {e}"}), 500
