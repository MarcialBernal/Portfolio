from flask import Flask
from tensorflow.keras.preprocessing import image
import numpy as np
import joblib
from FLOWER_CLASS import routes


###########################      #################################

app = Flask(__name__)

###########################      #################################
app.register_blueprint(routes.flower_pred)
###########################      #################################


###########################      #################################

###########################      #################################

###########################      #################################

from FLOWER_CLASS import routes