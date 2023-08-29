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
        self.cadena = []
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
        self.simbolo += self.__c

    def __aceptacion(self):
        self.__ind = self.__ind - 1
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
            cad = "id"

        elif self.tipo == Type.PESOS:
            cad = "Fin de la entrada"

        elif self.tipo == Type.SUMA:
            cad = "+"

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
                elif self.__c == "+":
                    self.__sigEstado(3)
                else:
                    self.__continua = False
            elif self.__estado == 1:
                if self.__esLetra(self.__c) or self.__esDigito(self.__c):
                    self.__sigEstado(1)
                else:
                    self.__aceptacion()
            elif self.__estado == 3:
                self.__aceptacion()

        if self.__estado == 1:
            self.tipo = Type.IDENTIFICADOR
        elif self.__estado == 3:
            self.tipo = Type.SUMA
        elif self.__estado == 0:
            self.tipo = Type.PESOS
            self.simbolo = self.__c
        else:
            self.simbolo += self.__c
            self.tipo = Type.ERROR

        return self.tipo

    def terminado(self):
        return self.__ind >= len(self.__fuente)-1

    def Cadena(self):
        while(self.simbolo != "$"):
            self.sigSimbolo()
            if(self.simbolo != "$"):
                self.cadena.append(self.tipoAcad(self.tipo))
        return self.cadena
