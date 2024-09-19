run:
	FLASK_APP=app FLASK_ENV=development flask run --port 5001
#	@echo "Running Flask app"
#	@export $(cat .env | xargs) && FLASK_APP=app FLASK_ENV=development flask run --port 5001


#migrate:
#	FLASK_APP=app flask db migrate -m "Initial migration."
#	FLASK_APP=app flask db upgrade

test:
	#pytest
	PYTHONPATH=./ pytest

#lint:
#	flake8

