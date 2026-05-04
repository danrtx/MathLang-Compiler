#!/usr/bin/env python3
import sys, os, glob

from generated.lexer_parser       import tokenize, Parser, LexerError, ParseError
from semantic_analyzer.analyzer   import SemanticAnalyzer
from codegen.code_generator       import TACGenerator, PythonCodeGenerator

GREEN  = "\033[92m"; RED    = "\033[91m"
YELLOW = "\033[93m"; CYAN   = "\033[96m"
BOLD   = "\033[1m";  RESET  = "\033[0m"

def banner(text, color=CYAN):
    print(f"\n{color}{BOLD}{'='*60}\n  {text}\n{'='*60}{RESET}")

def ok(m):   print(f"  {GREEN}✔ {m}{RESET}")
def fail(m): print(f"  {RED}✘ {m}{RESET}")
def info(m): print(f"  {YELLOW}→ {m}{RESET}")

def compile_source(source, name="input.txt"):
    result = {'tokens':None,'ast':None,'tac':None,'python_code':None,'errors':[],'success':False}

    banner("FASE 1: ANALISIS LEXICO")
    try:
        tokens = tokenize(source)
        result['tokens'] = tokens
        visible = [t for t in tokens if t.type != 'EOF']
        ok(f"Tokens generados: {len(visible)}")
        for t in visible: info(f"  {t.type:15} -> '{t.value}' (linea {t.line})")
    except LexerError as e:
        fail(str(e)); result['errors'].append(str(e)); return result

    banner("FASE 2: ANALISIS SINTACTICO")
    try:
        parser = Parser(tokens)
        ast    = parser.parse_program()
        result['ast'] = ast
        ok(f"AST construido con {len(ast)} nodo(s) raiz")
        for node in ast: info(f"  Nodo: {node['type']} -> '{node.get('name','')}' (linea {node.get('line','?')})")
    except ParseError as e:
        fail(str(e)); result['errors'].append(str(e)); return result

    banner("FASE 3: ANALISIS SEMANTICO")
    analyzer = SemanticAnalyzer()
    sem_ok   = analyzer.analyze(ast)
    if sem_ok:
        ok("Sin errores semanticos")
        print(f"\n{YELLOW}  Tabla de Simbolos:{RESET}")
        print(analyzer.symbol_table.dump())
    else:
        for e in analyzer.errors: fail(e)
        result['errors'].extend(analyzer.errors); return result

    banner("FASE 4: CODIGO INTERMEDIO (TAC)")
    tac_gen  = TACGenerator()
    tac_list = tac_gen.generate(ast)
    result['tac'] = tac_list
    ok(f"TAC generado: {len(tac_list)} instruccion(es)")
    for instr in tac_list: info(str(instr))

    banner("FASE 5: GENERACION DE CODIGO PYTHON")
    py_gen  = PythonCodeGenerator()
    py_code = py_gen.generate(ast)
    result['python_code'] = py_code
    ok("Codigo Python generado")
    print(f"\n{YELLOW}  Codigo generado:{RESET}")
    for i, line in enumerate(py_code.splitlines(), 1): print(f"    {i:3}: {line}")

    result['success'] = True
    return result

def run_compiler(input_file="input.txt", output_py="output_program.py", output_log="output.txt"):
    if not os.path.exists(input_file):
        print(f"{RED}Error: No se encontro '{input_file}'{RESET}"); sys.exit(1)
    with open(input_file, encoding='utf-8') as f: source = f.read()

    print(f"\n{BOLD}{CYAN}{'='*60}")
    print("  MathLang Compiler v1.0  |  UCC - Compiladores")
    print(f"{'='*60}{RESET}")
    print(f"\n{YELLOW}Archivo: {input_file}{RESET}")
    for i, line in enumerate(source.splitlines(), 1): print(f"  {i:3}: {line}")

    result = compile_source(source, input_file)
    log    = []

    if result['success']:
        banner("COMPILACION EXITOSA", GREEN)
        with open(output_py, 'w', encoding='utf-8') as f: f.write(result['python_code'])
        ok(f"Codigo escrito en '{output_py}'")
        log += ["=== COMPILACION EXITOSA ===", f"Fuente: {input_file}", f"Salida: {output_py}"]
        log += ["\n=== TOKENS ==="] + [f"  {t.type:15} -> '{t.value}'" for t in result['tokens'] if t.type != 'EOF']
        log += ["\n=== TAC ==="] + [str(i) for i in result['tac']]
        log += ["\n=== CODIGO PYTHON ===", result['python_code']]
    else:
        banner("COMPILACION FALLIDA", RED)
        log += ["=== COMPILACION FALLIDA ==="] + result['errors']
        for e in result['errors']: fail(e)

    with open(output_log, 'w', encoding='utf-8') as f: f.write('\n'.join(log))
    print(f"\n{YELLOW}Log guardado en '{output_log}'{RESET}\n")
    return result['success']

def run_tests():
    print(f"\n{BOLD}{CYAN}{'='*60}")
    print("  MathLang - Suite de Pruebas (20 casos)")
    print(f"{'='*60}{RESET}\n")
    passed = failed = total = 0

    print(f"{BOLD}--- Pruebas Validas ---{RESET}")
    for f in sorted(glob.glob("tests/valid/*.ml")):
        total += 1
        with open(f, encoding='utf-8') as fh: src = fh.read()
        res  = compile_source(src, f)
        name = os.path.basename(f)
        if res['success']:
            passed += 1; print(f"  {GREEN}PASS{RESET} {name}")
        else:
            failed += 1; print(f"  {RED}FAIL{RESET} {name}")
            for e in res['errors']: print(f"       {RED}{e}{RESET}")

    print(f"\n{BOLD}--- Pruebas con Errores ---{RESET}")
    for f in sorted(glob.glob("tests/errors/*.ml")):
        total += 1
        with open(f, encoding='utf-8') as fh: src = fh.read()
        res  = compile_source(src, f)
        name = os.path.basename(f)
        if not res['success']:
            passed += 1; print(f"  {GREEN}PASS{RESET} {name}")
            for e in res['errors']: print(f"       {YELLOW}  Detectado: {e}{RESET}")
        else:
            failed += 1; print(f"  {RED}FAIL{RESET} {name} <- debia fallar")

    print(f"\n{BOLD}{'='*60}")
    color = GREEN if failed == 0 else RED
    print(f"  {color}Resultados: {passed}/{total} pruebas pasaron{RESET}")
    print(f"{'='*60}{RESET}\n")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        run_tests()
    else:
        inp = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
        sys.exit(0 if run_compiler(inp) else 1)
