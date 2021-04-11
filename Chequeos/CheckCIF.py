def CheckCIF(cif):
    numeros = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    contador = 0

    if cif[0].isupper():
        contador += 1
    else:
        return False

    if(len(cif) == 9):
        for i in range(1, 9):
            if cif[i] in numeros:
                contador += 1
            else:
                return False
    else:
        return False

    if contador == 9:
        return cif
    else:
        return False




#esValido = check("7101s0690".upper())
#print(esValido)
