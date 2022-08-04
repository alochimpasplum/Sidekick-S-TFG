from Enums import LABEL
from typing import List


class Block:
    """This class handles the blocks on pictures"""
    id:  int
    objet_type: LABEL
    x_min: float
    x_max: float
    y_min: float
    y_max: float
    confidence: float
    Next_Blocks: List[str]

    def __init__(self, id, x_min, y_min, x_max, y_max, confidence, name):
        self.id = id
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
        self.confidence = confidence

        for entry in LABEL:
            if entry.name == name:
                self.objet_type = entry

    def to_string(self):
        return "id: {}, object_type: {}, x_min: {}, x_max: {}, y_min: {}, y_max: {}, confidence: {}".format(
            self.id, self.objet_type, self.x_min, self.x_max, self.y_max, self.y_max, self.confidence)
