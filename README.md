# Web IDE

#### :warning: This project is not suitable for production environment :warning:

This is a simple Online IDE created using Django, Django Channels and Docker.
It uses docker-in-docker (dind) to spin up docker containers for each user. 
The code runs inside the users isolated docker container.

Currently, it only supports python but more language support can be added easily.

## Run Project

**Build and Run The Project**

```console
docker-compose up --build
```

**Create a Super User**

```console
docker-compose exec web python3 manage.py createsuperuser
```


Then navigate to `http://127.0.0.1:8000/` and login to use the IDE

## Demo:

![Web_IDE](https://user-images.githubusercontent.com/24854406/129922226-5f834259-a2ae-45ac-90f6-d7f5f1d993cf.gif)

