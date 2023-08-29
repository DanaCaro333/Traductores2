import AnalizadorSintactico

prueba = AnalizadorSintactico.Lexico()
prueba.entrada("a+asd+kgf")

print("Resultado del analisis lexico\n\n")


print(prueba.__resultado)
