from FontCode.ANTLR4_Parser.Expressions import Expression
from FontCode.ANTLR4_Parser.Expressions.Variable import Variable
from FontCode.ANTLR4_Parser.Expressions.Number import Number


class MathOperation(Expression.Expression):
    operation: str
    assign: Expression
    left: Expression
    right: Expression

    def __init__(self, operation: str, assign: Expression, left: Expression, right: Expression):
        self.operation = operation
        self.assign = assign
        self.left = left
        self.right = right

    def get_assign(self) -> str:
        if isinstance(self.assign, Variable):
            return self.assign.name
        elif isinstance(self.assign, Number):
            return str(self.assign.num)

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
        print("Operation matemática: {0} = {1} {2} {3}".format(self.get_assign(), self.get_left(),
                                                               self.operation, self.get_right()))
