# Use the official Python slim image as a base
FROM python:3.9.20-slim-bullseye AS build-stage

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential libpq-dev --no-install-recommends 

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install virtualenv and create a virtual environment
RUN pip install --upgrade pip
RUN pip install virtualenv
RUN virtualenv venv

# Activate the virtual environment and install Python dependencies
RUN . venv/bin/activate && pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

EXPOSE 5001
# Set the default command to use the virtual environment and run the Flask app
CMD ["/bin/bash", "-c", ". venv/bin/activate && make run "]
#CMD ["/bin/bash", "-c", ". venv/bin/activate && flask run --host=0.0.0.0 --port=5001"]

# Expose the port on which the Flask app will run
#EXPOSE 5000

