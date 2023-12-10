from ast import Raise
import sys
import re
import math

class Token:
    def __init__(self,type:str=None,value:int=None) -> None:
        self.type = type
        self.value = value
        
class Tokenizer:
    def __init__(self,source:str,position:int,next:Token) -> None:
        self.source =  source
        self.position = position
        self.next =next
        self.reservadas=["variavel","inteiro","decimal","string","mostre","se","senao","para","raiz","log","sen","cos","tan"]

    def selectNext(self):
        if(self.position==len(self.source)):
            self.next.type="EOF"
            self.next.value="'"
        elif(self.source[self.position] == "\n"):
            self.next.type="QUEBRA"
            self.next.value=self.source[self.position]
            self.position += 1
        elif(self.source[self.position].isspace()) :
            self.position += 1
            self.selectNext()
        elif (self.source[self.position] == "+"):
            self.next.type="PLUS"
            self.next.value=self.source[self.position]
            self.position += 1
        elif(self.source[self.position] == "-"):
            self.next.type="MINUS"
            self.next.value=self.source[self.position]
            self.position += 1
        elif(self.source[self.position] == "*"):
            self.next.type="MULT"
            self.next.value=self.source[self.position]
            self.position += 1
        elif(self.source[self.position] == ":"):
            self.next.type="DIV"
            self.next.value=self.source[self.position]
            self.position += 1
        elif(self.source[self.position] == ">"):
            self.next.type="MAIOR"
            self.next.value=self.source[self.position]
            self.position += 1
        elif(self.source[self.position] == "<"):
            self.next.type="MENOR"
            self.next.value=self.source[self.position]
            self.position += 1
        elif(self.source[self.position] == "!"):
            self.next.type="NOT"
            self.next.value=self.source[self.position]
            self.position += 1
        elif(self.source[self.position] == ";"):
            self.next.type="PONTOVIRGULA"
            self.next.value=self.source[self.position]
            self.position += 1
        elif(self.source[self.position] == "("):
            self.next.type="parenesquerda"
            self.next.value=self.source[self.position]
            self.position += 1
        elif(self.source[self.position] == ")"):
            self.next.type="parendireita"
            self.next.value=self.source[self.position]
            self.position += 1
        elif(self.source[self.position] == "{"):
            self.next.type="CHAVEESQUERDA"
            self.next.value=self.source[self.position]
            self.position += 1
        elif(self.source[self.position] == "}"):
            self.next.type="CHAVEDIREITA"
            self.next.value=self.source[self.position]
            self.position += 1
        elif(self.source[self.position:self.position+2] == "=="):
            self.next.type="EQUAL"
            self.next.value=self.source[self.position:self.position+2]
            self.position += 2
        elif(self.source[self.position] == "="):
            self.next.type="ASSIGN"
            self.next.value=self.source[self.position]
            self.position += 1 
        elif(self.source[self.position:self.position+2] == "||"):
            self.next.type="OR"
            self.next.value=self.source[self.position:self.position+2]
            self.position += 2 
        elif(self.source[self.position:self.position+2] == "&&"):
            self.next.type="AND"
            self.next.value=self.source[self.position:self.position+2]
            self.position += 2 
        elif(self.source[self.position] == ','):
            self.next.type="VIRGULA"
            self.next.value=''
            self.position += 1
        elif(self.source[self.position] == "^"):
            self.next.type="POWERS"
            self.next.value=self.source[self.position]
            self.position += 1
        elif(self.source[self.position] == "|"):
            self.next.type="MODULO"
            self.next.value=self.source[self.position]
            self.position += 1
        elif(self.source[self.position] == '"'):
            self.next.type="string"
            self.next.value=''
            self.position += 1
            while(self.position<len(self.source) and self.source[self.position] != '"'):
                #se receber \n antes de fechar as aspas, tem q gerar raise
                if( self.source[self.position] == "\n"):
                      raise Exception("error")
                self.next.value += self.source[self.position]
                self.position += 1
            self.position += 1 
        elif (re.search(r'\b[a-zA-Z_]\w*\b', self.source[self.position])):
             self.next.value=''
             while(self.position<len(self.source) and re.search(r'\b\w+\b', self.source[self.position])):
                self.next.value += self.source[self.position]
                self.position += 1
             if(self.next.value not in self.reservadas):
                 self.next.type="IDEN"
             else:
                self.next.type="STATEMENT"

        else:
            self.next.value=''
            while(self.source[self.position] in "0123456789."):
                self.next.value += self.source[self.position]
                self.position += 1
                if self.position==len(self.source):
                    break
            if "." in self.next.value:
                self.next.type="FLOAT" 
            else:
                self.next.type = "INT"

