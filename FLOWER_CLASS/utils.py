from tensorflow.keras.preprocessing import image
import numpy as np
import joblib

model_path = 'C:\\Users\\Marcial\\Desktop\\DEV\\PORTFOLIO\\FLOWER_CLASS\\model\\flower_classifier_model.joblib'
model = joblib.load(model_path)

flower_dict = {0: 'daisy', 1: 'dandelion', 2: 'rose', 3: 'sunflower', 4: 'tulip'}

def predict_flower(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    predictions = model.predict(img_array)
    return flower_dict[np.argmax(predictions)]