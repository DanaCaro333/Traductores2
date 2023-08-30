import AnalizadorLexico
import Pila
import Epila


class Sintactico(object):
    def __init__(self, resultado) -> None:
        self.__pila = Pila.Pila()
        self.__continua = True
        self.__lexico = AnalizadorLexico.Lexico()
        self.__lexico.entrada("a+asd+kgf")
        self.__tabla = ["d2", "-1", "-1", "1"], ["-1", "-1", "r0", "-1"], ["-1",
                                                                           "d3", "-1", "-1"], ["d4", "-1", "-1", "-1"], ["-1", "-1", "r1", "-1"]

        self.__resultado = resultado

        self._reglas = []

        self.crearMatriz()

    def crearMatriz(self):
        with open("compilador.lr", "r") as file:
                for line in file:
                    renglon = []
                    for dato in line.split():
                        renglon.append(dato)
                    self._reglas.append(renglon)

    def apilar(self):
        self.__pila.push(Epila.T("$"))
        self.__pila.push(Epila.E("0"))
        while len(self.__resultado) > 0 and self.__continua:
            self.__pila.muestra()
            x = self.__resultado[0]

            if self.__tabla[int(getattr(self.__pila.top(), "dato"))][x] != "-1":

                ans = self.__tabla[int(getattr(self.__pila.top(), "dato"))][x]
                self.__pila.push(Epila.EP(self.__resultado[0]))
                self.__resultado.pop(0)
                self.__pila.push(Epila.EP(ans[len(ans)-1]))
            else:
                print(self.__resultado[0])
                self.__resultado.pop(0)