class SymbolTable:
       def __init__(self) -> None:
            self.table={}
       def getter(self,chave):
           return self.table[chave]
       def setter(self,chave,valor):
           if(chave in self.table):
               if(valor[1]==self.table[chave][1]):
                    self.table[chave]=valor
               else:
                   raise Exception("Not valid")   
           else:
               raise Exception("Not valid")  
       def create(self,chave,valor) :
           if (chave not in self.table):
               self.table[chave]=valor
           else:
               raise Exception("Not valid")   
               

class PrePro:
    def __init__(self,code:str) -> None:
        self.code =  code
        #remover comentários
    def filter(self):
        linhas = self.code.split('\n')
        linhas_sem_comentarios = []

        for linha in linhas:
            # Verifique se a linha contém "//" e, se sim, remova tudo depois dele
            if '//' in linha:
                linha_sem_comentario = linha.split('//')[0]
            else:
                linha_sem_comentario = linha
            linhas_sem_comentarios.append(linha_sem_comentario)
        # Junte as linhas sem comentários de volta em uma única string
        texto_sem_comentarios = '\n'.join(linhas_sem_comentarios)
        return texto_sem_comentarios

class Node:
    def __init__(self,value,children:list) -> None:
        self.value =  value
        self.children = children
    def Evaluate(self,ST):
        pass
         
class BinOp(Node):
     def __init__(self,value,children:list) -> None:
        super().__init__(value,children)
     def Evaluate(self,ST):
         filho_1 = self.children[0].Evaluate(ST)
         filho_2 = self.children[1].Evaluate(ST)
         if (filho_1[1] == "string" and filho_2[1] == "string"):
            if(self.value==">"):
                resultado=int(filho_1[0] > filho_2[0])
                return (resultado),"int"
            elif(self.value=="=="):
                resultado=int(filho_1[0] == filho_2[0])
                return (resultado),"int" 
            elif(self.value=="<"):
                resultado=int(filho_1[0] < filho_2[0])
                return int(resultado),"int"
         elif (filho_1[1] == "int" and filho_2[1] == "int"):
            if(self.value=="+"):
                resultado=filho_1[0] + filho_2[0]
                return resultado,"int"
            elif(self.value=="-"):
                resultado=filho_1[0] - filho_2[0]
                return resultado,"int"
            elif(self.value=="*"):
                resultado=filho_1[0] * filho_2[0]
                return resultado ,"int"  
            elif(self.value=="^"):
                resultado=filho_1[0] ** filho_2[0]
                return resultado ,"int"  
            elif(self.value==":"):
                resultado=filho_1[0] // filho_2[0]
                return resultado,"int"
            elif(self.value=="||"):
                resultado=filho_1[0] or filho_2[0]
                return int(resultado),"int"
            elif(self.value=="&&"):
                resultado=filho_1[0] and filho_2[0]
                return int(resultado),"int"
            elif(self.value==">"):
                resultado=filho_1[0] > filho_2[0]
                return int(resultado),"int"
            elif(self.value=="<"):
                resultado=filho_1[0] < filho_2[0]
                return int(resultado),"int"
            elif(self.value=="=="):
                resultado=filho_1[0] == filho_2[0]
                return int(resultado),"int" 
            elif(self.value=="."):
                resultado=str(filho_1[0]) + str(filho_2[0]) 
                return (resultado),"string"
         elif (filho_1[1] in ["int","float"] and filho_2[1] in ["int","float"]):
            if(self.value=="+"):
                resultado=filho_1[0] + filho_2[0]
                return resultado,"float"
            elif(self.value=="-"):
                resultado=filho_1[0] - filho_2[0]
                return resultado,"float"
            elif(self.value=="*"):
                resultado=filho_1[0] * filho_2[0]
                return resultado ,"float"  
            elif(self.value==":"):
                resultado=filho_1[0] / filho_2[0]
                return resultado,"float"
            elif(self.value=="^"):
                resultado=filho_1[0] ** filho_2[0]
                return resultado ,"float"  
            elif(self.value=="||"):
                resultado=filho_1[0] or filho_2[0]
                return int(resultado),"float"
            elif(self.value=="&&"):
                resultado=filho_1[0] and filho_2[0]
                return int(resultado),"float"
            elif(self.value==">"):
                resultado=filho_1[0] > filho_2[0]
                return int(resultado),"float"
            elif(self.value=="<"):
                resultado=filho_1[0] < filho_2[0]
                return int(resultado),"float"
            elif(self.value=="=="):
                resultado=filho_1[0] == filho_2[0]
                return int(resultado),"float" 
            elif(self.value=="."):
                resultado=str(filho_1[0]) + str(filho_2[0]) 
                return (resultado),"string"
         elif(filho_1[1] == "string" or filho_2[1] == "string"):
            if(self.value=="."):
                resultado=str(filho_1[0]) + str(filho_2[0]) 
                return (resultado),"string"
            raise Exception("Error")
         raise Exception("Error")

