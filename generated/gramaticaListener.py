# Generated from gramatica.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete listener for a parse tree produced by gramaticaParser.
class gramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by gramaticaParser#program.
    def enterProgram(self, ctx:gramaticaParser.ProgramContext):
        pass

    # Exit a parse tree produced by gramaticaParser#program.
    def exitProgram(self, ctx:gramaticaParser.ProgramContext):
        pass


    # Enter a parse tree produced by gramaticaParser#AssignStmt.
    def enterAssignStmt(self, ctx:gramaticaParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by gramaticaParser#AssignStmt.
    def exitAssignStmt(self, ctx:gramaticaParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by gramaticaParser#FuncDeclStmt.
    def enterFuncDeclStmt(self, ctx:gramaticaParser.FuncDeclStmtContext):
        pass

    # Exit a parse tree produced by gramaticaParser#FuncDeclStmt.
    def exitFuncDeclStmt(self, ctx:gramaticaParser.FuncDeclStmtContext):
        pass


    # Enter a parse tree produced by gramaticaParser#PrintStatement.
    def enterPrintStatement(self, ctx:gramaticaParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by gramaticaParser#PrintStatement.
    def exitPrintStatement(self, ctx:gramaticaParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by gramaticaParser#ReturnStatement.
    def enterReturnStatement(self, ctx:gramaticaParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by gramaticaParser#ReturnStatement.
    def exitReturnStatement(self, ctx:gramaticaParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by gramaticaParser#functionDecl.
    def enterFunctionDecl(self, ctx:gramaticaParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by gramaticaParser#functionDecl.
    def exitFunctionDecl(self, ctx:gramaticaParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by gramaticaParser#paramList.
    def enterParamList(self, ctx:gramaticaParser.ParamListContext):
        pass

    # Exit a parse tree produced by gramaticaParser#paramList.
    def exitParamList(self, ctx:gramaticaParser.ParamListContext):
        pass


    # Enter a parse tree produced by gramaticaParser#assignment.
    def enterAssignment(self, ctx:gramaticaParser.AssignmentContext):
        pass

    # Exit a parse tree produced by gramaticaParser#assignment.
    def exitAssignment(self, ctx:gramaticaParser.AssignmentContext):
        pass


    # Enter a parse tree produced by gramaticaParser#printStmt.
    def enterPrintStmt(self, ctx:gramaticaParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by gramaticaParser#printStmt.
    def exitPrintStmt(self, ctx:gramaticaParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by gramaticaParser#returnStmt.
    def enterReturnStmt(self, ctx:gramaticaParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by gramaticaParser#returnStmt.
    def exitReturnStmt(self, ctx:gramaticaParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by gramaticaParser#AddSub.
    def enterAddSub(self, ctx:gramaticaParser.AddSubContext):
        pass

    # Exit a parse tree produced by gramaticaParser#AddSub.
    def exitAddSub(self, ctx:gramaticaParser.AddSubContext):
        pass


    # Enter a parse tree produced by gramaticaParser#ExprTerm.
    def enterExprTerm(self, ctx:gramaticaParser.ExprTermContext):
        pass

    # Exit a parse tree produced by gramaticaParser#ExprTerm.
    def exitExprTerm(self, ctx:gramaticaParser.ExprTermContext):
        pass


    # Enter a parse tree produced by gramaticaParser#TermFactor.
    def enterTermFactor(self, ctx:gramaticaParser.TermFactorContext):
        pass

    # Exit a parse tree produced by gramaticaParser#TermFactor.
    def exitTermFactor(self, ctx:gramaticaParser.TermFactorContext):
        pass


    # Enter a parse tree produced by gramaticaParser#MulDiv.
    def enterMulDiv(self, ctx:gramaticaParser.MulDivContext):
        pass

    # Exit a parse tree produced by gramaticaParser#MulDiv.
    def exitMulDiv(self, ctx:gramaticaParser.MulDivContext):
        pass


    # Enter a parse tree produced by gramaticaParser#NumberLit.
    def enterNumberLit(self, ctx:gramaticaParser.NumberLitContext):
        pass

    # Exit a parse tree produced by gramaticaParser#NumberLit.
    def exitNumberLit(self, ctx:gramaticaParser.NumberLitContext):
        pass


    # Enter a parse tree produced by gramaticaParser#FloatLit.
    def enterFloatLit(self, ctx:gramaticaParser.FloatLitContext):
        pass

    # Exit a parse tree produced by gramaticaParser#FloatLit.
    def exitFloatLit(self, ctx:gramaticaParser.FloatLitContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Identifier.
    def enterIdentifier(self, ctx:gramaticaParser.IdentifierContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Identifier.
    def exitIdentifier(self, ctx:gramaticaParser.IdentifierContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Parenthesized.
    def enterParenthesized(self, ctx:gramaticaParser.ParenthesizedContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Parenthesized.
    def exitParenthesized(self, ctx:gramaticaParser.ParenthesizedContext):
        pass


    # Enter a parse tree produced by gramaticaParser#FuncCallExpr.
    def enterFuncCallExpr(self, ctx:gramaticaParser.FuncCallExprContext):
        pass

    # Exit a parse tree produced by gramaticaParser#FuncCallExpr.
    def exitFuncCallExpr(self, ctx:gramaticaParser.FuncCallExprContext):
        pass


    # Enter a parse tree produced by gramaticaParser#UnaryMinus.
    def enterUnaryMinus(self, ctx:gramaticaParser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by gramaticaParser#UnaryMinus.
    def exitUnaryMinus(self, ctx:gramaticaParser.UnaryMinusContext):
        pass


    # Enter a parse tree produced by gramaticaParser#funcCall.
    def enterFuncCall(self, ctx:gramaticaParser.FuncCallContext):
        pass

    # Exit a parse tree produced by gramaticaParser#funcCall.
    def exitFuncCall(self, ctx:gramaticaParser.FuncCallContext):
        pass


    # Enter a parse tree produced by gramaticaParser#argList.
    def enterArgList(self, ctx:gramaticaParser.ArgListContext):
        pass

    # Exit a parse tree produced by gramaticaParser#argList.
    def exitArgList(self, ctx:gramaticaParser.ArgListContext):
        pass



del gramaticaParser