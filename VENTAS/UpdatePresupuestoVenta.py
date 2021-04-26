'''Que se puede modificar de un presupuesto:
1) el cliente
2) cantidad productos a comprar

tareas:
Hay que mostrar todos presupuestos.
Elegir el que se quiere modificar.
Y modificar el dato seleccionado.

'''
from Chequeos import Seleccion
from LISTADOS import ListarPresupuestos, SeleccionPresupuesto


def updatePres(db):
    cursor1 = db.cursor()
    consultaPres = "select distinct presupuestosventas.idPresupuesto, clientes.idClientes, presupuestosventas.FechaPresupuesto,usuarios.NombreUSR from presupuestosventas,usuarios,presupuestosventassproductos, clientes where presupuestosventas.idCliente = clientes.idCliente and	presupuestosventas.idVendedor= usuarios.idUsuario order by presupuestosventas.idPresupuesto"

    cursor1.execute(consultaPres)
    presupuestos = cursor1.fetchall()
    #Mostar todos los presupuestos.
    print("---------------LISTA DE PRESUPUESTOS---------------------")
    ListarPresupuestos.listarPresupuestos(db, "ventas")

    presupuestoElegido = SeleccionPresupuesto.SeleccionPresupuestoID(db, consultaPres)

    seguir = 0
   #DAto que desean modificar.
    while seguir != 1 and seguir != 2:
        try:
            print("Que deseas modificar: ")
            print(" 1) Cliente \n 2) Producto")
            seguir = int(input())
        except:
            print("El dato introducido no es válido.")


    if seguir == 1: # ---------------Modificar cliente ---------

        # mostrar todos los clientes menos el que tenemos en el presupuesto.
        clienteID=-1
        for presupuesto in presupuestos:
            if presupuesto[0] == presupuestoElegido:
                clienteID = presupuesto[1]

        consultaClientes = "select idCliente, Nombre from clientes where idCliente != %s"
        cursor1.execute(consultaClientes,clienteID)
        clientes = cursor1.fetchall()
        listaClientes =[]

        for prov in clientes:
            print("|{:^4}|{:^20}|".format(prov[0], prov[1]))
            listaClientes.append(prov[0])

        print("---------- ELIGE OTRO CLIENTE ------------------")
        cambioCliente = Seleccion.seleccion2(-1, listaClientes)

        #----aqui tendremos que hacer el update y modificar el cliente.
        actualizacion = "update presupuestosventas set idCliente = '" + str(cambioCliente) + "' WHERE idCliente = '" + str(clienteID) + "'"
        cursor1.execute(actualizacion)
        db.commit()

    else: #----------------------Modificar cantidad producto-----------
        consultaProductosCompra = "select productoscreados.idProducto, productoscreados.NombreProducto, presupuestosventasproductos.Cantidad from presupuestosventasproductos, productoscreados where presupuestosventasproductos.idPresupuesto = %s and productoscreados.idProducto = presupuestosventasproductos.idProducto"
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


        #----aqui tendremos que hacer el update y modificar el cliente.
        actualizacion = "update presupuestosventasproductos set Cantidad = '" + str(cantidad) + "' WHERE idPresupuesto = '" + str(presupuestoElegido) + "' and idProducto = '" + str(cambioProductoCantidad) + "'"
        cursor1.execute(actualizacion)
        db.commit()
