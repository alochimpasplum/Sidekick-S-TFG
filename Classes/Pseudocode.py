import Constants


class Pseudocode:
    lines: [str] = []
    variables: {} = {}
    functions: [] = []

    def __init__(self, lines: [str], variables: {}, functions: []):
        self.lines = lines
        self.variables = variables
        self.functions = functions

    def to_pseudocode(self) -> [str]:
        lines: [str] = []
        for line in self.lines:
            line.replace(Constants.TAB, "\t")
        return lines

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