class UnOp(Node):
     def __init__(self,value,children:list) -> None:
        super().__init__(value,children)
     def Evaluate(self,ST):
         resultado=0
         filho_1 = self.children[0].Evaluate(ST) 
         if(self.value=="+"):
            resultado+=filho_1[0]
            return resultado,filho_1[1]
         elif(self.value=="-"):
            resultado-=filho_1[0]
            return resultado,filho_1[1]
         elif(self.value=="!"):
            resultado=not(filho_1[0])
            return resultado,filho_1[1]
         
class IntVal(Node):
    def __init__(self,value,children:list) -> None:
        super().__init__(value,children)
    def Evaluate(self,ST):
         return self.value,"int"
    
class FloatVal(Node):
    def __init__(self,value,children:list) -> None:
        super().__init__(value,children)
    def Evaluate(self,ST):
         return self.value,"float"
    
class Modulo(Node):
    def __init__(self,value,children:list) -> None:
        super().__init__(value,children)
    def Evaluate(self,ST):
         ch = self.children[0].Evaluate(ST)
         return abs(ch[0]),ch[1]
    
class Log(Node):
    def __init__(self,value,children:list) -> None:
        super().__init__(value,children)
    def Evaluate(self,ST):
        exp = self.children[0].Evaluate(ST)[0]
        base =self.children[1].Evaluate(ST)[0] 
        return math.log(exp,base), "float"
    
class Sen(Node):
    def __init__(self,value,children:list) -> None:
        super().__init__(value,children)
    def Evaluate(self,ST):
        degree = self.children[0].Evaluate(ST)[0]
        return math.sin(math.radians(degree)), "float"

class Cos(Node):
    def __init__(self,value,children:list) -> None:
        super().__init__(value,children)
    def Evaluate(self,ST):
        degree = self.children[0].Evaluate(ST)[0]
        return math.cos(math.radians(degree)), "float"
    
class Tan(Node):
    def __init__(self,value,children:list) -> None:
        super().__init__(value,children)
    def Evaluate(self,ST):
        degree = self.children[0].Evaluate(ST)[0]
        return math.tan(math.radians(degree)), "float"
    
class Raiz(Node):
    def __init__(self,value,children:list) -> None:
        super().__init__(value,children)
    def Evaluate(self,ST):
         return math.sqrt(self.children[0].Evaluate(ST)[0]),"float"
    
class StringVal(Node):
    def __init__(self,value,children:list) -> None:
        super().__init__(value,children)
    def Evaluate(self,ST):
         return self.value,"string"
    
class NoOp(Node):
    def __init__(self,value,children:list,tipo="int") -> None:
        super().__init__(value,children)
        self.tipo = tipo
    def Evaluate(self,ST):
         return None,self.tipo
class Block(Node):
    def __init__(self,value,children:list) -> None:
        super().__init__(value,children)
    def Evaluate(self,ST):
         for filho in self.children:
             filho.Evaluate(ST)
class Println(Node):
     def __init__(self,value,children:list) -> None:
        super().__init__(value,children)
     def Evaluate(self,ST):
        print(self.children[0].Evaluate(ST)[0])
