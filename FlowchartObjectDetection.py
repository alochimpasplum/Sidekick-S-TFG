# Functions in this file handles everything related to flowchart object detection
from PIL import Image
from BlockDetection import detect_blocks


def detect(img: Image) -> None:
    detect_blocks(img)
