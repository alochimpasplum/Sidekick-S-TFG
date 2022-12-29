from FontCode.ANTLR4_Parser.Expressions import Expression


class Print(Expression.Expression):
    child: Expression

    def __init__(self, child: Expression):
        self.child = child

    def to_string(self):
        print("Print: {0}".format(self.child.to_string()))
