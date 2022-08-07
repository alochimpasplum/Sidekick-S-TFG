import easyocr
import numpy as np
from PIL import Image
from Classes import Text, Block


def get_text(img: Image, blocks: [Block]) -> [Block]:
    texts: [Text] = []
    reader = easyocr.Reader(['en'])
    image = np.array(img)
    results = reader.readtext(image)

    for i, res in enumerate(results):
        text: Text = Text(i, res[0][0][0], res[0][0][1], res[0][2][0], res[0][2][1], res[2], res[1])
        texts.append(text)

    temp: [[Block], [Text]] = _get_inner_texts(texts, blocks)
    blocks = temp[0]


def _get_inner_texts(texts: [Text], blocks: [Block]) -> [[Block], [Text]]:
    outer_texts: [Text] = []
    block: Block
    text: Text
    for text in texts:
        is_outside: bool = True
        for block in blocks:
            if _is_text_inner(text, block):
                is_outside = False
                block.text.append(text)
            print(block.text)
            # todo: continuar aqui

        if is_outside:
            outer_texts.append(text)

    return [blocks, outer_texts]


def _is_text_inner(text: Text, block: Block) -> bool:
    center_x: float = (text.x_max + text.x_min) / 2
    center_y: float = (text.y_max + text.y_min) / 2
    print("text: {}, block: {}".format(text.text, block.id))
    print(block.x_max > center_x > block.x_min and block.y_max > center_y > block.y_min)
    return block.x_max > center_x > block.x_min and block.y_max > center_y > block.y_min
