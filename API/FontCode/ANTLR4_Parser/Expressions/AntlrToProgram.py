from FontCode.ANTLR4_Parser.Antlr4_Files.PythonParser import PythonParser
from FontCode.ANTLR4_Parser.Antlr4_Files.PythonVisitor import PythonVisitor
from FontCode.ANTLR4_Parser.Expressions.Program import Program
from FontCode.ANTLR4_Parser.Expressions.AntlrToExpression import AntlrToExpression


class AntlrToProgram(PythonVisitor):
    def visitProg(self, ctx: PythonParser.ProgContext):
        prog: Program = Program()
        expression_visitor: AntlrToExpression = AntlrToExpression()

        for i in range(0, ctx.getChildCount()):
            if i < ctx.getChildCount():  # Así no visito el nodo EOF
                prog.add_expression(PythonVisitor.visit(ctx.getChild(i)))
