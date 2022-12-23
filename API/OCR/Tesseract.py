import pytesseract
import math
import sys
import Debug

from PIL import Image
from Classes.Text import Text
from Classes.Block import Block

array_positions: {} = {
    "text": 11,
    "x_min": 6,
    "y_min": 7,
    "width": 8,
    "height": 9,
    "confidence": 10
}


def get_text(img: Image, blocks: [Block]) -> [Block]:
    texts: [Text] = []
    lines: [str] = pytesseract.image_to_data(img).splitlines()
    line: str
    for i, line in enumerate(lines):
        lines_data: [str] = line.split()
        if len(lines_data) == 12 and i != 0:
            text: Text = Text(i, int(lines_data[array_positions["x_min"]]), int(lines_data[array_positions["y_min"]]),
                              int(lines_data[array_positions["x_min"]]) + int(lines_data[array_positions["width"]]),
                              int(lines_data[array_positions["y_min"]]) + int(lines_data[array_positions["height"]]),
                              float(lines_data[array_positions["confidence"]]), lines_data[array_positions["text"]])
            texts.append(text)

    Debug.get_ocr(texts, img).save('C:\\Users\\Lagos\\Downloads\\img.jpg')

    temp: [[Block], [Text]] = __get_inner_texts(texts, blocks)
    blocks = __get_outer_text(temp[0], temp[1])

    return blocks


def __get_inner_texts(texts: [Text], blocks: [Block]) -> [[Block], [Text]]:
    inner_texts: [Text] = []
    block: Block

    for block in blocks:
        if "arrow" not in block.object_type.name:
            txt: [Text] = [x for x in texts if __is_text_inner(x, block)]
            block.Texts = txt
            for t in txt:
                inner_texts.append(t)
            block.sort_text()

    outer_texts: [Text] = texts
    for t in inner_texts:
        if t in outer_texts:
            outer_texts.remove(t)

    return [blocks, outer_texts]


def __get_outer_text(blocks: [Block], texts: [Text]) -> [Block]:
    text: Text
    for text in texts:
        block: Block = __get_conditional_arrow(text, blocks)
        block.Texts = [text]

    return blocks


def __is_text_inner(text: Text, block: Block) -> bool:
    center_x: float = (text.x_max + text.x_min) / 2
    center_y: float = (text.y_max + text.y_min) / 2
    return block.x_max > center_x > block.x_min and block.y_max > center_y > block.y_min


def __get_conditional_arrow(text: Text, blocks: [Block]) -> Block:
    center_text: (float, float) = (((text.x_max + text.x_min) / 2), ((text.y_max + text.y_min) / 2))
    block_points: [(float, float)] = [(float, float)]
    distances: {} = {}
    block: Block
    for block in blocks:
        if "arrow" in block.object_type.name:
            block_points.clear()
            block_points.append((block.x_max, block.y_max))
            block_points.append((block.x_max, block.y_min))
            block_points.append((block.x_min, block.y_max))
            block_points.append((block.x_min, block.y_min))
            block_points.append(((block.x_min + block.x_max) / 2, (block.y_min + block.y_max) / 2))

            distance: float = sys.float_info.max
            for point in block_points:
                if math.dist(point, center_text) < distance:
                    distance = math.dist(point, center_text)

            distances[block] = distance

    return min(distances.keys(), key=lambda k: distances[k])
