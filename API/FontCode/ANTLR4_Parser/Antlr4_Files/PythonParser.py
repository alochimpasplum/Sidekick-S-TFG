# Generated from Python.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,30,60,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,4,0,23,8,0,11,0,12,0,24,1,0,1,
        0,1,1,1,1,1,1,3,1,32,8,1,1,2,1,2,3,2,36,8,2,1,3,1,3,1,4,1,4,1,4,
        1,5,1,5,1,6,1,6,3,6,47,8,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,
        9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,0,55,0,22,1,0,0,0,2,
        31,1,0,0,0,4,35,1,0,0,0,6,37,1,0,0,0,8,39,1,0,0,0,10,42,1,0,0,0,
        12,46,1,0,0,0,14,48,1,0,0,0,16,52,1,0,0,0,18,56,1,0,0,0,20,23,3,
        2,1,0,21,23,3,12,6,0,22,20,1,0,0,0,22,21,1,0,0,0,23,24,1,0,0,0,24,
        22,1,0,0,0,24,25,1,0,0,0,25,26,1,0,0,0,26,27,5,0,0,1,27,1,1,0,0,
        0,28,32,3,6,3,0,29,32,3,10,5,0,30,32,3,8,4,0,31,28,1,0,0,0,31,29,
        1,0,0,0,31,30,1,0,0,0,32,3,1,0,0,0,33,36,5,28,0,0,34,36,5,29,0,0,
        35,33,1,0,0,0,35,34,1,0,0,0,36,5,1,0,0,0,37,38,5,7,0,0,38,7,1,0,
        0,0,39,40,5,6,0,0,40,41,3,4,2,0,41,9,1,0,0,0,42,43,3,18,9,0,43,11,
        1,0,0,0,44,47,3,14,7,0,45,47,3,16,8,0,46,44,1,0,0,0,46,45,1,0,0,
        0,47,13,1,0,0,0,48,49,5,2,0,0,49,50,3,4,2,0,50,51,5,3,0,0,51,15,
        1,0,0,0,52,53,3,4,2,0,53,54,5,27,0,0,54,55,3,4,2,0,55,17,1,0,0,0,
        56,57,5,4,0,0,57,58,3,4,2,0,58,19,1,0,0,0,5,22,24,31,35,46
    ]

