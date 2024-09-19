SHELL := /bin/bash

run: install
	FLASK_APP=app FLASK_ENV=development flask run --port 5001

test:
	PYTHONPATH=./ pytest

lint:
	flake8

activate:
	source venv/bin/activate

install:activate
	pip install -r requirements.txt