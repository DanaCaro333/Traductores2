import AnalizadorLexico
import AnalizadorSintactico

prueba = AnalizadorLexico.Lexico()
prueba.entrada(open("prueba.txt").read())

print("Resultado del analisis lexico\n\n")

entrada = prueba.evaluate()
sintactico = AnalizadorSintactico.Sintactico(entrada)
sintactico.analiza()
