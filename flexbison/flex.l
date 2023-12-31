%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "bison.tab.h"

char* yyval;

%}
%option yylineno
%option noyywrap


CONDICIONAL se
ELSE senao
PARA para
MOSTRE mostre
VARIAVEL variavel
INT inteiro
FLOAT decimal
PARENDIREITA (
PARENESQUERDA )
COLCHETEDIREITA {
COLCHETEESQUERDA }
VIRGULA ,
PONTOVIRGULA ;
IGUAL  ==
MAIOR >
MENOR <
MODULO |
SOMA +
SUB -
MULTIPLICACAO *
DIVISAO :
ASSIGN =
NOT !
POTENCIA ^
SEN sen
COS cos
TAN tan
LOG log 
RAIZ raiz 
INTEIRO [0-9]+
DECIMAL [0-9]+"."[0-9]+
NOVALINHA \n
IDENTIFIER [a-zA-Z_][a-zA-Z0-9_]*
STRING \"([^\\\"]|\\.)*\" 


%%

[ \t]            ; /* Ignora espaços em branco e tabulações */
"se"             { yyval = strdup(yytext); return CONDICIONAL; }
"senao"           { yyval = strdup(yytext); return ELSE; }
"para"        { yyval = strdup(yytext); return PARA; }
"mostre"             { yyval = strdup(yytext); return MOSTRE; }
"variavel"          { yyval = strdup(yytext); return VARIAVEL; }
"inteiro"           { yyval = strdup(yytext); return INT; }
"decimal"           { yyval = strdup(yytext); return FLOAT; }
","       { yyval = strdup(yytext); return VIRGULA; }
";" { yyval = strdup(yytext); return PONTOVIRGULA; }
"(" { yyval = strdup(yytext); return PARENESQUERDA; }
")" { yyval = strdup(yytext); return PARENDIREITA; }
"{" { yyval = strdup(yytext); return COLCHETEESQUERDA; }
"}" { yyval = strdup(yytext); return COLCHETEDIREITA; }
"=="          { yyval = strdup(yytext); return IGUAL; }
">"            { yyval = strdup(yytext); return MAIOR; }
"<"            { yyval = strdup(yytext); return MENOR; }
"|"            { yyval = strdup(yytext); return MODULO; }
"+"              { yyval = strdup(yytext); return SOMA; }
"-"              { yyval = strdup(yytext); return SUB; }
"*"              { yyval = strdup(yytext); return MULTIPLICACAO; }
":"              { yyval = strdup(yytext); return DIVISAO; }
"^"              { yyval = strdup(yytext); return POTENCIA; }
"log"              { yyval = strdup(yytext); return LOG; }
"raiz"             { yyval = strdup(yytext); return RAIZ; }
"sen"             { yyval = strdup(yytext); return SEN; }
"cos"             { yyval = strdup(yytext); return COS; }
"tan"             { yyval = strdup(yytext); return TAN; }
"="              { yyval = strdup(yytext); return ASSIGN; }
"!"              { yyval = strdup(yytext); return NOT; }
[0-9]+           { yyval = strdup(yytext); return INTEIRO; }
[0-9]+(\.[0-9]+)?          { yyval = strdup(yytext); return DECIMAL; }
[a-zA-Z_][a-zA-Z0-9_]* { yyval = strdup(yytext); return IDENTIFIER; }
\"([^\\\"]|\\.)*\" { yyval = strdup(yytext); return STRING; }

"//".*          ; /* Ignora comentários de uma linha */


\n                { yyval = strdup(yytext); return NOVALINHA; }

.               { yyval = strdup(yytext); printf("%s",yyval); }

%%