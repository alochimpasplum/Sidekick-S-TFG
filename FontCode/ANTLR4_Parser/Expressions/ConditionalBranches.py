from FontCode.ANTLR4_Parser.Expressions import Expression


class ConditionalBranches(Expression.Expression):
    branches: [Expression]

    def __init__(self, branches: [Expression]):
        self.branches = branches

    def to_string(self):
        print("Condition branch with {0} branches".format(len(self.branches)))
        for branch in self.branches:
            print(branch.to_string())
