#!/bin/sh
echo "Running database migrations..."
flask db upgrade  # Replace this with your actual migration command
echo "Database migrations completed."
