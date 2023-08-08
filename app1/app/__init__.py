from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.dev')

    db.init_app(app)

    from app.routes import app_bp
    app.register_blueprint(app_bp, url_prefix='/api')

    return app
