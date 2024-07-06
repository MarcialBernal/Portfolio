
from WEBSITE import app
from flask import render_template, send_from_directory


####################    ####################  

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/download_cv')
def download_cv():
    return send_from_directory(directory='static', filename='CV.pdf')


