'''Funcion para dar de alta usuarios.
Desde el Departamento de RRHH se encargan de dar de alta los usuarios con todos los datos.
Incluido usuario y contraseña.
FUNCIONES REUTILIZADAS DE OTROS EJERCICIOS:
- Chequear el NIF
- Validar email
- funcion "seleccion" en la seleccion del departamento.
(envio de un dato int, + listado, y el nº que se escoja debe estar dentro del rango del listado)

CONSULTAS A LA BASE DE DATOS:
- Hacemos una select para saber los departamentos disponibles.
'''
import hashlib

from datetime import datetime
import pymysql

from Chequeos import CheckNIF, ValidarEmail, Seleccion



def CrearUsuario(db):
    nombre = None
    apellidos = None
    nif = None
    fechaAlta = None
    departamentoID = None
    usuario = None
    contrasena = None
    email = None


    print("Datos para crear nuevo usuario.")

    while nombre == None or nombre == "":
        print("Nombre trabajador: ")
        nombre = input().title()
    while apellidos == None or apellidos == "":
        print("Apellidos: ")
        apellidos = input().title()
    while nif == None or nif == "" or nif == False:
        print("Nif ( 8 digitos +  letra): ")
        nif = CheckNIF.CheckNIF(input().upper())
    while (email == False or email == None):
        print("Email: ")
        email = ValidarEmail.Email(input())

    print("Fecha de alta (yyyy-mm-dd): ")
    while True:
        try:
            fechaAlta = input()
            datetime.strptime(fechaAlta, '%Y-%m-%d')
            break
        except:
            print("No ha introducido una fecha correcta. Vuelva a intentarlo: ")

    activo = -1
    while activo < 0 or activo > 2:
        print("Usuario Activo? Si = 1/ No = 0")

        try:
            activo = int(input())
        except:
            print("Dato no valido.")


    consultaDepat = "select * from departamentos"
    cursor = db.cursor()
    cursor.execute(consultaDepat)
    departamentos = cursor.fetchall()
    nDepart = 0

    for dep in departamentos:
        print(dep[0], " -> ", dep[1])
        nDepart = nDepart + 1

    departamentoID = Seleccion.seleccion(-1, departamentos)

    while usuario == None or usuario == "":
        print("Nombre usuario: ")
        usuario = input().title()
    while contrasena == None or contrasena == "":
        print("Contraseña: ")
        contrasena = input().title()

    #codificar pass
   # passw = hashlib.sha256(contrasena.encode())
    

    datos = (nombre, apellidos, nif, fechaAlta, activo, departamentoID, usuario, contrasena, email)
    insertarUSR = "INSERT INTO usuarios( NombreUSR, ApellidosUSR, NIF, FechaAlta, Activo, idDepartamento, usuario, password, email) VALUES (%s, %s, %s , %s, %s, %s, %s, %s, %s)"

    cursor.execute(insertarUSR, datos)

    db.commit()
