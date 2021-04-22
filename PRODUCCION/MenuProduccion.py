from PRODUCCION import OrdenProd

def RolProductor(db):

    opcProd = -1
    while opcProd == -1 or opcProd < 4:
        print("\n ------------ PRODUCCION -----------------\n"
          "\n     1. Añadir Orden "
          "\n     2. Listar productos utilizados para la producción"
          "\n     3. Grafico productos utilizados para la producción "
          "\n     4. Salir\n"
          "\n -------ELIGE UNA OPCION: -----------\n")

        try:
            opcProd = int(input())
        except:
            print("Dato no valido.")
    # ---------------------------opcVendion 1 - Añadir Orden produccion -------------------------------------------
        if (opcProd - 1) == 0:
            # vamos a --> OPCIONESPRODUCTOR - OrdenProd -- CrearOrdenProd()

            OrdenProd.CrearOrdenProd(db, "productoscreados")

            opcProd = -1
    # ---------------------------opcion 2 -  Listar productos utilizados para la produccion ---------------------------
       # elif (opcProd - 1) == 1:
            # vamos a --> OPCIONESPRODUCTOR -- GrafCantidadMPUtilizada - ListarMatPri()
            #Terminamos en este menu el listado-el printeado - porque utilizo ListarMatPri  en el grafico.

        #    opcProd = -1
    # ---------------------------opcion 3 -  Grafico productos utilizados para la produccion ---------------------------
      #  elif (opcProd - 1) == 2:
            # vamos a --> OPCIONESPRODUCTOR -- GrafCantidadMPUtilizada -- GrafMPUtilizada()
           # SolicitudPresupuesto.CrearPresupuesto()

      #      opcProd = -1
