from antlr4 import *
from FontCode.ANTLR4_Parser.Build.PythonLexer import PythonLexer
from FontCode.ANTLR4_Parser.Build.PythonParser import PythonParser
from FontCode.ANTLR4_Parser.Build.PythonListener import PythonListener


def antlr4_operation(input_str: str):
    lexer = PythonLexer(InputStream(input_str))
    stream = CommonTokenStream(lexer)
    parser = PythonParser(stream)
    tree = parser.main_function()
    __handle_children__(tree)


def __handle_children__(tree):
    child: PythonParser.SentenceContext
    for child in tree.getChildren():
        print(child.getText())
