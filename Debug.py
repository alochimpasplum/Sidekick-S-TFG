import cv2
import numpy

from Classes import Block
from Enums import LABEL
from PIL import Image


def show_detections(blocks: [Block], image: Image) -> Image:
    img = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
    font = cv2.FONT_HERSHEY_SIMPLEX

    for block in blocks:
        color: [int, int, int] = _get_color(block)
        cv2.rectangle(img, (int(block.x_max), int(block.y_max)), (int(block.x_min), int(block.y_min)), color, 4)
        cv2.putText(img, str(block.objet_type.name),
                    (int(block.x_max), int((block.y_max+block.y_min)/2)), font, 2, color, 1)
        cv2.putText(img, "ID:" + str(block.id),
                    (int(block.x_max), int(block.y_max)), font, 1, (0, 0, 0), 1)

    img: Image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    return img


def _get_color(block: Block) -> [int, int, int]:
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
