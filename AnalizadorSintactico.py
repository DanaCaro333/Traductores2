class Pila(object):
    def __init__(self) -> None:
        self.__lista = list

    def push(self, x):
        self.__lista.append(x)

    def pop(self):
        self.__lista.pop(len(self.__lista)-1)

    def top(self):
        return self.__lista[len(self.__lista)-1]

    def muestra(self):
        for _ in self.__lista:
            print(_)
        print("\n")
