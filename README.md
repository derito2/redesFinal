
Uso del Servidor

Ejecuta el servidor (server.py):
python server.py

Para subir y encriptar una imagen:
Utiliza una herramienta como Postman o CURL para enviar una solicitud POST a http://127.0.0.1:5000/upload, adjuntando una imagen como archivo.
La imagen será encriptada y guardada en la carpeta uploads.
Para desencriptar la imagen:
Abre un navegador y visita http://127.0.0.1:5000/decrypt.
La imagen encriptada será desencriptada y guardada como decrypted_image.jpg en la carpeta decrypted.
Notas
Asegúrate de tener permisos de escritura en las carpetas uploads y decrypted para que el servidor pueda guardar las imágenes encriptadas y desencriptadas correctamente.
Este ejemplo simplificado utiliza rutas estáticas para la ubicación de los archivos encriptados y desencriptados. En un entorno de producción, es posible que desees implementar una lógica más robusta para manejar múltiples archivos y clientes.
