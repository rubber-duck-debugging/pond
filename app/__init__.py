import os
from config import config
from flask import Flask, redirect, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate =  Migrate()


def createApp(configName):
    app = Flask(__name__)
    app.config.from_object(config[configName])
    config[configName].init_app(app)

    db.init_app(app)
    migrate.init_app(app)
    # csrf.init_app(app)
    # login_manager.init_app(app)
    # admin.init_app(app)

    from .blueprints.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
