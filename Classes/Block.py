from Enums import LABEL
from Classes.Text import Text


class Block:
    """This class handles the blocks on pictures"""
    id:  int
    objet_type: LABEL
    x_min: float
    x_max: float
    y_min: float
    y_max: float
    confidence: float
    Texts: [Text] = []
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

    def sort_text(self) -> None:
        if len(self.Texts) > 0:
            self.Texts.sort(key=lambda x: x.x_min)
            id: int = self.Texts[0].id
            x_min: float = self.Texts[0].x_min
            y_min: float = self.Texts[0].y_min
            x_max: float = self.Texts[len(self.Texts) - 1].x_max
            y_max: float = self.Texts[len(self.Texts) - 1].y_max
            confidence: float = sum(x.confidence for x in self.Texts) / len(self.Texts)
            txt: str = ""
            for t in self.Texts:
                txt += "{} ".format(t.text)
            text: Text = Text(id, x_min, y_min, x_max, y_max, confidence, txt)
            self.Texts.clear()
            self.Texts.append(text)

    def to_string(self) -> str:
        string: str = "id: {}, object_type: {}, x_min: {}, x_max: {}, y_min: {}, y_max: {}, confidence: {}\n".format(
            self.id, self.objet_type, self.x_min, self.x_max, self.y_max, self.y_min, self.confidence)

        string += "next blocks count: {}\n".format(len(self.Next_Blocks))
        neighbour: int
        for i, neighbour in enumerate(self.Next_Blocks):
            string += "-Neighbour {}: {}\n".format(i, neighbour)

        string += "previous blocks count: {}\n".format(len(self.Previous_Blocks))
        neighbour: int
        for i, neighbour in enumerate(self.Previous_Blocks):
            string += "-Neighbour {}: {}\n".format(i, neighbour)

        string += "Inner texts: {}\n".format(len(self.Texts))
        for text in self.Texts:
            string += "{}\n".format(text.text)

        return string
