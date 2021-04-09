def CheckTelefono(telf):

    numeros = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    contador = 0

    if len(telf) == 9 :
        for i in range(0, len(telf)):
            if telf[i] in numeros:
                contador += 1
            else:
                return False
    else:
        return False

    if contador == 9:
        return telf
    else:
        return False
