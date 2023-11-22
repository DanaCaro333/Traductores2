import AnalizadorLexico
import Pila
import Epila
import ArbolSintactico


class Sintactico(object):

    def __init__(self, resultado) -> None:
        self.__pila = Pila.Pila()
        self.__continua = True
        self.__resultado = resultado
        self.__token_table = []
        self.__tabla = []
        self._tipoTemp = None
        self.crearMatriz()
        self.arbolS = ArbolSintactico.Nodo()

    class token(object):
        def __init__(self, tipo, nombre) -> None:
            self.tipo = tipo
            self.nombre = nombre

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
       # self.__pila.muestra()

        x = int(getattr(self.__resultado[0], "type"))
        y = int(getattr(self.__pila.top(), "type"))+54

        ans = int(self.__tabla[y][x])

        if ans > 0:
            aux = Epila.E(ans)
            self.__pila.push(Epila.T(
                getattr(self.__resultado[0], "type"), getattr(self.__resultado[0], "data"), aux))
            self.__pila.push(aux)
            if(self.__resultado[0].type == 4):
                self._tipoTemp = self.__resultado[0].data
            self.__resultado.pop(0)
        elif ans < 0:
            neutral = (ans * -1)-1
            if neutral > 0:
                nt = self.__tabla[neutral][2]
                print("------------" + nt + "------------")
                ans = self.reduccion(ans)
                self.__pila.push(Epila.E(ans))
            else:
                self.__continua = False
        else:
            print("ERROR")

    def reduccion(self, ans):
        neutral = (ans * -1)-1

        if neutral != 0:
            tipo = self.__tabla[neutral][2]

            auxData = []
            reduce = int(self.__tabla[neutral][1]) * 2

            while reduce > 0:
                if(isinstance(self.__pila.top(), Epila.T) or isinstance(self.__pila.top(), Epila.NT)):
                    auxData.append(self.__pila.top())
                self.__pila.pop()
                reduce = reduce - 1

            x = int(self.__tabla[neutral][0])
            y = int(getattr(self.__pila.top(), "type"))+54

            self.__pila.push(
                Epila.NT(tipo, self.createBranch(neutral, auxData)))
            ans = self.__tabla[y][x]

            return ans

    def createBranch(self, ans, auxData):
        if ans == 1:
            aux = ArbolSintactico.R1(auxData[0])
        elif ans == 2:
            aux = ArbolSintactico.R2()
        elif ans == 3:
            aux = ArbolSintactico.R3(auxData[1], auxData[0])
        elif ans == 4:
            aux = ArbolSintactico.R4(auxData[0])
        elif ans == 5:
            aux = ArbolSintactico.R5(auxData[0])
        elif ans == 6:
            self.addTokenTable(auxData[3].type, auxData[2].data)
            aux = ArbolSintactico.R6(
                auxData[3], auxData[2], auxData[1], auxData[0])

        elif ans == 7:
            aux = ArbolSintactico.R7()
        elif ans == 8:
            self.addTokenTable(self._tipoTemp, auxData[1].data)
            aux = ArbolSintactico.R8(auxData[2], auxData[1], auxData[0])
        elif ans == 9:
            self.addTokenTable(auxData[5].type, auxData[4].data)
            aux = ArbolSintactico.R9(
                auxData[5], auxData[4], auxData[3], auxData[2], auxData[1], auxData[0])
        elif ans == 10:
            aux = ArbolSintactico.R10()
        elif ans == 11:
            self.addTokenTable(auxData[2].type, auxData[1].data)
            aux = ArbolSintactico.R11(auxData[2], auxData[1], auxData[0])
        elif ans == 12:
            aux = ArbolSintactico.R12()
        elif ans == 13:
            self.addTokenTable(auxData[2].type, auxData[1].data)
            aux = ArbolSintactico.R13(
                auxData[3], auxData[2], auxData[1], auxData[0])
        elif ans == 14:
            aux = ArbolSintactico.R14(auxData[2], auxData[1], auxData[0])
        elif ans == 15:
            aux = ArbolSintactico.R15()
        elif ans == 16:
            aux = ArbolSintactico.R16(auxData[1], auxData[0])
        elif ans == 17:
            aux = ArbolSintactico.R17(auxData[0])
        elif ans == 18:
            aux = ArbolSintactico.R18(auxData[0])
        elif ans == 19:
            aux = ArbolSintactico.R19()
        elif ans == 20:
            aux = ArbolSintactico.R20(auxData[1], auxData[0])
        elif ans == 21:
            self.checkTokenTable(auxData[3].data)
            aux = ArbolSintactico.R21(
                auxData[3], auxData[2], auxData[1], auxData[0])
        elif ans == 22:
            aux = ArbolSintactico.R22(
                auxData[5], auxData[4], auxData[3], auxData[2], auxData[1], auxData[0])
        elif ans == 23:
            aux = ArbolSintactico.R23(
                auxData[4], auxData[3], auxData[2], auxData[1], auxData[0])
        elif ans == 24:
            aux = ArbolSintactico.R24(auxData[2], auxData[1], auxData[0])
        elif ans == 25:
            aux = ArbolSintactico.R25(auxData[1], auxData[0])
        elif ans == 26:
            aux = ArbolSintactico.R26()
        elif ans == 27:
            aux = ArbolSintactico.R27(auxData[1], auxData[0])
        elif ans == 28:
            aux = ArbolSintactico.R28(auxData[2], auxData[1], auxData[0])
        elif ans == 29:
            aux = ArbolSintactico.R29()
        elif ans == 30:
            aux = ArbolSintactico.R30(auxData[0])
        elif ans == 31:
            aux = ArbolSintactico.R31()
        elif ans == 32:
            aux = ArbolSintactico.R32(auxData[1], auxData[0])
        elif ans == 33:
            aux = ArbolSintactico.R33()
        elif ans == 34:
            aux = ArbolSintactico.R34(auxData[2], auxData[1], auxData[0])
        elif ans == 35:
            aux = ArbolSintactico.R35(auxData[0])
        elif ans == 36:
            self.checkTokenTable(auxData[0].data)
            aux = ArbolSintactico.R36(auxData[0])
        elif ans == 37:
            aux = ArbolSintactico.R37(auxData[0])
        elif ans == 38:
            aux = ArbolSintactico.R38(auxData[0])
        elif ans == 39:
            aux = ArbolSintactico.R39(auxData[0])
        elif ans == 40:
            self.checkTokenTable(auxData[3].data)
            aux = ArbolSintactico.R40(
                auxData[3], auxData[2], auxData[1], auxData[0])
        elif ans == 41:
            aux = ArbolSintactico.R41(auxData[0])
        elif ans == 42:
            aux = ArbolSintactico.R42(auxData[0])
        elif ans == 43:
            aux = ArbolSintactico.R43(auxData[2], auxData[1], auxData[0])
        elif ans == 44:
            aux = ArbolSintactico.R44(auxData[1], auxData[0])
        elif ans == 45:
            aux = ArbolSintactico.R45(auxData[1], auxData[0])
        elif ans == 46:
            aux = ArbolSintactico.R46(auxData[2], auxData[1], auxData[0])
        elif ans == 47:
            aux = ArbolSintactico.R47(auxData[2], auxData[1], auxData[0])
        elif ans == 48:
            aux = ArbolSintactico.R48(auxData[2], auxData[1], auxData[0])
        elif ans == 49:
            aux = ArbolSintactico.R49(auxData[2], auxData[1], auxData[0])
        elif ans == 50:
            aux = ArbolSintactico.R50(auxData[2], auxData[1], auxData[0])
        elif ans == 51:
            aux = ArbolSintactico.R51(auxData[2], auxData[1], auxData[0])
        elif ans == 52:
            aux = ArbolSintactico.R52(auxData[0])

        return aux

    def addTokenTable(self, tipo, name):
        i = 0
        while i < len(self.__token_table):
            if name == self.__token_table[i].nombre:
                print("ERROR la variable YA se encuentra declarada")
                return False
            i = i + 1
        aux = self.token(tipo, name)
        self.__token_table.append(aux)

    def checkTokenTable(self, name):
        i = 0
        while i < len(self.__token_table):
            if name == self.__token_table[i].nombre:
                return True
            i = i + 1
        print("ERROR la variable no se encuentra declarada")
