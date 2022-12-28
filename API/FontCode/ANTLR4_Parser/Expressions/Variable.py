from FontCode.ANTLR4_Parser.Expressions import Expression


class Variable(Expression):
    name: str
    var_type: str

    def __init__(self, name: str, var_type: str):
        self.name = name
        self.var_type = var_type

    def to_string(self):
        print('name: {0}, var_type: {1}'.format(self.name, self.var_type))
