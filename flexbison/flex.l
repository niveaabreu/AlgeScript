%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "parser.tab.h"

char* yyval;

%}
%option yylineno
%option noyywrap


CONDICIONAL se
ELSE senao
ENQUANTO para
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
DIVISAO /
ASSIGN =
NOT !
POTENCIA ^
LOG log 
RAIZ raiz 
NUMERO [0-9]
NOVALINHA \n
IDENTIFIER [a-zA-Z_][a-zA-Z0-9_]*
STRING \"([^\\\"]|\\.)*\" 


%%

[ \t]            ; /* Ignora espaços em branco e tabulações */
"se"             { yyval = strdup(yytext); return CONDICIONAL; }
"senao"           { yyval = strdup(yytext); return ELSE; }
"para"        { yyval = strdup(yytext); return ENQUANTO; }
"mostre"             { yyval = strdup(yytext); return MOSTRE; }
"variavel"          { yyval = strdup(yytext); return VARIAVEL; }
"int"           { yyval = strdup(yytext); return INT; }
"decimal"           { yyval = strdup(yytext); return FLOAT; }
","       { yyval = strdup(yytext); return VIRGULA; }
";" { yyval = strdup(yytext); return PONTOVIRGULA; }
"(" { yyval = strdup(yytext); return PARENDIREITA; }
")" { yyval = strdup(yytext); return PARENESQUERDA; }
"{" { yyval = strdup(yytext); return COLCHETEDIREITA; }
"}" { yyval = strdup(yytext); return COLCHETEESQUERDA; }
"=="          { yyval = strdup(yytext); return IGUAL; }
">"            { yyval = strdup(yytext); return MAIOR; }
"<"            { yyval = strdup(yytext); return MENOR; }
"|"            { yyval = strdup(yytext); return MODULO; }
"+"              { yyval = strdup(yytext); return SOMA; }
"-"              { yyval = strdup(yytext); return SUB; }
"*"              { yyval = strdup(yytext); return MULTIPLICACAO; }
"/"              { yyval = strdup(yytext); return DIVISAO; }
"^"              { yyval = strdup(yytext); return POTENCIA; }
"log"              { yyval = strdup(yytext); return LOG; }
"raiz"             { yyval = strdup(yytext); return RAIZ; }
"+"              { yyval = strdup(yytext); return PLUS; }
"-"              { yyval = strdup(yytext); return MINUS; }
"*"              { yyval = strdup(yytext); return TIMES; }
"/"              { yyval = strdup(yytext); return DIVIDE; }
"="              { yyval = strdup(yytext); return ASSIGN; }
"!"              { yyval = strdup(yytext); return NOT; }
[0-9]+           { yyval = strdup(yytext); return NUMERO; }
[a-zA-Z_][a-zA-Z0-9_]* { yyval = strdup(yytext); return IDENTIFIER; }
\"([^\\\"]|\\.)*\" { yyval = strdup(yytext); return STRING; }

"//".*          ; /* Ignora comentários de uma linha */

"\\\n"           ; /* Ignora quebras de linha precedidas por \ */

\n                { yyval = strdup(yytext); return NEWLINE; }

.               { yyval = strdup(yytext); printf("%s",yyval); }

%%