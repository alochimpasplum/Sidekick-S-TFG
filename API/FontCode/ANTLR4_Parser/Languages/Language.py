from abc import ABC, abstractmethod
from FontCode.ANTLR4_Parser.Expressions.MainFunction import MainFunction
from FontCode.ANTLR4_Parser.Expressions.VariableDeclaration import VariableDeclaration
from FontCode.ANTLR4_Parser.Expressions.VariableAssign import VariableAssign
from FontCode.ANTLR4_Parser.Expressions.Print import Print
from FontCode.ANTLR4_Parser.Expressions.MathOperation import MathOperation


class Language(ABC):

    @abstractmethod
    def __generate_code__(self):
        pass

    @abstractmethod
    def __handle_main_function__(self, expression: MainFunction):
        pass

    @abstractmethod
    def __handle_variable_declaration__(self, expression: VariableDeclaration):
        pass

    @abstractmethod
    def __handle_variable_assign__(self, expression: VariableAssign):
        pass

    @abstractmethod
    def __handle_print__(self, expression: Print):
        pass

    @abstractmethod
    def __handle_math_operation__(self, expression: MathOperation):
        pass
