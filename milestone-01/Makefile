# Variables
VENV_DIR = venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip
DB_USER = root
DB_PASSWORD = newpassword
DB_HOST = localhost
DB_PORT = 3306
DB_NAME = studentdb1
TEST_DB_NAME = test_db


# Check if the virtual environment exists, if not, create it
$(VENV_DIR)/bin/activate: requirements.txt
	@test -d $(VENV_DIR) || python3 -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Install dependencies inside the virtual environment
install: $(VENV_DIR)/bin/activate
	$(PIP) install -r requirements.txt

# Check if MySQL is installed and user is created, then create the databases if they don't exist
check_mysql:
	@command -v mysql >/dev/null 2>&1 || { echo >&2 "MySQL is not installed. Aborting."; exit 1; }

# Reset Alembic version table in MySQL (if it exists)
reset_alembic:
	@mysql -u $(DB_USER) -p$(DB_PASSWORD) -e "DROP TABLE IF EXISTS $(DB_NAME).alembic_version;"

# Initialize Alembic (if not already initialized)
alembic_init:
	@test -f migrations/env.py || flask db init

# Generate a new migration based on the models.py schema
migrate: alembic_init
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
all: install check_mysql reset_alembic migrate upgrade start

# Cleanup: remove virtual environment and other generated files (but not migrations)
clean:
	rm -rf $(VENV_DIR)
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	

# Full cleanup, including Alembic migrations (use with caution)
clean-full: clean
	rm -rvf .mypy_cache

# PHONY target tells make that these are not files
#.PHONY: install check_mysql reset_alembic alembic_init migrate upgrade start resume create_test_db test all clean clean_full
