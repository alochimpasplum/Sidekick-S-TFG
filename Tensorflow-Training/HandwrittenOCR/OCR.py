# https://deepnote.com/@davidespalla/Recognizing-handwriting-with-Tensorflow-and-OpenCV-cfc4acf5-188e-4d3b-bdb5-a13aa463d2b0
import copy

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
from HandwrittenOCR.Letter import Letter


def OCR(img_path: str, threshold: float = 0.001, get_predictions: bool = False, get_all_statistics: bool = False):
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
        chars.append((padded, (x, y, w, h)))

    boxes = [b[1] for b in chars]
    chars = np.array([c[0] for c in chars], dtype="float32")
    # OCR the characters using our handwriting recognition model
    preds = model.predict(chars)
    # define the list of label names
    
    labelPositions = {
        "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9,
        "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19,
        "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25, "0": 26, "1": 27, "2": 28, "3": 29,
        "4": 30, "5": 31, "6": 32, "7": 33, "8": 34, "9": 35, "-": 36, "(": 37, ")": 38, "+": 39,
        "=": 40, "div": 41, "geq": 42, "gt": 43, "lt": 44, "leq": 45, "neq": 46}
    
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
    letters: [Letter] = []

    for (pred, (x, y, w, h)) in zip(preds, boxes):

        i = np.argmax(pred)
        prob = pred[i]
        label = labelNames[i]

        letters.append(Letter(x, x + w, y, y + h, prob, label, i))

    letters = __remove_duplicates__(letters)
    __remove_inner_letters__(letters)
    __fix_e__(letters)
    __fix_h__(letters)
    __fix_i__(letters)

    for letter in letters:
        label_preds[letter.index] = label_preds[letter.index] + letter.confidence

        label_text = f"{letter.value},{letter.confidence * 100:.1f}%"
        cv2.rectangle(image, (letter.x_min, letter.y_min), (letter.x_max, letter.y_max), (0, 255, 0), 1)
        cv2.putText(image, label_text, (letter.x_min - 10, letter.y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    if get_predictions:
        line: [str] = ""
        for key, value in label_preds.items():
            value = value / len(letters)
            if value < 0.001:
                value = 0
            line += "{}\t".format(value)
        line = line.replace(".", ",")

        f = open("HandwrittenOCR/tests/results/{}.txt".format(filename), "w")
        f.write(line)
        f.close()

        cv2.imwrite('HandwrittenOCR/tests/results/{}_edged.png'.format(filename), edged)
        cv2.imwrite('HandwrittenOCR/tests/results/{}_predictions.png'.format(filename), image)

    if get_all_statistics:
        predictions: [str] = [x for x in os.listdir("HandwrittenOCR/tests/results/") if x.endswith(".txt")]

        lines: [str] = [None] * (len(labelPositions) + 2)

        for pred in predictions:
            do_write: bool = True
            f = open("HandwrittenOCR/tests/results/" + pred)
            line = f.readline()
            f.close()
            symbol = os.path.splitext(pred)[0]
            if "%" in symbol:
                lines[len(labelPositions)] = line
                do_write = False
            if "div" in symbol:
                lines[len(labelPositions) + 1] = line
                do_write = False
            if "greater" in symbol:
                symbol = "gt"
            if "less" in symbol:
                symbol = "lt"
            if "multiply" in symbol:
                do_write = False

            if do_write:
                lines[labelPositions[symbol]] = line

        f = open("HandwrittenOCR/tests/results.txt", "w")
        line: str = ""
        for line in lines:
            if line is not None:
                f.write(line + "\n")
            else:
                f.write("\n")
        f.close()

        f = open("HandwrittenOCR/tests/results.txt", "r")
        lines: [str] = f.readlines()

        lines[len(labelPositions)] = lines[len(labelPositions)].replace(",", ".")
        lines[len(labelPositions) + 1] = lines[len(labelPositions) + 1].replace(",", ".")

        div1: [str] = lines[len(labelPositions)].split("\t")
        div2: [str] = lines[len(labelPositions) + 1].split("\t")
        div: str = ""
        for i in range(0, len(labelPositions) - 1):
            prob: float = (float(div1[i]) + float(div2[i])) / 2
            div += "{}\t".format(prob)

        div += "\n"
        div = div.replace(".", ",")
        lines[labelPositions["div"]] = div
        f.close()

        f = open("HandwrittenOCR/tests/results.txt", "w")
        lines[len(labelPositions)] = lines[len(labelPositions)].replace(".", ",")
        lines[len(labelPositions) + 1] = lines[len(labelPositions) + 1].replace(".", ",")
        f.writelines(lines)
        f.close()


def __remove_duplicates__(letters: [Letter]) -> [Letter]:
    letter_seen: [Letter] = []

    for letter in letters:
        if letter not in letter_seen:
            if not __check_seen__(letter_seen, letter):
                letter_seen.append(letter)

    return letter_seen


def __check_seen__(letter_seen: [Letter], letter: Letter) -> bool:
    is_seen: bool = False
    l: Letter
    for l in letter_seen:
        if l.y_min == letter.y_min and l.x_min == letter.x_min and l.y_max == letter.y_max and l.x_max == letter.x_max:
            is_seen = True
    return is_seen


def __remove_inner_letters__(letters: [Letter]) -> None:
    inner_letters: [Letter] = []

    for letter in letters:
        if __check_inner_letter__(letter, letters):
            inner_letters.append(letter)

    for letter in inner_letters:
        letters.remove(letter)


def __check_inner_letter__(letter: Letter, letters: [Letter]) -> bool:
    is_inner: bool = False
    l: Letter
    for l in letters:
        if l is not letter:
            if (l.x_min <= letter.x_min and l.x_max >= letter.x_max and l.y_min <= letter.y_min and
                    l.y_max >= letter.y_max):
                is_inner = True
                break
    return is_inner


def __fix_e__(letters: [Letter]) -> None:
    letter_e: [Letter] = [x for x in letters if x.value == "E"]
    letters_to_remove: [Letter] = []

    for letter in letter_e:
        l: Letter
        for l in letters:
            if l.value != "E":
                middle: [float, float] = [(l.x_min + l.x_max) / 2, (l.y_min + l.y_max) / 2]
                if letter.x_min < middle[0] < letter.x_max and letter.y_min < middle[1] < letter.y_max:
                    if l not in letters_to_remove:
                        letters_to_remove.append(l)

    for letter in letters_to_remove:
        if letter in letters:
            letters.remove(letter)


def __fix_h__(letters: [Letter]) -> None:
    letter_h: [Letter] = [x for x in letters if x.value == "H"]
    letters_to_remove: [Letter] = []

    for letter in letter_h:
        l: Letter
        for l in letters:
            if l.value != "H":
                middle_left: [float, float] = [l.x_min, (l.y_min + l.y_max) / 2]
                middle_right: [float, float] = [l.x_max, (l.y_min + l.y_max) / 2]
                if letter.y_min < middle_left[1] < letter.y_max:
                    if (letter.x_min < middle_left[0] or letter.x_max > middle_right[0]) and\
                            ("(" in l.value or ")" in l.value):
                        if l not in letters_to_remove:
                            letters_to_remove.append(l)

    for letter in letters_to_remove:
        if letter in letters:
            letters.remove(letter)


def __fix_i__(letters: [Letter]) -> None:
    letter_i: [Letter] = [x for x in letters if x.value == "I"]
    letters_to_remove: [Letter] = []

    for letter in letter_i:
        l: Letter
        for l in letters:
            if l.value == "T":
                middle: [float, float] = [(l.x_min + l.x_max) / 2, (l.y_min + l.y_max) / 2]
                if letter.x_min < middle[0] < letter.x_max and letter.y_min < middle[1] < letter.y_max:
                    if l not in letters_to_remove:
                        letters_to_remove.append(l)

    for letter in letter_i:
        if letter not in letters_to_remove:
            for l in letters:
                if l.value == "I" and l != letter:
                    middle: [float, float] = [(l.x_min + l.x_max) / 2, (l.y_min + l.y_max) / 2]
                    if letter.x_min < middle[0] < letter.x_max and letter.y_min < middle[1] < letter.y_max:
                        if l not in letters_to_remove:
                            letters_to_remove.append(l)

    letter_j: [Letter] = [x for x in letters if x.value == "J"]
    letter_minus: [Letter] = [x for x in letters if x.value == "-"]

    for letter in letter_j:
        for l in letter_minus:
            middle: [float, float] = [(l.x_min + l.x_max) / 2, l.y_min]
            if letter.x_min <= middle[0] <= letter.x_max and letter.y_min <= middle[1] <= letter.y_max:
                letter.value = "I"
                letter.index = 8
                if l not in letters_to_remove:
                    letters_to_remove.append(l)

    for letter in letters_to_remove:
        if letter in letters:
            letters.remove(letter)
