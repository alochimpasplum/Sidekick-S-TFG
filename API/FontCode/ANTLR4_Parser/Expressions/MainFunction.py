from FontCode.ANTLR4_Parser.Expressions import Expression


class MainFunction(Expression.Expression):
    name: str

    def __init__(self, name: str):
        self.name = name

    def to_string(self):
        print("Main function, name: {0}".format(self.name))
