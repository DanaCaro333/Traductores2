import Token


class Type:
    ERROR = -1
    IDENTIFICADOR = 0
    ENTERO = 1
    REAL = 2
    CADENA = 3
    TIPO = 4
    SUMA = 5
    MULT = 6
    RELAC = 7
    OR = 8
    AND = 9
    NOT = 10
    IGUALDAD = 11
    PUNTO_Y_COMA = 12
    COMA = 13
    PARENTESIS_ABRIR = 14
    PARENTESIS_CERRAR = 15
    LLAVE_ABRIR = 16
    LLAVE_CERRAR = 17
    ASIGNACION = 18
    CONDICIONAL = 19
    BUCLE = 20
    RETURN = 21
    CONDICIONAL_ELSE = 22
    PESOS = 23


class Lexico(object):
    def __init__(self) -> None:
        self.__fuente = ""
        self.__ind = -1
        self.__continua = True
        self.__c = ''
        self.__estado = 0

        self.token = ""
        self.tipo = 0

    def __sigCaracter(self):
        if self.terminado():
            self.__ind = self.__ind + 1
            return '$'
        else:
            self.__ind = self.__ind + 1
            return self.__fuente[self.__ind]

    def __sigEstado(self, estado):
        self.__estado = estado
        self.token += self.__c

    def __aceptacion(self):
        self.__ind = self.__ind - 1
        self.__continua = False

    def __esLetra(self, c):
        return self.__c.isalpha() or self.__c == '_'

    def __esDigito(self, c):
        return self.__c.isdigit()

    def __esEspacio(self, c):
        return self.__c == ' ' or c == '\t' or c == '\n'

    def __retroceso(self):
        if self.__c != '$':
            self.__continua == False
        return

    def entrada(self, fuente):
        self.__ind = -1
        self.__fuente = fuente

    def tipoAcad(self, tipo):
        cad = ""

        if self.tipo == Type.IDENTIFICADOR:
            cad = "Identificador"

        elif self.tipo == Type.SUMA:
            cad = "Suma"

        elif self.tipo == Type.MULT:
            cad = "Multiplicacion"

        elif self.tipo == Type.PESOS:
            cad = "Fin de la entrada"

        elif self.tipo == Type.ENTERO:
            cad = "Entero"

        elif self.tipo == Type.REAL:
            cad = "Real"

        elif self.tipo == Type.TIPO:
            cad = "Tipo"

        elif self.tipo == Type.RELAC:
            cad = "Relacion"

        elif self.tipo == Type.OR:
            cad = "Compuerta OR"

        elif self.tipo == Type.AND:
            cad = "Compuerta AND"

        elif self.tipo == Type.NOT:
            cad = "Compuerta NOT"

        elif self.tipo == Type.IGUALDAD:
            cad = "Igualdad"

        elif self.tipo == Type.ASIGNACION:
            cad = "Asignacion"

        elif self.tipo == Type.PUNTO_Y_COMA:
            cad = "Punto y coma"

        elif self.tipo == Type.COMA:
            cad = "Coma"

        elif self.tipo == Type.PARENTESIS_ABRIR:
            cad = "Parentesis abrir"

        elif self.tipo == Type.PARENTESIS_CERRAR:
            cad = "Parentesis cerrar"

        elif self.tipo == Type.LLAVE_ABRIR:
            cad = "llave abrir"

        elif self.tipo == Type.LLAVE_CERRAR:
            cad = "llave cerrar"

        elif self.tipo == Type.CONDICIONAL:
            cad = "Condicional"

        elif self.tipo == Type.BUCLE:
            cad = "Bucle"

        elif self.tipo == Type.CONDICIONAL_ELSE:
            cad = "Condicional Else"

        elif self.tipo == Type.RETURN:
            cad = "Regresa"

        elif self.tipo == Type.ERROR:
            cad = "Error en el token"

        elif self.tipo == Type.CADENA:
            cad = "Cadena"

        return cad

    def sigtoken(self):
        self.__estado = 0
        self.__continua = True
        self.token = ""

        if(self.__esEspacio(self.__c)):
            while(self.__esEspacio(self.__c)):
                self.__c = self.__sigCaracter()
            self.__ind = self.__ind - 1

        while(self.__continua):
            self.__c = self.__sigCaracter()

            if self.__estado == 0:
                if self.__esLetra(self.__c):
                    self.__sigEstado(1)
                elif self.__esDigito(self.__c):
                    self.__sigEstado(3)
                elif self.__c == '"':
                    self.__sigEstado(7)
                else:
                    self.__sigEstado(5)

            elif self.__estado == 1:
                if self.__esLetra(self.__c):
                    self.__sigEstado(1)
                elif self.__esDigito(self.__c):
                    self.__sigEstado(2)
                else:
                    self.__aceptacion()

            elif self.__estado == 2:
                if self.__esLetra(self.__c) or self.__esDigito(self.__c):
                    self.__sigEstado(2)
                else:
                    self.__aceptacion()
            elif self.__estado == 3:
                if self.__esDigito(self.__c):
                    self.__sigEstado(3)
                elif self.__c == ".":
                    self.__sigEstado(4)
                else:
                    self.__aceptacion()
            elif self.__estado == 4:
                if self.__esDigito(self.__c):
                    self.__sigEstado(4)
                else:
                    self.__aceptacion()
            elif self.__estado == 5:
                if self.__esDigito(self.__c) == False and self.__esLetra(self.__c) and self.__esEspacio(self.__c):
                    self.__sigEstado(6)
                else:
                    self.__aceptacion()
            elif self.__estado == 6:
                self.__aceptacion()

            elif self.__estado == 7:
                if self.__c == '"':
                    self.__sigEstado(7)
                    self.__ind = self.__ind+2
                    self.__aceptacion()
                else:
                    self.__sigEstado(7)

        if self.token == "$":
            self.tipo = Type.PESOS
        elif self.__estado == 1:
            self.evaluatePalabra(self.token)
        elif self.__estado == 2:
            self.tipo = Type.IDENTIFICADOR
        elif self.__estado == 3:
            self.tipo = Type.ENTERO
        elif self.__estado == 4:
            self.tipo = Type.REAL
        elif self.__estado == 5 or self.__estado == 6:
            self.evaluateSignos(self.token)
        elif self.__estado == 7:
            self.tipo = Type.CADENA

        else:
            self.token += self.__c
            self.tipo = Type.ERROR

        return self.tipo

    def evaluatePalabra(self, token):
        if token == "if":
            self.tipo = Type.CONDICIONAL
        elif token == "while":
            self.tipo = Type.BUCLE
        elif token == "return":
            self.tipo = Type.RETURN
        elif token == "else":
            self.tipo = Type.CONDICIONAL_ELSE
        elif token == "int" or token == "float" or token == "void":
            self.tipo = Type.TIPO
        else:
            self.tipo = Type.IDENTIFICADOR

    def evaluateSignos(self, token):
        if token == "+" or token == "-":
            self.tipo = Type.SUMA
        elif token == "*" or token == "/":
            self.tipo = Type.MULT
        elif token == "<" or token == ">" or token == "<=" or token == ">=":
            self.tipo = Type.RELAC
        elif token == "||":
            self.tipo = Type.OR
        elif token == "&&":
            self.tipo = Type.AND
        elif token == "!":
            self.tipo = Type.NOT
        elif token == "=":
            self.tipo = Type.ASIGNACION
        elif token == "(":
            self.tipo = Type.PARENTESIS_ABRIR
        elif token == ")":
            self.tipo = Type.PARENTESIS_CERRAR
        elif token == "{":
            self.tipo = Type.LLAVE_ABRIR
        elif token == "}":
            self.tipo = Type.LLAVE_CERRAR
        elif token == ";":
            self.tipo = Type.PUNTO_Y_COMA
        elif token == ",":
            self.tipo = Type.COMA
        elif token == token == "==" or token == "!=":
            self.tipo = Type.IGUALDAD
        else:
            self.tipo = Type.ERROR

    def terminado(self):
        return self.__ind >= len(self.__fuente)-1

    def evaluate(self):
        entrada = []

        while(self.token != "$"):
            self.sigtoken()
            aux = Token.Token(self.tipo, self.token)
            entrada.append(aux)
            if(self.token != "$"):
                print(self.token+"\t\t"+self.tipoAcad(self.tipo)+"\n")
            else:
                print(self.token+"\t\t"+self.tipoAcad(self.tipo)+"\n")
        return entrada
