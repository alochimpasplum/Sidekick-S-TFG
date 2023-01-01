from FontCode.ANTLR4_Parser.Expressions import Expression


class ConditionalBranches(Expression.Expression):
    branches: [Expression]

    def __init__(self, branches: [Expression]):
        self.branches = branches

    # todo: devolver las expresiones

    def to_string(self):
        pass
