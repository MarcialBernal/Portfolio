
# ------------------------
# Loading model from disk
# ------------------------
import tensorflow as tf
import os

def loadModelH5():

    MODEL_H5_FILE = "flowers_model_full_tf2.h5"
    MODEL_H5_PATH = "DEEP-LEARNING_deployment/tf2x/keras/full"

    # Cargar el modelo DL desde disco
    loaded_model = tf.keras.models.load_model(MODEL_H5_PATH + MODEL_H5_FILE)
    print(MODEL_H5_FILE, " Loading from disk >> ", loaded_model)

    return loaded_model

