from FontCode.ANTLR4_Parser.Expressions import Expression
from FontCode.ANTLR4_Parser.Expressions.Variable import Variable
from FontCode.ANTLR4_Parser.Expressions.Number import Number


class If(Expression.Expression):
    left: Expression
    right: Expression
    condition: str

    def __init__(self, left: Expression, right: Expression, condition: str):
        self.left = left
        self.right = right
        self.condition = condition

    def get_left(self):
        if isinstance(self.left, Variable):
            return self.left.name
        elif isinstance(self.left, Number):
            return str(self.left.num)

    def get_right(self):
        if isinstance(self.right, Variable):
            return self.right.name
        elif isinstance(self.right, Number):
            return str(self.right.num)

    def to_string(self):
        print("IF: {0} {1} {2}".format(self.get_left(), self.condition, self.get_right()))
