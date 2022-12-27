from FontCode.ANTLR4_Parser.Build.PythonParser import PythonParser
from FontCode.ANTLR4_Parser.Expressions import Expression
from FontCode.ANTLR4_Parser.Build.PythonVisitor import PythonVisitor


class AntlrToExpression(PythonVisitor):
    def visitExpr(self, ctx: PythonParser.ExprContext):
        return super().visitExpr(ctx)

    def visitFunction(self, ctx: PythonParser.FunctionContext):
        return super().visitFunction(ctx)

    def visitMain_function(self, ctx: PythonParser.Main_functionContext):
        return super().visitMain_function(ctx)

    def visitCustom_function(self, ctx: PythonParser.Custom_functionContext):
        return super().visitCustom_function(ctx)

    def visitBuilt_function(self, ctx: PythonParser.Built_functionContext):
        return super().visitBuilt_function(ctx)

    def visitVariable(self, ctx: PythonParser.VariableContext):
        return super().visitVariable(ctx)

    def visitVar_decl(self, ctx: PythonParser.Var_declContext):
        return super().visitVar_decl(ctx)

    def visitVar_assign(self, ctx: PythonParser.Var_assignContext):
        return super().visitVar_assign(ctx)

    def visitPrint(self, ctx: PythonParser.PrintContext):
        return super().visitPrint(ctx)
