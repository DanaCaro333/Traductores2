import AnalizadorLexico
import Pila


class Sintactico(object):
    def __init__(self) -> None:
        self.__pila = Pila.Pila()
        self.__continua = True
        self.__lexico = AnalizadorLexico.Lexico()
        self.__lexico.entrada("a+asd+kgf")
        self.__tabla = ["d2", "-1", "-1", "1"], ["-1", "-1", "r0", "-1"], ["-1",
                                                                           "d3", "-1", "-1"], ["d4", "-1", "-1", "-1"], ["-1", "-1", "r1", "-1"]

        self.__resultado = []

    def calis(self):
        self.__resultado = self.__lexico.Cadena()

    def to_num(self):
        if self.__resultado[0] == "id":
            return 0
        elif self.__resultado[0] == "+":
            return 1
        elif self.__resultado[0] == "$":
            return 2
        if self.__resultado[0] == "E":
            return 3

    def apilar(self):
        self.__pila.push("$")
        self.__pila.push("0")
        self.calis()
        while len(self.__resultado) > 0 and self.__continua:
            self.__pila.muestra()
            x = self.to_num()

            if self.__tabla[int(self.__pila.top())][x] != "-1":
                ans = self.__tabla[int(self.__pila.top())][x]
                i = 0
                self.__pila.push(self.__resultado[0])
                self.__resultado.pop(0)
                self.__pila.push(ans[len(ans)-1])
            else:
                print("ERROR")
                self.__continua = False
