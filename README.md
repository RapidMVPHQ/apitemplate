# apitemplate

[![Build Status](https://travis-ci.org/luckyadogun/apitemplate.svg?branch=master)](https://travis-ci.org/luckyadogun/apitemplate)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

App templates from rapidmvp. Check out the project's [documentation](http://luckyadogun.github.io/apitemplate/).

# Prerequisites

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