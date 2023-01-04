from FontCode.ANTLR4_Parser.Expressions import Expression
from FontCode.ANTLR4_Parser.Expressions.Variable import Variable
from FontCode.ANTLR4_Parser.Expressions.Number import Number


class Scan(Expression.Expression):
    storing_var: Expression

    def __init__(self, storing_var: Expression):
        self.storing_var = storing_var

    def get_var(self) -> str:
        if isinstance(self.storing_var, Variable):
            return self.storing_var.name
        elif isinstance(self.storing_var, Number):
            return str(self.storing_var.num)

    def to_string(self):
        pass
