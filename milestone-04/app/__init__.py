# pylint: disable=missing-module-docstring
import os
import logging
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from .utils import setup_logging

# Load environment variables.
load_dotenv()

# Initialize database and migration.
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    # Load configuration from environment variables
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize logging, database, and migrations
    setup_logging()
    db.init_app(app)
    migrate.init_app(app, db)

    # Import routes
    with app.app_context():
        from . import routes

        routes.init_app(app)

    # Healthcheck endpoint
    @app.route("/healthcheck", methods=["GET"])
    def healthcheck():
        return "API Service is up and running!", 200

    # Log requests and responses
    @app.before_request
    def log_request_info():
        if request.method in ["POST", "PUT", "PATCH"]:
            logging.info(
                f"{request.method} {request.url}, Body: {request.get_data(as_text=True)}"
            )
        else:
            logging.info(f"{request.method} {request.url}")

    @app.after_request
    def log_response_info(response):
        logging.info(f"Status: {response.status}, Headers: {response.headers}")
        return response

    return app
