from FontCode.ANTLR4_Parser.Expressions import Expression
from FontCode.ANTLR4_Parser.Expressions.Variable import Variable
from FontCode.ANTLR4_Parser.Expressions.Number import Number


class Conditional(Expression.Expression):
    condition: Expression
    conditional_branches: Expression

    def __init__(self, condition: Expression, conditional_branches: Expression):
        self.condition = condition
        self.conditional_branches = conditional_branches

    def get_condition(self) -> str:
        if isinstance(self.condition, Variable):
            return self.condition.name
        elif isinstance(self.condition, Number):
            return str(self.condition.num)

    def to_string(self):
        print("Conditional block")
        print(self.condition.to_string())
        print(self.conditional_branches.to_string())
        print("End conditional block")
