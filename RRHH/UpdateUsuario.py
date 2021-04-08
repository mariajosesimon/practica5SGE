'''En la modificacion de usuario debemos poder modificar alguno de los datos siguientes:
- fecha de baja
- activo
- email

REUTILIZACION DE FUNCIONES:
-> "Seleccion" ya que los ids de los usuarios pueden no ser correlativos (seguidos)
y necesito ver si está dentro del listado
-> "Validar email"


'''
from datetime import datetime

from Chequeos import Seleccion, ValidarEmail
from Chequeos.Seleccion import seleccion


def ModificarUSR(db):
    opcUpdateUSR = -1

    while opcUpdateUSR == -1 or opcUpdateUSR < 3:
        print("\n ------------ MODIFICAR USUARIO -----------------\n"
              "\n     1. Buscar todos los usuarios. "
              "\n     2. Buscar con filtro de Activo+departamento "
              "\n     3. Salir\n"
              "\n -------ELIGE UNA OPCION: -----------\n")

        try:
            opcUpdateUSR = int(input())
        except:
            print("Dato no valido.")

        # ---------------------------Mostrar todos los usuarios -------------------------------------------
        if (opcUpdateUSR - 1) == 0:
            # Muestro los usuarios y debo guardar el id en un listado.
            # con el listado podre escoger el usuario a modificar.
            consultaTodos = "SELECT `idUsuario`, `NombreUSR`,`ApellidosUSR`,`NIF`,`FechaAlta`,`FechaBaja`,`Activo`,`usuario`,`password`,`email`, `NombreDepartamento` FROM `usuarios`, departamentos where usuarios.idDepartamento = departamentos.idDepartamento"
            idsUSR = MostrarDatosUSR(db, consultaTodos, None)
            usuario = Seleccion.seleccion2(-1, idsUSR)
            UpdateUSR(usuario, db)
            opcUpdateUSR = 3


        # ---------------------------Crear filtro Activo + departamento ---------------------------
        elif (opcUpdateUSR - 1) == 1:

            # Mostrar los departamentos
            consultaDepat = "select * from departamentos"
            cursor = db.cursor()
            cursor.execute(consultaDepat)
            departamentos = cursor.fetchall()
            nDepart = 0

            print("ID -> DEPARTAMENTO:")

            for dep in departamentos:
                print(dep[0], " -> ", dep[1])
                nDepart = nDepart + 1

            departamentoID = seleccion(-1, departamentos)

            activo = -1
            while activo < 0 or activo > 2:
                print("Mostrar Usuarios Activos? Si = 1/ No = 0")

                try:
                    activo = int(input())
                except:
                    print("Dato no valido.")

            datos = (departamentoID, activo)
            consultaFiltro = "SELECT `idUsuario`,`NombreUSR`,`ApellidosUSR`,`NIF`,`FechaAlta`,`FechaBaja`,`Activo`,`usuario`,`password`,`email`, `NombreDepartamento` FROM `usuarios`, departamentos where usuarios.idDepartamento = departamentos.idDepartamento and departamentos.idDepartamento = %s  and usuarios.Activo = %s"
            idsUSR = MostrarDatosUSR(db, consultaFiltro, datos)
            usuario = Seleccion.seleccion2(-1, idsUSR)
            UpdateUSR(usuario, db)
            opcUpdateUSR = 3


def MostrarDatosUSR(db, consulta, datos):
    cursor = db.cursor()
    cursor.execute(consulta, datos)
    users = cursor.fetchall()
    guion = "-"
    id = "ID"
    nombre = "NOMBRE"
    apellidos = "APELLIDOS"
    nif = "NIF"
    fechaAlta = "FECHA ALTA"
    fechaBaja = "FECHA BAJA"
    ac = "ACTIVO"
    usuario = "USUARIO"
    contrasena = "CONTRASEÑA"
    email = "EMAIL"
    departamento = "DEPARTAMENTO"
    print("ELIGE EL USUARIO QUE DESEAS MODIFICAR: ")
    print(guion.rjust(152, "-"))
    print(
        "|{:^4}|{:^15}|{:^15}|{:^11}|{:^12}|{:^12}|{:^6}|{:^15}|{:^15}|{:^20}|{:^15}|".format(id, nombre,
                                                                                              apellidos, nif,
                                                                                              fechaAlta,
                                                                                              fechaBaja, ac,
                                                                                              usuario, contrasena,
                                                                                              email, departamento))

    print(guion.rjust(152, "-"))
    listaids = []

    for user in users:
        if (user[6] == 1):
            act = "SI"
        else:
            act = "NO"

        print(
            "|{:^4}|{:^15}|{:^15}|{:^11}|{:^12}|{:^12}|{:^6}|{:^15}|{:^15}|{:^20}|{:^15}|".format(user[0], user[1],
                                                                                                  user[2], user[3],
                                                                                                  str(user[4]),
                                                                                                  str(user[5]), act,
                                                                                                  user[7], user[8],
                                                                                                  str(user[9]),
                                                                                                  user[10]))
        listaids.append(user[0])

    print(guion.rjust(152, "-"))

    return listaids


def UpdateUSR(usuario, db):

    campo = None
    valor = None
    datoMod = -1
    cursor = db.cursor()

    while datoMod == -1 or datoMod < 4:
        print("\n ------------ MODIFICAR DATO -----------------\n"
              "\n     1. EMAIL. "
              "\n     2. FECHA DE BAJA "
              "\n     3. ACTIVO \n"
              "\n -------ELIGE UNA OPCION: -----------\n")

        try:
            datoMod = int(input())
        except:
            print("Dato no valido.")

        if (datoMod - 1) == 0:  # ------------EMAIL---------------
            email = None
            while (email == False or email == None):
                print("Email: ")
                email = ValidarEmail.Email(input())
            campo = "email"
            valor = email
            datoMod = 4
        elif (datoMod - 1) == 1:  # ------------FECHA DE BAJA---------------
            print("Fecha de baja (yyyy-mm-dd): ")
            while True:
                try:
                    fechaBaja = input()
                    datetime.strptime(fechaBaja, '%Y-%m-%d')
                    break
                except:
                    print("No ha introducido una fecha correcta. Vuelva a intentarlo: ")
            campo = "FechaBaja"
            valor = fechaBaja
            datoMod = 4

        elif (datoMod - 1) == 2:  # ------------ACTIVO------ ESTA OPCION NO FUNCIONA---------
            # si selecciona esta opcion simplemente lo cambiaremos de activo a no activo o viceversa sin interaccion con el usuario
            consulta = "select Activo from usuarios where idUsuario = %s"

            print(consulta)
            activoUSR = 9
            print("Activo -- usuario", activoUSR, usuario)

            activoUSR = cursor.execute(consulta, usuario)
            print("Activo ", activoUSR)
            printi("Activo type - ", type(activoUSR))
            if activoUSR == 1:
                valor = 0
            else:
                valor = 1
            campo = "Activo"
            datoMod = 4


    print("Valor", valor)
    datos = (campo, valor, usuario)
    actualizacion = "UPDATE usuarios SET %s = %s WHERE idUsuario = %s"

    #print(datos)

    cursor.execute(actualizacion, datos)
    db.commit()
