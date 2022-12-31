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


    # Visit a parse tree produced by PythonParser#Function_A.
    def visitFunction_A(self, ctx:PythonParser.Function_AContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#Function_B.
    def visitFunction_B(self, ctx:PythonParser.Function_BContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#Function_C.
    def visitFunction_C(self, ctx:PythonParser.Function_CContext):
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


    # Visit a parse tree produced by PythonParser#Built_print.
    def visitBuilt_print(self, ctx:PythonParser.Built_printContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#Built_scan.
    def visitBuilt_scan(self, ctx:PythonParser.Built_scanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#Var_A.
    def visitVar_A(self, ctx:PythonParser.Var_AContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#Var_B.
    def visitVar_B(self, ctx:PythonParser.Var_BContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#var_decl.
    def visitVar_decl(self, ctx:PythonParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#var_assign.
    def visitVar_assign(self, ctx:PythonParser.Var_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#Math_Operation.
    def visitMath_Operation(self, ctx:PythonParser.Math_OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#print.
    def visitPrint(self, ctx:PythonParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#scan.
    def visitScan(self, ctx:PythonParser.ScanContext):
        return self.visitChildren(ctx)



del PythonParser