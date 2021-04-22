from COMPRAS import AddProveedor, AddProducto, SolicitudPresupuesto, UpdatePresupuesto, GraficoCompras, EliminarPresupuesto, FacturarCompra
from LISTADOS import ListarPresupuestos


def RolComprador(db):

    opcCom = -1
    while opcCom == -1 or opcCom < 9:
        print("\n ------------ COMPRAS -----------------\n"
          "\n     1. Añadir Proveedor "
          "\n     2. Añadir Producto "
          "\n     3. Solicitud de presupuesto de compra"
          "\n     4. Listar presupuestos"
          "\n     5. Modificar un presupuesto"
          "\n     6. Eliminar presupuesto "
          "\n     7. Facturar un presupuesto "
          "\n     8. Producto en stock "
          "\n     9. Salir\n"
          "\n -------ELIGE UNA OPCION: -----------\n")

        try:
            opcCom = int(input())
        except:
            print("Dato no valido.")
    # ---------------------------opcComion 1 - Añadir Proveedor -------------------------------------------
        if (opcCom - 1) == 0:
            # vamos a --> OPCIONESCOMPRADOR - AddProveedor - funcion CrearProveedor()
            AddProveedor.CrearProveedor(db)
            opcCom = -1
    # ---------------------------opcion 2 -  Añadir Producto ---------------------------
        elif (opcCom - 1) == 1:
            # vamos a --> OPCIONESCOMPRADOR -- AddProducto - funcion CrearProducto()

            AddProducto.CrearProducto(db, 'productoscomprados')
            opcCom = -1
    # ---------------------------opcion 3 -  Solicitud de presupuesto---------------------------
        elif (opcCom - 1) == 2:
            # vamos a --> OPCIONESCOMPRADOR -- SolicitudPresupuesto -- CrearPresupuesto()
            SolicitudPresupuesto.CrearPresupuestoCompra(db)
            opcCom = -1
    # ---------------------------opcion 4 -  Listar presupuestos de un comprador---------------------------
        elif (opcCom - 1) == 3:
            # vamos a --> LISTADOS - ListarPresupuestos - listarPresupuesto()
            ListarPresupuestos.listarPresupuestos(db, "compras")
            opcCom = -1
    # ---------------------------opcion 5 -  Modificar presupuesto---------------------------
        elif (opcCom - 1) == 4:
            # vamos a --> OPCIONESCOMPRADOR - FacturarPresupuesto - FacturarPep()
            UpdatePresupuesto.updatePres(db)
            opcCom = -1
     # ---------------------------opcion 6 -  Eliminar presupuesto---------------------------
        elif (opcCom - 1) == 5:
            # vamos a --> OPCIONESCOMPRADOR - GraficoCompras - GrafProvTotales()
            EliminarPresupuesto.EliminarPres(db)
            opcCom = -1

    # ---------------------------opcion 7 -  Facturar presupuesto---------------------------
        elif (opcCom - 1) == 6:
            # vamos a --> OPCIONESCOMPRADOR - GraficoCompras - GrafProvTotales()
            FacturarCompra.facturarCompra(db)
            opcCom = -1
    # ---------------------------opcion 8 -  Grafica---------------------------
        elif (opcCom - 1) == 7:
            # vamos a --> OPCIONESCOMPRADOR - GraficoCompras - GrafProvTotales()
            GraficoCompras.GraficaProductosStock(db)
            opcCom = -1
