from OCR import EasyOCR, Tesseract
from OCR.HandwrittenOCR import OCR
from PIL import Image
from Classes.Text import Text
from Classes.Block import Block


def get_text(img: Image, blocks: [Block]) -> [Block]:
    OCR.OCR(img, blocks, get_predictions=True)
    # return Tesseract.get_text(img, blocks)
    # return EasyOCR.get_text(img, blocks)
    return []