#ele le no ST por isso usamos o ST
class Identifier(Node):
     def __init__(self,value,children:list) -> None:
        super().__init__(value,children)
     def Evaluate(self,ST):
       return(ST.getter(self.value))
     
#o Assigment ele escreve por isso usamos o ST setter
class Assigment(Node):
    def __init__(self,value,children:list) -> None:
        super().__init__(value,children)
    def Evaluate(self,ST):
       ST.setter(self.children[0].value,self.children[1].Evaluate(ST))

class If(Node):
    def __init__(self,value,children:list) -> None:
        super().__init__(value,children)
    def Evaluate(self,ST):
        if(self.children[0].Evaluate(ST)[0]):
            self.children[1].Evaluate(ST)
        elif(len(self.children)==3):
            #o else sendo executado
            self.children[2].Evaluate(ST)

class For(Node):
    def __init__(self,value,children:list) -> None:
        super().__init__(value,children)
    def Evaluate(self,ST):
        self.children[0].Evaluate(ST)
        while True:
            if not(self.children[1].Evaluate(ST)[0]):
                break
            self.children[3].Evaluate(ST)
            self.children[2].Evaluate(ST)

class Vardec(Node):
    def __init__(self,value,children:list) -> None:
        super().__init__(value,children)
    def Evaluate(self,ST):
       ST.create(self.children[0].value,self.children[1].Evaluate(ST))


