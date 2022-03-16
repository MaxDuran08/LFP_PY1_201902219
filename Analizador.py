from prettytable import PrettyTable
from Error import Error
from Token import Token

class Analizador:
    def __init__(self):
        self.listaTokens  = []
        self.listaErrores = []
        self.linea = 1
        self.columna = 0
        self.buffer = ''
        self.estado = 0
        self.i = 0

    def agregar_token(self,caracter,linea,columna,token):
        self.listaTokens.append(Token(caracter,linea,columna,token))
        self.buffer = ''


    def agregar_error(self,caracter,linea,columna):
        self.listaErrores.append(Error(caracter, linea, columna))

    def q0(self,caracter:str):
        if caracter.isalpha():
            self.estado = 1
            self.buffer += caracter
            self.columna += 1
        elif caracter == '>':
            self.estado = 2
            self.buffer += caracter
            self.columna += 1
        elif caracter == '<':
            self.estado = 3
            self.buffer += caracter
            self.columna += 1
        elif caracter == '~':
            self.estado = 4
            self.buffer += caracter
            self.columna += 1
        elif caracter == '[':
            self.estado = 5
            self.buffer += caracter
            self.columna += 1
        elif caracter == ':':
            self.estado = 6
            self.buffer += caracter
            self.columna += 1
        elif caracter == '\"':
            self.estado = 7
            self.buffer += caracter
            self.columna += 1
        elif caracter == ',':
            self.estado = 8
            self.buffer += caracter
            self.columna += 1
        elif caracter == ']':
            self.estado = 9
            self.buffer += caracter
            self.columna += 1
        elif caracter == '\'':
            self.estado = 10
            self.buffer += caracter
            self.columna += 1
        elif caracter == '-':
            self.estado = 11
            self.buffer += caracter
            self.columna += 1
        elif caracter== '\n':
            self.linea += 1
            self.columna = 0
        elif caracter in ['\t',' ']:
            self.columna += 1
        elif caracter == '$':
            print('[ANALIZAR]: Analisis completado')
        else:
            self.agregar_error(caracter,self.linea,self.columna)
    
    def q1(self,caracter:str):
        if caracter.isalpha():
            self.estado = 1
            self.buffer += caracter
            self.columna += 1
        elif caracter.isdigit():
            self.estado = 1
            self.buffer += caracter
            self.columna += 1          
        else: 
            if self.buffer in ['valor','tipo','fondo','nombre','valores','evento']:
                self.agregar_token(self.buffer,self.linea,self.columna,'reservada_'+self.buffer)    
                self.estado = 0
                self.i -= 1
            else:
                self.agregar_token(self.buffer,self.linea,self.columna,'identificador')
                self.estado = 0
                self.i -= 1
    
    def q2(self,caracter:str):
        self.agregar_token(self.buffer,self.linea,self.columna,'mayorQue')
        self.estado = 0
        self.i -= 1
    
    def q3(self,caracter:str):
        self.agregar_token(self.buffer,self.linea,self.columna,'menorQue')
        self.estado = 0
        self.i -= 1

    def q4(self,caracter:str):
        self.agregar_token(self.buffer,self.linea,self.columna,'virgulilla')
        self.estado = 0
        self.i -= 1

    def q5(self,caracter:str):
        self.agregar_token(self.buffer,self.linea,self.columna,'corcheteIzquierdo')
        self.estado = 0
        self.i -= 1

    def q6(self,caracter:str):
        self.agregar_token(self.buffer,self.linea,self.columna,'dosPuntos')
        self.estado = 0
        self.i -= 1

    def q7(self,caracter:str):
        self.agregar_token(self.buffer,self.linea,self.columna,'comillas')
        self.estado = 0
        self.i -= 1

    def q8(self,caracter:str):
        self.agregar_token(self.buffer,self.linea,self.columna,'coma')
        self.estado = 0
        self.i -= 1

    def q9(self,caracter:str):
        self.agregar_token(self.buffer,self.linea,self.columna,'corcheteDerecho')
        self.estado = 0
        self.i -= 1

    def q10(self,caracter:str):
        self.agregar_token(self.buffer,self.linea,self.columna,'comilla')
        self.estado = 0
        self.i -= 1
    
    def q11(self,caracter:str):
        self.agregar_token(self.buffer,self.linea,self.columna,'guion')
        self.estado = 0
        self.i -= 1
    
    def analizar(self, cadena):
        cadena = cadena + '$'
        self.listaErrores = []
        self.listaTokens = []
        self.i = 0
        while self.i<len(cadena):
            if self.estado==0:
                self.q0(cadena[self.i])
            elif self.estado == 1:
                self.q1(cadena[self.i])
            elif self.estado == 2:
                self.q2(cadena[self.i])
            elif self.estado == 3:
                self.q3(cadena[self.i])  
            elif self.estado == 4:
                self.q4(cadena[self.i])
            elif self.estado == 5:
                self.q5(cadena[self.i])
            elif self.estado == 6:
                self.q6(cadena[self.i])
            elif self.estado == 7:
                self.q7(cadena[self.i])
            elif self.estado == 8:
                self.q8(cadena[self.i])
            elif self.estado == 9:
                self.q9(cadena[self.i])
            elif self.estado == 10:
                self.q10(cadena[self.i])
            elif self.estado == 11:
                self.q11(cadena[self.i])
            self.i += 1    

    def imprimirTokens(self):
        '''Imprime una tabla con los tokens'''
        x = PrettyTable()
        x.field_names = ["Lexema","linea","columna","tipo"]
        for token in self.listaTokens:
            x.add_row([token.lexema, token.linea, token.columna,token.tipo])
        print(x)

    def imprimirErrores(self):
        '''Imprime una tabla con los errores'''
        x = PrettyTable()
        x.field_names = ["DEscripcion","linea","columna"]
        for error_ in self.listaErrores:
            x.add_row([error_.descripcion, error_.linea, error_.columna])
        print(x)   