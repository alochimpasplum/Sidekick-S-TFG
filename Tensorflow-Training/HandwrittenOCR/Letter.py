class Letter:
    x_min: float
    x_max: float
    y_min: float
    y_max: float
    confidence: float
    value: str

    def __init__(self, x_min, x_max, y_min, y_max, confidence, value):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.confidence = confidence
        self.value = value
