# Generated from gramatica.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete generic visitor for a parse tree produced by gramaticaParser.

class gramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramaticaParser#program.
    def visitProgram(self, ctx:gramaticaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#AssignStmt.
    def visitAssignStmt(self, ctx:gramaticaParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#FuncDeclStmt.
    def visitFuncDeclStmt(self, ctx:gramaticaParser.FuncDeclStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#PrintStatement.
    def visitPrintStatement(self, ctx:gramaticaParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#ReturnStatement.
    def visitReturnStatement(self, ctx:gramaticaParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#functionDecl.
    def visitFunctionDecl(self, ctx:gramaticaParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#paramList.
    def visitParamList(self, ctx:gramaticaParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#assignment.
    def visitAssignment(self, ctx:gramaticaParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#printStmt.
    def visitPrintStmt(self, ctx:gramaticaParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#returnStmt.
    def visitReturnStmt(self, ctx:gramaticaParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#AddSub.
    def visitAddSub(self, ctx:gramaticaParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#ExprTerm.
    def visitExprTerm(self, ctx:gramaticaParser.ExprTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#TermFactor.
    def visitTermFactor(self, ctx:gramaticaParser.TermFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#MulDiv.
    def visitMulDiv(self, ctx:gramaticaParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#NumberLit.
    def visitNumberLit(self, ctx:gramaticaParser.NumberLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#FloatLit.
    def visitFloatLit(self, ctx:gramaticaParser.FloatLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Identifier.
    def visitIdentifier(self, ctx:gramaticaParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Parenthesized.
    def visitParenthesized(self, ctx:gramaticaParser.ParenthesizedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#FuncCallExpr.
    def visitFuncCallExpr(self, ctx:gramaticaParser.FuncCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#UnaryMinus.
    def visitUnaryMinus(self, ctx:gramaticaParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#funcCall.
    def visitFuncCall(self, ctx:gramaticaParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#argList.
    def visitArgList(self, ctx:gramaticaParser.ArgListContext):
        return self.visitChildren(ctx)



del gramaticaParser