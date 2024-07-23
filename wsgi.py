from WEBSITE import app
from FLOWER_CLASS import flower_pred

app.register_blueprint(flower_pred, url_prefix='/flowers')

if __name__ == "__main__":
    app.run() 