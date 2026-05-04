import re

TOKEN_PATTERNS = [
    ('BLOCK_COMMENT', r'/\*.*?\*/'),
    ('LINE_COMMENT',  r'//[^\n]*'),
    ('FLOAT',         r'\d+\.\d+'),
    ('NUMBER',        r'\d+'),
    ('FUNC',          r'\bfunc\b'),
    ('PRINT',         r'\bprint\b'),
    ('RETURN',        r'\breturn\b'),
    ('ID',            r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('LBRACE',        r'\{'),
    ('RBRACE',        r'\}'),
    ('LPAREN',        r'\('),
    ('RPAREN',        r'\)'),
    ('COMMA',         r','),
    ('SEMICOLON',     r';'),
    ('PLUS',          r'\+'),
    ('MINUS',         r'-'),
    ('STAR',          r'\*'),
    ('SLASH',         r'/'),
    ('ASSIGN',        r'='),
    ('WS',            r'[ \t\r\n]+'),
]

MASTER_PATTERN = re.compile(
    '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_PATTERNS),
    re.DOTALL
)

class Token:
    def __init__(self, ttype, value, line):
        self.type  = ttype
        self.value = value
        self.line  = line
    def __repr__(self):
        return f"Token({self.type}, {self.value!r}, line={self.line})"

class LexerError(Exception):
    def __init__(self, message, line=None):
        self.line = line
        super().__init__(f"[ERROR LEXICO] {'Linea '+str(line)+': ' if line else ''}{message}")

class ParseError(Exception):
    def __init__(self, message, line=None):
        self.line = line
        super().__init__(f"[ERROR SINTACTICO] {'Linea '+str(line)+': ' if line else ''}{message}")

def tokenize(source: str):
    tokens = []
    line   = 1
    pos    = 0
    while pos < len(source):
        mo = MASTER_PATTERN.match(source, pos)
        if mo is None:
            raise LexerError(f"Caracter no reconocido: '{source[pos]}'", line)
        kind  = mo.lastgroup
        value = mo.group()
        line += value.count('\n')
        pos   = mo.end()
        if kind in ('WS', 'LINE_COMMENT', 'BLOCK_COMMENT'):
            continue
        tokens.append(Token(kind, value, line))
    tokens.append(Token('ENDOFTOKEN', '', line))
    return tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos    = 0

    def current(self): return self.tokens[self.pos]
    def advance(self):
        tok = self.tokens[self.pos]
        if tok.type != 'ENDOFTOKEN': self.pos += 1
        return tok
    def expect(self, ttype):
        tok = self.current()
        if tok.type != ttype:
            raise ParseError(f"Se esperaba '{ttype}' pero se encontro '{tok.type}' ('{tok.value}')", tok.line)
        return self.advance()
    def match(self, *ttypes): return self.current().type in ttypes

    def parse_program(self):
        stmts = []
        while not self.match('ENDOFTOKEN'):
            stmts.append(self.parse_statement())
        return stmts

    def parse_statement(self):
        tok = self.current()
        if tok.type == 'FUNC':   return self.parse_function_decl()
        if tok.type == 'PRINT':  return self.parse_print_stmt()
        if tok.type == 'RETURN': return self.parse_return_stmt()
        if tok.type == 'ID':
            if self.pos+1 < len(self.tokens) and self.tokens[self.pos+1].type == 'ASSIGN':
                return self.parse_assignment()
            raise ParseError(f"Sentencia invalida con '{tok.value}'. Falta '='?", tok.line)
        raise ParseError(f"Sentencia no reconocida: '{tok.value}' ({tok.type})", tok.line)

    def parse_assignment(self):
        name_tok = self.expect('ID')
        self.expect('ASSIGN')
        expr = self.parse_expr()
        self.expect('SEMICOLON')
        return {'type':'assignment','name':name_tok.value,'expr':expr,'line':name_tok.line}

    def parse_function_decl(self):
        func_tok = self.expect('FUNC')
        name_tok = self.expect('ID')
        self.expect('LPAREN')
        params = self.parse_param_list()
        self.expect('RPAREN')
        self.expect('LBRACE')
        body = []
        while not self.match('RBRACE','ENDOFTOKEN'):
            body.append(self.parse_statement())
        self.expect('RBRACE')
        return {'type':'functionDecl','name':name_tok.value,'params':params,'body':body,'line':func_tok.line}

    def parse_param_list(self):
        params = []
        if self.match('ID'):
            params.append(self.advance().value)
            while self.match('COMMA'):
                self.advance()
                params.append(self.expect('ID').value)
        return params

    def parse_print_stmt(self):
        tok = self.expect('PRINT')
        self.expect('LPAREN')
        expr = self.parse_expr()
        self.expect('RPAREN')
        self.expect('SEMICOLON')
        return {'type':'printStmt','expr':expr,'line':tok.line}

    def parse_return_stmt(self):
        tok = self.expect('RETURN')
        expr = self.parse_expr()
        self.expect('SEMICOLON')
        return {'type':'returnStmt','expr':expr,'line':tok.line}

    def parse_expr(self):
        left = self.parse_term()
        while self.match('PLUS','MINUS'):
            op_tok = self.advance()
            right  = self.parse_term()
            left   = {'type':'binop','op':op_tok.value,'left':left,'right':right,'line':op_tok.line}
        return left

    def parse_term(self):
        left = self.parse_factor()
        while self.match('STAR','SLASH'):
            op_tok = self.advance()
            right  = self.parse_factor()
            left   = {'type':'binop','op':op_tok.value,'left':left,'right':right,'line':op_tok.line}
        return left

    def parse_factor(self):
        tok = self.current()
        if tok.type == 'NUMBER':
            self.advance()
            return {'type':'number','value':int(tok.value),'line':tok.line}
        if tok.type == 'FLOAT':
            self.advance()
            return {'type':'float','value':float(tok.value),'line':tok.line}
        if tok.type == 'ID':
            self.advance()
            if self.match('LPAREN'):
                self.advance()
                args = self.parse_arg_list()
                self.expect('RPAREN')
                return {'type':'funcCall','name':tok.value,'args':args,'line':tok.line}
            return {'type':'identifier','name':tok.value,'line':tok.line}
        if tok.type == 'LPAREN':
            self.advance()
            expr = self.parse_expr()
            self.expect('RPAREN')
            return expr
        if tok.type == 'MINUS':
            self.advance()
            operand = self.parse_factor()
            return {'type':'unary','operand':operand,'line':tok.line}
        raise ParseError(f"Factor invalido: '{tok.value}' ({tok.type})", tok.line)

    def parse_arg_list(self):
        args = []
        if not self.match('RPAREN'):
            args.append(self.parse_expr())
            while self.match('COMMA'):
                self.advance()
                args.append(self.parse_expr())
        return args
