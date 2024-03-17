# ex_pagination

Este repo ha sido creado con la única intensión de apoyar al tutorial:
## [Usar paginación en vistas genéricas ListView](https://jeremiasenriquez.com/tutoriales/usar-paginacion-en-vistas-genericas-listview/)

### Pasos para el despliegue en entorno local
1. Clonar el repositiorio
```
git clone (url del repo)
```
2. Crear tu entorno de desarrollo Python (recomendado crearlo dentro de la carpeta que se crea al clonar el repo)
```
python -m venv venv
```
3. Instalar los requerimentos
```
pip install -r requirements.txt
```
4. Ejecutar las migraciones
```
python manage.py migrate
```
5. Crear el super usuario (te solicitará los datos en la terminal)
```
python manage.py createsuperuser
```
6. Ejecutar el servidor
```
python manage.py runserver
```

Una vez completados los pasos puedes visitar el sitio web en tu `localhost:8000`

Url del admin `localhost:8000/admin`
