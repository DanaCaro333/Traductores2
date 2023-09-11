class Nodo(object):
    def __init__(self) -> None:
        self.simbolo = ""
        self.sig = Nodo()


class Tipo(Nodo):
    def __init__(self, simbolo) -> None:
        super().__init__()
        self.simbolo = simbolo
        self.sig = None


class Expresion(Nodo):
    def __init__(self) -> None:
        super().__init__()
        izq = Expresion()
        der = Expresion()


class Identificador(Expresion):
    def __init__(self, simbolo, sig) -> None:
        super().__init__()
        self.simbolo = simbolo
        self.sig = sig


class DefVar(Nodo):
    def __init__(self, tipo, listaVar, sig) -> None:
        super().__init__()
        self.tipo = tipo
        self.listaVar = listaVar
        self.sig = sig


class Parametro(Nodo):
    def __init__(self, tipo, id, sig) -> None:
        super().__init__()
        self.tipo = tipo
        self.id = id
        self.sig = sig


class DefFunc(Nodo):
    def __init__(self, tipo, id, parametro, bloqueFunc, sig) -> None:
        super().__init__()
        self.tipo = tipo
        self.id = id
        self.parametro = parametro
        self.bloqueFunc = bloqueFunc
        self.sig = sig


class Asignacion(Nodo):
    def __init__(self, id, expresion, sig) -> None:
        super().__init__()
        self.id = id
        self.expresion = expresion
        self.sig = sig


class Regresa(Nodo):
    def __init__(self, expresion, sig) -> None:
        super().__init__()
        self.expresion = expresion
        self.sig = sig


class Entero(Expresion):
    def __init__(self, simbolo, sig) -> None:
        super().__init__()
        self.simbolo = simbolo
        self.sig = sig


class Real(Expresion):
    def __init__(self, simbolo, sig) -> None:
        super().__init__()
        self.simbolo = simbolo
        self.sig = sig


class Cadena(Expresion):
    def __init__(self, simbolo, sig) -> None:
        super().__init__()
        self.simbolo = simbolo
        self.sig = sig


class Signo(Expresion):
    def __init__(self, simbolo, sig) -> None:
        super().__init__()
        self.simbolo = simbolo
        self.sig = sig


class Mult(Expresion):
    def __init__(self, simbolo, izq, der) -> None:
        super().__init__()
        self.der = der
        self.simbolo = simbolo
        self.izq = izq
        self.sig = None


class Sumayyy(Expresion):
    def __init__(self, simbolo, izq, der) -> None:
        super().__init__()
        self.der = der
        self.simbolo = simbolo
        self.izq = izq
        self.sig = None
