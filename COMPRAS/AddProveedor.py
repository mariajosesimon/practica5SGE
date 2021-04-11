
from Chequeos import ValidarEmail
from Chequeos import CheckTelf
from Chequeos import CheckCIF


def CrearProveedor(db):
    nombre = None
    ciudad = None
    telefono = None
    cif = None
    email = None

    print("Datos para crear nuevo proveedor.")

    while nombre == None or nombre == "":
        print("Nombre proveedor: ")
        nombre = input().title()
    while ciudad == None or nombre == "":
        print("Ciudad: ")
        ciudad = input().title()
    while telefono == None or telefono == "" or telefono == False:
        print("Telefono: ")
        telefono = CheckTelf.CheckTelefono(input())
    while cif == None or cif == "" or cif == False:
        print("Cif (empieza por letra + 8 digitos): ")
        cif = CheckCIF.CheckCIF(input().upper())
    while (email == False or email == None):
        print("Email: ")
        email = ValidarEmail.Email(input())

    datos = (nombre, ciudad, telefono, cif, email)
    insertarProveedor = "INSERT INTO proveedores( Nombre,  Ciudad, Telefono, CIF, Email) VALUES (%s, %s , %s, %s, %s)"
    cursor = db.cursor()
    cursor.execute(insertarProveedor, datos)
    print("Se ha añadido el proveedor a la base de datos.")

    db.commit()

    print("Se ha creado el proveedor.")
