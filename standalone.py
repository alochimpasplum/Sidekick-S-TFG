# Class used to test api functions locally
import sys
import FlowchartObjectDetection
import Debug
import JsonOperations
import BlockDetection
from PIL import Image
from Classes.Block import Block
from Image_Correction import correct_image


def main():
    img: Image
    try:
        dropped_file = sys.argv[1]
        img = Image.open(dropped_file)
    except IndexError:
        img = Image.open('./TestStuff/Helloworld5.1.jpg')
    corrected_image: Image = correct_image(img)
    blocks: [Block] = BlockDetection.detect_blocks(img)


if __name__ == "__main__":
    main()
