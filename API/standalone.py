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
    print_header()
    dir_list: [str] = get_image_list()
    selection: int = image_selection(dir_list)

    img: Image
    img = Image.open(r"{0}{1}\{2}".format(os.getcwd(), Constants.INPUT_FOLDER, dir_list[selection]))

    selection_ocr = detection_system()
    selection_language = language_selection()

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

    with open(file_path, 'w') as f:

        for line in code.lines:
            f.write(line)

            f.write('\n')

    print("")

    print("")

    print("Process finished, output saved at: {0}".format(file_path))

    print("Press a button to exit")

    s = input()


def print_header() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("### SIDEKICK-S ###")
    print("Developed by: Juan Antonio Lagos Carrera")
    print("")


def get_image_list() -> [str]:
    dir_list = os.listdir("{0}{1}".format(os.getcwd(), Constants.INPUT_FOLDER))
    if len(dir_list) <= 0:
        print("No images to read")
        print("Press a button to exit")
        s = input()
        sys.exit(0)
    return dir_list


def image_selection(dir_list: [str]) -> int:
    seleccion_correcta: bool = False

    while not seleccion_correcta:
        print("Choose your image:")
        for i in range(0, len(dir_list)):
            print("{0} - {1}".format(i, dir_list[i]))
        print("{0} - Exit program".format("q"))
        selection = input()
        if selection.isdecimal() and (0 <= int(selection) < len(dir_list)):
            return int(selection)
        elif selection == "q":
            print("Closing program...")
        else:
            print_header()
            print("Please, choose a valid option")


def detection_system() -> int:
    seleccion_correcta: bool = False

    values = [member.value for member in Enums.OCR]
    names = [member.name for member in Enums.OCR]

    while not seleccion_correcta:
        print_header()
        print("Choose detection system:")
        for i in range(0, len(values)):
            print("{0} - {1}".format(values[i], names[i]))
        print("{0} - Exit program".format("q"))
        selection = input()
        if selection.isdecimal() and (0 <= int(selection) < len(values)):
            return int(selection)
        elif selection == "q":
            print("Closing program...")
        else:
            print_header()
            print("Please, choose a valid option")


def language_selection() -> int:
    seleccion_correcta: bool = False

    values = [member.value for member in Enums.supported_languages]
    names = [member.name for member in Enums.supported_languages]

    while not seleccion_correcta:
        print_header()
        print("Choose language output:")
        for i in range(0, len(values)):
            print("{0} - {1}".format(values[i], names[i]))
        print("{0} - Exit program".format("q"))
        selection = input()
        if selection.isdecimal() and (0 <= int(selection) < len(values)):
            return int(selection)
        elif selection == "q":
            print("Closing program...")
        else:
            print_header()
            print("Please, choose a valid option")


if __name__ == "__main__":
    main()
