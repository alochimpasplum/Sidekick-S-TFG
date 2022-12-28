from FontCode.ANTLR4_Parser.Antlr4_Files.PythonParser import PythonParser
from FontCode.ANTLR4_Parser.Antlr4_Files.PythonVisitor import PythonVisitor
from FontCode.ANTLR4_Parser.Expressions import Program


class AntlrToProgram(PythonVisitor):
    def visitProg(self, ctx: PythonParser.ProgContext):
        return super().visitProg(ctx)
