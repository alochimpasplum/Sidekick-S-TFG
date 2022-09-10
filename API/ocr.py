from OCR import EasyOCR, Tesseract
from PIL import Image
from Classes.Text import Text
from Classes.Block import Block


def get_text(img: Image, blocks: [Block]) -> [Block]:
    return Tesseract.get_text(img, blocks)
    # return EasyOCR.get_text(img, blocks)
