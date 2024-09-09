from flask import Flask
from dotenv import load_dotenv
from config import DevelopmentConfig, ProductionConfig
import os
from FLOWER_CLASS.routes import flower_bp 

####################    ####################  

load_dotenv()

app = Flask(__name__)

app.register_blueprint(flower_bp, url_prefix='/flowers')

if os.getenv("FLASK_ENV") == "production":
    app.config.from_object(ProductionConfig)
    
elif os.getenv("FLASK_ENV") == "development":
    app.config.from_object(DevelopmentConfig)
    
####################    ####################  

from WEBSITE import routes
