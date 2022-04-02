# Real Estate API

This project contains **2 microservices**, the first is built without using any framework and the second is conceptual.

The main idea is having a tool for users who want to search sold and available properties. Also, they can use different filters like **status**, **year** and **city**. In adittion to this, users can like their favorite properties in order to have an internal ranking.

## 1. Search microservice

### Technologies

The used technologies were:

- **HTTP Server:** It's a native library built in Python that allows you create a simple HTTP server (https://docs.python.org/3/library/http.server.html).
- **Dotenv:** It allows you read the .env files and load into an environment like **production**, **staging** or **development** (https://pypi.org/project/python-dotenv/).
- **MySQL Connector:** It's a driver that allows you connect to MySQL server easily and access to the tools that it offers (https://pypi.org/project/mysql-connector/).
- **Unittest:** It's a native library built in Python that allows you test the applications and it can run **unit** and **integration** tests (https://docs.python.org/3/library/unittest.html).
- **Black:** It's a tool to format and have a good understading of the code. It also uses **PEP8** as its standard styles guide (https://pypi.org/project/black/).
- **Docker Swarm:** It's a tool that runs containerized applications with Docker in cluster mode. In this case the application was deployed in a **Digital Ocean** server (https://docs.docker.com/engine/swarm/).
- **Traefik:** It's an HTTP reverse proxy and load balancer that allows you deploy microservices ensuring the HTTPS secure protocol (https://doc.traefik.io/traefik/).

### Execution

#### App in development mode

First of all, you need to have a working environment:

	$ python3.10 -m venv python3.10
    $ source python3.10/bin/activate
    $ pip install -r requirements.txt
    $ source .env.dev

Later, you can run the app:

    $ python main.py

#### App in production mode with Docker Compose

    $ docker build -t stivenramireza/real-estate-api:latest .
    $ docker push stivenramireza/real-estate-api:latest
	$ docker-compose up -d
	$ docker logs -f real_estate_api

#### App in production mode with Docker Swarm and Traefik

    $ docker build -t stivenramireza/real-estate-api:latest .
    $ docker push stivenramireza/real-estate-api:latest
    $ docker stack deploy -c stack.yml production --with-registry-auth
	$ docker service logs -f production_real-estate-api

The execution of the API in production mode was recorded in a **Loom** video that you can check in this link:

https://www.loom.com/share/f049c101bb8846fe84b3df0e943b4357

### Testing

#### Unit tests

In this case some units tests were created in order to check the property service is running successfully.

    $ python -m unittest tests/**/*.py --verbose

<p align="center">
<img src="https://user-images.githubusercontent.com/31974084/159540017-d690e085-342c-40c6-8617-b21384ac169f.png">
</p>

## 2. "Like" microservice

This microservice allows users like a specific property after their register in the database.

### Diagrama Entidad-Relación

<p align="center">
<img src="https://user-images.githubusercontent.com/31974084/159550727-6760b9c7-d3e7-4453-8365-f5047ea2013d.png">
</p>

The database model would extend in this way because we can ensure that a user can have multiple liked properties. For that reason is necessary establish the **user_id** and **property_id** foreign keys related to the **auth_user** (registered users) and **property** (properties) tables respectively.

In addition to this, a new field **active** will be added that can be important for **data analytics** cause we could have a register of the user who liked a property and later unliked it. In this case we need to establish a business strategy, if applicable, where we can validate when users stopped being interested the property and how we could recommend similar properties or they adjust the new necessity of the customers.

The SQL sentence in order to extend this model:

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
