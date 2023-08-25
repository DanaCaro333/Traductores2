import AnalizadorLexico

prueba = AnalizadorLexico.Lexico()
prueba.entrada("a23hola 23.54 while ifif 435 kkola ( )")

print("Resultado del analisis lexico\n\n")

while(prueba.token != "$"):
    prueba.sigtoken()
    if(prueba.token != "$"):
        print(prueba.token+"\t\t"+prueba.tipoAcad(prueba.tipo)+"\n")
    else:
        print(prueba.tipoAcad(prueba.tipo)+"\n")
