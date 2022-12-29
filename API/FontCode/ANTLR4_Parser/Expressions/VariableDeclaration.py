from FontCode.ANTLR4_Parser.Expressions import Expression


class VariableDeclaration(Expression):
    child: Expression
    var_type: str

    def __init__(self, child: Expression, var_type: str):
        self.child = child
        self.var_type = var_type

    def to_string(self):
        print("Variable declaration, var_type: {0}, var: {1}".format(self.var_type, self.child.to_string()))
