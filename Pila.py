import Epila


class Pila(object):
    def __init__(self) -> None:
        self.__lista: Epila = []

    def push(self, x: Epila):
        self.__lista.append(x)

    def pop(self):
        self.__lista.pop(len(self.__lista)-1)

    def top(self):
        return self.__lista[len(self.__lista)-1]

    def muestra(self):
        for x in self.__lista:
            if isinstance(x, Epila.T):
                print(getattr(x, "data"), end="")
            else:
                print(getattr(x, "type"), end="")
        print(" ")
