class SemanticError(Exception):
    def __init__(self, message, line=None):
        self.line = line
        self.message = message
        super().__init__(f"[ERROR SEMANTICO] {'Linea '+str(line)+': ' if line else ''}{message}")

class Symbol:
    def __init__(self, name, sym_type, value=None, params=None, line=None):
        self.name     = name
        self.sym_type = sym_type
        self.value    = value
        self.params   = params or []
        self.line     = line
    def __repr__(self):
        if self.sym_type == 'function':
            return f"Symbol(func {self.name}, params={self.params})"
        return f"Symbol(var {self.name}={self.value})"

class SymbolTable:
    def __init__(self):
        self.scopes = [{}]
    def enter_scope(self):  self.scopes.append({})
    def exit_scope(self):
        if len(self.scopes) > 1: self.scopes.pop()
    def define(self, symbol):
        self.scopes[-1][symbol.name] = symbol
    def lookup(self, name):
        for scope in reversed(self.scopes):
            if name in scope: return scope[name]
        return None
    def dump(self):
        result = []
        for i, scope in enumerate(self.scopes):
            level = "GLOBAL" if i == 0 else f"LOCAL[{i}]"
            result.append(f"  Ambito {level}:")
            for name, sym in scope.items():
                result.append(f"    {name}: {sym}")
        return "\n".join(result)

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table     = SymbolTable()
        self.errors           = []
        self.current_function = None

    def error(self, message, line=None):
        err = SemanticError(message, line)
        self.errors.append(str(err))
        return err

    def analyze(self, ast_nodes):
        for node in ast_nodes:
            self.analyze_statement(node)
        return len(self.errors) == 0

    def analyze_statement(self, node):
        kind = node.get('type')
        if   kind == 'assignment':   self._check_assignment(node)
        elif kind == 'functionDecl': self._check_function_decl(node)
        elif kind == 'printStmt':    self._check_print(node)
        elif kind == 'returnStmt':   self._check_return(node)
        else: self.error(f"Tipo de sentencia desconocido: '{kind}'")

    def _check_assignment(self, node):
        val = self._check_expr(node['expr'])
        self.symbol_table.define(Symbol(node['name'], 'variable', value=val, line=node.get('line')))

    def _check_function_decl(self, node):
        name   = node['name']
        params = node.get('params', [])
        self.symbol_table.define(Symbol(name, 'function', params=params, line=node.get('line')))
        prev = self.current_function
        self.current_function = name
        self.symbol_table.enter_scope()
        for param in params:
            self.symbol_table.define(Symbol(param, 'variable', line=node.get('line')))
        for stmt in node.get('body', []):
            self.analyze_statement(stmt)
        self.symbol_table.exit_scope()
        self.current_function = prev

    def _check_print(self, node):   self._check_expr(node['expr'])

    def _check_return(self, node):
        if self.current_function is None:
            self.error("'return' fuera de una funcion", node.get('line'))
        self._check_expr(node['expr'])

    def _check_expr(self, node):
        if node is None: return None
        kind = node.get('type')
        if kind in ('number', 'float'): return node['value']
        if kind == 'identifier':
            sym = self.symbol_table.lookup(node['name'])
            if sym is None:
                self.error(f"Variable '{node['name']}' no declarada antes de su uso", node.get('line'))
                return None
            return sym.value
        if kind == 'binop':
            left  = self._check_expr(node['left'])
            right = self._check_expr(node['right'])
            if node['op'] == '/' and right == 0:
                self.error("Division por cero detectada", node.get('line'))
                return None
            return None
        if kind == 'unary':    return self._check_expr(node['operand'])
        if kind == 'funcCall': return self._check_func_call(node)
        self.error(f"Tipo de expresion desconocido: '{kind}'")
        return None

    def _check_func_call(self, node):
        name = node['name']
        args = node.get('args', [])
        sym  = self.symbol_table.lookup(name)
        if sym is None or sym.sym_type != 'function':
            self.error(f"Funcion '{name}' no declarada", node.get('line'))
            return None
        expected = len(sym.params)
        got      = len(args)
        if expected != got:
            self.error(f"Funcion '{name}' espera {expected} argumento(s), pero recibio {got}", node.get('line'))
        for arg in args: self._check_expr(arg)
        return None
