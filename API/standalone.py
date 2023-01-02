import sys
import FlowchartObjectDetection
import Debug
import Constants
import Enums
import os
from PIL import Image
from Classes.Block import Block
from Enums import OCR
from FontCode import FontCode


def main():
    print("### SIDEKICK-S ###")
    print("Developed by: Juan Antonio Lagos Carrera")
    print("")
    print("Choose your image:")
    dir_list = os.listdir("{0}{1}".format(os.getcwd(), Constants.INPUT_FOLDER))
    if len(dir_list) <= 0:
        print("No images to read")
    else:
        for i in range(0, len(dir_list)):
            print("{0} - {1}".format(i, dir_list[i]))
        selection = int(input())

        img: Image
        img = Image.open(r"{0}{1}\{2}".format(os.getcwd(), Constants.INPUT_FOLDER, dir_list[selection]))

        print("")
        print("")

        print("Choose detection system:")
        values = [member.value for member in Enums.OCR]
        names = [member.name for member in Enums.OCR]

        for i in range(0, len(values)):
            print("{0} - {1}".format(values[i], names[i]))
        selection_ocr = int(input())

        print("")
        print("")

        print("Choose output language:")
        values = [member.value for member in Enums.supported_languages]
        names = [member.name for member in Enums.supported_languages]

        for i in range(0, len(values)):
            print("{0} - {1}".format(values[i], names[i]))
        selection_language = int(input())

        blocks: [Block] = FlowchartObjectDetection.get_blocks(img, ocr_system=OCR(selection_ocr))
        # Debug.print_blocks(blocks)

        code: FontCode.FontCode = FontCode.FontCode(blocks, Enums.supported_languages(selection_language))

        file_path: str = "{0}{1}".format(os.getcwd(), Constants.OUTPUT_FOLDER)
        file_name: str = dir_list[selection].split(".")[0]

        if Enums.supported_languages(selection_language) == Enums.supported_languages.python:
            file_path += r"\{0}.py".format(file_name)
        if Enums.supported_languages(selection_language) == Enums.supported_languages.java:
            file_path += r"\{0}.java".format(file_name)

        if os.path.exists(file_path):
            os.remove(file_path)

        print(file_path)

        with open(file_path, 'w') as f:
            for line in code.lines:
                f.write(line)
                f.write('\n')

        print("")
        print("")

        print("Process finished, output saved at: {0}".format(file_path))
        print("Press a button to exit")
        s = input()


if __name__ == "__main__":
    main()
