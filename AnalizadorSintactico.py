import AnalizadorLexico
import Pila
import Epila


class Sintactico(object):
    def __init__(self, resultado) -> None:
        self.__pila = Pila.Pila()
        self.__continua = True
        self.__lexico = AnalizadorLexico.Lexico()
        self.__lexico.entrada("a+asd+kgf")
        self.__resultado = resultado
        self.__tabla = []
        self.crearMatriz()

    def crearMatriz(self):
        with open("compilador.lr", "r") as file:
            for line in file:
                renglon = []
                for dato in line.split():
                    renglon.append(dato)
                self.__tabla .append(renglon)

    def apilar(self):
        self.__pila.push(Epila.T("$"))
        self.__pila.push(Epila.E("0"))
        while len(self.__resultado) > 0 and self.__continua:
            self.__pila.muestra()
            x = self.__resultado[0]

            y = int(getattr(self.__pila.top(), "dato"))+54

            ans = self.__tabla[y][x]

            if int(ans) > 0:
                self.__pila.push(Epila.EP(ans))
                self.__resultado.pop(0)
            elif int(ans) < 0:
                self.__pila.push(Epila.EP(self.reduccion(int(ans))))
            else:
                print("ERROR")

    def reduccion(self, ans):
        neutral = (ans * -1)-1
        index = int(self.__tabla[neutral][0])

        if neutral != 0:
            reduce = int(self.__tabla[neutral][1])

            while reduce > 0:
                self.__pila.pop()
                reduce = reduce - 1

            x = index
            y = int(getattr(self.__pila.top(), "dato"))+54

            ans = self.__tabla[y][x]

            return ans
        self.__continua = False
