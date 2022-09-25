from OCR import EasyOCR, Tesseract
from OCR.HandwrittenOCR import OCR
from PIL import Image
from Classes.Text import Text
from Classes.Block import Block


def get_text(img: Image, blocks: [Block]) -> [Block]:
    path: str = img.filename
    OCR.OCR(path, blocks)
    # return Tesseract.get_text(img, blocks)
    # return EasyOCR.get_text(img, blocks)
    return []
