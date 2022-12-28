from FontCode.ANTLR4_Parser.Antlr4_Files.PythonParser import PythonParser
from FontCode.ANTLR4_Parser.Antlr4_Files.PythonVisitor import PythonVisitor
from FontCode.ANTLR4_Parser.Expressions.Number import Number
from FontCode.ANTLR4_Parser.Expressions.Variable import Variable
import Constants


class AntlrToExpression(PythonVisitor):

    variables: {} = {}

    def visitFunction(self, ctx: PythonParser.FunctionContext):
        return super().visitFunction(ctx)

    def visitVariable(self, ctx: PythonParser.VariableContext):
        name: str = ctx.getChild(0).getText()
        if name not in self.variables:
            self.variables[name] = Constants.STRING
        return Variable(name, self.variables[name])

    def visitNumber(self, ctx: PythonParser.NumberContext):
        num: str = ctx.getChild(0).getText()
        return Number(int(num))

    def visitMain_function(self, ctx: PythonParser.Main_functionContext):
        return super().visitMain_function(ctx)

    def visitCustom_function(self, ctx: PythonParser.Custom_functionContext):
        return super().visitCustom_function(ctx)

    def visitBuilt_function(self, ctx: PythonParser.Built_functionContext):
        return super().visitBuilt_function(ctx)

    def visitVar(self, ctx: PythonParser.VarContext):
        return super().visitVar(ctx)

    def visitVar_decl(self, ctx: PythonParser.Var_declContext):
        name: str = ctx.getChild(1).getChild(0).getText()
        var_type: str = ctx.getChild(2).getText()
        self.variables[name] = var_type
        return Variable(name, var_type)

    def visitVar_assign(self, ctx: PythonParser.Var_assignContext):
        return super().visitVar_assign(ctx)

    def visitPrint(self, ctx: PythonParser.PrintContext):
        return super().visitPrint(ctx)
