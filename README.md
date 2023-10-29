# AlgeScript
Linguagem de Programação cujo objetivo é introduzir alunos de Ensino Fundamental a algoritmos por meio de resolução de problemas da área de matemática

## EBNF
```
PROGRAM = { STATEMENT };

BLOCK = { "{", STATEMENT, "}"};

STATEMENT = ( λ | ASSIGNMENT | CONDICIONAL | MOSTRE | ENQUANTO | VARIAVEL ), "\n" ;

ASSIGMENT = IDENTIFIER, "=", REXPRESSION;

VARIAVEL = "variavel", IDENTIFIER, { "inteiro" | "decimal" | "=", EXPRESSION};

MOSTRE = "mostre", "(", REXPRESSION, ")";

ENQUANTO = "para", ASSIGMENT, ";", REXPRESSION, ";", ASSIGMENT, BLOCK;

CONDICIONAL = "se", REXPRESSION, {"senão", BLOCK|BLOCK};

REXPRESSION = EXPRESSION, {("==" | ">" | "<"), EXPRESSION};

EXPRESSION = TERM, {("+" | "-" ), TERM};

TERM = POWERS, {("*" | ":"), POWERS };

POWERS = FACTOR, {("^" | RAIZ | LOG ), FACTOR };

RAIZ = "raiz", "(", EXPRESSION, ")";

LOG = "log", NUMBER ,"(", EXPRESSION, ")";

FACTOR = (("+" | "-" | "!"), FACTOR | INT |FLOAT | LETTER | MODULO | "(", EXPRESSION, ")" | IDENTIFIER);

MODULO = "|", EXPRESSION, "|";

IDENTIFIER = LETTER, { LETTER | DIGIT | "_"};

FLOAT  = {NUMBER}, ".", {NUMBER}

INT = {NUMBER}+

NUMBER = DIGIT, { DIGIT };

LETTER = ( a | ... | z | A | .. | Z);

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 );
```
