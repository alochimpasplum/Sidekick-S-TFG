import easyocr
import numpy as np
from PIL import Image
from Classes.Text import Text
from Classes.Block import Block


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

    for b in blocks:
        print(b.to_string())


def _get_inner_texts(texts: [Text], blocks: [Block]) -> [[Block], [Text]]:
    outer_texts: [Text] = []
    block: Block
    text: Text
    for text in texts:
        is_outside: bool = True
        for block in blocks:
            if __is_text_inner(text, block):
                is_outside = False
                if block.text is not None:
                    block.text = __mix_texts(block.text, text)
                else:
                    block.text = text

        if is_outside:
            outer_texts.append(text)

    return [blocks, outer_texts]


def __is_text_inner(text: Text, block: Block) -> bool:
    center_x: float = (text.x_max + text.x_min) / 2
    center_y: float = (text.y_max + text.y_min) / 2
    return block.x_max > center_x > block.x_min and block.y_max > center_y > block.y_min


def __mix_texts(text_a: Text, text_b: Text) -> Text:
    # TODO: ¿Que pasa cuando hay tres textos y ya he evaluado los textos de los extremos?
    text: Text = Text(text_a.id, text_a.x_min, text_a.y_min, text_a.x_max, text_a.y_max, text_a.confidence, text_a.text)
    is_text_a_left: bool = text_a.x_min < text_b.x_min

    if is_text_a_left:
        text.text = "{} {}".format(text_a.text, text_b.text)
        text.x_min = text_a.x_min
        text.x_max = text_b.x_max

    else:
        text.text = "{} {}".format(text_b.text, text_a.text)
        text.x_min = text_b.x_min
        text.x_max = text_a.x_max

    text.confidence = (text_a.confidence + text_b.confidence) / 2

    return text
