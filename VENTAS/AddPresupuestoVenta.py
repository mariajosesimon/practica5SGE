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
    print("Datos para crear nuevo presupuesto de venta. \n")

    # consultas necesarias y ejecuciones
    consultaClientes = "select idCliente, Nombre, Ciudad from Clientes"
    consultaProductos = "select * from productoscreados"

    cursor.execute(consultaProductos)
    prodCreados = cursor.fetchall()

    clienteElegido = None
    crearCliente = "k"

    if len(prodCreados) > 0:
        cursor.execute(consultaClientes)
        clientes = cursor.fetchall()


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
                    clienteElegido = 1
                else:
                    clienteElegido = 0

    ##################################################################################
    # tendremos que hacer lo mismo con el productos.


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

                productoElegido = Seleccion.seleccion(-1, prodCreados)

                try:
                    print("Cantidad a comprar: ")
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

        print("Se ha creado el presupuesto.")
    else:
         print("No hay productos comprados para poder crear un producto.")
