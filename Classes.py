from Enums import LABEL
from typing import List
import uuid


class Block:
    """This class handles the blocks on pictures"""
    id: str
    objet_type: LABEL
    x_min: float
    x_max: float
    y_min: float
    y_max: float
    confidence: float
    Next_Blocks: List[str]

    def __init__(self, x_min, y_min, x_max, y_max, confidence, name):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
        self.confidence = confidence
        # self.objet_type = name

        for label in LABEL:
            print(label)
