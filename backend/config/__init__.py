from flask import Flask
from backend.config.settings import Config
from backend import db

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    return app