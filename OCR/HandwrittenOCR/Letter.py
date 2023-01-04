class Letter:
    x_min: float
    x_max: float
    y_min: float
    y_max: float
    confidence: float
    value: str
    index: int

    replace_chars = {
        "div": "/",
        "geq": ">=",
        "gt": ">",
        "lt": "<",
        "leq": "<=",
        "neq": "!="
    }

    def __init__(self, x_min, x_max, y_min, y_max, confidence, value, index):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.confidence = confidence
        self.value = value
        self.index = index

        if self.value in self.replace_chars:
            self.value = self.replace_chars[self.value]
