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
        4,1,30,62,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,4,0,23,8,0,11,0,12,0,24,1,0,1,
        0,1,1,1,1,1,2,1,2,1,2,3,2,34,8,2,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,6,
        1,6,3,6,45,8,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,
        9,3,9,60,8,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,1,1,0,28,29,57,
        0,22,1,0,0,0,2,28,1,0,0,0,4,33,1,0,0,0,6,35,1,0,0,0,8,37,1,0,0,0,
        10,40,1,0,0,0,12,44,1,0,0,0,14,46,1,0,0,0,16,50,1,0,0,0,18,59,1,
        0,0,0,20,23,3,4,2,0,21,23,3,12,6,0,22,20,1,0,0,0,22,21,1,0,0,0,23,
        24,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,26,1,0,0,0,26,27,5,0,0,
        1,27,1,1,0,0,0,28,29,7,0,0,0,29,3,1,0,0,0,30,34,3,6,3,0,31,34,3,
        10,5,0,32,34,3,8,4,0,33,30,1,0,0,0,33,31,1,0,0,0,33,32,1,0,0,0,34,
        5,1,0,0,0,35,36,5,7,0,0,36,7,1,0,0,0,37,38,5,6,0,0,38,39,3,2,1,0,
        39,9,1,0,0,0,40,41,3,18,9,0,41,11,1,0,0,0,42,45,3,14,7,0,43,45,3,
        16,8,0,44,42,1,0,0,0,44,43,1,0,0,0,45,13,1,0,0,0,46,47,5,2,0,0,47,
        48,3,2,1,0,48,49,5,3,0,0,49,15,1,0,0,0,50,51,3,2,1,0,51,52,5,27,
        0,0,52,53,3,2,1,0,53,17,1,0,0,0,54,55,5,4,0,0,55,60,3,2,1,0,56,57,
        5,4,0,0,57,58,5,3,0,0,58,60,3,2,1,0,59,54,1,0,0,0,59,56,1,0,0,0,
        60,19,1,0,0,0,5,22,24,33,44,59
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
    RULE_expr = 1
    RULE_function = 2
    RULE_main_function = 3
    RULE_custom_function = 4
    RULE_built_function = 5
    RULE_variable = 6
    RULE_var_decl = 7
    RULE_var_assign = 8
    RULE_print = 9

    ruleNames =  [ "prog", "expr", "function", "main_function", "custom_function", 
                   "built_function", "variable", "var_decl", "var_assign", 
                   "print" ]

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


        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.VariableContext)
            else:
                return self.getTypedRuleContext(PythonParser.VariableContext,i)


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
                    self.variable()
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PythonParser.ID, 0)

        def NUMBER(self):
            return self.getToken(PythonParser.NUMBER, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = PythonParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def main_function(self):
            return self.getTypedRuleContext(PythonParser.Main_functionContext,0)


        def built_function(self):
            return self.getTypedRuleContext(PythonParser.Built_functionContext,0)


        def custom_function(self):
            return self.getTypedRuleContext(PythonParser.Custom_functionContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = PythonParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.main_function()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.built_function()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
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
            self.state = 35
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
            self.state = 37
            self.match(PythonParser.FUNCTION)
            self.state = 38
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

        def print_(self):
            return self.getTypedRuleContext(PythonParser.PrintContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_built_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuilt_function" ):
                listener.enterBuilt_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuilt_function" ):
                listener.exitBuilt_function(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBuilt_function" ):
                return visitor.visitBuilt_function(self)
            else:
                return visitor.visitChildren(self)




    def built_function(self):

        localctx = PythonParser.Built_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_built_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.print_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(PythonParser.Var_declContext,0)


        def var_assign(self):
            return self.getTypedRuleContext(PythonParser.Var_assignContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_variable

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




    def variable(self):

        localctx = PythonParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variable)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.var_decl()
                pass
            elif token in [28, 29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
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
            self.state = 46
            self.match(PythonParser.VARIABLE_DECLARATIONS)
            self.state = 47
            self.expr()
            self.state = 48
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
            self.state = 50
            self.expr()
            self.state = 51
            self.match(PythonParser.ASSIGN)
            self.state = 52
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


        def VARIABLE_TYPE(self):
            return self.getToken(PythonParser.VARIABLE_TYPE, 0)

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
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(PythonParser.PRINT)
                self.state = 55
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.match(PythonParser.PRINT)
                self.state = 57
                self.match(PythonParser.VARIABLE_TYPE)
                self.state = 58
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





