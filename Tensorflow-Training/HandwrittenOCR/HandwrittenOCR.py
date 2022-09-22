# https://deepnote.com/@davidespalla/Recognizing-handwriting-with-Tensorflow-and-OpenCV-cfc4acf5-188e-4d3b-bdb5-a13aa463d2b0
from keras.models import load_model
import numpy as np
import pandas as pd
import os
import imutils
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from imutils.contours import sort_contours


def HandWrittenOCR(img_path: str, threshold: float = 0.001, get_predictions: bool = False):
    threshold: float = threshold

    base = os.path.basename(img_path)
    filename = os.path.splitext(base)[0]

    # Do not use GPU if CUDA is not configured
    os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

    # loads the model
    model_path = 'HandwrittenOCR/model_full.h5'
    model = load_model(model_path)

    # loads the input image
    image = cv2.imread(img_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cropped = gray[120:,:]
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    edged = cv2.Canny(blurred, 30, 250)  # low_threshold, high_threshold
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
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
    labelNames = {
        0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J",
        10: "K", 11: "L", 12: "M", 13: "N", 14: "O", 15: "P", 16: "Q", 17: "R", 18: "S", 19: "T",
        20: "U", 21: "V", 22: "W", 23: "X", 24: "Y", 25: "Z", 26: "0", 27: "1", 28: "2", 29: "3",
        30: "4", 31: "5", 32: "6", 33: "7", 34: "8", 35: "9", 36: "-", 37: "(", 38: ")", 39: "+",
        40: "=", 41: "div", 42: "geq", 43: "gt", 44: "lt", 45: "leq", 46: "neq"}

    label_preds = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0,
        10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0,
        20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0,
        30: 0, 31: 0, 32: 0, 33: 0, 34: 0, 35: 0, 36: 0, 37: 0, 38: 0, 39: 0,
        40: 0, 41: 0, 42: 0, 43: 0, 44: 0, 45: 0, 46: 0}

    image = cv2.imread(img_path)

    for (pred, (x, y, w, h)) in zip(preds, boxes):
        # find the index of the label with the largest corresponding
        # probability, then extract the probability and label
        for index, p in enumerate(pred):
            label_preds[index] = label_preds[index] + p

        i = np.argmax(pred)
        prob = pred[i]
        label = labelNames[i]
        # draw the prediction on the image and it's probability
        label_text = f"{label},{prob * 100:.1f}%"
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, label_text, (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    if get_predictions:
        line: [str] = ""
        for key, value in label_preds.items():
            value = value / len(preds)
            if value < 0.001:
                value = 0
            line += "{}\t".format(value)
        line = line.replace(".", ",")

        f = open("HandwrittenOCR/tests/results/{}.txt".format(filename), "w")
        f.write(line)
        f.close()

        cv2.imwrite('HandwrittenOCR/tests/results/{}_edged.png'.format(filename), edged)
        cv2.imwrite('HandwrittenOCR/tests/results/{}_predictions.png'.format(filename), image)
