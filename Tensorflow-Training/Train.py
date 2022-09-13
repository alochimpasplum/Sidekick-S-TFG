import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
import keras
import os

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

if tf.test.gpu_device_name():
    print('GPU found')
else:
    print("No GPU found")

mnist = keras.datasets.mnist
(train_images_mnist,train_labels_mnist),(test_images_mnist,test_labels_mnist) = mnist.load_data()

train_images_mnist = np.reshape(train_images_mnist,(train_images_mnist.shape[0],28,28,1))
test_images_mnist = np.reshape(test_images_mnist,(test_images_mnist.shape[0],28,28,1))

# download from https://www.kaggle.com/datasets/sachinpatel21/az-handwritten-alphabets-in-csv-format
# download from https://www.kaggle.com/datasets/sagyamthapa/handwritten-math-symbols
az_data_path = './Datasets/handwritingdataset'
AZ_data = pd.read_csv(az_data_path +'/A_Z Handwritten Data.csv',header = None)
# the first column contains label values, while the remaining are the flattened array of 28 x 28 image pixels
AZ_labels = AZ_data.values[:,0]
AZ_images = AZ_data.values[:,1:]
# images are reshaped to be used by the flow method of a keras ImageGenerator
AZ_images = np.reshape(AZ_images,(AZ_images.shape[0], 28, 28, 1))

math_symbols_path = './Datasets/math_symbols.csv'
math_symbols_data = pd.read_csv(math_symbols_path, header=None)
math_symbols_labels = math_symbols_data.values[:, 0]
math_symbols_images = math_symbols_data.values[:, 1:]
math_symbols_images = np.reshape(math_symbols_images, (math_symbols_images.shape[0], 28, 28, 1))

# join datasets
# split AZ data in train and test
from sklearn.model_selection import train_test_split

test_size_AZ = float(len(test_labels_mnist))/len(train_labels_mnist)
print(f'AZ test set size: {test_size_AZ}')
train_images_AZ, test_images_AZ, train_labels_AZ, test_labels_AZ = train_test_split(AZ_images,AZ_labels, test_size=test_size_AZ)
#shift mnist labels
train_labels_mnist = train_labels_mnist + max(AZ_labels)+1
test_labels_mnist = test_labels_mnist + max(AZ_labels)+1

test_size_math = float(len(test_labels_mnist))/len(math_symbols_labels)
print(f'Math test set size: {test_size_math}')
train_images_math, test_images_math, train_labels_math, test_labels_math = train_test_split(math_symbols_images,math_symbols_labels, test_size=test_size_math)


# concatenate datasets
train_images = np.concatenate((train_images_AZ,train_images_mnist, train_images_math),axis=0)
train_labels = np.concatenate((train_labels_AZ,train_labels_mnist, train_labels_math))
test_images = np.concatenate((test_images_AZ,test_images_mnist, test_images_math),axis=0)
test_labels = np.concatenate((test_labels_AZ,test_labels_mnist, test_labels_math))

print('Data ready')

from keras.optimizers import RMSprop
model = tf.keras.models.Sequential([
    # Note the input shape is the desired size of the image 150x150 with 3 bytes color
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # Flatten the results to feed into a DNN
    tf.keras.layers.Flatten(),
    # 512 neuron hidden layer
    tf.keras.layers.Dense(512, activation='relu'),
    # Only 1 output neuron. It will contain a value from 0-1 where 0 for 1 class ('cats') and 1 for the other ('dogs')
    tf.keras.layers.Dense(len(np.unique(train_labels)), activation='softmax')
])

model.compile(optimizer=RMSprop(learning_rate=1e-4),
              loss='sparse_categorical_crossentropy',
              metrics = ['accuracy'])

model.summary()

from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(
      rescale=1./255,
      rotation_range=15,
      width_shift_range=0.1,
      height_shift_range=0.1,
      shear_range=0.1,
      zoom_range=0.2,
      horizontal_flip=False,
      fill_mode='nearest')

test_datagen = ImageDataGenerator(rescale=1./255)

# Flow training images in batches using generator
train_generator = train_datagen.flow(train_images, train_labels, batch_size=50, shuffle=True)
validation_generator = test_datagen.flow(test_images, test_labels, batch_size=50, shuffle=True)

history = model.fit(
      train_generator,
      steps_per_epoch=500,
      epochs=10,
      validation_data=validation_generator,
      validation_steps=50,
      verbose=2)
model.save('model_full.h5')
