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

