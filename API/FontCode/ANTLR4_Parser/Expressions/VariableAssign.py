from FontCode.ANTLR4_Parser.Expressions import Expression


class VariableAssign(Expression.Expression):
    left: Expression
    right: Expression

    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def get_variable_id(self) -> str:
        return self.left.name

    def get_assign_value(self) -> str:
        return str(self.right.num)

    def to_string(self):
        print("Start Variable assign")
        print("Left: {0}".format(self.left.to_string()))
        print("Right: {0}".format(self.right.to_string()))
        print("End Variable assign")
