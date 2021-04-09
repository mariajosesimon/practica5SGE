
from VENTAS import AddCliente

def RolVendedor(db):

    opcVend = -1
    while opcVend == -1 or opcVend < 6:
        print("\n ------------ VENTAS -----------------\n"
          "\n     1. Añadir Cliente "
          "\n     2. Crear presupuesto para venta"
          "\n     3. Facturar una venta."
          "\n     4. Grafica Importes/Vendedores"
          "\n     5. Cambiar contraseña OJO QUIZAS QUITAR"
          "\n     6. Salir\n"
          "\n -------ELIGE UNA OPCION: -----------\n")
#--------------******************************OJO CON EL WHILE ***************************************************

        try:
            opcVend = int(input())
        except:
            print("Dato no valido.")
    # ---------------------------opcVendion 1 - Añadir Cliente -------------------------------------------
        if (opcVend - 1) == 0:
            # vamos a --> VENTAS - AddCliente - funcion CrearCliente()
            AddCliente.CrearCliente(db)
            opcVend = -1
    # ---------------------------opcion 2 -  Crear presupuesto ---------------------------
        elif (opcVend - 1) == 1:
            # vamos a --> VENTAS -- AddPresupuestoVenta - funcion CrearPresupuestoVenta()
           # AddPresupuestoVenta.CrearPresupuestoVenta()
            opcVend = -1
    # ---------------------------opcion 3 -  Facturar un presupuesto--------------------------
        elif (opcVend - 1) == 2:
            # vamos a --> VENTAS -- FacturarVenta -- FacturarVenta()
          #  FacturarVenta.FacturarVenta()
            opcVend = -1
    # ---------------------------opcion 4 -  Grafico Ventas--------------------------
        elif (opcVend - 1) == 3:
            # vamos a --> VENTAS - GraficaVentas - GrafVentas()
          #  if ExisteFile.checkFileExistance('Archivos/facturasVentas.csv'):
           #     GraficaVentas.GrafVentas()

           # else:
           #     print("No hay facturas de ventas, no se mostrará nada.")


            opcVend = -1
      # ---------------------------opcion 5 -  Cambio contraseña--------------------------
        elif (opcVend - 1) == 4:
    # vamos a --> OPCIONESVENDEDOR - GraficaVentas - GrafVentas()
            #if ExisteFile.checkFileExistance('Archivos/facturasVentas.csv'):



            opcVend = -1
    #
