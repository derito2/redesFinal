"""
from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
import os

app = Flask(__name__)

# Generar una clave para encriptación
key = Fernet.generate_key()
cipher = Fernet(key)

# Directorio para almacenar las imágenes encriptadas
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Encriptar la imagen
    encrypted_data = cipher.encrypt(file.read())

    # Guardar la imagen encriptada
    encrypted_filename = os.path.join(UPLOAD_FOLDER, 'encrypted_image.dat')
    with open(encrypted_filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    return jsonify({'message': 'File uploaded and encrypted successfully'}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
"""


from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
import os

app = Flask(__name__)

# Generar una clave para encriptación
key = Fernet.generate_key()
cipher = Fernet(key)

# Directorio para almacenar las imágenes encriptadas y desencriptadas
UPLOAD_FOLDER = 'uploads'
DECRYPTED_FOLDER = 'decrypted'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(DECRYPTED_FOLDER):
    os.makedirs(DECRYPTED_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Leer la imagen
    image_data = file.read()

    # Encriptar la imagen
    encrypted_data = cipher.encrypt(image_data)

    # Guardar la imagen encriptada en un archivo en la carpeta 'uploads'
    encrypted_filename = os.path.join(UPLOAD_FOLDER, 'encrypted_image.dat')
    with open(encrypted_filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    return jsonify({'message': 'File uploaded and encrypted successfully'}), 200

@app.route('/decrypt', methods=['GET'])
def decrypt_file():
    # Leer la imagen encriptada desde el archivo en la carpeta 'uploads'
    encrypted_filename = os.path.join(UPLOAD_FOLDER, 'encrypted_image.dat')
    if not os.path.exists(encrypted_filename):
        return jsonify({'error': 'Encrypted image not found'}), 404

    with open(encrypted_filename, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    # Desencriptar la imagen
    decrypted_data = cipher.decrypt(encrypted_data)

    # Guardar la imagen desencriptada en un archivo en la carpeta 'decrypted'
    decrypted_filename = os.path.join(DECRYPTED_FOLDER, 'decrypted_image.jpg')
    with open(decrypted_filename, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    return jsonify({'message': 'Image decrypted and saved successfully'}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
