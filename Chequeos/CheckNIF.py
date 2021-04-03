def CheckNIF(dni):
    numeros = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    contador = 0

    if len(dni) == 9:
        for i in range(0,8):
            if dni[i] in numeros:
                contador += 1
            else:
                print("es letra")
        if dni[8].isupper():
            contador += 1
    else:
        return (print("Vuelva a intentarlo dni"))



    if contador == 9:
        return dni
    else:
        return False




#esValido = check("7101s0690".upper())
#print(esValido)
