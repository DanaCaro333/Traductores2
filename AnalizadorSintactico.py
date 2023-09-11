import AnalizadorLexico
import Pila
import Epila
import ArbolSintactico

class Sintactico(object):
    def __init__(self, resultado) -> None:
        self.__pila = Pila.Pila()
        self.__continua = True
        self.__lexico = AnalizadorLexico.Lexico()
        self.__lexico.entrada("a+asd+kgf")
        self.__resultado = resultado
        self.__tabla = []
        self.crearMatriz()
        self.arbolS = ArbolSintactico.Nodo()

    def crearMatriz(self):
        with open("compilador.lr", "r") as file:
            for line in file:
                renglon = []
                for dato in line.split():
                    renglon.append(dato)
                self.__tabla .append(renglon)

    def analiza(self):
        self.__pila.push(Epila.T("$"))
        self.__pila.push(Epila.E("0"))

        while len(self.__resultado) > 0 and self.__continua:
            self.__pila.muestra()
            x = int(getattr(self.__resultado[0], "type"))
            y = int(getattr(self.__pila.top(), "dato"))+54

            ans = int(self.__tabla[y][x])

            if ans > 0:
                self.__pila.push(Epila.T(ans))
                self.__resultado.pop(0)
            elif ans < 0:
                neutral = (ans * -1)-1
                if neutral > 0:
                    nt = self.__tabla[neutral][2]
                    print("------------" + nt + "------------")
                self.__pila.push(Epila.NT(self.reduccion(ans)))
            else:
                print("ERROR")

    def reduccion(self, ans):
        neutral = (ans * -1)-1
        tipo = self.__tabla[neutral][2]
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
    
    def crearNodo(self, tipo):
        if tipo == 1