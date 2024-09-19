from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import logging
from .utils import setup_logging

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    
    # Load configuration from environment variables
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'mysql+pymysql://root:one2n1234(Rajesh@localhost/studentdb')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)
    setup_logging()

    with app.app_context():
        from . import routes
        routes.init_app(app)
        db.create_all()

    @app.route('/healthcheck', methods=['GET'])
    def healthcheck():
        return 'Service is up and running!', 200

    return app

