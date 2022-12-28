# Generated from Python.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser

# This class defines a complete generic visitor for a parse tree produced by PythonParser.

class PythonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PythonParser#prog.
    def visitProg(self, ctx:PythonParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#function.
    def visitFunction(self, ctx:PythonParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#Variable.
    def visitVariable(self, ctx:PythonParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#Number.
    def visitNumber(self, ctx:PythonParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#main_function.
    def visitMain_function(self, ctx:PythonParser.Main_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#custom_function.
    def visitCustom_function(self, ctx:PythonParser.Custom_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#built_function.
    def visitBuilt_function(self, ctx:PythonParser.Built_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#var.
    def visitVar(self, ctx:PythonParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#var_decl.
    def visitVar_decl(self, ctx:PythonParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#var_assign.
    def visitVar_assign(self, ctx:PythonParser.Var_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#print.
    def visitPrint(self, ctx:PythonParser.PrintContext):
        return self.visitChildren(ctx)



del PythonParser