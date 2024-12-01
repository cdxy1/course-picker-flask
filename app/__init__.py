from flask import Flask

from app.config import Config
from app.extensions import db
from app.routes.user import user


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(user)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
