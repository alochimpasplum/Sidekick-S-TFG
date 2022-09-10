from keras.models import load_model
import tensorflow as tf
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
import os

import imutils
from imutils.contours import sort_contours

# https://deepnote.com/@davidespalla/Recognizing-handwriting-with-Tensorflow-and-OpenCV-cfc4acf5-188e-4d3b-bdb5-a13aa463d2b0

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

if tf.test.gpu_device_name():
    print('GPU found')
else:
    print("No GPU found")

# loads the model with the keras load_model function
model_path = 'model_v2'
print("Loading NN model...")
model = load_model(model_path)
print("Done")

# loads the input image
image_path = './tests/HelloWorld2.jpg'
image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cropped = gray[120:,:]
blurred = cv2.GaussianBlur(gray, (5, 5), 0)


edged = cv2.Canny(blurred, 30, 250) #low_threshold, high_threshold
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sort_contours(cnts, method="left-to-right")[0]

chars = []
# loop over the contours
for c in cnts:
    # compute the bounding box of the contour and isolate ROI
    (x, y, w, h) = cv2.boundingRect(c)
    roi = gray[y:y + h, x:x + w]

    # binarize image, finds threshold with OTSU method
    thresh = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    # resize largest dimension to input size
    (tH, tW) = thresh.shape
    if tW > tH:
        thresh = imutils.resize(thresh, width=28)
    # otherwise, resize along the height
    else:
        thresh = imutils.resize(thresh, height=28)

    # find how much is needed to pad
    (tH, tW) = thresh.shape
    dX = int(max(0, 28 - tW) / 2.0)
    dY = int(max(0, 28 - tH) / 2.0)
    # pad the image and force 28 x 28 dimensions
    padded = cv2.copyMakeBorder(thresh, top=dY, bottom=dY,
                                left=dX, right=dX, borderType=cv2.BORDER_CONSTANT,
                                value=(0, 0, 0))
    padded = cv2.resize(padded, (28, 28))
    # reshape and rescale padded image for the model
    padded = padded.astype("float32") / 255.0
    padded = np.expand_dims(padded, axis=-1)
    # append image and bounding box data in char list
    chars.append((padded, (x, y, w, h)))

boxes = [b[1] for b in chars]
chars = np.array([c[0] for c in chars], dtype="float32")
# OCR the characters using our handwriting recognition model
preds = model.predict(chars)
# define the list of label names
labelNames = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

image = cv2.imread(image_path)

for (pred, (x, y, w, h)) in zip(preds, boxes):
    # find the index of the label with the largest corresponding
    # probability, then extract the probability and label
  i = np.argmax(pred)
  prob = pred[i]
  label = labelNames[i]
  # draw the prediction on the image and it's probability
  label_text = f"{label},{prob * 100:.1f}%"
  cv2.rectangle(image, (x, y), (x + w, y + h), (0,255 , 0), 2)
  cv2.putText(image, label_text, (x - 10, y - 10),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0,255, 0), 1)

cv2.imwrite('edged.png', edged)
cv2.imwrite('predictions.png', image)
