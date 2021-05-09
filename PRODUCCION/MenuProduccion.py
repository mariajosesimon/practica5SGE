from PRODUCCION import OrdenProd, ProduccionAnio

def RolProductor(db):

    opcProd = -1
    while opcProd == -1 or opcProd < 3:
        print("\n ------------ PRODUCCION -----------------\n"
          "\n     1. Añadir Orden "
          "\n     2. Grafico productos utilizados para la producción"
          "\n     3. Salir\n"
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
    # ---------------------------opcion 2 -  Grafico productos utilizados para la produccion ---------------------------
        elif (opcProd - 1) == 1:

            ProduccionAnio.produccionAnual(db)

            opcProd = -1
