import AnalizadorLexico

prueba = AnalizadorLexico.Lexico()
prueba.entrada("a23*2.0+234*")

print("Resultado del analisis lexico\n\n")

while(prueba.simbolo != "$"):
    prueba.sigSimbolo()
    if(prueba.simbolo != "$"):
        print(prueba.simbolo+"\t\t"+prueba.tipoAcad(prueba.tipo)+"\n")
    else:
        print(prueba.tipoAcad(prueba.tipo)+"\n")
