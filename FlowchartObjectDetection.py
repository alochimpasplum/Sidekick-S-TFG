# Functions in this file handles everything related to flowchart object detection
from Classes import Block
from Constants import CONFIDENCE_THRESHOLD
import torch
import json


def detect(img: str) -> [Block]:
    # Model
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='./TestStuff/best(L).pt', force_reload=True)
    model
    # Inference
    results = model(img)

    serialized_json = results.pandas().xyxy[0].to_json(orient="records")

    deserialized_json = json.loads(serialized_json)

    results_list: [Block] = []

    for entry in deserialized_json:
        if entry['confidence'] > CONFIDENCE_THRESHOLD:
            temp: Block = Block(['xmin'], ['ymin'], ['xmax'], ['ymax'], ['confidence'], ['name'])
            results_list.append(temp)

    return results_list
