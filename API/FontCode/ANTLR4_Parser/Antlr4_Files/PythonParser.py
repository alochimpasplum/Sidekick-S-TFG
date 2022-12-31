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
        4,1,30,76,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,4,0,28,
        8,0,11,0,12,0,29,1,0,1,0,1,1,1,1,1,1,3,1,37,8,1,1,2,1,2,3,2,41,8,
        2,1,3,1,3,1,4,1,4,1,4,1,5,1,5,3,5,50,8,5,1,6,1,6,3,6,54,8,6,1,7,
        1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,
        10,1,11,1,11,1,11,1,11,0,0,12,0,2,4,6,8,10,12,14,16,18,20,22,0,1,
        1,0,14,17,71,0,27,1,0,0,0,2,36,1,0,0,0,4,40,1,0,0,0,6,42,1,0,0,0,
        8,44,1,0,0,0,10,49,1,0,0,0,12,53,1,0,0,0,14,55,1,0,0,0,16,59,1,0,
        0,0,18,63,1,0,0,0,20,69,1,0,0,0,22,72,1,0,0,0,24,28,3,2,1,0,25,28,
        3,12,6,0,26,28,3,18,9,0,27,24,1,0,0,0,27,25,1,0,0,0,27,26,1,0,0,
        0,28,29,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,31,1,0,0,0,31,32,
        5,0,0,1,32,1,1,0,0,0,33,37,3,6,3,0,34,37,3,10,5,0,35,37,3,8,4,0,
        36,33,1,0,0,0,36,34,1,0,0,0,36,35,1,0,0,0,37,3,1,0,0,0,38,41,5,28,
        0,0,39,41,5,29,0,0,40,38,1,0,0,0,40,39,1,0,0,0,41,5,1,0,0,0,42,43,
        5,7,0,0,43,7,1,0,0,0,44,45,5,6,0,0,45,46,3,4,2,0,46,9,1,0,0,0,47,
        50,3,20,10,0,48,50,3,22,11,0,49,47,1,0,0,0,49,48,1,0,0,0,50,11,1,
        0,0,0,51,54,3,14,7,0,52,54,3,16,8,0,53,51,1,0,0,0,53,52,1,0,0,0,
        54,13,1,0,0,0,55,56,5,2,0,0,56,57,3,4,2,0,57,58,5,3,0,0,58,15,1,
        0,0,0,59,60,3,4,2,0,60,61,5,27,0,0,61,62,3,4,2,0,62,17,1,0,0,0,63,
        64,3,4,2,0,64,65,5,27,0,0,65,66,3,4,2,0,66,67,7,0,0,0,67,68,3,4,
        2,0,68,19,1,0,0,0,69,70,5,4,0,0,70,71,3,4,2,0,71,21,1,0,0,0,72,73,
        5,5,0,0,73,74,3,4,2,0,74,23,1,0,0,0,6,27,29,36,40,49,53
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
    RULE_math_op = 9
    RULE_print = 10
    RULE_scan = 11

    ruleNames =  [ "prog", "function", "expr", "main_function", "custom_function", 
                   "built_function", "var", "var_decl", "var_assign", "math_op", 
                   "print", "scan" ]

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


        def math_op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.Math_opContext)
            else:
                return self.getTypedRuleContext(PythonParser.Math_opContext,i)


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
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 27
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 24
                    self.function()
                    pass

                elif la_ == 2:
                    self.state = 25
                    self.var()
                    pass

                elif la_ == 3:
                    self.state = 26
                    self.math_op()
                    pass


                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 805306612) != 0):
                    break

            self.state = 31
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
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = PythonParser.Function_AContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.main_function()
                pass
            elif token in [4, 5]:
                localctx = PythonParser.Function_BContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.built_function()
                pass
            elif token in [6]:
                localctx = PythonParser.Function_CContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 35
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
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                localctx = PythonParser.VariableContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(PythonParser.ID)
                pass
            elif token in [29]:
                localctx = PythonParser.NumberContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 39
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
            self.state = 42
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
            self.state = 44
            self.match(PythonParser.FUNCTION)
            self.state = 45
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


    class Built_scanContext(Built_functionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.Built_functionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def scan(self):
            return self.getTypedRuleContext(PythonParser.ScanContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuilt_scan" ):
                listener.enterBuilt_scan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuilt_scan" ):
                listener.exitBuilt_scan(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBuilt_scan" ):
                return visitor.visitBuilt_scan(self)
            else:
                return visitor.visitChildren(self)



    def built_function(self):

        localctx = PythonParser.Built_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_built_function)
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                localctx = PythonParser.Built_printContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.print_()
                pass
            elif token in [5]:
                localctx = PythonParser.Built_scanContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.scan()
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
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = PythonParser.Var_AContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.var_decl()
                pass
            elif token in [28, 29]:
                localctx = PythonParser.Var_BContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 52
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
            self.state = 55
            self.match(PythonParser.VARIABLE_DECLARATIONS)
            self.state = 56
            self.expr()
            self.state = 57
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
            self.state = 59
            self.expr()
            self.state = 60
            self.match(PythonParser.ASSIGN)
            self.state = 61
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Math_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonParser.RULE_math_op

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Math_OperationContext(Math_opContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.Math_opContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonParser.ExprContext,i)

        def ASSIGN(self):
            return self.getToken(PythonParser.ASSIGN, 0)
        def PLUS(self):
            return self.getToken(PythonParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(PythonParser.MINUS, 0)
        def MULT(self):
            return self.getToken(PythonParser.MULT, 0)
        def DIV(self):
            return self.getToken(PythonParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMath_Operation" ):
                listener.enterMath_Operation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMath_Operation" ):
                listener.exitMath_Operation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMath_Operation" ):
                return visitor.visitMath_Operation(self)
            else:
                return visitor.visitChildren(self)



    def math_op(self):

        localctx = PythonParser.Math_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_math_op)
        self._la = 0 # Token type
        try:
            localctx = PythonParser.Math_OperationContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.expr()
            self.state = 64
            self.match(PythonParser.ASSIGN)
            self.state = 65
            self.expr()
            self.state = 66
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 67
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
        self.enterRule(localctx, 20, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(PythonParser.PRINT)
            self.state = 70
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCAN(self):
            return self.getToken(PythonParser.SCAN, 0)

        def expr(self):
            return self.getTypedRuleContext(PythonParser.ExprContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_scan

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScan" ):
                listener.enterScan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScan" ):
                listener.exitScan(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScan" ):
                return visitor.visitScan(self)
            else:
                return visitor.visitChildren(self)




    def scan(self):

        localctx = PythonParser.ScanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_scan)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(PythonParser.SCAN)
            self.state = 73
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





