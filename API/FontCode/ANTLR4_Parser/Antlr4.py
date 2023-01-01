from antlr4 import *
from FontCode.ANTLR4_Parser.Antlr4_Files.PythonLexer import PythonLexer
from FontCode.ANTLR4_Parser.Antlr4_Files.PythonParser import PythonParser
from FontCode.ANTLR4_Parser.Antlr4_Files.PythonListener import PythonListener
from Enums import supported_languages
from FontCode.ANTLR4_Parser.Languages.Python import Python
from FontCode.ANTLR4_Parser.Languages.Java import Java
from FontCode.ANTLR4_Parser.Expressions.AntlrToProgram import AntlrToProgram
from FontCode.ANTLR4_Parser.Expressions.Program import Program
from FontCode.ANTLR4_Parser.Languages.Language import Language
import Debug


def antlr4_operation(input_str: str, language: supported_languages = supported_languages.java) -> [str]:
    # Lexer
    lexer: PythonLexer = PythonLexer(InputStream(input_str))
    stream = CommonTokenStream(lexer)

    # Parser
    parser: PythonParser = PythonParser(stream)

    # Tree
    tree: PythonParser.ProgContext = parser.prog()

    # Debug.print_tree(tree, parser)

    # Visitor
    visitor: AntlrToProgram = AntlrToProgram()
    program: Program = visitor.visit(tree)

    if language == supported_languages.python:
        lang: Python = Python(program)
        return lang.get_lines()

    if language == supported_languages.java:
        lang: Java = Java(program)
        return lang.get_lines()
