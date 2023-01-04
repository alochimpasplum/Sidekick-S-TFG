from FontCode.ANTLR4_Parser.Expressions import Expression


class ConditionalLines(Expression.Expression):
    lines: [Expression] = []

    def __init__(self, lines: [Expression]):
        self.lines = lines

    def to_string(self):
        print("Conditional lines with {0} lines".format(len(self.lines)))
        for line in self.lines:
            print(line.to_string())
