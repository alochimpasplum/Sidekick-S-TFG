import os

import fontTools.ttLib

import HandwrittenOCR.OCR as OCR

base_path: str = 'HandwrittenOCR/tests/'
path: str = 'HandwrittenOCR/tests/7.jpg'

get_all_detections: bool = False
get_predictions: bool = True
get_statistics: bool = True

if get_all_detections:
    files = [x for x in os.listdir(base_path) if 'results' not in x]
    for file in files:
        if 'HelloWorld' not in file:
            OCR.OCR(base_path+file, get_predictions=get_predictions, get_all_statistics=get_statistics)
else:
    OCR.OCR(path, get_predictions=get_predictions, get_all_statistics=get_statistics)
