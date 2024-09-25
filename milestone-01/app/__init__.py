from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import logging
from .utils import setup_logging
from dotenv import load_dotenv
from flask_migrate import Migrate

# Load environment variables from .env file (optional)
load_dotenv()

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    # Load configuration from environment variables
    # Fallback to a default DB if env var is not set
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Set up logging
    setup_logging()

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from . import routes
        routes.init_app(app)
        # Create all tables (if they don't exist yet)
        db.create_all()

    # Healthcheck endpoint
    @app.route('/healthcheck', methods=['GET'])
    def healthcheck():
        return 'Hi, The Web REST API Service is up and running!', 200

    # Log each request
    @app.before_request
    def log_request_info():
        logging.info(f'Received {request.method} request for {request.url}')
        logging.info(f'Request headers: {request.headers}')
        if request.method in ['POST', 'PUT', 'PATCH']:
            logging.info(f'Request body: {request.get_data(as_text=True)}')

    @app.after_request
    def log_response_info(response):
        logging.info(f'Response status: {response.status}')
        logging.info(f'Response headers: {response.headers}')
        return response
    # Log code end 

    return app
