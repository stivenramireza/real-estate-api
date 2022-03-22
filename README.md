# Real Estate API

Este proyecto contiene **2 microservicios**, el primero construido sin usar ningún framework y el segundo es conceptual.

La idea principal es tener una herramienta para los usuarios que desean buscar los inmuebles vendidos y disponibles. También, ellos pueden usar diferentes filtros como **status**, **year** y **city**. Adicionalmente, los usuarios pueden darle "Me gusta" a sus inmuebles favoritos con el objetivo de tener un ranking interno.

## 1. Microservicio de búsqueda

### Tecnologías

Las tecnologías usadas fueron:

- **HTTP Server:** Es una librería nativa construida en Python que permite crear un simple servidor HTTP (https://docs.python.org/3/library/http.server.html).
- **Dotenv:** Permite leer los archivos .env y cargarlos en un ambiente como **production**, **staging** o **development** (https://pypi.org/project/python-dotenv/).
- **MySQL Connector:** Es un driver que permite conectarse a un servidor de MySQL fácilmente y acceder a las herramientas que éste ofrece (https://pypi.org/project/mysql-connector/).
- **Unittest:** Es una librería nativa construida en Python que permite testear las aplicaciones y se pueden correr **pruebas unitarias y de integración** (https://docs.python.org/3/library/unittest.html).
- **Black:**  Es una herramienta para formatear y tener un buen entendimiento del código Python. También usa **PEP8** como su guía estándar de estilos (https://pypi.org/project/black/).
- **Docker Swarm:** Es un herramienta orquestadora que corre aplicaciones contenerizadas con Docker en modo clúster. En este caso se desplegó la API en un servidor de **Digital Ocean** (https://docs.docker.com/engine/swarm/).
- **Traefik:** Es un proxy inverso HTTP y balanceador de cargas que permite realizar despliegues de microservicios asegurando el protocolo de seguridad HTTPS (https://doc.traefik.io/traefik/).

### Ejecución

#### App en modo desarrollo

Primero que todo se necesita establecer un ambiente de trabajo:

	$ python3.10 -m venv python3.10
    $ source python3.10/bin/activate
    $ pip install -r requirements.txt
    $ source .env.dev

Luego, se procede a ejecutar la app:

    $ python main.py

#### App en modo producción con Docker Compose

    $ docker build -t stivenramireza/real-estate-api:latest .
    $ docker push stivenramireza/real-estate-api:latest
	$ docker-compose up -d
	$ docker logs -f real_estate_api

#### App en modo producción con Docker Swarm y Traefik

    $ docker build -t stivenramireza/real-estate-api:latest .
    $ docker push stivenramireza/real-estate-api:latest
    $ docker stack deploy -c stack.yml production --with-registry-auth
	$ docker service logs -f production_real-estate-api

La ejecución de la **API en producción** se puede ver en el siguiente video de **Loom**:

https://www.loom.com/share/f049c101bb8846fe84b3df0e943b4357

### Pruebas

#### Pruebas unitarias

En este caso se han creado algunas **pruebas unitarias** con el objetivo de verificar que el servicio de propiedades está correctamente funcionando.

    $ python -m unittest tests/**/*.py --verbose

<p align="center">
<img src="https://user-images.githubusercontent.com/31974084/159540017-d690e085-342c-40c6-8617-b21384ac169f.png">
</p>

## 2. Microservicio de "Me gusta"

Este microservicio permite a los usuarios darle un "Me gusta" a un inmueble en específico luego de haberse registrado en la base de datos.

### Diagrama Entidad-Relación

<p align="center">
<img src="https://user-images.githubusercontent.com/31974084/159550727-6760b9c7-d3e7-4453-8365-f5047ea2013d.png">
</p>

El modelo de base de datos se extendería de esta forma porque así podríamos asegurar que un usuario pueda tener múltiples propiedades marcadas con "Me gusta". Por eso es necesario establecer las llaves foráneas de **user_id** y **property_id** haciendo relación a las respectivas tablas de **auth_user** (usuarios registrados)  y **property** (inmuebles).

Adicionalmente se añade un campo **active** que puede resultar útil al momento de hacer **análisis de datos** debido a que podríamos tener registro de los usuarios que antes le había dado "Me gusta" a un inmueble y luego lo quitaron. Esto con el objetivo de establecer una estrategia de negocio, si es el caso, donde se valide con los usuarios en qué momento les dejó de interesar el inmueble y de qué manera podríamos recomendar inmuebles similares o que se ajusten a la nueva necesidad de los clientes.

El código SQL para extender este modelo:

```sql
CREATE TABLE liked_properties ( 
	id INT NOT NULL AUTO_INCREMENT, 
    user_id INT NOT NULL, 
    property_id INT NOT NULL, 
    active BIT,
    create_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id), 
    FOREIGN KEY (user_id) REFERENCES auth_user(id), 
    FOREIGN KEY (property_id) REFERENCES property(id) 
);
```
