from FontCode.ANTLR4_Parser.Expressions import Expression


class Variable(Expression.Expression):
    name: str

    def __init__(self, name: str):
        self.name = name

    def to_string(self):
        print('Variable name: {0}'.format(self.name))
