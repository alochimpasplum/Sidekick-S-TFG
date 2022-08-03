# Functions in this file handles everything related to flowchart object detection

import torch


def detect(img: str) -> str:
    # Model
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='./TestStuff/best(L).pt', force_reload=True)
    model
    # Inference
    results = model(img)
    results.show()

    return results.pandas().xyxy[0].to_json(orient="records")
