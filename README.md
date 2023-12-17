
# Configuración de Docker Compose para Aplicación Django DEPLOY LOCAL

## Descripción
Esta configuración de Docker Compose establece un entorno multi-contenedor para una aplicación Django junto con los servicios de MySQL, Adminer y Nginx.

### Servicios
- **mysql**: Ejecuta la base de datos MySQL para la aplicación Django.
- **adminer**: Proporciona una interfaz web para administrar la base de datos MySQL.
- **django**: Ejecuta la aplicación Django.
- **nginx**: Configura Nginx como un servidor proxy inverso para la aplicación Django.

## Detalles de la Configuración

### Servicio MySQL
- **Imagen**: mysql:v0.1
- **Mapeo de Puertos**: 3306:3306 (Host:Contenedor)
- **Variables de Entorno**:
  - `MYSQL_ROOT_PASSWORD`: Configurada como `admin`
- **Chequeo de Estado**: Verifica si el servicio MySQL está saludable al conectarse a la base de datos.

### Servicio Adminer
- **Imagen**: adminer
- **Puerto**: 8080:8080 (Host:Contenedor)

### Servicio Django
- **Imagen**: django:0.0.1
- **Puerto**: 8000:8000 (Host:Contenedor)
- **Volúmenes**:
  - `media`: Monta el directorio de archivos de medios para la aplicación Django.
  - `staticfiles`: Monta el directorio de archivos estáticos para la aplicación Django.
- **Archivo de Entorno**: Archivo `.env` para las variables de entorno.
- **Dependencias**: Depende del servicio MySQL para estar saludable antes de iniciar.

### Servicio Nginx
- **Nombre del Contenedor**: nginx
- **Volúmenes**:
  - Monta los directorios de archivos de medios y estáticos para Nginx.
  - Monta los archivos de configuración de nginx.
- **Puerto**: 80:80 (Host:Contenedor)
- **Dependencias**: Dependiente del servicio Django.
- **Configuración de Proxy**: Sirve como un servidor proxy inverso para la aplicación Django.

## Uso

### Iniciar los Servicios
Para iniciar los servicios, dirígete al directorio que contiene el archivo `docker-compose.yml` y ejecuta:
```
docker-compose up -d
```

### Acceder a los Servicios
- **Django**: Accede a la aplicación Django en `http://localhost:8000`
- **Adminer**: Accede a la interfaz de Adminer en `http://localhost:8080`
- **MySQL**: Conecta con la base de datos MySQL en `mysql://localhost:3306`
