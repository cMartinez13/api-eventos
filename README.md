# RESERVA DE SERVICIOS DE EVENTOS

### Indice de contenidos
- [RESERVA DE SERVICIOS DE EVENTOS](#reserva-de-servicios-de-eventos)
    - [Indice de contenidos](#indice-de-contenidos)
    - [Integrantes](#integrantes)
    - [Introducción](#introducción)
    - [Repositorio](#repositorio)
    - [Pasos a seguir para la instalación y ejecución del proyecto](#pasos-a-seguir-para-la-instalación-y-ejecución-del-proyecto)
    - [Listado de Endpoints de la API](#listado-de-endpoints-de-la-api)
    - [Requerimientos técnicos](#requerimientos-técnicos)

### Integrantes 
- Garcia Gabriel
- Giovanetti Hugo
- Martinez Sebastian
- Martinez Camila

### Introducción
Este proyecto  representa una aplicación destinada a la reserva de servicios para eventos. Está diseñada con el fin de que el usuario, pueda visualizar y reservar los servicios ofrecidos por la empresa de una forma fácil y dinámica. Tambien la aplicación nos ofrece desde el punto de vista de la empresa la posibilidad de crear nuevos servicios, dar de alta, modificar y desactivar nuevos empleados y coordinadores.   

### Repositorio
```
https://github.com/cMartinez13/api-eventos/
```
### Pasos a seguir para la instalación y ejecución del proyecto
1. Abrir la terminar de VSC o el editor de código de su preferencia.
2. Clonar el repositorio utilizando el comando: 
   - git clone https://github.com/cMartinez13/api-eventos/
3. Abrir la terminal cmd y crear el entorno virtual con el comando: 
   - python -m venv venv
4. Activar el entorno virtual con el comando :
   - venv\Scripts\activate
5. Instalar las dependecias con el comando:
   - pip install django jinja2 djangorestframework
6. Ejecutar el servidor con el comando:
   - python manage.py runserver

### Listado de Endpoints de la API
| PETICION | URL | DESCRIPCION 
|:--:|:--:|:-----:|
|GET| [/empleados](http://localhost:8000/api/empleados/)| Retorna el listado de datos de todos los empleados activos |
|GET|  [/empleados/id](http://localhost:8000/api/empleados/<int:pk>/) | Retorna el detalle de un empleado según el ID ingresado |
|GET| [/coordinadores](http://localhost:8000/api/coordinadores/)| Retorna el listado de datos de todos los coordinadores activos |
|GET|  [/coordinadores/id](http://localhost:8000/api/coordinadores/<int:pk>/) | Retorna el detalle de un coordinador según el ID ingresado |
|GET| [/servicios](http://localhost:8000/api/servicios/)| Retorna el listado de datos de todos los servicios activos que tiene la empresa |
|GET|  [/servicios/id](http://localhost:8000/api/servicios/<int:pk>/) | Retorna el detalle de un servicio especifico según el ID ingresado |
|GET| [/reservas_servicios](http://localhost:8000/api/reservas_servicios/)| Retorna el listado de las reservas realizadas por los clientes |
|GET|  [/reservas_servicios/id](http://localhost:8000/api/reservas_servicios/<int:pk>/) | Retorna el detalle de una reserva según el ID de la misma |


### Requerimientos técnicos

- asgiref 3.7.2
- Djando 4.2.7
- djangorestframework 3.14.0
- Jinja2 3.1.2
- MarkupSafe 2.1.3
- pytz 2023.3.post1
- tzdata 2023.3