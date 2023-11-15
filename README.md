Recomendaciones

Crea un archivo .env en la raíz de tu proyecto. Ahí agregaremos nuestras variables de entorno

    SECRET_KEY=tu-clave-secreta
    DEBUG=False
    DB_NAME=tu-nombre-de-db
    DB_USER=tu-db-user
    DB_PASSWORD=tu-db-password
    DB_HOST=tu-db-host
    ALLOWED_HOSTS=tu-host1, tu-host2, tu-host3

Para comprobar la conexion con nuestra base de datos vamos a realizar la primera migración

    python manage.py makemigrations
    python manage.py migrate