# apitemplate

[![Build Status](https://travis-ci.org/luckyadogun/apitemplate.svg?branch=master)](https://travis-ci.org/luckyadogun/apitemplate)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

App templates from rapidmvp. Check out the project's [documentation](http://luckyadogun.github.io/apitemplate/).

# Features:
Just clone it, add your features, deploy

- JWT/Social Authentication
- Deployment ready (Heroku)
- CORS handling
- Bring Your Config


# Prerequisites
- [Heroku](https://dashboard.heroku.com)
- [Docker](https://docs.docker.com/docker-for-mac/install/)  

# Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

# Production Environment (Heroku optimized)
### Heroku Config Vars
```bash
DATABASE_URL: ***
DJANGO_AWS_ACCESS_KEY_ID: ***
DJANGO_AWS_REGION: ***
DJANGO_AWS_SECRET_ACCESS_KEY: ***
DJANGO_AWS_STORAGE_BUCKET_NAME: ***
DJANGO_DEBUG: ***
DJANGO_SECRET_KEY: ***
DJANGO_SUPERUSER_EMAIL: ***
DJANGO_SUPERUSER_PASSWORD: ***
```
### Heroku Deploy Commands:
- Login:
```bash
heroku container:login
```
- Build the image:
```bash
# Apple Mac/ARM (M1):
docker buildx -t registry.heroku.com/<app_name>/web .
# Non-M1 Machines:
docker build -t registry.heroku.com/<app_name>/web .
```
- Push to the registry:
```bash
docker push registry.heroku.com/<app_name>/web
```
- Release the image:
```bash
heroku container:release -a <app_name> web
```