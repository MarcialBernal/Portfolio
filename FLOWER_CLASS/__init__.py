from flask import Flask, Blueprint
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from FLOWER_CLASS import app

###########################      #################################

app = Flask(__name__)

###########################      #################################

flower_pred = Blueprint('flower_pred', __name__, static_folder="static", template_folder="templates")

###########################      #################################

model_path = 'model/flower_classifier_model.h5'
model = load_model(model_path)

###########################      #################################

flower_dict = {0: 'margarita', 1: 'diente de león', 2: 'rosa', 3: 'girasol', 4: 'tulipán'}

def predict_flower(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    predictions = model.predict(img_array)
    return flower_dict[np.argmax(predictions)]

###########################      #################################



###########################      #################################

from FLOWER_CLASS import routes