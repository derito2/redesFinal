import requests

def encrypt_and_upload_image(filename, server_url):
    # Leer la imagen
    with open(filename, 'rb') as file:
        image_data = file.read()

    # Enviar la imagen encriptada al servidor
    files = {'file': image_data}
    response = requests.post(server_url, files=files)

    if response.status_code == 200:
        print("Image uploaded and encrypted successfully.")
    else:
        print("Error uploading or encrypting image.")

if __name__ == '__main__':
    image_filename = 'si.jpg'
    server_url = 'http://127.0.0.1:5000/upload'

    encrypt_and_upload_image(image_filename, server_url)

