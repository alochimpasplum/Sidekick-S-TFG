import Constants
from FontCode.ANTLR4_Parser.Languages.Language import Language
from FontCode.ANTLR4_Parser.Expressions.Program import Program
from FontCode.ANTLR4_Parser.Expressions.Expression import Expression
from FontCode.ANTLR4_Parser.Expressions.MainFunction import MainFunction
from FontCode.ANTLR4_Parser.Expressions.VariableDeclaration import VariableDeclaration
from FontCode.ANTLR4_Parser.Expressions.VariableAssign import VariableAssign
from FontCode.ANTLR4_Parser.Expressions.Print import Print
from FontCode.ANTLR4_Parser.Expressions.MathOperation import MathOperation
from FontCode.ANTLR4_Parser.Expressions.Scan import Scan
from FontCode.ANTLR4_Parser.Expressions.Conditional import Conditional
from FontCode.ANTLR4_Parser.Expressions.ConditionalBranches import ConditionalBranches
from FontCode.ANTLR4_Parser.Expressions.ConditionalBranch import ConditionalBranch
from FontCode.ANTLR4_Parser.Expressions.ConditionalLines import ConditionalLines
from FontCode.ANTLR4_Parser.Expressions.If import If
from FontCode.ANTLR4_Parser.Expressions.SwitchCase import SwitchCase
from FontCode.ANTLR4_Parser.Expressions.MathOperationSimplified import MathOperationSimplified


class Python(Language):
    program: Program
    code_lines: [str] = []
    tab: str = "\t"
    null: str = "None"

    def __init__(self, program: Program):
        self.program = program
        self.__generate_code__()

    def __generate_code__(self):
        for expression in self.program.expressions:
            self.code_lines.extend(self.__handle_expression__(expression))

    def __handle_expression__(self, expression: Expression) -> [str]:
        lines: [str] = []

        if isinstance(expression, MainFunction):
            lines.append(self.__handle_main_function__(expression))
        if isinstance(expression, VariableDeclaration):
            lines.append("{0}{1}".format(self.tab, self.__handle_variable_declaration__(expression)))
        if isinstance(expression, VariableAssign):
            lines.append("{0}{1}".format(self.tab, self.__handle_variable_assign__(expression)))
        if isinstance(expression, Print):
            lines.append("{0}{1}".format(self.tab, self.__handle_print__(expression)))
        if isinstance(expression, MathOperation):
            lines.append("{0}{1}".format(self.tab, self.__handle_math_operation__(expression)))
        if isinstance(expression, MathOperationSimplified):
            lines.append("{0}{1}".format(self.tab, self.__handle_math_operation_simplified__(expression)))
        if isinstance(expression, Scan):
            lines.append("{0}{1}".format(self.tab, self.__handle_scan__(expression)))
        if isinstance(expression, Conditional):
            if isinstance(expression.condition, If):
                lines.extend(self.__handle_if__(expression))
            if isinstance(expression.condition, SwitchCase):
                lines.extend(self.__handle_switch_case__(expression))

        return lines

    def __handle_main_function__(self, expression: MainFunction) -> str:
        return "def main():"

    def __handle_variable_declaration__(self, expression: VariableDeclaration) -> str:
        var_type: str = ""
        if expression.var_type == Constants.STRING:
            var_type = "str"
        elif expression.var_type == Constants.INTEGER:
            var_type = "int"
        return "{0}: {1} = {2}".format(expression.get_variable_id(), var_type, self.null)

    def __handle_variable_assign__(self, expression: VariableAssign) -> str:
        return "{0} = {1}".format(expression.get_variable_id(), expression.get_assign_value())

    def __handle_print__(self, expression: Print) -> str:
        return "print({0})".format(expression.get_print())

    def __handle_math_operation__(self, expression: MathOperation) -> str:
        return "{0} = {1} {2} {3}".format(expression.get_assign(),
                                          expression.get_left(),
                                          expression.operation,
                                          expression.get_right())

    def __handle_math_operation_simplified__(self, expression: MathOperationSimplified) -> str:
        return "{0} {1} {2}".format(expression.get_left(), expression.operation, expression.get_right())

    def __handle_scan__(self, expression: Scan) -> str:
        return "{0} = input()".format(expression.get_var())

    def __handle_if__(self, expression: Conditional) -> [str]:
        lines: [str] = []
        condition_true: [str] = ['YES', 'SI', 'TRUE', 'VERDADERO', '1']
        condition_false: [str] = ['NO', 'FALSE', 'FALSO', '0']

        if isinstance(expression.condition, If):
            lines.append("if {0} {1} {2}:".format(
                expression.condition.get_left(),
                expression.condition.condition,
                expression.condition.get_right()))

        if isinstance(expression.conditional_branches, ConditionalBranches):
            branch_true: [ConditionalBranch] = [x for x in expression.conditional_branches.branches if
                                                x.get_condition().upper() in condition_true]
            branch_false: [ConditionalBranch] = [x for x in expression.conditional_branches.branches if
                                                 x.get_condition().upper() in condition_false]

            true: ConditionalBranch = branch_true[0]
            false: ConditionalBranch = branch_false[0]
            conditional_lines: ConditionalLines

            # True statement
            conditional_lines = true.conditional_lines
            for line in conditional_lines.lines:
                lines.extend(self.__handle_expression__(line))

            # False statement
            conditional_lines = false.conditional_lines
            lines.append("else:")
            for line in conditional_lines.lines:
                lines.extend(self.__handle_expression__(line))

            # Add tabs
            for i in range(0, len(lines)):
                lines[i] = "{0}{1}".format(self.tab, lines[i])

        return lines

    def __handle_switch_case__(self, expression: Conditional) -> [str]:
        lines: [str] = []
        # TODO: implementar
        return lines

    def get_lines(self) -> [str]:
        return self.code_lines
