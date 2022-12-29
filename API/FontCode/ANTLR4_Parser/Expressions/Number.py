from FontCode.ANTLR4_Parser.Expressions import Expression


class Number(Expression.Expression):
    num: int

    def __init__(self, num: int):
        self.num = num

    def to_string(self):
        print(self.num)
