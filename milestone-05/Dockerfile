# Stage 1: Build Stage
FROM python:3.9.20-alpine3.20 AS build-stage

# Set working directory
WORKDIR /flask-app

# Install required system dependencies
RUN apk update && \
    apk add libpq-dev \  
    && rm -rf /var/lib/apt/lists/*

# Copy the rest of the application code into the container
ADD app /flask-app/app
ADD migrations /flask-app/migrations
COPY requirements.txt run.sh /flask-app/
RUN chmod +x /flask-app/run.sh

# Activate the virtual environment and install dependencies
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Stage 2: Poduction Stage (Final)
FROM python:3.9.20-alpine3.20 AS production-stage

# Set working directory
WORKDIR /flask-app

# Depanedency 
COPY --from=build-stage /usr/local/lib/python3.9 /usr/local/lib/python3.9

# Copy the virtual environment and app code from the build stage
COPY --from=build-stage /flask-app /flask-app

# Set environment variables
ENV FLASK_APP=app/__init__.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Expose the port the Flask app will run on
EXPOSE 5000

# Default command to activate the virtual environment and start the Flask app
# CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000" ]
# Run the run.sh script
ENTRYPOINT ["sh", "/flask-app/run.sh"]