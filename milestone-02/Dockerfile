# Stage 1: Build Stage
FROM python:3.9.20-alpine3.20 AS build-stage

# Set working directory
WORKDIR /flask-app

# Install required system dependencies
RUN apk update && \
    apk add libpq-dev \  
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file to the container
# RUN mkdir -p /flask-app/app /flask-app/migartions /flask-app/migartions/versions/

# COPY requirements.txt .
# 
# COPY app/__init__.py /flask-app/app 
# COPY app/models.py /flask-app/app 
# COPY app/routes.py /flask-app/app 
# COPY app/schemas.py /flask-app/app 
# COPY app/utils.py /flask-app/app 
# 
# COPY migrations/alembic.ini /flask-app/migartions/
# COPY migrations/env.py /flask-app/migartions/
# COPY migrations/README /flask-app/migartions/
# COPY migrations/script.py.mako /flask-app/migartions/
# 
# COPY migrations/versions/687592955894_create_student_table_with_name_age_and_.py  /flask-app/migartions/versions/
# COPY migrations/versions/a39a02475e4a_main_687592955894.py  /flask-app/migartions/versions/
# COPY migrations/versions/ce1567562de8_merge_heads.py  /flask-app/migartions/versions/
# COPY migrations/versions/d0ff8dcdef1b_merge_heads.py  /flask-app/migartions/versions/
# COPY migrations/versions/d82742c929ea_.py   /flask-app/migartions/versions/
# COPY migrations/versions/e0444c82c76a_merged_latest_heads.py   /flask-app/migartions/versions/
# COPY migrations/versions/ecbd600814a7_.py   /flask-app/migartions/versions/
# 
# COPY .env /flask-app/

ADD app /flask-app/app
ADD migrations /flask-app/migrations
COPY .env /flask-app/
COPY requirements.txt /flask-app/

# Activate the virtual environment and install dependencies
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
#COPY . .
#COPY app /flask-app/
#COPY migrations /flask-app/
#COPY .env /flask-app/

# Stage 2: Poduction Stage (Final)
FROM python:3.9.20-alpine3.20 AS production-stage

# Set working directory
WORKDIR /flask-app

# Depanedency 
COPY --from=build-stage /usr/local/lib/python3.9 /usr/local/lib/python3.9

# Copy the virtual environment and app code from the build stage
COPY --from=build-stage /flask-app /flask-app

# Expose the port the Flask app will run on
EXPOSE 5000

# Default command to activate the virtual environment and start the Flask app
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000" ]
