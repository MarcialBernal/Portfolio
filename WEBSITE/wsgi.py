####################  01  ####################

from flask import Flask, render_template, send_from_directory
from config import DevelopmentConfig, ProductionConfig
import os


####################  02  ####################

if os.getenv('FLASK_ENV') == 'production':
    app_config = ProductionConfig
else:
    app_config = DevelopmentConfig
 
####################  03  ####################   

app = Flask(__name__)

app.config.from_object(app_config)

####################  04  ####################  

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/download_cv')
def download_cv():
    return send_from_directory(directory='static', filename='CV.pdf')


####################  05  ####################

if __name__ == '__main__':
    app.run()