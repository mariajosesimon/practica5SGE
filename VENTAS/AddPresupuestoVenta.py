'''Datos para crear un presupuesto:
- Cliente (puede o no existir.
    a) Si no existe ninguno: hay que crear
    b) sino:
        b1)se puede escoger
        b2) crear nuevo cliente





FUNCIONES REUTILIZADAS DE OTROS EJERCICIOS:
- funcion "seleccion" en la seleccion del departamento.
-
'''
from datetime import datetime

from Chequeos import Seleccion
from VENTAS import AddCliente


def CrearPresupuestoVenta(db):

# en esta funcion necesitamos antes de seguir si hay productos creados / producidos. Si no hay no continuamos.
    cursor = db.cursor()


    # consultas necesarias y ejecuciones
    consultaClientes = "select idCliente, Nombre, Ciudad from Clientes"
    consultaProductos = "select * from productoscreados"

    cursor.execute(consultaProductos)
    prodCreados = cursor.fetchall()
    listaProductos=[]
    clienteElegido = None
    crearCliente = "k"

    if len(prodCreados) > 0:
        cursor.execute(consultaClientes)
        clientes = cursor.fetchall()
        print("Datos para crear nuevo presupuesto de venta. \n")

        print("LISTADO DE CLIENTES. ELIGE UN CLIENTE.\n")
        print("|{:^4}|{:^20}|{:^20}|".format("ID", "CLIENTE", "CIUDAD"))
        if len(clientes) > 0:
            for cliente in clientes:
                print("|{:^4}|{:^20}|{:^20}|".format(cliente[0],cliente[1],cliente[2]))
            clienteElegido = Seleccion.seleccion(-1, clientes)
        else:
            print("No hay clientes. Hay que crear un cliente antes de realizar un presupuesto.")
            while crearCliente != "SI" and crearCliente != "NO":
                print("Quieres crear un cliente nuevo: si / no")
                crearcliente = input().upper()
                if crearcliente == "SI":
                # llamar a OPCIONESVENDEDOR - Addcliente - Crearcliente()
                    AddCliente.CrearCliente(db)
                    consultaUltimoCliente = "select idCliente from clientes"
                    cursor.execute(consultaUltimoCliente)
                    client = cursor.fetchone()
                    clienteElegido = client[0]
                    print("Cliente elegido : ", clienteElegido)
                else:
                    clienteElegido = 0

    ##################################################################################


    # introduzco estas 3 variables antes de los if, para que no nos den error por no inicializarlas.
        addProductoPresupuestoVenta = {}
        cantidad = None
        crearProducto = "k"
        if clienteElegido != 0:
            seguir = "SI"

            print("\nLISTADO DE PRODUCTOS. ELIGE UN PRODUCTO.\n")
            while seguir != "NO":
                if seguir == "SI":
                    print("|{:^4}|{:^20}|{:^20}|{:^20}|".format("ID", "PRODUCTO", "PRECIO", "STOCK"))
                    for prod in prodCreados:
                        print("|{:^4}|{:^20}|{:^20}|{:^20}|".format(prod[0],prod[1],prod[2], prod[3]))
                        listaProductos.append(prod[0])

                productoElegido = Seleccion.seleccion(-1, listaProductos)

                try:
                    print("Cantidad a vender: ")
                    cantidad = int(input())
                except:
                    print("Dato no valido.")

                addProductoPresupuestoVenta[productoElegido] = cantidad
                print("Deseas continuar añadiendo productos: SI / NO")
                seguir = input().upper()
                if seguir == "NO":
                    break


        ##### EL USUARIO LOGADO SERÁ EL COMPRADOR SIEMPRE
        fechaPresupuesto = ""

        print("Fecha del presupuesto (yyyy-mm-dd): ")

        while True:
            try:
                fechaPresupuesto = input()  # Aqui me pasa lo mismo, tengo que dar un enter para continuar cuando es correcto el dato.
                datetime.strptime(fechaPresupuesto, '%Y-%m-%d')
                break
            except:
                print("No ha introducido una fecha correcta. Vuelva a intentarlo: ")



        ## **********GUARDAR EN EL ARCHIVO LOS PRESPUESTOS ****************************************

#para insertar el presupuesto, tengo que insertar 1 el presupuesto, guardar el id que me ha generado,
        # y posteriormente, guardar los datos de productos + cantidad en la tabla de presventasproductos.

        # el usuario con rol "Vendedor" que es el que está logado, será el comprador que solicita el presupuesto al proveedor.
        cursor.execute("select idUsuario from userlogin")
        idUser = cursor.fetchone()

        datosPres=(clienteElegido,fechaPresupuesto,idUser[0])
        insertarPresupuesto = "INSERT INTO presupuestosventas (idCliente, FechaPresupuesto, idVendedor) VALUES (%s, %s, %s)"
        cursor.execute(insertarPresupuesto, datosPres)


        #insertar en la tabla "presupuestoscomprasproductos" cada producto.
        consultaUltimoPres = "select idPresupuesto from presupuestosventas where idCliente = %s and FechaPresupuesto = %s and idVendedor =%s"
        cursor.execute(consultaUltimoPres, datosPres)
        presupuesto = cursor.fetchone()

        for k, v in addProductoPresupuestoVenta.items():
            datosPres=(presupuesto[0], k, v)
            insertarPresProd = "INSERT INTO presupuestosventasproductos (idPresupuesto, idProducto, Cantidad) VALUES (%s, %s, %s)"
            cursor.execute(insertarPresProd, datosPres)
        db.commit()


        print("Se ha creado el presupuesto.")
    else:
         print("No hay productos creados para poder venderlos.")
