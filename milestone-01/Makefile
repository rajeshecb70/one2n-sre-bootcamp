# Define the virtual environment directory
VENV_DIR = venv

# Define the Python interpreter and pip within the virtual environment
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip

# Target to create the virtual environment if it doesn't exist
$(VENV_DIR)/bin/activate:
	python3 -m venv $(VENV_DIR)

# Target to install dependencies
install: $(VENV_DIR)/bin/activate
	$(PIP) install -r requirements.txt

# Target to run the Flask application
run: install
	@echo 'Checking the Health of API : http://127.0.0.1:5000/healthcheck'
	@echo 'Starting the Flask application...'
	$(PYTHON) -m flask run
	

# Perform a health check on the running Flask app
healthcheck:
	@curl -s http://127.0.0.1:5000/healthcheck || echo 'Health check failed or service is not running'

# Target to run everything (virtual env setup, dependencies installation, and running Flask)
all: install run
	@echo 'Run the above URL(s) on the browser to interact with the application.'

# Target to clean up the virtual environment
clean:
	rm -rf $(VENV_DIR)

# Test the application 
test:
	pytest
	

