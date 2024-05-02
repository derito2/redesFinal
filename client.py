
import socket
from cryptography.fernet import Fernet

def encrypt_image(image_path, key):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
    cipher_suite = Fernet(key)
    encrypted_image_data = cipher_suite.encrypt(image_data)
    return encrypted_image_data

def send_encrypted_image(server_host, server_port, encrypted_image_data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_host, server_port))
        s.sendall(encrypted_image_data)

key = Fernet.generate_key()  # Guarda esta clave para desencriptar la imagen en el servidor
image_path = 'path_to_your_image.png'
encrypted_image_data = encrypt_image(image_path, key)
send_encrypted_image('localhost', 12345, encrypted_image_data)
