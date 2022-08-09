# Class used to test api functions locally
import sys
from FlowchartObjectDetection import detect
from PIL import Image


def main():
    img: Image
    try:
        dropped_file = sys.argv[1]
        img = Image.open(dropped_file)
    except IndexError:
        img = Image.open('./TestStuff/HelloWorld7.jpg')
    detect(img)


if __name__ == "__main__":
    main()
