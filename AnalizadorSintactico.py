import AnalizadorLexico
import Pila
import Epila
#import ArbolSintactico


class Sintactico(object):
    def __init__(self, resultado) -> None:
        self.__pila = Pila.Pila()
        self.__continua = True
        self.__lexico = AnalizadorLexico.Lexico()
        self.__lexico.entrada("a+asd+kgf")
        self.__resultado = resultado
        self.__tabla = []
        self.crearMatriz()
        #self.arbolS = ArbolSintactico.Nodo()

    def crearMatriz(self):
        with open("compilador.lr", "r") as file:
            for line in file:
                renglon = []
                for dato in line.split():
                    renglon.append(dato)
                self.__tabla .append(renglon)

    def analiza(self):
        aux = Epila.E("0")
        self.__pila.push(Epila.T("$", "$", aux))
        self.__pila.push(aux)

        while len(self.__resultado) > 0 and self.__continua:
            self.analisisRecursivo()

    def analisisRecursivo(self):
        self.__pila.muestra()

        x = int(getattr(self.__resultado[0], "type"))
        y = int(getattr(self.__pila.top(), "type"))+54

        ans = int(self.__tabla[y][x])

        if ans > 0:
            aux = Epila.E(ans)
            self.__pila.push(Epila.T(
                getattr(self.__resultado[0], "type"), getattr(self.__resultado[0], "data"), aux))
            self.__pila.push(aux)
            self.__resultado.pop(0)
        elif ans < 0:
            neutral = (ans * -1)-1
            if neutral > 0:
                nt = self.__tabla[neutral][2]
                print("------------" + nt + "------------")
            self.__pila.push(Epila.E(self.reduccion(ans)))
        else:
            print("ERROR")

    def reduccion(self, ans):
        neutral = (ans * -1)-1

        if neutral != 0:
            tipo = self.__tabla[neutral][2]

            aux = Epila.NT(tipo)
            reduce = int(self.__tabla[neutral][1]) * 2

            while reduce > 0:
                aux.nodo.__setattr__("sig", aux.nodo.sig)
                self.__pila.pop()
                reduce = reduce - 1

            x = int(self.__tabla[neutral][0])
            y = int(getattr(self.__pila.top(), "type"))+54

            ans = self.__tabla[y][x]

            self.__pila.push(Epila.NT(tipo))
            return ans
        self.__continua = False

    def crearNodo(self, tipo):
        if tipo == "Parametros":
            return
