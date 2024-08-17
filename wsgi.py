from flask import Flask

from WEBSITE import app
from FLOWER_CLASS.routes import flower_pred


def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(flower_pred)

    return app