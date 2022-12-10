import Enums
from OCR import EasyOCR, Tesseract, AzureOCR
from OCR.HandwrittenOCR import OCR
from PIL import Image
from Classes.Text import Text
from Classes.Block import Block


def get_text(img: Image, blocks: [Block], ocr_system: Enums.OCR) -> [Block]:

    if ocr_system == Enums.OCR.CUSTOM:
        blocks = EasyOCR.get_text(img, blocks)  # Necessary in order to get text bounds
        OCR.OCR(img, blocks)
    elif ocr_system == Enums.OCR.TESSERACT:
        blocks = Tesseract.get_text(img, blocks)
    elif ocr_system == Enums.OCR.EASY_OCR:
        blocks = EasyOCR.get_text(img, blocks)
    elif ocr_system == Enums.OCR.AZURE:
        blocks = AzureOCR.OCR(img, blocks)

    return blocks
