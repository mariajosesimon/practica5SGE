'''
He creado dos funciones en este archivo.
La funcion "preguntar" simplemente cambia la opcion de mayusculas, minusculas, simbolos y numeros.
He tenido que poner la variable "escoge = 5" para inicializarla porque con el 0 entraba siempre en el bucle.
Tiene que devolver un boolean segun la contestación del usuario.

La funcion de "generadorPW" devuelve un listado de los parametros escogidos: booleanos + la longitud escogida.
'''


def preguntar(dato, cadena):
    escoge = 5
    while escoge == 5:
        print("Quieres que tenga", cadena, "la contraseña: s/n")
        dato = input().lower()
        if dato == "n":
            escoge = False
        elif dato == "s":
            escoge = True
    return escoge


def generadorPW():
    longitud = -1
    dato = "os"
    seguridadDicc = {
        "may": None,
        "min": None,
        "simbolos": None,
        "num": None
    }
    contador=0

    while longitud == -1:
        try:
            longitud = int(input("Longitud de la contraseña: "))
        except ValueError:
            print("La longitud dada no es valida. Escriba un numero mayor de -1.")

    opc = "J"

    for key in seguridadDicc.keys():
        while opc != "N" and opc != "Y":
            print("Quieres que tu contraseña tenga ", key, " (Y/N): ")
            opc = input().upper()
        if seguridadDicc["may"] == False and seguridadDicc["min"] == False and seguridadDicc["simbolos"] == False:
            opc = "S"
        if (opc == "N"):
            seguridadDicc[key]= False
            opc="K"
        elif (opc == "S" or contador <= longitud):
            seguridadDicc[key]= True
            contador = contador + 1
            opc="K"
        if contador == longitud:
            break


    for key in seguridadDicc.keys():
        if seguridadDicc[key]== None:
            seguridadDicc[key]= False


    return ([longitud, seguridadDicc["may"], seguridadDicc["min"], seguridadDicc["simbolos"], seguridadDicc["num"]])
