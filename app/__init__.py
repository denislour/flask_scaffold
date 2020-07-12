from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from config import config


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    from .core.views import core
    app.register_blueprint(core)

    from .errors.handlers import errors
    app.register_blueprint(errors)

    from .auth.views import auth
    app.register_blueprint(auth, url_prefix="/auth")

    from .context.context_processor import context
    app.register_blueprint(context)

    return app
