import csv

from Chequeos import ValidarEmail
from Chequeos import CheckTelf
from Chequeos import CheckNIF


def CrearCliente(db):
    nombre = None
    apellidos = None
    ciudad = None
    telefono = None
    nif = None
    email = None

    print("Datos para crear nuevo cliente.")

    while nombre == None or nombre == "":
        print("Nombre cliente: ")
        nombre = input().title()
    while apellidos == None or apellidos == "":
        print("Apellidos: ")
        apellidos = input().title()
    while ciudad == None or nombre == "":
        print("Ciudad: ")
        ciudad = input().title()
    while telefono == None or telefono == "" or telefono == False:
        print("Telefono: ")
        telefono = CheckTelf.CheckTelefono(input())
    while nif == None or nif == "" or nif == False:
        print("Nif ( 8 digitos +  letra): ")
        nif = CheckNIF.CheckNIF(input().upper())
    while (email == False or email == None):
        print("Email: ")
        email = ValidarEmail.Email(input())

    datos = (nombre, apellidos, ciudad, telefono, nif, email)
    insertarCliente = "INSERT INTO CLIENTES( Nombre, Apellidos, Ciudad, Telefono, NIF, Email) VALUES (%s, %s, %s , %s, %s, %s)"
    cursor = db.cursor()
    cursor.execute(insertarCliente, datos)
    print("Se ha añadido el cliente a la base de datos.")

    db.commit()
