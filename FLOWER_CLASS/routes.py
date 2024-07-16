from FLOWER_CLASS import app, predict_flower
from flask import render_template, request

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        file_path = os.path.join('static', file.filename)
        file.save(file_path)
        prediction = predict_flower(file_path)
        return render_template('index.html', prediction=prediction, img_path=file_path)
    return render_template('index.html', prediction=None)