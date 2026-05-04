// ============================================================
// MathLang - Mini Lenguaje de Fórmulas Matemáticas Científicas
// Universidad Cooperativa de Colombia - Compiladores
// Gramática ANTLR4 (Léxica + Sintáctica)
// ============================================================

grammar gramatica;

// ============================================================
// REGLAS SINTÁCTICAS (Parser) - inician en minúscula
// ============================================================

program
    : statement+ EOF
    ;

statement
    : assignment          # AssignStmt
    | functionDecl        # FuncDeclStmt
    | printStmt           # PrintStatement
    | returnStmt          # ReturnStatement
    ;

functionDecl
    : 'func' ID '(' paramList? ')' '{' statement+ '}'
    ;

paramList
    : ID (',' ID)*
    ;

assignment
    : ID '=' expr ';'
    ;

printStmt
    : 'print' '(' expr ')' ';'
    ;

returnStmt
    : 'return' expr ';'
    ;

expr
    : expr ('+' | '-') term    # AddSub
    | term                     # ExprTerm
    ;

term
    : term ('*' | '/') factor  # MulDiv
    | factor                   # TermFactor
    ;

factor
    : NUMBER                   # NumberLit
    | FLOAT                    # FloatLit
    | ID                       # Identifier
    | '(' expr ')'             # Parenthesized
    | funcCall                 # FuncCallExpr
    | '-' factor               # UnaryMinus
    ;

funcCall
    : ID '(' argList? ')'
    ;

argList
    : expr (',' expr)*
    ;

// ============================================================
// REGLAS LÉXICAS (Lexer) - inician en MAYÚSCULA
// ============================================================

FUNC   : 'func' ;
PRINT  : 'print' ;
RETURN : 'return' ;

ID     : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER : [0-9]+ ;
FLOAT  : [0-9]+ '.' [0-9]+ ;

WS            : [ \t\r\n]+  -> skip ;
LINE_COMMENT  : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;
