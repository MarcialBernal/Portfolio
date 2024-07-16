import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow.keras import layers, models
import numpy as np

# Cargar el dataset
dataset, info = tfds.load('tf_flowers', with_info=True, as_supervised=True)

# Función de preprocesamiento
def preprocess(image, label):
    image = tf.image.resize(image, (224, 224)) / 255.0  # Redimensionar y normalizar
    return image, label

# Separar el dataset en entrenamiento y prueba (80%-20%)
data = dataset['train']
data = data.shuffle(1000, reshuffle_each_iteration=False)
train_size = int(0.8 * len(data))

train_dataset = data.take(train_size)
test_dataset = data.skip(train_size)

train_dataset = train_dataset.map(preprocess).batch(32).shuffle(buffer_size=1000)
test_dataset = test_dataset.map(preprocess).batch(32)

# Construir el modelo de CNN
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(5, activation='softmax')  # 5 categorías de flores
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
history = model.fit(train_dataset, epochs=10, validation_data=test_dataset)

# Guardar el modelo entrenado
model.save('flower_classifier_model.h5')