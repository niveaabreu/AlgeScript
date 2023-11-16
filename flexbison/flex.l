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
"foreach"        { yyval = strdup(yytext); return FOREACH; }
"to"             { yyval = strdup(yytext); return TO; }
"while"          { yyval = strdup(yytext); return WHILE; }
"show"           { yyval = strdup(yytext); return SHOW; }
"rule"           { yyval = strdup(yytext); return RULE; }
"match"          { yyval = strdup(yytext); return MATCH; }
"scanhost"       { yyval = strdup(yytext); return SCANHOST; }
"traffic_information" { yyval = strdup(yytext); return TRAFFIC_INFORMATION; }
"input"          { yyval = strdup(yytext); return INPUT; }
":"            { yyval = strdup(yytext); return DECLARE; }
"int"            { yyval = strdup(yytext); return INT; }
"str"            { yyval = strdup(yytext); return STR; }
"("              { yyval = strdup(yytext); return LPAREN; }
")"              { yyval = strdup(yytext); return RPAREN; }
"{"              { yyval = strdup(yytext); return LBRACE; }
"}"              { yyval = strdup(yytext); return RBRACE; }
","              { yyval = strdup(yytext); return COMMA; }
";"              { yyval = strdup(yytext); return SEMICOLON; }
"=="             { yyval = strdup(yytext); return EQ; }
">"              { yyval = strdup(yytext); return GT; }
"<"              { yyval = strdup(yytext); return LT; }
"&&"             { yyval = strdup(yytext); return AND; }
"||"             { yyval = strdup(yytext); return OR; }
"+"              { yyval = strdup(yytext); return PLUS; }
"-"              { yyval = strdup(yytext); return MINUS; }
"*"              { yyval = strdup(yytext); return TIMES; }
"/"              { yyval = strdup(yytext); return DIVIDE; }
"="              { yyval = strdup(yytext); return ASSIGN; }
"!"              { yyval = strdup(yytext); return NOT; }
[0-9]+           { yyval = strdup(yytext); return NUMBER; }
[a-zA-Z_][a-zA-Z0-9_]* { yyval = strdup(yytext); return IDENTIFIER; }
\"([^\\\"]|\\.)*\" { yyval = strdup(yytext); return STRING; }

"//".*          ; /* Ignora comentários de uma linha */

"\\\n"           ; /* Ignora quebras de linha precedidas por \ */

\n                { yyval = strdup(yytext); return NEWLINE; }

.               { yyval = strdup(yytext); printf("%s",yyval); }

%%