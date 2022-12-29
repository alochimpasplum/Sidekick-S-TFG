import antlr4.tree.Tree
from antlr4 import *
from FontCode.ANTLR4_Parser.Antlr4_Files.PythonLexer import PythonLexer
from FontCode.ANTLR4_Parser.Antlr4_Files.PythonParser import PythonParser
from FontCode.ANTLR4_Parser.Antlr4_Files.PythonListener import PythonListener
from Enums import supported_languages
from FontCode.ANTLR4_Parser.Languages import Python


def antlr4_operation(input_str: str, language: supported_languages = supported_languages.python):
    # Lexer
    lexer: PythonLexer = PythonLexer(InputStream(input_str))
    stream = CommonTokenStream(lexer)

    # Parser
    parser: PythonParser = PythonParser(stream)
    tree: PythonParser.Main_functionContext = parser.prog()

    lang = None

    if language == supported_languages.python:
        lang = Python.Python(lexer, parser, tree, True)

