import pymysql
from MenuLogin import MenuLogin
from LOGIN import Logon, CambiarPass
from RRHH import MenuRH
from VENTAS import MenuVendedor
from COMPRAS import MenuComprador
from PRODUCCION import MenuProduccion

#CREAMOS LA CONEXION
db = pymysql.connect(host="127.0.0.1", user="root", db="mibd", port=3306)

opc = -1

while opc == -1 or opc < 4:

    MenuLogin()

    try:
        opc = int(input())
    except:
        print("Dato no valido.")


    # ---------------------------opcion 1 - logarse-------------------------------------------
    if (opc - 1) == 0:
        # vamos a --> LOGIN.Logon.logarse()

        resuelve = Logon.logarse(db)

        if resuelve == 1: # ------------------RRHH--------  #ir al menu de RRHH------------
            MenuRH.RolRH(db)

        elif resuelve == 2:# ------------------Compras--------------------
            MenuComprador.RolComprador(db)

        elif resuelve == 3:  # ------------------Ventas--------------------
            MenuVendedor.RolVendedor(db)

        elif resuelve == 4:
            MenuProduccion.RolProductor(db)
        #elif resuelve == 4: # ------------------Producción--------------------
            #menuproducción.
        else:
            print("Error de acceso. \n")


    # ---------------------------opcion 2 - Cambiar contraseña. ---------------------------
    elif (opc - 1) == 1:
        # vamos a --> LOGIN.RegistroUSR.registro()
        #  print(RegistroUSR.registro())
        CambiarPass.cambio(db)
        opc = -1
    elif (opc -1) == 2:
        db.close()
        break

