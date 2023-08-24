class Type:
    ERROR = -1
    IDENTIFICADOR = 0
    SUMA = 1
    MULT = 2
    PESOS = 3
    ENTERO = 4
    REAL = 5


class Lexico(object):
    def __init__(self) -> None:
        self.__fuente = ""
        self.__ind = -1
        self.__continua = True
        self.__c = ''
        self.__estado = 0

        self.simbolo = ""
        self.tipo = 0

    def __sigCaracter(self):
        if self.terminado():
            return '$'
        else:
            self.__ind = self.__ind + 1
            return self.__fuente[self.__ind]

    def __sigEstado(self, estado):
        self.__estado = estado
        self.simbolo += self.__c

    def __aceptacion(self, estado):
        self.__sigEstado(estado)
        self.__continua = False

    def __esLetra(self, c):
        return self.__c.isalpha() or self.__c == '_'

    def __esDigito(self, c):
        return self.__c.isdigit()

    def __esEspacio(self, c):
        return self.__c == ' ' or c == '\t'

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

        elif self.tipo == Type.ERROR:
            cad = "Error en el token"

        return cad

    def sigSimbolo(self):
        self.__estado = 0
        self.__continua = True
        self.simbolo = ""

        while(self.__continua):
            self.__c = self.__sigCaracter()

            if self.__estado == 0:
                if self.__esLetra(self.__c):
                    self.__sigEstado(1)
                elif self.__esDigito(self.__c):
                    self.__sigEstado(3)
                else:
                    self.__continua = False
            elif self.__estado == 1:
                if self.__esLetra(self.__c) or self.__esDigito(self.__c):
                    self.__sigEstado(1)
                elif self.__c == "*":
                    self.__aceptacion(2)
                else:
                    self.__continua = False
            elif self.__estado == 3:
                if self.__esDigito(self.__c):
                    self.__sigEstado(3)
                elif self.__c == ".":
                    self.__sigEstado(4)
                else:
                    self.__continua = False
            elif self.__estado == 4:
                if self.__esDigito(self.__c):
                    self.__sigEstado(4)
                elif self.__c == "+":
                    self.__aceptacion(5)
                else:
                    self.__continua = False

        if self.__estado == 5:
            self.tipo = Type.REAL
        elif self.__estado == 2:
            self.tipo = Type.IDENTIFICADOR
        elif self.__estado == 0:
            self.tipo = Type.PESOS
            self.simbolo = self.__c
        else:
            self.simbolo += self.__c
            self.tipo = Type.ERROR

        return self.tipo

    def terminado(self):
        return self.__ind >= len(self.__fuente)-1
