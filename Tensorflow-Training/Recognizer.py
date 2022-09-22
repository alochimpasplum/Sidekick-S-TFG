import os

import fontTools.ttLib

import HandwrittenOCR.OCR as OCR

base_path: str = 'HandwrittenOCR/tests/'
path: str = 'HandwrittenOCR/tests/I.jpg'

get_all_detections: bool = True
get_predictions: bool = True
get_statistics: bool = True

labelPositions = {
        "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9,
        "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19,
        "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25, "0": 26, "1": 27, "2": 28, "3": 29,
        "4": 30, "5": 31, "6": 32, "7": 33, "8": 34, "9": 35, "-": 36, "(": 37, ")": 38, "+": 39,
        "=": 40, "div": 41, "geq": 42, "gt": 43, "lt": 44, "leq": 45, "neq": 46}

if get_all_detections:
    files = [x for x in os.listdir(base_path) if 'results' not in x]
    for file in files:
        if 'HelloWorld' not in file:
            OCR.OCR(base_path+file, get_predictions=get_predictions, get_all_statistics=get_statistics)
else:
    OCR.OCR(path, get_predictions=get_predictions, get_all_statistics=get_statistics)









