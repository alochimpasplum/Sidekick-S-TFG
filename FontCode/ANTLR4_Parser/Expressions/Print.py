from FontCode.ANTLR4_Parser.Expressions import Expression
from FontCode.ANTLR4_Parser.Expressions.Variable import Variable
from FontCode.ANTLR4_Parser.Expressions.Number import Number


class Print(Expression.Expression):
    child: Expression

    def __init__(self, child: Expression):
        self.child = child

    def get_print(self) -> str:
        if isinstance(self.child, Variable):
            return self.child.name
        elif isinstance(self.child, Number):
            return str(self.child.num)

    def to_string(self):
        print("Print: {0}".format(self.child.to_string()))
