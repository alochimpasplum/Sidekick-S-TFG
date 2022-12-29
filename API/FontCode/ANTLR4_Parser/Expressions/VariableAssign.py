from FontCode.ANTLR4_Parser.Expressions import Expression


class VariableAssign(Expression):
    left: Expression
    right: Expression

    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def to_string(self):
        print("Start Variable assign")
        print("Left: {0}".format(self.left.to_string()))
        print("Right: {0}".format(self.right.to_string()))
        print("End Variable assign")
