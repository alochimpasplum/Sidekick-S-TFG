import tensorflow as tf
import numpy as np
import pandas as pd
import keras
import os
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import RMSprop

datagen = ImageDataGenerator()

datasets_folder: str = "./Datasets/handwritten_math_symbols_ready"


train_it = datagen.flow_from_directory(datasets_folder + '/train', class_mode='binary', target_size=(45, 45),
                                       batch_size=64, color_mode="grayscale")
val_it = datagen.flow_from_directory(datasets_folder + '/validation', class_mode='binary', target_size=(45, 45),
                                     batch_size=64, color_mode="grayscale")

model = tf.keras.models.Sequential([
    # Note the input shape is the desired size of the image 150x150 with 3 bytes color
    tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu', input_shape=(45, 45, 1)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # Flatten the results to feed into a DNN
    tf.keras.layers.Flatten(),
    # 512 neuron hidden layer
    tf.keras.layers.Dense(512, activation='relu')
])

model.compile(optimizer=RMSprop(learning_rate=1e-4),
              loss='sparse_categorical_crossentropy',
              metrics = ['accuracy'])

model.fit_generator(train_it, steps_per_epoch=16, validation_data=val_it, validation_steps=8)

model.summary()

history = model.fit(
      train_it,
      steps_per_epoch=500,
      epochs=100,
      validation_data=val_it,
      validation_steps=50,
      verbose=2)

model.save('model_math_symbols')
