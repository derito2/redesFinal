# server.py
import socket
from cryptography.fernet import Fernet

def decrypt_image(encrypted_image_data, key):
    cipher_suite = Fernet(key)
    decrypted_image_data = cipher_suite.decrypt(encrypted_image_data)
    return decrypted_image_data

def save_decrypted_image(image_path, decrypted_image_data):
    with open(image_path, 'wb') as image_file:
        image_file.write(decrypted_image_data)

def receive_encrypted_image(server_host, server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((server_host, server_port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            encrypted_image_data = conn.recv(1024)
            return encrypted_image_data

key = b'your_key_here'  # Usa la misma clave que generaste en el cliente
encrypted_image_data = receive_encrypted_image('localhost', 12345)
decrypted_image_data = decrypt_image(encrypted_image_data, key)
save_decrypted_image('decrypted_image.png', decrypted_image_data)
