import cv2
import numpy

from Classes.Text import Text
from Classes.Block import Block
from Enums import LABEL
from PIL import Image


def get_detections(blocks: [Block], image: Image) -> Image:
    img = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
    font = cv2.FONT_HERSHEY_SIMPLEX

    block: Block
    for block in blocks:
        color: [int, int, int] = __get_color(block)
        # Block stuff
        cv2.rectangle(img, (int(block.x_max), int(block.y_max)), (int(block.x_min), int(block.y_min)), color, 4)
        cv2.putText(img, str(block.objet_type.name),
                    (int(block.x_max), int((block.y_max+block.y_min)/2)), font, 2, color, 1)
        cv2.putText(img, "ID:" + str(block.id),
                    (int(block.x_max), int(block.y_max)), font, 1, (0, 0, 0), 1)
        # Text stuff
        if "arrow" not in block.objet_type.name:
            if len(block.Texts) > 0:
                cv2.rectangle(img, (int(block.Texts[0].x_max), int(block.Texts[0].y_max)),
                              (int(block.Texts[0].x_min), int(block.Texts[0].y_min)), (255, 255, 255), -1)
                cv2.rectangle(img, (int(block.Texts[0].x_max), int(block.Texts[0].y_max)),
                              (int(block.Texts[0].x_min), int(block.Texts[0].y_min)), color, 1)
                cv2.putText(img, str(block.Texts[0].text),
                            (int(block.Texts[0].x_min),
                             int(block.Texts[0].y_max)), font, 2, (0, 0, 0), 1)
        else:
            if len(block.Texts) > 0:
                cv2.rectangle(img, (int(block.x_min), int(block.y_min)),
                              (int(block.x_min + (block.Texts[0].x_max - block.Texts[0].x_min)),
                               int(block.y_min + (block.Texts[0].y_max - block.Texts[0].y_min))), (255, 255, 255), -1)
                cv2.putText(img, str(block.Texts[0].text),
                            (int(block.x_min), int(block.y_min + (block.Texts[0].y_max - block.Texts[0].y_min))),
                            font, 2, (0, 0, 0), 1)

    img: Image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    return img


def get_ocr(texts: [Text], image: Image) -> Image:
    img = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
    font = cv2.FONT_HERSHEY_SIMPLEX

    for text in texts:
        color: [int, int, int] = (0, 0, 255)
        cv2.rectangle(img, (int(text.x_max), int(text.y_max)), (int(text.x_min), int(text.y_min)), color, 4)
        # cv2.putText(img, str(text.confidence),
        #            (int(text.x_max), int((text.y_max + text.y_min) / 2)), font, 2, color, 1)
        cv2.putText(img, str(text.text),
                    (int(text.x_max), int(text.y_max)), font, 2, color, 2)

    img: Image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    return img


def __get_color(block: Block) -> [int, int, int]:
    if block.objet_type == LABEL.start_end:
        return 255, 192, 192
    if block.objet_type == LABEL.scan:
        return 255, 0, 0
    if block.objet_type == LABEL.decision:
        return 255, 255, 0
    if block.objet_type == LABEL.print:
        return 128, 128, 0
    if block.objet_type == LABEL.process:
        return 0, 255, 0
    if block.objet_type == LABEL.arrow_line_up:
        return 0, 255, 255
    if block.objet_type == LABEL.arrow_line_down:
        return 0, 0, 255
    if block.objet_type == LABEL.arrow_line_right:
        return 255, 0, 255
    if block.objet_type == LABEL.arrow_line_left:
        return 128, 0, 128
    if block.objet_type == LABEL.pointer:
        return 192, 192, 192


def print_blocks(blocks: [Block]) -> None:
    for block in blocks:
        print(block.to_string())
