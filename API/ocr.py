from OCR import EasyOCR, Tesseract
from OCR.HandwrittenOCR import OCR
from PIL import Image
from Classes.Text import Text
from Classes.Block import Block


def get_text(img: Image, blocks: [Block], OCR_SYSTEM: str = "CUSTOM") -> [Block]:

    if OCR_SYSTEM == "CUSTOM":
        blocks = EasyOCR.get_text(img, blocks)
        OCR.OCR(img, blocks)
    elif OCR_SYSTEM == "TESSERACT":
        blocks = Tesseract.get_text(img, blocks)
    elif OCR_SYSTEM == "EASY_OCR":
        blocks = EasyOCR.get_text(img, blocks)

    return blocks