class Parser:
    def _init_(self,source:str,position:int,tokenizer:Tokenizer) -> None:
        self.source =  source
        self.position = position
        self.tokenizer = tokenizer

    @staticmethod
    def Assign(tokenizer):
        variavel=Identifier(tokenizer.next.value,[])
        tokenizer.selectNext()
        if (tokenizer.next.type == "ASSIGN"):   
            resultado_igual=Assigment("=",[variavel,Parser.parseRelExpression(tokenizer)])
            return resultado_igual
        raise Exception("Not valid")   
    
    @staticmethod
    def parseProgram(tokenizer):  
        resultado_no=Block(None,[])
        tokenizer.selectNext()
        while(tokenizer.next.type!="EOF"):
            if tokenizer.next.type=="STATEMENT" or tokenizer.next.type=="IDEN" or tokenizer.next.type=="QUEBRA":
                resultado_no.children.append(Parser.parseStatement(tokenizer))
                tokenizer.selectNext()
            else:
                raise Exception("error")
        return resultado_no
    
        
    @staticmethod
    def parseBlock(tokenizer):  
        resultado_no=Block(None,[])
        if(tokenizer.next.type=="CHAVEESQUERDA"):
            tokenizer.selectNext()
            while(tokenizer.next.type=="QUEBRA"):
                tokenizer.selectNext()
                resultado_no.children.append(Parser.parseStatement(tokenizer))
            if(tokenizer.next.type=="CHAVEDIREITA"):
                tokenizer.selectNext()
                return resultado_no
            raise Exception("Not valid")  
        raise Exception("Not valid")  
       
    
    @staticmethod
    def parseStatement(tokenizer):
        if(tokenizer.next.type=="QUEBRA"):    
            return NoOp(None,[])
        elif (tokenizer.next.type == "IDEN"):
            resultado = Parser.Assign(tokenizer)
            if(tokenizer.next.type=="QUEBRA" or tokenizer.next.type=="EOF"):
                return resultado
            raise Exception("error")
        elif(tokenizer.next.type == "STATEMENT"):
            if(tokenizer.next.value == "mostre"):
                tokenizer.selectNext()
                if (tokenizer.next.type == "parenesquerda"):
                    resultado=Parser.parseRelExpression(tokenizer)
                    if(tokenizer.next.type == "parendireita"):
                        no_print=Println("mostre",[resultado])
                        tokenizer.selectNext()
                        if(tokenizer.next.type=="QUEBRA" or tokenizer.next.type=="EOF"):
                            return no_print
                        raise Exception("Not valid") 
                    raise Exception("Not valid") 
                raise Exception("Not valid") 
            elif(tokenizer.next.value=="variavel"):
                tokenizer.selectNext()
                if (tokenizer.next.type == "IDEN"):
                    resultado= tokenizer.next.value
                    no_identifier = Identifier(value=resultado,children=[])
                    tokenizer.selectNext()
                    if (tokenizer.next.value=="inteiro" or tokenizer.next.value=="string" or tokenizer.next.value=="decimal"):
                        tipo = tokenizer.next.value
                        tokenizer.selectNext()
                        if(tokenizer.next.type=="QUEBRA"):
                            no_saida = Vardec(resultado, [no_identifier,NoOp(None,[],tipo=tipo)])
                            return no_saida
                        elif (tokenizer.next.type == "ASSIGN"):
                            expr = Parser.parseRelExpression(tokenizer)
                            no_saida = Vardec(resultado, [no_identifier,expr])
                            return no_saida
                        raise Exception("Not valid") 
                    raise Exception("Not valid") 
                raise Exception("Not valid") 
            elif(tokenizer.next.value=="se"):
                condition=Parser.parseRelExpression(tokenizer)
                no_block=Parser.parseBlock(tokenizer)
                if(tokenizer.next.value == "senao"):
                    tokenizer.selectNext()
                    else_block=Parser.parseBlock(tokenizer)
                    if_block = If(value="se",children= [condition,no_block,else_block])
                    return if_block
                if_block = If(value="se",children= [condition,no_block])
                return if_block
            
            elif(tokenizer.next.value=="para"):
                tokenizer.selectNext()
                init=Parser.parseStatement(tokenizer)
                if(tokenizer.next.type == "PONTOVIRGULA"):
                    condition=Parser.parseRelExpression(tokenizer)
                    if(tokenizer.next.type == "PONTOVIRGULA"):
                        tokenizer.selectNext()
                        incremento=Parser.Assign(tokenizer)
                        block=Parser.parseBlock(tokenizer)
                        for_block = For(value="para",children=[init,condition,incremento,block])
                        return for_block
        elif (tokenizer.next.type == "INT"):
            raise Exception("not valid")
        return NoOp(None,[])

    @staticmethod
    def parseRelExpression(tokenizer):
        resultado_Node=Parser.parseExpression(tokenizer)
        while(tokenizer.next.type=="MAIOR" or tokenizer.next.type=="MENOR" or tokenizer.next.type=="EQUAL"):    
            if(tokenizer.next.type=="MAIOR"):
                variavel=Parser.parseExpression(tokenizer)  
                resultado_Node=BinOp(">",[resultado_Node,variavel])
            elif(tokenizer.next.type=="MENOR"):
                variavel=Parser.parseExpression(tokenizer)  
                resultado_Node=BinOp("<",[resultado_Node,variavel])
            else: 
                variavel=Parser.parseTerm(tokenizer)  
                resultado_Node=BinOp("==",[resultado_Node,variavel])
        return resultado_Node
   
    @staticmethod
    def parseExpression(tokenizer):
        resultado_Node=Parser.parseTerm(tokenizer)
        while(tokenizer.next.type=="PLUS" or tokenizer.next.type=="MINUS" or tokenizer.next.type=="CONCAT"):    
            if(tokenizer.next.type=="MINUS"):
                variavel=Parser.parseTerm(tokenizer)  
                resultado_Node=BinOp("-",[resultado_Node,variavel])
            elif(tokenizer.next.type=="PLUS"): 
                variavel=Parser.parseTerm(tokenizer)  
                resultado_Node=BinOp("+",[resultado_Node,variavel])
            else:
                variavel=Parser.parseTerm(tokenizer)  
                resultado_Node=BinOp(".",[resultado_Node,variavel])

        return resultado_Node

    @staticmethod
    def parseTerm(tokenizer):
        resultado_Node=Parser.parsePowers(tokenizer) 
        while(tokenizer.next.type=="MULT" or tokenizer.next.type=="DIV"):
            if(tokenizer.next.type=="MULT"):
                variavel=Parser.parsePowers(tokenizer)  
                resultado_Node=BinOp("*",[resultado_Node,variavel]) 
            else: 
                variavel=Parser.parsePowers(tokenizer)  
                resultado_Node=BinOp(":",[resultado_Node,variavel]) 
                         
        return resultado_Node
    
    @staticmethod
    def parsePowers(tokenizer):
        resultado_Node=Parser.parseFactor(tokenizer) 
        while(tokenizer.next.type=="POWERS"):
                variavel=Parser.parseFactor(tokenizer)  
                resultado_Node=BinOp("^",[resultado_Node,variavel]) 
                         
        return resultado_Node


    @staticmethod
    def parseFactor(tokenizer):
        tokenizer.selectNext()
        resultado=0
        if(tokenizer.next.type=="INT"):
            resultado= int(tokenizer.next.value)
            tokenizer.selectNext()
            resultado_int=IntVal(resultado,None) 
            return resultado_int
        elif(tokenizer.next.type=="FLOAT"):
            resultado = float(tokenizer.next.value)
            tokenizer.selectNext()
            resultado_float=FloatVal(resultado,None) 
            return resultado_float
        elif(tokenizer.next.type=="string"):
            resultado= tokenizer.next.value
            tokenizer.selectNext()
            resultado_string=StringVal(resultado,None) 
            return resultado_string
        elif(tokenizer.next.type=="IDEN"):
            resultado_ident=Identifier(tokenizer.next.value,[]) 
            tokenizer.selectNext()
            return resultado_ident
        elif (tokenizer.next.type == "PLUS"):
            resultado=UnOp("+",[Parser.parseFactor(tokenizer)])   
            return resultado
        elif(tokenizer.next.type == "MINUS"):
            resultado=UnOp("-",[Parser.parseFactor(tokenizer)]) 
            return resultado
        elif(tokenizer.next.type == "NOT"):
            resultado=UnOp("!",[Parser.parseFactor(tokenizer)]) 
            return resultado
        elif(tokenizer.next.value == "raiz"):
            tokenizer.selectNext()
            if (tokenizer.next.type == "parenesquerda"):
                resultado=Parser.parseRelExpression(tokenizer)
                if(tokenizer.next.type == "parendireita"):
                    tokenizer.selectNext()
                    return Raiz(value="raiz",children=[resultado])
            raise Exception("error")
        elif(tokenizer.next.value == "sen"):
            tokenizer.selectNext()
            if (tokenizer.next.type == "parenesquerda"):
                resultado=Parser.parseRelExpression(tokenizer)
                if(tokenizer.next.type == "parendireita"):
                    tokenizer.selectNext()
                    return Sen(value="sen",children=[resultado])
            raise Exception("error")
        elif(tokenizer.next.value == "cos"):
            tokenizer.selectNext()
            if (tokenizer.next.type == "parenesquerda"):
                resultado=Parser.parseRelExpression(tokenizer)
                if(tokenizer.next.type == "parendireita"):
                    tokenizer.selectNext()
                    return Cos(value="cos",children=[resultado])
            raise Exception("error")
        elif(tokenizer.next.value == "tan"):
            tokenizer.selectNext()
            if (tokenizer.next.type == "parenesquerda"):
                resultado=Parser.parseRelExpression(tokenizer)
                if(tokenizer.next.type == "parendireita"):
                    tokenizer.selectNext()
                    return Tan(value="tan",children=[resultado])
            raise Exception("error")
        elif(tokenizer.next.value == "log"):
            tokenizer.selectNext()
            if (tokenizer.next.type == "parenesquerda"):
                expressao=Parser.parseRelExpression(tokenizer)
                if (tokenizer.next.type == "VIRGULA"):
                    base=Parser.parseRelExpression(tokenizer)
                    if(tokenizer.next.type == "parendireita"):
                        tokenizer.selectNext()
                        return Log(value="log",children=[expressao,base])
            raise Exception("error")
        elif(tokenizer.next.type == "MODULO"):
            resultado=Parser.parseRelExpression(tokenizer)
            if(tokenizer.next.type == "MODULO"):
                tokenizer.selectNext()
                return Modulo(value="modulo",children=[resultado])
        elif (tokenizer.next.type == "parenesquerda"):
            resultado=Parser.parseRelExpression(tokenizer)
            if(tokenizer.next.type == "parendireita"):
                tokenizer.selectNext()
                return resultado
        else:
            raise Exception("error")
     
    @staticmethod
    def run(code:str):
        code=PrePro(code).filter()
        tokenizer = Tokenizer(code,0,Token())
        result = Parser.parseProgram(tokenizer)
        if(tokenizer.next.type != "EOF"):
              raise Exception("Not valid") 
        return result

source = sys.argv[1]#nome de arquivo
with open(source,'r') as arquivo:
    code = arquivo.read()
ST=SymbolTable()
node=Parser.run(code)
node.Evaluate(ST)