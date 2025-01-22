from flask import Flask, request, jsonify
import jwt
import os

app = Flask(__name__)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    # Lógica de autenticación (ej. validación de usuario en base de datos)
    # Generación del JWT
    token = jwt.encode({"user": data["username"]}, os.getenv('SECRET_KEY'), algorithm="HS256")
    return jsonify({"token": token})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)  # Servicio de autenticación en el puerto 5001
