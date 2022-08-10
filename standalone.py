# Class used to test api functions locally
import sys
import FlowchartObjectDetection
import Debug
import JsonOperations
from PIL import Image
from Classes.Block import Block


def main():
    img: Image
    try:
        dropped_file = sys.argv[1]
        img = Image.open(dropped_file)
    except IndexError:
        img = Image.open('./TestStuff/HelloWorld7.jpg')
    blocks: [Block] = FlowchartObjectDetection.get_blocks(img)
    JsonOperations.block_list_to_block_json(blocks)


if __name__ == "__main__":
    main()
