from dotenv import load_dotenv
import os

####################    ####################  

load_dotenv()


class Config:
    DEBUG = False
    TESTING = False
    FLASK_ENV = os.getenv('FLASK_ENV')


class DevelopmentConfig(Config):
    DEBUG = True
    


class ProductionConfig(Config):
    DEBUG = False
    
    