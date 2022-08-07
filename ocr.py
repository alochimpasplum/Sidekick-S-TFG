import easyocr
import numpy as np
import cv2
from PIL import Image
from Debug import show_ocr
from Classes import Text, Block


def get_text(img: Image, blocks: [Block]) -> [Block]:
    texts: [Text] = []
    reader = easyocr.Reader(['en'])
    image = np.array(img)
    results = reader.readtext(image)

    for i, res in enumerate(results):
        text: Text = Text(i, res[0][0][0], res[0][0][1], res[0][2][0], res[0][2][1], res[2], res[1])
        texts.append(text)

    return texts
