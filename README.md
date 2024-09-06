# Gestion Tic Unisinú

# Gestión de Inventario de Dispositivos TICs

Aplicación web para gestionar el inventario de dispositivos de una institucion universitaria.

## Descripción

Esta aplicación permite registrar, actualizar y consultar información sobre dispositivos corporativos asignados a los funcionarios administrativos.

### Ofrece funcionalidades para:

- Registrar y catalogar dispositivos ✍
- Actualizar estados y detalles de los dispositivos 🖊
- Realizar búsquedas rápidas por diferentes criterios 🔎
- Conocer el usuario asiganado a determinado dispositivos
- Generar informes de inventario

## Funcionamiento

- Base de datos centralizada para almacenar información de dispositivos
- Interfaz web administrativa intuitiva para agregar, editar y eliminar registros
- Sistema de autenticación y autorización
- Reportes personalizados y filtros avanzados

## Tecnologías

- Python 3.12
- Django==5.0.6
- MySQL
- HTML/CSS
- Git

## Instalación

### 1. Clonar el repositorio:

```
git clone https://github.com/Dannjader/GestionTic
```

### 2. Crear y activar un entorno virtual de python

    - En linux ejecuta :

```
python3 -m venv venv
```

```
source ./venv/bin/activate
```

    - En Windows ejecuta :

```
py -m venv venv
```

```
.\venv\Scripts\activate
```

### 3. Instalar dependencias:

```
pip install -r requeriments.txt
```

### 4. Aplica las migraciones:

    - En linux

```
python3 manage.py migrate
```
* En windows

```
py manage.py migrate
```


### 5. Corre la aplicación:
~~~
python manage.py runserver
~~~

## Uso

1. Accede a la interfaz web en http://127.0.0.1:8000/admin
2. Inicia sesión con tu cuenta de administrador
3. Navega por las secciones para agregar, editar o eliminar dispositivos
4. Utiliza los filtros y reportes para analizar el inventario
