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
	$(PYTHON) -m flask run
	@echo 'Checking the Health of API : http://127.0.0.1:5000/healthcheck'

# Target for running everything (virtual env setup, dependencies installation, and running Flask)
all: install run
	@echo 'Run below URL on browser to check the application'
	@echo 'http://127.0.0.1:5000/api/v1/students'
	

# Target to clean up the virtual environment
clean:
	rm -rf $(VENV_DIR)
