from flask import Flask

from app.config import Config
from app.extensions import db, migrate, login
from app.routes.main import main
from app.routes.post import post
from app.routes.user import user


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(user)
    app.register_blueprint(post)
    app.register_blueprint(main)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    with app.app_context():
        db.create_all()

    return app
