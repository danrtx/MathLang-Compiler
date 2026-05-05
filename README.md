# MathLang Compiler

**Mini Lenguaje de Formulas Matematicas Cientificas**
Universidad Cooperativa de Colombia — Ingenieria de Software — Compiladores

---

## Diagrama de Arquitectura

```mermaid
flowchart TD
    A([📄 Codigo Fuente
.ml]) --> B

    subgraph FASE1 [Fase 1 - Analisis Lexico]
        B[tokenize
generated/lexer_parser.py]
    end

    subgraph FASE2 [Fase 2 - Analisis Sintactico]
        C[Parser
generated/lexer_parser.py]
    end

    subgraph FASE3 [Fase 3 - Analisis Semantico]
        E[SemanticAnalyzer
semantic_analyzer/analyzer.py]
        F[(Tabla de Simbolos
SymbolTable)]
    end

    subgraph FASE4 [Fase 4 - Codigo Intermedio]
        G[TACGenerator
codegen/code_generator.py]
    end

    subgraph FASE5 [Fase 5 - Generacion Final]
        I[PythonCodeGenerator
codegen/code_generator.py]
    end

    B -->|Tokens| C
    C -->|AST| E
    E <-->|define/lookup| F
    E -->|AST validado| G
    G -->|TAC Instructions| I
    I --> J([✅ output_program.py])
    J --> K([▶ Ejecucion Python])

    B -->|LexerError| ERR([❌ Error con linea
y mensaje])
    C -->|ParseError| ERR
    E -->|SemanticError| ERR

    style FASE1 fill:#EBF5FB,stroke:#2E86C1
    style FASE2 fill:#EAF4FB,stroke:#1A5276
    style FASE3 fill:#F4ECF7,stroke:#7D3C98
    style FASE4 fill:#EAFAF1,stroke:#1E8449
    style FASE5 fill:#FEF9E7,stroke:#B7950B
    style ERR fill:#FADBD8,stroke:#C0392B
    style J fill:#D5F5E3,stroke:#1E8449
    style K fill:#D5F5E3,stroke:#1E8449
```

---

## Uso

```bash
python3 main.py                 # compilar input.txt
python3 main.py archivo.ml     # compilar archivo propio
python3 main.py --test         # ejecutar 20 pruebas automatizadas
python3 output_program.py      # ejecutar el codigo Python generado
```

---

## Estructura del Proyecto

```
MathLang-Compiler/
├── main.py                        # Orquestador de todas las fases
├── gramatica.g4                   # Gramatica ANTLR4 del lenguaje
├── input.txt                      # Programa de prueba principal
├── output_program.py              # Codigo Python generado (auto)
├── output.txt                     # Log de ejecucion (auto)
├── README.md                      # Este archivo
├── generated/
│   ├── __init__.py
│   └── lexer_parser.py            # Fase 1 (Lexico) + Fase 2 (Sintactico)
├── semantic_analyzer/
│   ├── __init__.py
│   └── analyzer.py                # Fase 3: Semantico + Tabla de Simbolos
├── codegen/
│   ├── __init__.py
│   └── code_generator.py          # Fase 4 (TAC) + Fase 5 (Python)
└── tests/
    ├── valid/                     # 10 pruebas validas
    └── errors/                    # 10 pruebas con errores
```

---

## Sintaxis del Lenguaje MathLang

```
// Comentario de una linea
/* Comentario de bloque */

// Declaracion de funcion
func nombre(param1, param2) {
    return expresion;
}

// Asignacion de variable
variable = expresion;

// Imprimir resultado
print(expresion);
```

### Ejemplo completo

```
func cuadrado(x) {
    return x * x;
}

a = 5;
b = cuadrado(a) + 3;
print(b);
```

Codigo Python generado:

```python
def cuadrado(x):
    return (x * x)

a = 5
b = (cuadrado(a) + 3)
print(b)
```

Salida: `28`

---

## Fases del Compilador

| Fase | Archivo | Responsabilidad |
|------|---------|-----------------|
| Lexico | `generated/lexer_parser.py` | Tokenizacion, deteccion de caracteres ilegales |
| Sintactico | `generated/lexer_parser.py` | Parser recursivo descendente, construccion del AST |
| Semantico | `semantic_analyzer/analyzer.py` | Tabla de simbolos, ambitos, validaciones |
| Codigo Intermedio | `codegen/code_generator.py` | Generacion de TAC |
| Codigo Final | `codegen/code_generator.py` | Traduccion a Python ejecutable |

---

## Reglas Semanticas

- Variables deben declararse antes de usarse
- Funciones deben declararse antes de llamarse
- Numero de argumentos debe coincidir con parametros declarados
- `return` solo valido dentro de funciones
- Division por cero literal detectada en tiempo de compilacion

---

## Pruebas

```
python3 main.py --test
```

- 10 pruebas validas: suma, funciones, flotantes, precedencia, anidamiento, reasignacion
- 10 pruebas con errores: variable no declarada, funcion no declarada, args incorrectos,
  division por cero, caracter ilegal, falta de punto y coma, llave sin cerrar,
  return fuera de funcion

Resultado: **20/20 pruebas pasan**

---

**Universidad Cooperativa de Colombia** | Ingenieria de Software | Compiladores 2026
Danilo Andres Montezuma Ibarra | Juan Jose Burbano Bolanos | Juan Fernando Rosero Coral
