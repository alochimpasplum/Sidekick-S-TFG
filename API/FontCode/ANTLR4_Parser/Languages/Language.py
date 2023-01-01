from abc import ABC, abstractmethod
from FontCode.ANTLR4_Parser.Expressions.Expression import Expression
from FontCode.ANTLR4_Parser.Expressions.MainFunction import MainFunction
from FontCode.ANTLR4_Parser.Expressions.VariableDeclaration import VariableDeclaration
from FontCode.ANTLR4_Parser.Expressions.VariableAssign import VariableAssign
from FontCode.ANTLR4_Parser.Expressions.Print import Print
from FontCode.ANTLR4_Parser.Expressions.MathOperation import MathOperation
from FontCode.ANTLR4_Parser.Expressions.Scan import Scan
from FontCode.ANTLR4_Parser.Expressions.Conditional import Conditional


class Language(ABC):

    @abstractmethod
    def __generate_code__(self):
        pass

    @abstractmethod
    def __handle_expression__(self, expression: Expression) -> [str]:
        pass

    @abstractmethod
    def __handle_main_function__(self, expression: MainFunction) -> str:
        pass

    @abstractmethod
    def __handle_variable_declaration__(self, expression: VariableDeclaration) -> str:
        pass

    @abstractmethod
    def __handle_variable_assign__(self, expression: VariableAssign) -> str:
        pass

    @abstractmethod
    def __handle_print__(self, expression: Print) -> str:
        pass

    @abstractmethod
    def __handle_math_operation__(self, expression: MathOperation) -> str:
        pass

    @abstractmethod
    def __handle_scan__(self, expression: Scan) -> str:
        pass

    @abstractmethod
    def __handle_switch_case__(self, expression: Conditional) -> [str]:
        pass

    @abstractmethod
    def __handle_if__(self, expression: Conditional) -> [str]:
        pass

