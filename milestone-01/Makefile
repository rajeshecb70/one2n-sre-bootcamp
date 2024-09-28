ifneq (,$(wildcard ./.env))
    include .env
    export
endif

# Check if the virtual environment exists, if not, create it
$(VENV_DIR)/bin/activate: requirements.txt
	@test -d $(VENV_DIR) || python3 -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Install dependencies inside the virtual environment
install: $(VENV_DIR)/bin/activate
	$(PIP) install -r requirements.txt


# Initialize Alembic (if not already initialized)
alembic_init:
	@test -f migrations/env.py || flask db init

# Generate a new migration based on the models.py schema
migrate:
	flask db migrate

# Apply the database migrations (run 'upgrade')
upgrade:
	flask db upgrade

# Apply the database migrations (run 'downgrade')
downgrade:
	flask db downgrade

# Start the Flask application
start: install
	$(PYTHON) -m flask run

# Resume the Flask application without additional setup (restart server)
resume:
	$(PYTHON) -m flask run

# Create MySQL test database if it doesn't exist
create_test_db:
	@mysql -u $(DB_USER) -p$(DB_PASSWORD) -e "CREATE DATABASE IF NOT EXISTS $(TEST_DB_NAME);"

# Run tests using pytest, ensuring the test database exists
test: create_test_db install
	FLASK_ENV=test $(PYTHON) -m pytest

# The 'all' target that runs everything in order
all: install migrate upgrade start

# Cleanup: remove virtual environment and other generated files (but not migrations)
clean:
	rm -rf $(VENV_DIR)
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	

# Full cleanup, including Alembic migrations (use with caution)
clean-full: clean
	rm -rvf .mypy_cache .pytest_cache/
