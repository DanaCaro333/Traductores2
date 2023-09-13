import ArbolSintactico


class EP(object):
    def __init__(self, type) -> None:
        self.type = type
        self.nodo = None


class NT(EP):
    pass


class T(EP):
    def __init__(self, type, data) -> None:
        self.data = data
        super().__init__(type)

        if type == 0:
            self.nodo = ArbolSintactico.Identificador(data, None)
        elif type == 1:
            self.nodo = ArbolSintactico.Entero(data, None)
        elif type == 2:
            self.nodo = ArbolSintactico.Real(data, None)
        elif type == 3:
            self.nodo = ArbolSintactico.Cadena(data, None)
        elif type == 4:
            self.nodo = ArbolSintactico.Tipo(data)
        elif type == 5:
            self.nodo = ArbolSintactico.Suma(data, None, None)
        elif type == 6:
            self.nodo = ArbolSintactico.Mult(data, None, None)
        elif type in range(7, 18):
            self.nodo = ArbolSintactico.Signo(data, None)
        else:
            self.nodo = ArbolSintactico.Tipo(data)


class E(EP):
    pass
