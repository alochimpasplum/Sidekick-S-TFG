from FontCode.ANTLR4_Parser.Expressions import Expression


class String(Expression.Expression):
    value: str

    def __init__(self, value: str):
        self.value = value

    def to_string(self):
        print("String: {0}".format(self.value))
