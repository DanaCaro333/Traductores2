import AnalizadorLexico
import AnalizadorSintactico

prueba = AnalizadorLexico.Lexico()
prueba.entrada("a23hola 23.54+3+1 while ifif 435 kkola ( interf    ")

print("Resultado del analisis lexico\n\n")

entrada = []

while(prueba.token != "$"):
    prueba.sigtoken()
    entrada.append(prueba.tipo)
    if(prueba.token != "$"):
        print(prueba.token+"\t\t"+prueba.tipoAcad(prueba.tipo)+"\n")
    else:
        print(prueba.token+"\t\t"+prueba.tipoAcad(prueba.tipo)+"\n")
        print(prueba.tipoAcad(prueba.tipo)+"\n")

sintactico = AnalizadorSintactico.Sintactico(entrada)
sintactico.apilar()

