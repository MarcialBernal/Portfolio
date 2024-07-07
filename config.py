from dotenv import load_dotenv

####################    ####################  

load_dotenv()


class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = "development"

class ProductionConfig(Config):
    DEBUG = False
    FLASK_ENV = "production"
    
    