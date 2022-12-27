import antlr4.tree.Tree
from antlr4 import *
from FontCode.ANTLR4_Parser.Build.PythonLexer import PythonLexer
from FontCode.ANTLR4_Parser.Build.PythonParser import PythonParser
from FontCode.ANTLR4_Parser.Build.PythonListener import PythonListener
from Enums import supported_languages
from FontCode.ANTLR4_Parser.Languages import Python


def antlr4_operation(input_str: str, language: supported_languages = supported_languages.python):
    # Lexer
    lexer: PythonLexer = PythonLexer(InputStream(input_str))
    stream = CommonTokenStream(lexer)

    # Parser
    parser: PythonParser = PythonParser(stream)
    tree: PythonParser.Main_functionContext = parser.main_function()

    lang = None

    if language == supported_languages.python:
        lang = Python.Python(lexer, parser, tree, True)

    # print(tree.toStringTree(recog=parser))
    # __handle_children__(tree)


def __handle_children__(parsed_tree):
    child: PythonParser.SentenceContext
    for child in parsed_tree.getChildren():
        print(child.getText())
        print(isinstance(child, antlr4.tree.Tree.TerminalNode))
