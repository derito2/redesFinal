
Encriptación de Imágenes y Comunicación Cliente-Servidor

Este proyecto consiste en una aplicación cliente-servidor en Python que permite enviar una imagen encriptada desde el cliente al servidor para su posterior desencriptación utilizando el framework Flask y la biblioteca cryptography.

Requisitos
Asegúrate de tener instaladas las siguientes dependencias de Python:

Flask: Para crear el servidor web.
cryptography: Para realizar la encriptación y desencriptación de datos.
requests: Para realizar solicitudes HTTP desde el cliente.
Puedes instalar estas dependencias utilizando pip:

bash
Copy code
pip install Flask cryptography requests
Uso
Paso 1: Ejecutar el Servidor
Abre una terminal o línea de comandos.
Navega al directorio que contiene el archivo flask_server.py utilizando el comando cd.
Ejecuta el servidor Flask utilizando el siguiente comando:
bash
Copy code
python flask_server.py
Esto iniciará el servidor en la dirección http://127.0.0.1:5000/.


Paso 2: Ejecutar el Cliente
Abre otra terminal o línea de comandos.
Navega al directorio que contiene el archivo client.py y la imagen que deseas enviar.
Ejecuta el cliente Python utilizando el siguiente comando (reemplazando nombre_de_la_imagen.jpg con el nombre de tu imagen):
bash
Copy code
python client.py nombre_de_la_imagen.jpg
Asegúrate de que la imagen que deseas enviar se encuentre en el mismo directorio que client.py o especifica la ruta completa al archivo de imagen.
Detalles de Funcionamiento
El servidor (server.py) utiliza Flask para crear una API REST.
Cuando el cliente (client.py) se ejecuta y proporciona el nombre de la imagen como argumento, el cliente lee el archivo de imagen y envía los datos al servidor encriptados.
El servidor recibe los datos encriptados, los guarda en un archivo y realiza la operación inversa para desencriptar la imagen.
Archivos y Directorios
flask_server.py: Código del servidor Flask.
client.py: Código del cliente para enviar una imagen encriptada al servidor.
uploads/: Directorio donde se guardan los archivos encriptados.
Consideraciones Adicionales
Asegúrate de tener permisos de escritura en el directorio uploads/ para que el servidor pueda guardar los archivos encriptados correctamente.
Si deseas realizar pruebas con diferentes imágenes, simplemente ejecuta el cliente con el nombre de la nueva imagen como argumento.
Espero que esta guía te ayude a comprender cómo funciona la encriptación de imágenes mediante una comunicación cliente-servidor en Python utilizando Flask y cryptography. Si tienes alguna pregunta o problema, no dudes en preguntar. ¡Disfruta experimentando con este proyecto!
