# Functions in this file handles everything related to flowchart object detection
from PIL import Image
from BlockDetection import detect_blocks
from Classes.Block import Block
import Debug


def get_detected_image(img: Image) -> Image:
    blocks: [Block] = get_blocks(img)
    return Debug.get_detections(blocks, img)


def get_blocks(img: Image) -> [Block]:
    blocks: [Block] = detect_blocks(img)
    for block in blocks:
        print(block.to_string())
    return blocks
