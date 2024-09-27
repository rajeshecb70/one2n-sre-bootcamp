#!/bin/sh

# Check if the RUN_MIGRATION environment variable is set to "true"
if [ "$RUN_MIGRATION" = "true" ]; then
    echo "Running database migrations..."
    flask --app app/__init__.py db upgrade
fi

echo "Starting the Flask server..."
exec python3 -m flask run --host=0.0.0.0 --port=5000
