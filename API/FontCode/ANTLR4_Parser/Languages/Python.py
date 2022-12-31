import Constants
from FontCode.ANTLR4_Parser.Languages.Language import Language
from FontCode.ANTLR4_Parser.Expressions.Program import Program
from FontCode.ANTLR4_Parser.Expressions.Number import Number
from FontCode.ANTLR4_Parser.Expressions.Variable import Variable
from FontCode.ANTLR4_Parser.Expressions.Expression import Expression
from FontCode.ANTLR4_Parser.Expressions.Function import Function
from FontCode.ANTLR4_Parser.Expressions.MainFunction import MainFunction
from FontCode.ANTLR4_Parser.Expressions.CustomFunction import CustomFunction
from FontCode.ANTLR4_Parser.Expressions.BuiltFunction import BuiltFunction
from FontCode.ANTLR4_Parser.Expressions.Var import Var
from FontCode.ANTLR4_Parser.Expressions.VariableDeclaration import VariableDeclaration
from FontCode.ANTLR4_Parser.Expressions.VariableAssign import VariableAssign
from FontCode.ANTLR4_Parser.Expressions.Print import Print
from FontCode.ANTLR4_Parser.Expressions.MathOperation import MathOperation


class Python(Language):
    program: Program
    code_lines: [str] = []
    tab: str = "\t"
    null: str = "None"

    def __init__(self, program: Program):
        self.program = program
        self.__generate_code__()

    def __generate_code__(self):
        expression: Expression
        for expression in self.program.expressions:
            print(type(expression))
            if isinstance(expression, MainFunction):
                self.__handle_main_function__(expression)
            if isinstance(expression, VariableDeclaration):
                self.__handle_variable_declaration__(expression)
            if isinstance(expression, VariableAssign):
                self.__handle_variable_assign__(expression)
            if isinstance(expression, Print):
                self.__handle_print__(expression)
            if isinstance(expression, MathOperation):
                self.__handle_math_operation__(expression)

    def __handle_main_function__(self, expression: MainFunction):
        self.code_lines.append("def main():")

    def __handle_variable_declaration__(self, expression: VariableDeclaration):
        var_type: str = ""
        if expression.var_type == Constants.STRING:
            var_type = "str"
        elif expression.var_type == Constants.INTEGER:
            var_type = "int"
        self.code_lines.append("{0}{1}: {2} = {3}".format(self.tab, expression.get_variable_id(), var_type, self.null))

    def __handle_variable_assign__(self, expression: VariableAssign):
        self.code_lines.append("{0}{1} = {2}".format(self.tab, expression.get_variable_id(),
                                                     expression.get_assign_value()))

    def __handle_print__(self, expression: Print):
        self.code_lines.append("{0}print({1})".format(self.tab, expression.get_print()))

    def __handle_math_operation__(self, expression: MathOperation):
        self.code_lines.append("{0} = {1} {2} {3}".format(expression.get_assign(),
                                                          expression.get_left(),
                                                          expression.operation,
                                                          expression.get_right()))
