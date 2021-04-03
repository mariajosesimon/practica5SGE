from RRHH import AddUsuario, UpdateUsuario


def RolRH(db):

    opcRH = -1
    while opcRH == -1 or opcRH < 3:
        print("\n ------------ RECURSOS HUMANOS -----------------\n"
          "\n     1. Añadir Usuario "
          "\n     2. Modificar Usuario "
          "\n     3. Salir\n"
          "\n -------ELIGE UNA OPCION: -----------\n")

        try:
            opcRH = int(input())
        except:
            print("Dato no valido.")
    # ---------------------------opcRHion 1 - Añadir Usuario -------------------------------------------
        if (opcRH - 1) == 0:
            # vamos a --> OPCIONESCOMPRADOR - AddProveedor - funcion CrearProveedor()
            AddUsuario.CrearUsuario(db)
            opcRH = -1
    # ---------------------------opcion 2 -  Modificar Usuario ---------------------------
        elif (opcRH - 1) == 1:
            # vamos a --> OPCIONESCOMPRADOR -- AddProducto - funcion CrearProducto()
            UpdateUsuario.ModificarUSR(db)
            opcRH = -1
