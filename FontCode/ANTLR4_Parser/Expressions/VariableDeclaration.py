from FontCode.ANTLR4_Parser.Expressions import Expression


class VariableDeclaration(Expression.Expression):
    child: Expression
    var_type: str

    def __init__(self, child: Expression, var_type: str):
        self.child = child
        self.var_type = var_type

    def get_variable_id(self) -> str:
        return self.child.name

    def to_string(self):
        print("Variable declaration, var_type: {0}, var: {1}".format(self.var_type, self.child.to_string()))
