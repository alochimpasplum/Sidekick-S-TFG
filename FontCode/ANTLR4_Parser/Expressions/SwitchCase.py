from FontCode.ANTLR4_Parser.Expressions import Expression
from FontCode.ANTLR4_Parser.Expressions.Variable import Variable
from FontCode.ANTLR4_Parser.Expressions.Number import Number


class SwitchCase(Expression.Expression):
    condition: Expression

    def __init__(self, condition: Expression):
        self.condition = condition

    def get_condition(self) -> str:
        if isinstance(self.condition, Variable):
            return self.condition.name
        elif isinstance(self.condition, Number):
            return str(self.condition.num)

    def to_string(self):
        print("switch-case sentence, condition: {0}".format(self.get_condition()))
