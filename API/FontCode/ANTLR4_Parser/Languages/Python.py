from FontCode.ANTLR4_Parser.Antlr4_Files.PythonLexer import PythonLexer
from FontCode.ANTLR4_Parser.Antlr4_Files.PythonParser import PythonParser
from FontCode.ANTLR4_Parser.Antlr4_Files.PythonListener import PythonListener


class Python:
    lexer: PythonLexer
    parser: PythonParser
    tree: PythonParser.Main_functionContext

    def __init__(self, lexer: PythonLexer, parser: PythonParser, tree: PythonParser.Main_functionContext,
                 debug: bool = False):
        self.lexer = lexer
        self.parser = parser
        self.tree = tree

        if debug:
            self.to_string()

    def to_string(self):
        print("Parse tree")
        print(self.tree.toStringTree(recog=self.parser))
