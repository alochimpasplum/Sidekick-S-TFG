import os
import HandwrittenOCR.HandwrittenOCR as OCR

base_path: str = 'HandwrittenOCR/tests/'
path: str = 'HandwrittenOCR/tests/neq.jpg'

get_all_detections: bool = True
get_predictions: bool = True

if get_all_detections:
    files = [x for x in os.listdir(base_path) if 'results' not in x]
    for file in files:
        if 'HelloWorld' not in file:
            OCR.HandWrittenOCR(base_path+file, get_predictions=get_predictions)
else:
    OCR.HandWrittenOCR(path, get_predictions=get_predictions)
