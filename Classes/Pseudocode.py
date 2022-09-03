import Constants


class Pseudocode:
    lines: [str] = []
    variables: {} = {}
    functions: [] = []

    def __init__(self, lines: [str], functions: [], variables: {}):
        self.lines = lines
        self.variables = variables
        self.functions = functions

    def to_pseudocode(self) -> str:
        is_function: bool = False
        font_code: str = ""
        for line in self.lines:
            if Constants.MAIN_FUNCTION in line:
                line = line.replace(Constants.MAIN_FUNCTION, "function")
                line += "()"
                is_function = True
            if Constants.TAB in line:
                line = line.replace(Constants.TAB, "\t")
            if Constants.PRINT in line:
                line = line.replace(Constants.PRINT, "PRINT(")
                line += ")"
            if Constants.VARIABLE in line:
                line = line.replace(Constants.VARIABLE, "")
            if Constants.SCAN in line:
                line = line.replace(Constants.SCAN, "SCAN(")
                line += ")"
            if Constants.FUNCTION in line:
                line = line.replace(Constants.FUNCTION, "")
                line += "()"
            if Constants.MATH_OPERATION in line:
                line = line.replace(Constants.MATH_OPERATION, "")
            line += "\n"
            font_code += line

        if len(self.variables) > 0:
            font_code += "\n"
            line: str = ""
            for key, value in self.variables.items():
                if is_function:
                    line += "\t"
                line += "{} : {}".format(value, key)
                line += "\n"

                font_code += line
                line = ""

        print(font_code)
        return font_code

    def to_string(self) -> str:
        response: str = ""
        response += "--- LINES ---\n"
        for line in self.lines:
            response += "{}\n".format(line)
        response += "--- VARIABLES ---\n"
        for key, value in self.variables.items():
            response += "nombre variable: {}, tipo variable: {}".format(key, value)
        response += "--- FUNCIONES ---"
        for fun in self.functions:
            response += fun
        return response
