# Dumbdumb: dummy API

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-31011/)

## Local development

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then edit your API and test it in Swagger (http://127.0.0.1:8000/docs).

You can also build and run the docker image with `docker build -t dumbdumb . && docker run -p 8080:8080 -it dumbdumb`.

## Deployment

Install the [Fly.io](https://fly.io/docs/hands-on/install-flyctl/) CLI, sign up/sign in (`fly auth signup`, `fly auth login`), then run `fly launch` and follow the instructions.

The app while then be available through `https://dumbdumb.fly.dev/` (`https://dumbdumb.fly.dev/docs` for the swagger interface).
