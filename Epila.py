class EP(object):
    def __init__(self, dato) -> None:
        self.dato = dato
        self.nodo = None

class NT(EP):
    pass
class T(EP):
    pass
class E(EP):
    pass