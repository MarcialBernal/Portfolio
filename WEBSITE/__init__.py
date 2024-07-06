from flask import Flask
from dotenv import load_dotenv
from config import DevelopmentConfig, ProductionConfig
import os

load_dotenv()

app = Flask(__name__)

if os.getenv("FLASK_ENV") == "production":
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)
    

print(f"Flask running in {app.config['FLASK_ENV']} mode")

from WEBSITE import routes
