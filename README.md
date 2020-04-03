# Back-end application test

## Installation

```
docker-compose build local
```

## Run application

```
docker-compose up local
```
the server will start at http://localhost:8000/


## Authentication

The project use JWT authentication. Before use the endpoints,
you must to authenticate.

To create a superuser, run:

```
docker-compose run --rm local python src/manage.py createsuperuser
```

After you create a customer and get the JWT token, add the header and you
will be able to use the another endpoints:

```
{'Authorization': 'JWT <token>'}
```


## Run tests

```
docker-compose run --rm local python src/manage.py test
```

## Run lint

```
docker-compose run --rm local flake8 src
docker-compose run --rm local pylint src
```

## Documentation

http://localhost:8000/swagger/