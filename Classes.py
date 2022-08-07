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
    Next_Blocks: [int] = []
    Previous_Blocks: [int] = []

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
        string: str = "id: {}, object_type: {}, x_min: {}, x_max: {}, y_min: {}, y_max: {}, confidence: {}\n".format(
            self.id, self.objet_type, self.x_min, self.x_max, self.y_max, self.y_min, self.confidence)

        string += "next blocks count: {}\n".format(len(self.Next_Blocks))
        neighbour: id
        for i, neighbour in enumerate(self.Next_Blocks):
            string += "-Neighbour {}: {}\n".format(i, neighbour)

        string += "previous blocks count: {}\n".format(len(self.Previous_Blocks))
        neighbour: id
        for i, neighbour in enumerate(self.Previous_Blocks):
            string += "-Neighbour {}: {}\n".format(i, neighbour)

        print(string)


class Text:
    """This class handles texts"""
    id: int
    x_min: float
    x_max: float
    y_min: float
    y_max: float
    confidence: float
    text: str

    def __init__(self, id, x_min, y_min, x_max, y_max, confidence, text):
        self.id = id
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
        self.confidence = confidence
        self.text = text

    def to_string(self):
        string: str = "id: {}, x_min: {}, x_max: {}, y_min: {}, y_max: {}, confidence: {}, text: {}\n".format(
            self.id, self.x_min, self.x_max, self.y_max, self.y_min, self.confidence, self.text)
        print(string)
