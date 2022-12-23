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

    __fix_whitespaces(blocks)

    return blocks


def __fix_whitespaces(blocks: [Block]):
    block: Block
    special_characters: [str] = ['+', '-', '*', '/', '&', '|', '!', '<', '>', '=']

    for block in blocks:
        if len(block.Texts) > 0:
            block.Texts[0].text = block.Texts[0].text.replace(" ", "")
            text: str = ""
            is_last_char_special_char: bool = False

            for c in block.Texts[0].text:
                if (c in special_characters) and (not is_last_char_special_char):
                    is_last_char_special_char = True
                    text += " "
                elif is_last_char_special_char:
                    is_last_char_special_char = False
                    text += " "
                text += c

            block.Texts[0].text = text
