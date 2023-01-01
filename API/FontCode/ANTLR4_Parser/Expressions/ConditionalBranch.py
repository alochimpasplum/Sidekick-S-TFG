from FontCode.ANTLR4_Parser.Expressions import Expression
from FontCode.ANTLR4_Parser.Expressions.Variable import Variable
from FontCode.ANTLR4_Parser.Expressions.Number import Number


class ConditionalBranch(Expression.Expression):
    condition: Expression
    conditional_lines: Expression

    def __init__(self, condition: Expression, conditional_lines: Expression):
        self.condition = condition
        self.conditional_lines = conditional_lines

    def get_condition(self) -> str:
        if isinstance(self.condition, Variable):
            return self.condition.name
        elif isinstance(self.condition, Number):
            return str(self.condition.num)

    def to_string(self):
        print("Conditional branch")
        print(self.condition.to_string())
        print(self.conditional_lines.to_string())
