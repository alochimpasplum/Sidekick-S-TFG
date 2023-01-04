from FontCode.ANTLR4_Parser.Expressions import Expression


class Program:
    expressions: [Expression] = []

    def add_expression(self, e: Expression):
        self.expressions.append(e)
