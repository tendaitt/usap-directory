# services/server/src/__init__.py

from flask import Flask


def create_app():

    # instantiate app
    app = Flask(__name__)

    # set configs
    # app_settings = os.getenv("APP_SETTINGS")
    # app.config.from_object(app_settings)

    # register api to flask
    from src.api import api

    api.init_app(app)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app}

    return app
