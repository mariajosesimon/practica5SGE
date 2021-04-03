'''crear la contraseña y va chequeando que cumple las condiciones'''
import string


def Comprobar(pw, datoComprobar):
    devuelve = False
    for i in pw:
        for letra in range(len(datoComprobar)):
            if i == datoComprobar[letra]:
                devuelve = True
    return devuelve


def TuPW(listaParametros):
    min = string.ascii_lowercase
    may = string.ascii_uppercase
    simb = string.punctuation
    digitos = string.digits

    pw = input("Escribe la contraseña: ")

    while (listaParametros[0] != len(pw) or
           listaParametros[1] != Comprobar(pw, may) or
           listaParametros[2] != Comprobar(pw, min) or
           listaParametros[3] != Comprobar(pw, simb) or
           listaParametros[4] != Comprobar(pw, digitos)):
        print("La contraseña escrita no es valida. Vuelve a intentarlo")
        pw = input("Escribe la contraseña: ")

    return pw
