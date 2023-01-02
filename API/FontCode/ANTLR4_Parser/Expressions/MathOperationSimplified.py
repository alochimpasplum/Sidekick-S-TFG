from FontCode.ANTLR4_Parser.Expressions import Expression
from FontCode.ANTLR4_Parser.Expressions.Variable import Variable
from FontCode.ANTLR4_Parser.Expressions.Number import Number


class MathOperationSimplified(Expression.Expression):
    left: Expression
    right: Expression
    operation: str

    def __init__(self, left: Expression, right: Expression, operation: str):
        self.left = left
        self.right = right
        self.operation = "{0}=".format(operation)

    def get_left(self) -> str:
        if isinstance(self.left, Variable):
            return self.left.name
        elif isinstance(self.left, Number):
            return str(self.left.num)

    def get_right(self) -> str:
        if isinstance(self.right, Variable):
            return self.right.name
        elif isinstance(self.right, Number):
            return str(self.right.num)

    def to_string(self):
        print("Math simplified operation: {0} {1} {2}".format(self.get_left(), self.operation, self.get_right()))
