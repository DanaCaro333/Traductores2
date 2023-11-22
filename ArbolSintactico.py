class Nodo(object):
    def __init__(self) -> None:
        self.der = None
        


class R1(Nodo):
    def __init__(self, der) -> None:
        super().__init__()
        self.der = der


class R2(Nodo):
    def __init__(self) -> None:
        super().__init__()


class R3(Nodo):
    def __init__(self, izq, der) -> None:
        super().__init__()
        self.der = der
        self.izq = izq


class R4(Nodo):
    def __init__(self, der) -> None:
        super().__init__()
        self.der = der


class R5(Nodo):
    def __init__(self, der) -> None:
        super().__init__()
        self.der = der


class R6(Nodo):
    def __init__(self, tipo, identificador, der, simbolo) -> None:
        super().__init__()
        self.tipo = tipo
        self.identificador = identificador
        self.der = der
        self.simbolo = simbolo


class R7(Nodo):
    def __init__(self) -> None:
        super().__init__()


class R8(Nodo):
    def __init__(self, simbolo, identificador, der) -> None:
        super().__init__()
        self.identificador = identificador
        self.der = der
        self.simbolo = simbolo


class R9(Nodo):
    def __init__(self, tipo, identificador, par1, izq, par2, der) -> None:
        super().__init__()
        self.tipo = tipo
        self.identificador = identificador
        self.par1 = par1
        self.der = der
        self.par2 = par2
        self.izq = izq


class R10(Nodo):
    def __init__(self) -> None:
        super().__init__()


class R11(Nodo):
    def __init__(self, tipo, identificador, der) -> None:
        super().__init__()
        self.tipo = tipo
        self.identificador = identificador
        self.der = der


class R12(Nodo):
    def __init__(self) -> None:
        super().__init__()


class R13(Nodo):
    def __init__(self, simbolo, tipo, identificador, der) -> None:
        super().__init__()
        self.simbolo = simbolo
        self.tipo = tipo
        self.identificador = identificador
        self.der = der


class R14(Nodo):
    def __init__(self, simb1, der, simb2) -> None:
        super().__init__()
        self.simb1 = simb1
        self.der = der
        self.simb2 = simb2


class R15(Nodo):
    def __init__(self) -> None:
        super().__init__()


class R16(Nodo):
    def __init__(self, izq, der) -> None:
        super().__init__()
        self.der = der
        self.izq = izq


class R17(Nodo):
    def __init__(self, der) -> None:
        super().__init__()
        self.der = der


class R18(Nodo):
    def __init__(self, der) -> None:
        super().__init__()
        self.der = der


class R19(Nodo):
    def __init__(self) -> None:
        super().__init__()


class R20(Nodo):
    def __init__(self, izq, der) -> None:
        super().__init__()
        self.der = der
        self.izq = izq


class R21(Nodo):
    def __init__(self, identificador, simb1, der, simb2) -> None:
        super().__init__()
        self.identificador = identificador
        self.simb1 = simb1
        self.der = der
        self.simb2 = simb2


class R22(Nodo):
    def __init__(self, simb0, simb1, izq, simb2, der, otro) -> None:
        super().__init__()
        self.simb0 = simb0
        self.simb1 = simb1
        self.izq = izq
        self.simb2 = simb2
        self.der = der
        self.otro = otro


class R23(Nodo):
    def __init__(self, simb0, simb1, izq, simb2, der) -> None:
        super().__init__()
        self.simb0 = simb0
        self.simb1 = simb1
        self.izq = izq
        self.simb2 = simb2
        self.der = der


class R24(Nodo):
    def __init__(self, simbolo, der) -> None:
        super().__init__()
        self.simbolo = simbolo
        self.der = der


class R25(Nodo):
    def __init__(self, der, simbolo) -> None:
        super().__init__()
        self.der = der
        self.simbolo = simbolo


class R26(Nodo):
    def __init__(self) -> None:
        super().__init__()


class R27(Nodo):
    def __init__(self, simbolo, der) -> None:
        super().__init__()
        self.simbolo = simbolo
        self.der = der


class R28(Nodo):
    def __init__(self, simb1, der, simb2) -> None:
        super().__init__()
        self.simb1 = simb1
        self.der = der
        self.simb2 = simb2


class R29(Nodo):
    def __init__(self) -> None:
        super().__init__()


class R30(Nodo):
    def __init__(self, der) -> None:
        super().__init__()
        self.der = der


class R31(Nodo):
    def __init__(self) -> None:
        super().__init__()


class R32(Nodo):
    def __init__(self, izq, der) -> None:
        super().__init__()
        self.der = der
        self.izq = izq


class R33(Nodo):
    def __init__(self) -> None:
        super().__init__()