class PythonParser ( Parser ):

    grammarFileName = "Python.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<TAB>'", "'<VAR_DECLARATION>'", "<INVALID>", 
                     "'<PRINT>'", "'<SCAN>'", "'<FUNC>'", "'<BASE_FUNC>'", 
                     "'<IF>'", "'<IF_TRUE>'", "'</IF_TRUE>'", "'<IF_FALSE>'", 
                     "'</IF_FALSE>'", "'<END>'", "'+'", "'-'", "'*'", "'/'", 
                     "'&&'", "'||'", "'!'", "'>'", "'<'", "'>='", "'<='", 
                     "'=='", "'!='", "'='" ]

    symbolicNames = [ "<INVALID>", "TAB", "VARIABLE_DECLARATIONS", "VARIABLE_TYPE", 
                      "PRINT", "SCAN", "FUNCTION", "MAIN_FUNCTION", "IF", 
                      "IF_TRUE_START", "IF_TRUE_END", "IF_FALSE_START", 
                      "IF_FALSE_END", "END_CODE", "PLUS", "MINUS", "MULT", 
                      "DIV", "AND", "OR", "NOT", "GT", "LET", "GEQ", "LEQ", 
                      "EQ", "NEQ", "ASSIGN", "ID", "NUMBER", "WS" ]

    RULE_prog = 0
    RULE_function = 1
    RULE_expr = 2
    RULE_main_function = 3
    RULE_custom_function = 4
    RULE_built_function = 5
    RULE_var = 6
    RULE_var_decl = 7
    RULE_var_assign = 8
    RULE_print = 9

    ruleNames =  [ "prog", "function", "expr", "main_function", "custom_function", 
                   "built_function", "var", "var_decl", "var_assign", "print" ]

    EOF = Token.EOF
    TAB=1
    VARIABLE_DECLARATIONS=2
    VARIABLE_TYPE=3
    PRINT=4
    SCAN=5
    FUNCTION=6
    MAIN_FUNCTION=7
    IF=8
    IF_TRUE_START=9
    IF_TRUE_END=10
    IF_FALSE_START=11
    IF_FALSE_END=12
    END_CODE=13
    PLUS=14
    MINUS=15
    MULT=16
    DIV=17
    AND=18
    OR=19
    NOT=20
    GT=21
    LET=22
    GEQ=23
    LEQ=24
    EQ=25
    NEQ=26
    ASSIGN=27
    ID=28
    NUMBER=29
    WS=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PythonParser.EOF, 0)

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.FunctionContext)
            else:
                return self.getTypedRuleContext(PythonParser.FunctionContext,i)


        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.VarContext)
            else:
                return self.getTypedRuleContext(PythonParser.VarContext,i)


        def getRuleIndex(self):
            return PythonParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = PythonParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4, 6, 7]:
                    self.state = 20
                    self.function()
                    pass
                elif token in [2, 28, 29]:
                    self.state = 21
                    self.var()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 24 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 805306580) != 0):
                    break

            self.state = 26
            self.match(PythonParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonParser.RULE_function

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Function_BContext(FunctionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.FunctionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def built_function(self):
            return self.getTypedRuleContext(PythonParser.Built_functionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_B" ):
                listener.enterFunction_B(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_B" ):
                listener.exitFunction_B(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_B" ):
                return visitor.visitFunction_B(self)
            else:
                return visitor.visitChildren(self)


    class Function_AContext(FunctionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.FunctionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def main_function(self):
            return self.getTypedRuleContext(PythonParser.Main_functionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_A" ):
                listener.enterFunction_A(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_A" ):
                listener.exitFunction_A(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_A" ):
                return visitor.visitFunction_A(self)
            else:
                return visitor.visitChildren(self)


    class Function_CContext(FunctionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.FunctionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def custom_function(self):
            return self.getTypedRuleContext(PythonParser.Custom_functionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_C" ):
                listener.enterFunction_C(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_C" ):
                listener.exitFunction_C(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_C" ):
                return visitor.visitFunction_C(self)
            else:
                return visitor.visitChildren(self)



    def function(self):

        localctx = PythonParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = PythonParser.Function_AContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.main_function()
                pass
            elif token in [4]:
                localctx = PythonParser.Function_BContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.built_function()
                pass
            elif token in [6]:
                localctx = PythonParser.Function_CContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.custom_function()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VariableContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(PythonParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class NumberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(PythonParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = PythonParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                localctx = PythonParser.VariableContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.match(PythonParser.ID)
                pass
            elif token in [29]:
                localctx = PythonParser.NumberContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(PythonParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN_FUNCTION(self):
            return self.getToken(PythonParser.MAIN_FUNCTION, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_main_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain_function" ):
                listener.enterMain_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain_function" ):
                listener.exitMain_function(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_function" ):
                return visitor.visitMain_function(self)
            else:
                return visitor.visitChildren(self)




    def main_function(self):

        localctx = PythonParser.Main_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_main_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(PythonParser.MAIN_FUNCTION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Custom_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(PythonParser.FUNCTION, 0)

        def expr(self):
            return self.getTypedRuleContext(PythonParser.ExprContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_custom_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCustom_function" ):
                listener.enterCustom_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCustom_function" ):
                listener.exitCustom_function(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCustom_function" ):
                return visitor.visitCustom_function(self)
            else:
                return visitor.visitChildren(self)




    def custom_function(self):

        localctx = PythonParser.Custom_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_custom_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(PythonParser.FUNCTION)
            self.state = 40
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Built_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonParser.RULE_built_function

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Built_printContext(Built_functionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.Built_functionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def print_(self):
            return self.getTypedRuleContext(PythonParser.PrintContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuilt_print" ):
                listener.enterBuilt_print(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuilt_print" ):
                listener.exitBuilt_print(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBuilt_print" ):
                return visitor.visitBuilt_print(self)
            else:
                return visitor.visitChildren(self)



    def built_function(self):

        localctx = PythonParser.Built_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_built_function)
        try:
            localctx = PythonParser.Built_printContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.print_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonParser.RULE_var

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Var_AContext(VarContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.VarContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def var_decl(self):
            return self.getTypedRuleContext(PythonParser.Var_declContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_A" ):
                listener.enterVar_A(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_A" ):
                listener.exitVar_A(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_A" ):
                return visitor.visitVar_A(self)
            else:
                return visitor.visitChildren(self)


    class Var_BContext(VarContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.VarContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def var_assign(self):
            return self.getTypedRuleContext(PythonParser.Var_assignContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_B" ):
                listener.enterVar_B(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_B" ):
                listener.exitVar_B(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_B" ):
                return visitor.visitVar_B(self)
            else:
                return visitor.visitChildren(self)



    def var(self):

        localctx = PythonParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_var)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = PythonParser.Var_AContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.var_decl()
                pass
            elif token in [28, 29]:
                localctx = PythonParser.Var_BContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.var_assign()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_DECLARATIONS(self):
            return self.getToken(PythonParser.VARIABLE_DECLARATIONS, 0)

        def expr(self):
            return self.getTypedRuleContext(PythonParser.ExprContext,0)


        def VARIABLE_TYPE(self):
            return self.getToken(PythonParser.VARIABLE_TYPE, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decl" ):
                listener.enterVar_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decl" ):
                listener.exitVar_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = PythonParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(PythonParser.VARIABLE_DECLARATIONS)
            self.state = 49
            self.expr()
            self.state = 50
            self.match(PythonParser.VARIABLE_TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonParser.ExprContext,i)


        def ASSIGN(self):
            return self.getToken(PythonParser.ASSIGN, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_var_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_assign" ):
                listener.enterVar_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_assign" ):
                listener.exitVar_assign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_assign" ):
                return visitor.visitVar_assign(self)
            else:
                return visitor.visitChildren(self)




    def var_assign(self):

        localctx = PythonParser.Var_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_var_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.expr()
            self.state = 53
            self.match(PythonParser.ASSIGN)
            self.state = 54
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(PythonParser.PRINT, 0)

        def expr(self):
            return self.getTypedRuleContext(PythonParser.ExprContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = PythonParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(PythonParser.PRINT)
            self.state = 57
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





