# Class used to test api functions locally
import sys
import FlowchartObjectDetection
import Debug
from PIL import Image
from Classes.Block import Block
from Enums import OCR
from FontCode import FontCode


def main():
    img: Image
    try:
        dropped_file = sys.argv[1]
        img = Image.open(dropped_file)
    except IndexError:
        img = Image.open('./TestStuff/HelloWorld11.jpg')
    blocks: [Block] = FlowchartObjectDetection.get_blocks(img, ocr_system=OCR.AZURE)
    # Debug.print_blocks(blocks)
    code: FontCode.FontCode = FontCode.FontCode(blocks)


if __name__ == "__main__":
    main()
