from flask import Flask
from WEBSITE import app
from FLOWER_CLASS.routes import flower_bp


app.register_blueprint(flower_bp)

if __name__ == "__main__":
    app.run()