# AlgeScript
Linguagem de Programação com intuito de introduzir alunos de Ensino Fundamental a algoritmos por meio de uma linguagem com fins de facilitar a resolução de problemas algébricos e matemáticos simples.
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

## Exemplos de código
* EXEMPLO 1:
  
Descobrindo a raiz de um polinomio $x^2 + x - 1$
```python
variavel a inteiro = 1
variavel b inteiro = 1
variavel c inteiro =-1
variavel delta decimal = b^2 - 4*a*c
variavel x1 decimal= (-b + raiz(delta)) : 2a
variavel x2 decimal= (-b - raiz(delta)) : 2a
mostre(x1) #0.618
mostre(x2) #-1.61
```

* EXEMPLO 2:

  Resolvendo o somatório abaixo (considerando t = 2):
  
$$\sum_{i=0}^{10} (1+t)^i$$

```python
variavel t inteiro = 2
variavel resultado inteiro = 0
para variavel i inteiro = 1; i < 11; i = i + 1{
    resultado = resultado + (1+t)^i
}
mostre(resultado) #79798
```

* EXEMPLO 3:
  
Resolvendo a expressão algebrica abaixo para x=1 e y =4:

$$\log_4(xy) + |x - y|$$

```python

variavel x inteiro = 1
variavel y inteiro = 4
mostre(log4(x*y)+|x-y|) #4
```
