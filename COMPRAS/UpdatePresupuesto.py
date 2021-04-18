'''Que se puede modificar de un presupuesto:
1) el proveedor
2) cantidad productos a comprar

tareas:
Hay que mostrar todos presupuestos.
Elegir el que se quiere modificar.
Y modificar el dato seleccionado.

'''
from Chequeos import Seleccion
from LISTADOS import ListarPresupuestos, SeleccionPresCompra


def updatePres(db):
    cursor1 = db.cursor()
    consultaPres = "select distinct presupuestoscompras.idPresupuesto, proveedores.idProveedor, presupuestoscompras.FechaPresupuesto,usuarios.NombreUSR from presupuestoscompras,usuarios,presupuestoscomprasproductos, proveedores	where presupuestoscompras.idProveedor = proveedores.idProveedor and	presupuestoscompras.idComprador = usuarios.idUsuario order by presupuestoscompras.idPresupuesto"
    cursor1.execute(consultaPres)
    presupuestos = cursor1.fetchall()
    #Mostar todos los presupuestos.
    print("---------------LISTA DE PRESUPUESTOS---------------------")
    ListarPresupuestos.listarPresupuestos(db, "compras")

    presupuestoElegido = SeleccionPresCompra.SeleccionPresupuestoCompra(db)

    seguir = 0
   #DAto que desean modificar.
    while seguir != 1 and seguir != 2:
        try:
            print("Que deseas modificar: ")
            print(" 1) Proveedor \n 2) Producto")
            seguir = int(input())
        except:
            print("El dato introducido no es válido.")


    if seguir == 1: # ---------------Modificar proveedor ---------

        # mostrar todos los proveedores menos el que tenemos en el presupuesto.
        proveedorID=-1
        for presupuesto in presupuestos:
            if presupuesto[0] == presupuestoElegido:
                proveedorID = presupuesto[1]

        consultaProveedores = "select idProveedor, Nombre from proveedores where idProveedor != %s"
        cursor1.execute(consultaProveedores,proveedorID)
        proveedores = cursor1.fetchall()
        listaProveedores =[]

        for prov in proveedores:
            print("|{:^4}|{:^20}|".format(prov[0], prov[1]))
            listaProveedores.append(prov[0])

        print("---------- ELIGE OTRO PROVEEDOR ------------------")
        cambioProveedor = Seleccion.seleccion2(-1, listaProveedores)

        #----aqui tendremos que hacer el update y modificar el proveedor.
        actualizacion = "update presupuestoscompras set idProveedor = '" + str(cambioProveedor) + "' WHERE idProveedor = '" + str(proveedorID) + "'"
        cursor1.execute(actualizacion)
        db.commit()

    else: #----------------------Modificar cantidad producto-----------
        consultaProductosCompra = "select productoscomprados.idProducto, productoscomprados.NombreProducto, presupuestoscomprasproductos.Cantidad from presupuestoscomprasproductos, productoscomprados where presupuestoscomprasproductos.idPresupuesto = %s and productoscomprados.idProducto = presupuestoscomprasproductos.idProducto"
        cursor1.execute(consultaProductosCompra, presupuestoElegido)
        productos = cursor1.fetchall()
        listaProductos =[]

        productoID=-1
        guion = "-"
        print("|{:^4}|{:^20}|{:^20}|".format("ID" ,"PRODUCTO", "CANTIDAD"))
        print(guion.rjust(48, "-"))
        for presupuesto in presupuestos:
            if presupuesto[0] == presupuestoElegido:
                for producto in productos:
                    print("|{:^4}|{:^20}|{:^20}|".format(producto[0], producto[1], producto[2]))
                    listaProductos.append(producto[0])


        print("---------- ELIGE EL PRODUCTO A CAMBIAR CANTIDAD ------------------")
        cambioProductoCantidad = Seleccion.seleccion2(-1, listaProductos)

        cantidad = None
        while cantidad == None or cantidad == "Dato no valido.":
            try:
                print("Cantidad a comprar: ")
                cantidad = int(input())
            except:
                print("Dato no valido.")
                cantidad = None


        #----aqui tendremos que hacer el update y modificar el proveedor.
        actualizacion = "update presupuestoscomprasproductos set Cantidad = '" + str(cantidad) + "' WHERE idPresupuesto = '" + str(presupuestoElegido) + "' and idProducto = '" + str(cambioProductoCantidad) + "'"
        cursor1.execute(actualizacion)
        db.commit()