class R34(Nodo):
    def __init__(self, simbolo, izq, der) -> None:
        super().__init__()
        self.simbolo = simbolo
        self.izq = izq
        self.der = der


class R35(Nodo):
    def __init__(self, der) -> None:
        super().__init__()
        self.der = der


class R36(Nodo):
    def __init__(self, identificador) -> None:
        super().__init__()
        self.identificador = identificador


class R37(Nodo):
    def __init__(self, entero) -> None:
        super().__init__()
        self.entero = entero


class R38(Nodo):
    def __init__(self, real) -> None:
        super().__init__()
        self.real = real


class R39(Nodo):
    def __init__(self, cadena) -> None:
        super().__init__()
        self.cadena = cadena


class R40(Nodo):
    def __init__(self, identificador, simb1, der, simb2) -> None:
        super().__init__()
        self.identificador = identificador
        self.simb1 = simb1
        self.der = der
        self.simb2 = simb2


class R41(Nodo):
    def __init__(self, der) -> None:
        super().__init__()
        self.der = der


class R42(Nodo):
    def __init__(self, der) -> None:
        super().__init__()
        self.der = der


class R43(Nodo):
    def __init__(self, simb1, der, simb2) -> None:
        super().__init__()
        self.simb1 = simb1
        self.der = der
        self.simb2 = simb2


class R44(Nodo):
    def __init__(self, simb1, der) -> None:
        super().__init__()
        self.simb1 = simb1
        self.der = der


class R45(Nodo):
    def __init__(self, simb1, der) -> None:
        super().__init__()
        self.simb1 = simb1
        self.der = der


class R46(Nodo):
    def __init__(self, izq, simbolo, der) -> None:
        super().__init__()
        self.izq = izq
        self.simbolo = simbolo
        self.der = der


class R47(Nodo):
    def __init__(self, izq, simbolo, der) -> None:
        super().__init__()
        self.izq = izq
        self.simbolo = simbolo
        self.der = der


class R48(Nodo):
    def __init__(self, izq, simbolo, der) -> None:
        super().__init__()
        self.izq = izq
        self.simbolo = simbolo
        self.der = der


class R49(Nodo):
    def __init__(self, izq, simbolo, der) -> None:
        super().__init__()
        self.izq = izq
        self.simbolo = simbolo
        self.der = der


class R50(Nodo):
    def __init__(self, izq, simbolo, der) -> None:
        super().__init__()
        self.izq = izq
        self.simbolo = simbolo
        self.der = der


class R51(Nodo):
    def __init__(self, izq, simbolo, der) -> None:
        super().__init__()
        self.izq = izq
        self.simbolo = simbolo
        self.der = der


class R52(Nodo):
    def __init__(self, der) -> None:
        super().__init__()
        self.der = der


class Tipo(Nodo):
    def __init__(self, simbolo) -> None:
        self.simbolo = simbolo
        self.sig = None


class Expresion(Nodo):
    def __init__(self, simbolo, izq, der) -> None:
        self.der = der
        self.simbolo = simbolo
        self.izq = izq


class Identificador(Expresion):
    def __init__(self, simbolo, sig) -> None:
        self.simbolo = simbolo
        self.sig = sig


class DefVar(Nodo):
    def __init__(self, tipo, listaVar, sig) -> None:
        self.tipo = tipo
        self.listaVar = listaVar
        self.sig = sig


class Parametro(Nodo):
    def __init__(self, tipo, id, sig) -> None:
        self.tipo = tipo
        self.id = id
        self.sig = sig

    def __init__(self, sig) -> None:
        self.sig = sig


class DefFunc(Nodo):
    def __init__(self, tipo, id, parametro, bloqueFunc, sig) -> None:
        self.tipo = tipo
        self.id = id
        self.parametro = parametro
        self.bloqueFunc = bloqueFunc
        self.sig = sig


class Termino(Nodo):
    def __init__(self, termino) -> None:
        self.termino = termino


class Asignacion(Nodo):
    def __init__(self, id, expresion, sig) -> None:
        self.id = id
        self.expresion = expresion
        self.sig = sig


class Regresa(Nodo):
    def __init__(self, expresion, sig) -> None:
        self.expresion = expresion


class Entero(Expresion):
    def __init__(self, simbolo, sig) -> None:
        self.simbolo = simbolo


class Real(Expresion):
    def __init__(self, simbolo, sig) -> None:
        self.simbolo = simbolo


class Cadena(Expresion):
    def __init__(self, simbolo, sig) -> None:
        self.simbolo = simbolo


class Signo(Expresion):
    def __init__(self, simbolo, sig) -> None:
        self.simbolo = simbolo
        self.sig = sig
