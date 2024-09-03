from flask import Flask


app = Flask(__name__)

from .routes import flower_bp

app.register_blueprint(flower_bp)

if __name__== '__main__':
    app.run(debug =True)