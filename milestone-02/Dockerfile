FROM python:3.11-slim AS build-stage


# Set working directory
WORKDIR /app

# Install required system dependencies (Alpine does not use apt, but slim does)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install pip and create a virtual environment
RUN python -m venv venv

# Activate the Virtual Environment and install dependencies
RUN ./venv/bin/pip install --upgrade pip && ./venv/bin/pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the Flask app will run on
EXPOSE 5000

# Default command to activate the virtual environment and start the Flask app
CMD ["/bin/bash", "-c", ". venv/bin/activate && flask run", "0.0.0.0:5000"]