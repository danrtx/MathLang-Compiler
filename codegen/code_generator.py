class TACInstruction:
    def __init__(self, op, result=None, arg1=None, arg2=None):
        self.op = op; self.result = result; self.arg1 = arg1; self.arg2 = arg2
    def __repr__(self):
        if self.op == 'binop':      return f"  {self.result} = {self.arg1} {self.arg2[0]} {self.arg2[1]}"
        if self.op == 'assign':     return f"  {self.result} = {self.arg1}"
        if self.op == 'call':       return f"  {self.result} = CALL {self.arg1}({self.arg2})"
        if self.op == 'param':      return f"  PARAM {self.arg1}"
        if self.op == 'print':      return f"  PRINT {self.arg1}"
        if self.op == 'return':     return f"  RETURN {self.arg1}"
        if self.op == 'func_begin': return f"FUNC_BEGIN {self.arg1}({self.arg2})"
        if self.op == 'func_end':   return f"FUNC_END {self.arg1}"
        if self.op == 'unary':      return f"  {self.result} = -{self.arg1}"
        return f"  {self.op} {self.result} {self.arg1} {self.arg2}"

class TACGenerator:
    def __init__(self):
        self.instructions = []
        self.temp_count   = 0
    def new_temp(self):
        name = f"_t{self.temp_count}"; self.temp_count += 1; return name
    def emit(self, instr):
        self.instructions.append(instr); return instr
    def generate(self, ast_nodes):
        for node in ast_nodes: self.gen_statement(node)
        return self.instructions
    def gen_statement(self, node):
        kind = node.get('type')
        if kind == 'assignment':     self.gen_assignment(node)
        elif kind == 'functionDecl': self.gen_function_decl(node)
        elif kind == 'printStmt':    self.emit(TACInstruction('print',  arg1=self.gen_expr(node['expr'])))
        elif kind == 'returnStmt':   self.emit(TACInstruction('return', arg1=self.gen_expr(node['expr'])))
    def gen_assignment(self, node):
        val = self.gen_expr(node['expr'])
        self.emit(TACInstruction('assign', result=node['name'], arg1=val))
    def gen_function_decl(self, node):
        params_str = ', '.join(node.get('params', []))
        self.emit(TACInstruction('func_begin', arg1=node['name'], arg2=params_str))
        for stmt in node.get('body', []): self.gen_statement(stmt)
        self.emit(TACInstruction('func_end', arg1=node['name']))
    def gen_expr(self, node):
        kind = node.get('type')
        if kind in ('number', 'float'): return str(node['value'])
        if kind == 'identifier':        return node['name']
        if kind == 'unary':
            operand = self.gen_expr(node['operand'])
            temp = self.new_temp()
            self.emit(TACInstruction('unary', result=temp, arg1=operand)); return temp
        if kind == 'binop':
            left  = self.gen_expr(node['left'])
            right = self.gen_expr(node['right'])
            temp  = self.new_temp()
            self.emit(TACInstruction('binop', result=temp, arg1=left, arg2=(node['op'], right))); return temp
        if kind == 'funcCall':
            args = [self.gen_expr(a) for a in node.get('args', [])]
            for arg in args: self.emit(TACInstruction('param', arg1=arg))
            temp = self.new_temp()
            self.emit(TACInstruction('call', result=temp, arg1=node['name'], arg2=', '.join(args))); return temp
        return '?'

class PythonCodeGenerator:
    def __init__(self):
        self.lines        = []
        self.indent_level = 0
    def indent(self): return '    ' * self.indent_level
    def emit(self, line): self.lines.append(self.indent() + line)
    def generate(self, ast_nodes):
        self.lines = []
        self.lines.append("# Codigo Python generado por MathLang Compiler")
        self.lines.append("# Universidad Cooperativa de Colombia - Compiladores")
        self.lines.append("import math")
        self.lines.append("")
        for node in ast_nodes: self.gen_statement(node)
        return '\n'.join(self.lines)
    def gen_statement(self, node):
        kind = node.get('type')
        if kind == 'assignment':
            self.emit(f"{node['name']} = {self.gen_expr(node['expr'])}")
        elif kind == 'functionDecl':
            params = ', '.join(node.get('params', []))
            self.emit(f"def {node['name']}({params}):")
            self.indent_level += 1
            for stmt in node.get('body', []): self.gen_statement(stmt)
            self.indent_level -= 1
            self.emit("")
        elif kind == 'printStmt':
            self.emit(f"print({self.gen_expr(node['expr'])})")
        elif kind == 'returnStmt':
            self.emit(f"return {self.gen_expr(node['expr'])}")
    def gen_expr(self, node):
        kind = node.get('type')
        if kind in ('number', 'float'): return str(node['value'])
        if kind == 'identifier':        return node['name']
        if kind == 'unary':             return f"-{self.gen_expr(node['operand'])}"
        if kind == 'binop':
            return f"({self.gen_expr(node['left'])} {node['op']} {self.gen_expr(node['right'])})"
        if kind == 'funcCall':
            args = ', '.join(self.gen_expr(a) for a in node.get('args', []))
            return f"{node['name']}({args})"
        return '?'
