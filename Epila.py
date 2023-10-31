import ArbolSintactico


class EP(object):
    def __init__(self, type) -> None:
        self.type = type
        self.nodo = ArbolSintactico.Nodo()


class NT(EP):
    pass

class T(EP):
    def __init__(self, type, data, sig) -> None:
        self.data = data
        super().__init__(type)

        if type == 0:
            self.nodo = ArbolSintactico.Identificador(data, sig)
        elif type == 1:
            self.nodo = ArbolSintactico.Entero(data, sig)
        elif type == 2:
            self.nodo = ArbolSintactico.Real(data, sig)
        elif type == 3:
            self.nodo = ArbolSintactico.Cadena(data, sig)
        elif type == 4:
            self.nodo = ArbolSintactico.Tipo(data)
        elif type in range(7, 18):
            self.nodo = ArbolSintactico.Signo(data, sig)
        else:
            self.nodo = ArbolSintactico.Tipo(data)


class E(EP):
    pass
