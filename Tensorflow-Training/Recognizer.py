import os

import fontTools.ttLib

import HandwrittenOCR.OCR as OCR

base_path: str = 'HandwrittenOCR/tests/'
path: str = 'HandwrittenOCR/tests/A.jpg'

get_all_detections: bool = False
get_predictions: bool = True

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
            OCR.OCR(base_path+file, get_predictions=get_predictions)
else:
    OCR.OCR(path, get_predictions=get_predictions)

predictions: [str] = [x for x in os.listdir(base_path + "results/") if x.endswith(".txt")]

lines: [str] = [None] * (len(labelPositions) + 2)

for pred in predictions:
    do_write: bool = True
    f = open(base_path + "results/" + pred)
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


f = open(base_path + "results.txt", "w")
line: str = ""
for line in lines:
    if line is not None:
        f.write(line + "\n")
    else:
        f.write("\n")
f.close()


