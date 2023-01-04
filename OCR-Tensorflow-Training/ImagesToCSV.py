import os
import cv2
import csv
import numpy

directory: str = "./Datasets/handwritten_math_symbols"

symbols: [str] = ["-", "(", ")", "+", "=", "div", "geq", "gt", "lt", "leq", "neq"]
symbols_index: {} = {
    "-": 36,
    "(": 37,
    ")": 38,
    "+": 39,
    "=": 40,
    "div": 41,
    "geq": 42,
    "gt": 43,
    "lt": 44,
    "leq": 45,
    "neq": 46
}

directories = [f for f in os.scandir(directory) if f.name in symbols]
file = open('./Datasets/math_symbols.csv', 'w', newline='')
writer = csv.writer(file)

for d in directories:
    print("Starting {}...".format(d.name))
    index: int = symbols_index[d.name]
    files: [str] = [x for x in os.listdir(d.path) if os.path.isfile(os.path.join(d, x))]

    for f in files:
        original_file: str = "{}/{}".format(d.path, f)
        original_img = cv2.imread(original_file, cv2.IMREAD_GRAYSCALE)
        img_resized = cv2.resize(original_img, (28, 28), interpolation=cv2.INTER_LINEAR)
        img_resized = cv2.bitwise_not(img_resized)

        img_array = img_resized.flatten()
        img_array = numpy.insert(img_array, 0, index)

        writer.writerow(img_array)

file.close()