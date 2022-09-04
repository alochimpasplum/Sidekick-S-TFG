import Constants
from Classes import Pseudocode


class Python:
    lines: [str] = []
    variables: {} = {}
    functions: [] = []

    def __init__(self, pseudocode: Pseudocode):
        self.lines = pseudocode.lines
        self.variables = pseudocode.variables
        self.functions = pseudocode.functions

    def to_pseudocode(self) -> str:
        is_function: bool = False
        font_code: str = ""

        for line in self.lines:
            if Constants.VARIABLE_DECLARATIONS in line:
                if len(self.variables) > 0:
                    line = line.replace(Constants.VARIABLE_DECLARATIONS, "")
                    for key, value in self.variables.items():
                        if is_function:
                            line += "\t"
                        line += "{}: {}".format(key, value)
                        if value == "int":
                            line += "= 0"
                        elif value == "string":
                            line += " = \"\""
                        line += "\n"

                        font_code += line
                        line = ""
                font_code += "\n"

            if Constants.MAIN_FUNCTION in line:
                line = line.replace(Constants.MAIN_FUNCTION, "def")
                line += ":"
                is_function = True

            if Constants.TAB in line:
                line = line.replace(Constants.TAB, "\t")

            if Constants.PRINT in line:
                line = line.replace(Constants.PRINT, "print(")
                line += ")"

            if Constants.VARIABLE in line:
                line = line.replace(Constants.VARIABLE, "")

            if Constants.SCAN in line:
                line = line.replace(Constants.SCAN, "input(")
                line += ")"

            if Constants.FUNCTION in line:
                line = line.replace(Constants.FUNCTION, "")
                line += "()"

            if Constants.MATH_OPERATION in line:
                line = line.replace(Constants.MATH_OPERATION, "")

            if Constants.IF in line:
                line = line.replace(Constants.IF, "if ")

            if Constants.IF_TRUE_START in line:
                line = line.replace(Constants.IF_TRUE_START, ":")
                line += ""

            if Constants.IF_TRUE_END in line:
                line = line.replace(Constants.IF_TRUE_END, "")

            if Constants.IF_FALSE_START in line:
                line = line.replace(Constants.IF_FALSE_START, "else:")

            if Constants.IF_FALSE_END in line:
                line = line.replace(Constants.IF_FALSE_END, "")

            if Constants.END_CODE in line:
                line = line.replace(Constants.END_CODE, "")

            if len(line.strip()) > 0:
                line += "\n"
                font_code += line

        return font_code
