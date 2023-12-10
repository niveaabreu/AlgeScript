%{
#include <stdio.h>
int yylex();
void yyerror(const char *s);
%}

%token CONDICIONAL
%token ELSE
%token PARA
%token MOSTRE
%token VARIAVEL
%token INT
%token FLOAT
%token PARENDIREITA
%token PARENESQUERDA
%token COLCHETEDIREITA
%token COLCHETEESQUERDA
%token VIRGULA
%token PONTOVIRGULA
%token IGUAL
%token MAIOR
%token MENOR
%token MODULO
%token SOMA
%token SUB
%token MULTIPLICACAO
%token DIVISAO
%token ASSIGN
%token NOT
%token POTENCIA
%token LOG
%token RAIZ
%token SEN
%token COS
%token TAN
%token INTEIRO
%token DECIMAL
%token NOVALINHA
%token IDENTIFIER
%token STRING


%%
program: statement
        | program statement;

block: COLCHETEESQUERDA NOVALINHA statements COLCHETEDIREITA ;

statements: statement
          | statements statement
          ;

statement: assigment 
         | condicional
         | mostre
         | para
         | variavel
         ;

assigment : IDENTIFIER ASSIGN rexpression NOVALINHA
          | IDENTIFIER ASSIGN rexpression;

variavel : VARIAVEL IDENTIFIER tipos ASSIGN expression NOVALINHA
         | VARIAVEL IDENTIFIER tipos ASSIGN expression;   

tipos : INT 
      | FLOAT
      ;

condicional: CONDICIONAL rexpression  block
           | CONDICIONAL rexpression  block NOVALINHA
           | CONDICIONAL rexpression block ELSE block NOVALINHA
           ;

mostre: MOSTRE PARENESQUERDA rexpression PARENDIREITA NOVALINHA;

para: PARA variavel PONTOVIRGULA rexpression PONTOVIRGULA assigment block NOVALINHA;

rexpression: rexpression tiposdesinais expression 
           | expression
           ;

tiposdesinais: IGUAL | MAIOR | MENOR;

expression: expression tiposdeop term
          | term
          ;

tiposdeop: SOMA | SUB;

term: term tiposdeterm powers
    | powers
    ;

tiposdeterm: MULTIPLICACAO | DIVISAO;

powers: powers tiposdepower factor
      | factor
      ;

tiposdepower: POTENCIA;

factor: SOMA factor 
      | SUB factor
      | NOT factor
      | IDENTIFIER
      | numero 
      | modulo
      | raiz
      | sen
      | cos
      | tan
      | log
      | PARENESQUERDA expression PARENDIREITA
      ;

raiz: RAIZ PARENESQUERDA expression PARENDIREITA;

sen: SEN PARENESQUERDA expression PARENDIREITA;

cos: COS PARENESQUERDA expression PARENDIREITA;

tan: TAN PARENESQUERDA expression PARENDIREITA;

log: LOG PARENESQUERDA expression VIRGULA expression PARENDIREITA;

modulo: MODULO expression MODULO;

numero: INTEIRO | DECIMAL;

%%

void yyerror(const char *s) {
    extern int yylineno;
    extern char *yytext;
    printf("\nErro (%s): símbolo \"%s\" (linha %d)\n", s, yytext, yylineno);
}

int main() {
    yyparse();
    return 0;
}