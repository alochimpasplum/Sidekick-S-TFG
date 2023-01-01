from FontCode.ANTLR4_Parser.Expressions import Expression
from FontCode.ANTLR4_Parser.Expressions.Variable import Variable
from FontCode.ANTLR4_Parser.Expressions.Number import Number


class Conditional(Expression.Expression):
    condition: Expression
    conditional_branches: Expression

    def __init__(self, condition: Expression, conditional_branches: Expression):
        self.condition = condition
        self.conditional_branches = conditional_branches

    # todo: obtener condición y ramas

    def to_string(self):
        pass