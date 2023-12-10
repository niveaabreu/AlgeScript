# AlgeScript
Linguagem de Programação com intuito de introduzir alunos de Ensino Fundamental a algoritmos por meio de uma linguagem com fins de facilitar a resolução de problemas algébricos e matemáticos simples.
## EBNF
```
PROGRAM = { STATEMENT };

BLOCK = { "{", STATEMENT, "}"};

STATEMENT = ( λ | ASSIGNMENT | CONDICIONAL | MOSTRE | ENQUANTO | VARIAVEL ), "\n" ;

ASSIGMENT = IDENTIFIER, "=", REXPRESSION;

VARIAVEL = "variavel", IDENTIFIER,  ("inteiro" | "decimal") , "=", EXPRESSION;

MOSTRE = "mostre", "(", REXPRESSION, ")";

ENQUANTO = "para", VARIAVEL, ";", REXPRESSION, ";", ASSIGMENT, BLOCK;

CONDICIONAL = "se", REXPRESSION, {"senão", BLOCK|BLOCK};

REXPRESSION = EXPRESSION, {("==" | ">" | "<"), EXPRESSION};

EXPRESSION = TERM, {("+" | "-" ), TERM};

TERM = POWERS, {("*" | ":"), POWERS };

POWERS = FACTOR, {("^"), FACTOR };

RAIZ = "raiz", "(", EXPRESSION, ")";

SEN = "sen", "(", EXPRESSION, ")";

COS = "cos", "(", EXPRESSION, ")";

TAN = "tan", "(", EXPRESSION, ")";

LOG = "log" ,"(", EXPRESSION, "," , EXPRESSION ")";

FACTOR = (("+" | "-" | "!"), FACTOR | INT |FLOAT | LETTER | MODULO | LOG | SEN | COS | TAN | RAIZ | "(", EXPRESSION, ")" | IDENTIFIER);

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
variavel x1 decimal= (-b + raiz(delta)) : 2*a
variavel x2 decimal= (-b - raiz(delta)) : 2*a
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
mostre(resultado) #88572
```

* EXEMPLO 3:
  
Resolvendo a expressão algebrica abaixo para x=1 e y =4:

$$\log_4(xy) + |x - y|$$

```python

variavel x inteiro = 1
variavel y inteiro = 4
mostre(log(x*y,4)+|x-y|) #4
```


* EXEMPLO 4:
  
$$
\theta = 45°
,
\alpha = 30°
$$    

$$
x = sin(\theta)
$$

$$
y = cos(\alpha)
$$

$$
f(x,y) = \begin{cases}
x, & \text{se } x > y \\
y, & \text{senão}
\end{cases}
$$

```python
variavel theta inteiro = 30
variavel alpha inteiro = 45
variavel x decimal = sen(theta)
variavel y decimal = cos(alpha)
se x > y{
    mostre(x)
} senao {
    mostre(y)
}
```

## Para executar Análise Léxica e Sintática
Em um sistema operacional Linux, instale Flex e Bison, então, dentro da pasta **flexbison**, execute:

```
flex flex.l
bison -d bison.y
gcc lex.yy.c bison.tab.c -o parser
./parser < teste1.as
./parser < teste2.as
./parser < teste3.as
./parser < teste4.as
./parser < teste5.as
```

Dessa forma um programa de teste, será analisado pelo executável gerado, e caso respeite as normas gramaticas estabelecidas no EBNF, não deverá retornar nada.

## Para executar Análise Semântica e geração de código
Dentro da pasta **conceitoB**, execute:

```
python main.py teste1.as
python main.py teste2.as
python main.py teste3.as
python main.py teste4.as
python main.py teste5.as
```

Gerando as saídas esperadas.
