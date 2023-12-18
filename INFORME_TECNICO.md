![Alt text](./reporte_imagenes/ifts18-bg.png)

TRABAJO PRACTICO REALIZADO POR:
---
* ALUMNO: ANDERSON MICHEL OCAÑA TORRES
* DOCENTE A CARGO: ALBERTO CAMPAGNA

# Sistema de Gestión Mr Manager: Documentación Técnica

## Introducción
Mr Manager es un sistema integral de gestión de cursos, novedades y biblioteca técnica, diseñado para ofrecer una experiencia personalizada a los usuarios y empresas inscritas. Este sistema se basa en tecnologías robustas y se despliega en entornos de nube para garantizar su escalabilidad y modularidad.

## Funcionalidades Principales
- Gestión de Cursos: Permite la reserva de cursos y facilita la interacción entre usuarios y administradores.
- Biblioteca Técnica: Almacena información relevante sobre cursos y novedades.
- Personalización: Proporciona información personalizada a los usuarios y empresas inscritos.

## Tecnologías Utilizadas

### Frontend
- Desarrollo basado en Django aprovechando las capacidades de HTML, CSS, JS, JQuery & AJAX.
- Herramientas adicionales: AJAX para una comunicación asíncrona eficiente.

### Backend
- Django: Framework robusto para el desarrollo backend.
- Librerías: Pillow y WhiteNoise para funcionalidades específicas.
- Bases de datos: PostgreSQL 12 en Render.com y MySQL en PythonAnywhere.
- Seguridad: Encriptación de contraseñas mediante el algoritmo PBKDF2 con hash SHA256. Opcional: Argon.

### Autenticación Opcional
- Implementación de inicio de sesión utilizando GitHub o Gmail mediante AuthLib, Django-allauth, DjangoJWT o Passport.

### Despliegue
- Plataformas: render.com, pythonanywhere.com.
- Uso de Docker para versionado local.

## Arquitectura de Diseño
El sistema adopta una arquitectura monolítica modular para aprovechar la separación de servicios en un mismo servidor, optimizando la eficiencia y mantenibilidad.

### Opcionales
- NGINX: Funciona como servidor web con opción de balanceador de carga para los servicios de entrada.
- MySQL: Base de datos con la posibilidad de generar un volumen local para importar o exportar datos, gestionado por NGINX.
- ADMINER: Herramienta de visualización de bases de datos.

### Adicionales Opcionales
- Servicio de Caché: Redis o Varnish (No implementado).
- Monitoreo: Grafana con Prometheus (No implementado).

## Versionado y Stack Tecnológico
- Versionado con Git, con el repositorio en la nube de GitHub y uso de Codespaces para el despliegue y pruebas.
- Stack Tecnológico: Django & Python, HTML5, CSS, Bootstrap, SweetAlert, Ajax, JS y JQuery.
- Herramientas de desarrollo: Visual Studio Code.
- Sistemas Operativos: Linux y Windows.


