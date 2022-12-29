from FontCode.ANTLR4_Parser.Expressions import Expression


class CustomFunction(Expression):
    child: Expression

    def __init__(self, child: Expression):
        self.child = child

    def to_string(self):
        print("Custom function: {0}".format(self.child.to_string()))
