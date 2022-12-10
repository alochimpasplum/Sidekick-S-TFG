# Functions in this file handles everything related to flowchart object detection
from PIL import Image

import Enums
from BlockDetection import detect_blocks
from Classes.Block import Block
import Debug


def get_detected_image(img: Image) -> Image:
    blocks: [Block] = get_blocks(img)
    return Debug.get_detections(blocks, img)


def get_blocks(img: Image, ocr_system: Enums.OCR = Enums.OCR.CUSTOM) -> [Block]:
    blocks: [Block] = detect_blocks(img, ocr_system=ocr_system)
    return blocks
