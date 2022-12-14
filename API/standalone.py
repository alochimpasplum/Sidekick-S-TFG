# Class used to test api functions locally
import sys
import FlowchartObjectDetection
import Debug
import JsonOperations
import BlockDetection
from PIL import Image
from Classes.Block import Block
from Enums import OCR
from Image_Correction import correct_image


def main():
    img: Image
    try:
        dropped_file = sys.argv[1]
        img = Image.open(dropped_file)
    except IndexError:
        img = Image.open('./TestStuff/HelloWorld9.jpg')
    blocks: [Block] = FlowchartObjectDetection.get_blocks(img, ocr_system=OCR.AZURE)


if __name__ == "__main__":
    main()
