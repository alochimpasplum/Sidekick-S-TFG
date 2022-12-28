# Generated from Python.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser

# This class defines a complete listener for a parse tree produced by PythonParser.
class PythonListener(ParseTreeListener):

    # Enter a parse tree produced by PythonParser#prog.
    def enterProg(self, ctx:PythonParser.ProgContext):
        pass

    # Exit a parse tree produced by PythonParser#prog.
    def exitProg(self, ctx:PythonParser.ProgContext):
        pass


    # Enter a parse tree produced by PythonParser#function.
    def enterFunction(self, ctx:PythonParser.FunctionContext):
        pass

    # Exit a parse tree produced by PythonParser#function.
    def exitFunction(self, ctx:PythonParser.FunctionContext):
        pass


    # Enter a parse tree produced by PythonParser#Variable.
    def enterVariable(self, ctx:PythonParser.VariableContext):
        pass

    # Exit a parse tree produced by PythonParser#Variable.
    def exitVariable(self, ctx:PythonParser.VariableContext):
        pass


    # Enter a parse tree produced by PythonParser#Number.
    def enterNumber(self, ctx:PythonParser.NumberContext):
        pass

    # Exit a parse tree produced by PythonParser#Number.
    def exitNumber(self, ctx:PythonParser.NumberContext):
        pass


    # Enter a parse tree produced by PythonParser#main_function.
    def enterMain_function(self, ctx:PythonParser.Main_functionContext):
        pass

    # Exit a parse tree produced by PythonParser#main_function.
    def exitMain_function(self, ctx:PythonParser.Main_functionContext):
        pass


    # Enter a parse tree produced by PythonParser#custom_function.
    def enterCustom_function(self, ctx:PythonParser.Custom_functionContext):
        pass

    # Exit a parse tree produced by PythonParser#custom_function.
    def exitCustom_function(self, ctx:PythonParser.Custom_functionContext):
        pass


    # Enter a parse tree produced by PythonParser#built_function.
    def enterBuilt_function(self, ctx:PythonParser.Built_functionContext):
        pass

    # Exit a parse tree produced by PythonParser#built_function.
    def exitBuilt_function(self, ctx:PythonParser.Built_functionContext):
        pass


    # Enter a parse tree produced by PythonParser#var.
    def enterVar(self, ctx:PythonParser.VarContext):
        pass

    # Exit a parse tree produced by PythonParser#var.
    def exitVar(self, ctx:PythonParser.VarContext):
        pass


    # Enter a parse tree produced by PythonParser#var_decl.
    def enterVar_decl(self, ctx:PythonParser.Var_declContext):
        pass

    # Exit a parse tree produced by PythonParser#var_decl.
    def exitVar_decl(self, ctx:PythonParser.Var_declContext):
        pass


    # Enter a parse tree produced by PythonParser#var_assign.
    def enterVar_assign(self, ctx:PythonParser.Var_assignContext):
        pass

    # Exit a parse tree produced by PythonParser#var_assign.
    def exitVar_assign(self, ctx:PythonParser.Var_assignContext):
        pass


    # Enter a parse tree produced by PythonParser#print.
    def enterPrint(self, ctx:PythonParser.PrintContext):
        pass

    # Exit a parse tree produced by PythonParser#print.
    def exitPrint(self, ctx:PythonParser.PrintContext):
        pass



del PythonParser