class Type:
    ERROR = -1
    IDENTIFICADOR = 0
    SUMA = 1
    MULT = 2
    PESOS = 3
    ENTERO = 4


class Lexico(object):
    def __init__(self, fuente) -> None:
        self.__fuente = fuente
        self.__ind = 0
        self.__continua = True
        self.__c = ''
        self.__estado = 0

        self.simbolo = ""
        self.tipo = 0

    def __sigCaracter(self):
        if self.terminado(self):
            return '$'
        else:
            return self.__fuente[self.__ind+1]

    def __sigEstado(self, estado):
        self.__sigEstado = estado
        self.simbolo += self.__c
        return

    def __aceptacion(self, estado):
        self.__sigEstado(self, estado)
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
        self.__ind = 0
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

        return cad

    def sigSimbolo(self):
        self.__estado = 0
        self.__continua = True
        self.simbolo = ""

        while(self.__continua):
            self.__c = self.__sigCaracter(self)

            if self.__estado == 0:
                if self.__c == '+' or self.__c == '-':
                    self.__aceptacion(self, 2)
                elif self.__c == '$':
                    self.__aceptacion(self, 3)

        if self.__estado == 2:
            self.tipo = Type.SUMA
        else:
            self.tipo = Type.ERROR

        return self.tipo

    def terminado(self):
        print(self.__fuente)
        return self.__ind >= self.__fuente.len()
