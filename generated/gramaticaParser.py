# Generated from gramatica.g4 by ANTLR 4.13.1
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
        4,1,20,125,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,26,8,0,11,
        0,12,0,27,1,0,1,0,1,1,1,1,1,1,1,1,3,1,36,8,1,1,2,1,2,1,2,1,2,3,2,
        42,8,2,1,2,1,2,1,2,4,2,47,8,2,11,2,12,2,48,1,2,1,2,1,3,1,3,1,3,5,
        3,56,8,3,10,3,12,3,59,9,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,
        5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,5,7,82,8,7,10,7,12,
        7,85,9,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,93,8,8,10,8,12,8,96,9,8,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,108,8,9,1,10,1,10,1,10,3,
        10,113,8,10,1,10,1,10,1,11,1,11,1,11,5,11,120,8,11,10,11,12,11,123,
        9,11,1,11,0,2,14,16,12,0,2,4,6,8,10,12,14,16,18,20,22,0,2,1,0,8,
        9,1,0,10,11,128,0,25,1,0,0,0,2,35,1,0,0,0,4,37,1,0,0,0,6,52,1,0,
        0,0,8,60,1,0,0,0,10,65,1,0,0,0,12,71,1,0,0,0,14,75,1,0,0,0,16,86,
        1,0,0,0,18,107,1,0,0,0,20,109,1,0,0,0,22,116,1,0,0,0,24,26,3,2,1,
        0,25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,29,
        1,0,0,0,29,30,5,0,0,1,30,1,1,0,0,0,31,36,3,8,4,0,32,36,3,4,2,0,33,
        36,3,10,5,0,34,36,3,12,6,0,35,31,1,0,0,0,35,32,1,0,0,0,35,33,1,0,
        0,0,35,34,1,0,0,0,36,3,1,0,0,0,37,38,5,12,0,0,38,39,5,15,0,0,39,
        41,5,1,0,0,40,42,3,6,3,0,41,40,1,0,0,0,41,42,1,0,0,0,42,43,1,0,0,
        0,43,44,5,2,0,0,44,46,5,3,0,0,45,47,3,2,1,0,46,45,1,0,0,0,47,48,
        1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,50,1,0,0,0,50,51,5,4,0,0,
        51,5,1,0,0,0,52,57,5,15,0,0,53,54,5,5,0,0,54,56,5,15,0,0,55,53,1,
        0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,7,1,0,0,0,59,
        57,1,0,0,0,60,61,5,15,0,0,61,62,5,6,0,0,62,63,3,14,7,0,63,64,5,7,
        0,0,64,9,1,0,0,0,65,66,5,13,0,0,66,67,5,1,0,0,67,68,3,14,7,0,68,
        69,5,2,0,0,69,70,5,7,0,0,70,11,1,0,0,0,71,72,5,14,0,0,72,73,3,14,
        7,0,73,74,5,7,0,0,74,13,1,0,0,0,75,76,6,7,-1,0,76,77,3,16,8,0,77,
        83,1,0,0,0,78,79,10,2,0,0,79,80,7,0,0,0,80,82,3,16,8,0,81,78,1,0,
        0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,15,1,0,0,0,85,83,
        1,0,0,0,86,87,6,8,-1,0,87,88,3,18,9,0,88,94,1,0,0,0,89,90,10,2,0,
        0,90,91,7,1,0,0,91,93,3,18,9,0,92,89,1,0,0,0,93,96,1,0,0,0,94,92,
        1,0,0,0,94,95,1,0,0,0,95,17,1,0,0,0,96,94,1,0,0,0,97,108,5,16,0,
        0,98,108,5,17,0,0,99,108,5,15,0,0,100,101,5,1,0,0,101,102,3,14,7,
        0,102,103,5,2,0,0,103,108,1,0,0,0,104,108,3,20,10,0,105,106,5,9,
        0,0,106,108,3,18,9,0,107,97,1,0,0,0,107,98,1,0,0,0,107,99,1,0,0,
        0,107,100,1,0,0,0,107,104,1,0,0,0,107,105,1,0,0,0,108,19,1,0,0,0,
        109,110,5,15,0,0,110,112,5,1,0,0,111,113,3,22,11,0,112,111,1,0,0,
        0,112,113,1,0,0,0,113,114,1,0,0,0,114,115,5,2,0,0,115,21,1,0,0,0,
        116,121,3,14,7,0,117,118,5,5,0,0,118,120,3,14,7,0,119,117,1,0,0,
        0,120,123,1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,23,1,0,0,0,
        123,121,1,0,0,0,10,27,35,41,48,57,83,94,107,112,121
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "','", "'='", 
                     "';'", "'+'", "'-'", "'*'", "'/'", "'func'", "'print'", 
                     "'return'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "FUNC", "PRINT", "RETURN", "ID", "NUMBER", "FLOAT", 
                      "WS", "LINE_COMMENT", "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_functionDecl = 2
    RULE_paramList = 3
    RULE_assignment = 4
    RULE_printStmt = 5
    RULE_returnStmt = 6
    RULE_expr = 7
    RULE_term = 8
    RULE_factor = 9
    RULE_funcCall = 10
    RULE_argList = 11

    ruleNames =  [ "program", "statement", "functionDecl", "paramList", 
                   "assignment", "printStmt", "returnStmt", "expr", "term", 
                   "factor", "funcCall", "argList" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    FUNC=12
    PRINT=13
    RETURN=14
    ID=15
    NUMBER=16
    FLOAT=17
    WS=18
    LINE_COMMENT=19
    BLOCK_COMMENT=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(gramaticaParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.StatementContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = gramaticaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.statement()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0)):
                    break

            self.state = 29
            self.match(gramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignment(self):
            return self.getTypedRuleContext(gramaticaParser.AssignmentContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)


    class PrintStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def printStmt(self):
            return self.getTypedRuleContext(gramaticaParser.PrintStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)


    class ReturnStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def returnStmt(self):
            return self.getTypedRuleContext(gramaticaParser.ReturnStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)


    class FuncDeclStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionDecl(self):
            return self.getTypedRuleContext(gramaticaParser.FunctionDeclContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDeclStmt" ):
                listener.enterFuncDeclStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDeclStmt" ):
                listener.exitFuncDeclStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDeclStmt" ):
                return visitor.visitFuncDeclStmt(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = gramaticaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                localctx = gramaticaParser.AssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.assignment()
                pass
            elif token in [12]:
                localctx = gramaticaParser.FuncDeclStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.functionDecl()
                pass
            elif token in [13]:
                localctx = gramaticaParser.PrintStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.printStmt()
                pass
            elif token in [14]:
                localctx = gramaticaParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 34
                self.returnStmt()
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


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(gramaticaParser.FUNC, 0)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def paramList(self):
            return self.getTypedRuleContext(gramaticaParser.ParamListContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.StatementContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_functionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = gramaticaParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(gramaticaParser.FUNC)
            self.state = 38
            self.match(gramaticaParser.ID)
            self.state = 39
            self.match(gramaticaParser.T__0)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 40
                self.paramList()


            self.state = 43
            self.match(gramaticaParser.T__1)
            self.state = 44
            self.match(gramaticaParser.T__2)
            self.state = 46 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 45
                self.statement()
                self.state = 48 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0)):
                    break

            self.state = 50
            self.match(gramaticaParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.ID)
            else:
                return self.getToken(gramaticaParser.ID, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = gramaticaParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(gramaticaParser.ID)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 53
                self.match(gramaticaParser.T__4)
                self.state = 54
                self.match(gramaticaParser.ID)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(gramaticaParser.ExprContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = gramaticaParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(gramaticaParser.ID)
            self.state = 61
            self.match(gramaticaParser.T__5)
            self.state = 62
            self.expr(0)
            self.state = 63
            self.match(gramaticaParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(gramaticaParser.PRINT, 0)

        def expr(self):
            return self.getTypedRuleContext(gramaticaParser.ExprContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = gramaticaParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(gramaticaParser.PRINT)
            self.state = 66
            self.match(gramaticaParser.T__0)
            self.state = 67
            self.expr(0)
            self.state = 68
            self.match(gramaticaParser.T__1)
            self.state = 69
            self.match(gramaticaParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(gramaticaParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(gramaticaParser.ExprContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = gramaticaParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(gramaticaParser.RETURN)
            self.state = 72
            self.expr(0)
            self.state = 73
            self.match(gramaticaParser.T__6)
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
            return gramaticaParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(gramaticaParser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(gramaticaParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ExprTermContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(gramaticaParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprTerm" ):
                listener.enterExprTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprTerm" ):
                listener.exitExprTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprTerm" ):
                return visitor.visitExprTerm(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = gramaticaParser.ExprTermContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 76
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 83
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramaticaParser.AddSubContext(self, gramaticaParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 78
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 79
                    _la = self._input.LA(1)
                    if not(_la==8 or _la==9):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 80
                    self.term(0) 
                self.state = 85
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class TermFactorContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(gramaticaParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermFactor" ):
                listener.enterTermFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermFactor" ):
                listener.exitTermFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermFactor" ):
                return visitor.visitTermFactor(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(gramaticaParser.TermContext,0)

        def factor(self):
            return self.getTypedRuleContext(gramaticaParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_term, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = gramaticaParser.TermFactorContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 87
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 94
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramaticaParser.MulDivContext(self, gramaticaParser.TermContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 89
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 90
                    _la = self._input.LA(1)
                    if not(_la==10 or _la==11):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 91
                    self.factor() 
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FloatLitContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(gramaticaParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatLit" ):
                listener.enterFloatLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatLit" ):
                listener.exitFloatLit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatLit" ):
                return visitor.visitFloatLit(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesizedContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(gramaticaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesized" ):
                listener.enterParenthesized(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesized" ):
                listener.exitParenthesized(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesized" ):
                return visitor.visitParenthesized(self)
            else:
                return visitor.visitChildren(self)


    class NumberLitContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(gramaticaParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberLit" ):
                listener.enterNumberLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberLit" ):
                listener.exitNumberLit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberLit" ):
                return visitor.visitNumberLit(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(gramaticaParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinus" ):
                listener.enterUnaryMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinus" ):
                listener.exitUnaryMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinus" ):
                return visitor.visitUnaryMinus(self)
            else:
                return visitor.visitChildren(self)


    class FuncCallExprContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def funcCall(self):
            return self.getTypedRuleContext(gramaticaParser.FuncCallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCallExpr" ):
                listener.enterFuncCallExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCallExpr" ):
                listener.exitFuncCallExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCallExpr" ):
                return visitor.visitFuncCallExpr(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = gramaticaParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_factor)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = gramaticaParser.NumberLitContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.match(gramaticaParser.NUMBER)
                pass

            elif la_ == 2:
                localctx = gramaticaParser.FloatLitContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.match(gramaticaParser.FLOAT)
                pass

            elif la_ == 3:
                localctx = gramaticaParser.IdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 99
                self.match(gramaticaParser.ID)
                pass

            elif la_ == 4:
                localctx = gramaticaParser.ParenthesizedContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 100
                self.match(gramaticaParser.T__0)
                self.state = 101
                self.expr(0)
                self.state = 102
                self.match(gramaticaParser.T__1)
                pass

            elif la_ == 5:
                localctx = gramaticaParser.FuncCallExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 104
                self.funcCall()
                pass

            elif la_ == 6:
                localctx = gramaticaParser.UnaryMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 105
                self.match(gramaticaParser.T__8)
                self.state = 106
                self.factor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def argList(self):
            return self.getTypedRuleContext(gramaticaParser.ArgListContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_funcCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCall" ):
                listener.enterFuncCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCall" ):
                listener.exitFuncCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCall" ):
                return visitor.visitFuncCall(self)
            else:
                return visitor.visitChildren(self)




    def funcCall(self):

        localctx = gramaticaParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(gramaticaParser.ID)
            self.state = 110
            self.match(gramaticaParser.T__0)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 229890) != 0):
                self.state = 111
                self.argList()


            self.state = 114
            self.match(gramaticaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExprContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_argList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgList" ):
                listener.enterArgList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgList" ):
                listener.exitArgList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = gramaticaParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.expr(0)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 117
                self.match(gramaticaParser.T__4)
                self.state = 118
                self.expr(0)
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expr_sempred
        self._predicates[8] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




