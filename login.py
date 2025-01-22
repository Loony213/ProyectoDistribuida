from app import app  # Importamos la aplicación desde el archivo app.py

if __name__ == '__main__':
    app.secret_key = os.getenv('SECRET_KEY')
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
