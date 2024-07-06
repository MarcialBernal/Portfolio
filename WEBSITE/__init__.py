from flask import Flask
from config import ProductionConfig, DevelopmentConfig

app = Flask(__name__)

if app.config['ENV'] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

from WEBSITE import routes