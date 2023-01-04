
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

    def to_string(self) -> str:
        string: str = "id: {}, x_min: {}, x_max: {}, y_min: {}, y_max: {}, confidence: {}, text: {}\n".format(
            self.id, self.x_min, self.x_max, self.y_max, self.y_min, self.confidence, self.text)
        return string
