# Real Estate API

This project contains a **microservice** built without using any framework like Flask, Django o FastAPI.

The main idea is having a tool for users who want to search about the available and sold properties . Also, they can use different filters like **status**, **year** and **city**.

## Technologies

The used technologies were:

- **HTTP Server:** It's a native library built in Python who lets you create a simple HTTP server (https://docs.python.org/3/library/http.server.html).
- **Dotenv:** It lets you read some .env files and loads into an environment like **production**, **staging** or **development** (https://pypi.org/project/python-dotenv/).
- **MySQL Connector:** It's a driver to connect to MySQL server easily and use the differents tools that it offers (https://pypi.org/project/mysql-connector/).
- **Unittest:** It's a native library built in Python who lets you test the applications and you can run **unit** and **integration** tests (https://docs.python.org/3/library/unittest.html).
- **Black:**  It's a formatter to have a good understanding of the Python code. It also uses **PEP8** as its standard style guides (https://pypi.org/project/black/).
- **Docker Swarm:** It's an orchestration management tool that runs on Docker applications.in cluster mode. In this case we use to deploy the API in a **Digital Ocean** server (https://docs.docker.com/engine/swarm/).
- **Traefik:** It's an HTTP reverse proxy and load balance to deploy the microservice ensuring the HTTPS protocol (https://doc.traefik.io/traefik/).

## How to run

### Run app in development mode

First of all, you need to have a working environment.

	$ python3.10 -m venv python3.10
    $ source python3.10/bin/activate
    $ pip install -r requirements.txt
    $ source .env.dev

Later, you can run it:

    $ python main.py

### Run app in production mode with Docker Compose

    $ docker build -t stivenramireza/real-estate-api:latest .
    $ docker push stivenramireza/real-estate-api:latest
	$ docker-compose up -d
	$ docker logs -f real_estate_api

### Run app in production mode with Docker Swarm + Traefik

    $ docker build -t stivenramireza/real-estate-api:latest .
    $ docker push stivenramireza/real-estate-api:latest
    $ docker stack deploy -c stack.yml production --with-registry-auth
	$ docker service logs -f production_real-estate-api

You can check the app running in production mode via **Loom**: https://www.loom.com/share/f049c101bb8846fe84b3df0e943b4357

## Tests

### Run tests

In this case we've created some **unit tests** in order to check that the property service is ok.

    $ python -m unittest tests/**/*.py --verbose

<p align="center">
<img src="https://user-images.githubusercontent.com/31974084/159540017-d690e085-342c-40c6-8617-b21384ac169f.png">
</p>
