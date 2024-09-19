from flask import render_template, request, Blueprint
from .utils import predict_flower 
from . import app
import os

flower_bp = Blueprint('flower_bp', __name__, static_folder="static", template_folder="templates")

@flower_bp.route('/pred', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        
        # Ruta absoluta para el directorio 'static'
        static_folder = os.path.join(app.root_path, 'static')
        file_path = os.path.join(static_folder, file.filename)
        
        # Asegúrate de que la carpeta exista
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Guarda el archivo
        file.save(file_path)

        # Genera la predicción
        prediction = predict_flower(file_path)

        # Prepara la ruta relativa para enviar a la plantilla
        img_path = os.path.join('static', file.filename)

        return render_template('classif/index.html', prediction=prediction, img_path=img_path)
    
    return render_template('classif/index.html', prediction=None)