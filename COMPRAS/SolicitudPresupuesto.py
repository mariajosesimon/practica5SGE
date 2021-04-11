from datetime import datetime

from COMPRAS import AddProveedor, AddProducto
from Chequeos  import Seleccion


def CrearPresupuestoCompra(db):

    cursor = db.cursor()
    # consultas necesarias y ejecuciones
    consultaProveedores = "select idProveedor, Nombre from proveedores"
    consultaProductosComp = "select * from productoscomprados"

    cursor.execute(consultaProveedores)
    proveedores = cursor.fetchall()

    cursor.execute(consultaProductosComp)
    prodComprados = cursor.fetchall()

    print("Datos para crear nuevo presupuesto. \n")

    proveedorElegido = None
    crearProveedor = "k"

    # IF: si tenemos datos de proveedores:
    # tenemos que llamar a Chequeos --> Seleccion --> seleccion()
    # para que el dato que escojamos este dentro del rango del listado que pasamos
    # y almacenamos en la variable el id del proveedor.

    # ELSE: no tenemos datos de proveedores: opciones
    # crear un nuevo proveedor
    # finalizar la solicitud de presupuesto.
    listaproveedores = []
    if len(proveedores) > 0:
        print("LISTADO DE PROVEEDORES. ELIGE UN PROVEEDOR.\n")
        print("|{:^4}|{:^20}|".format("ID", "PROVEEDOR"))
        for prov in proveedores:
                print("|{:^4}|{:^20}|".format(prov[0],prov[1]))
                listaproveedores.append(prov[0])
        proveedorElegido = Seleccion.seleccion2(-1, listaproveedores)
        print("proveedor elegido ", proveedorElegido)
    else:
        print("No hay proveedores. Hay que crear un proveedor antes de realizar un presupuesto.")
        while crearProveedor != "SI" and crearProveedor != "NO":
            print("Quieres crear un proveedor nuevo: si / no")
            crearProveedor = input().upper()
            if crearProveedor == "SI":
                # llamar a OPCIONESCOMPRADOR - AddProveedor - CrearProveedor()
                AddProveedor.CrearProveedor(db)
                consultaUltimoProv = "select idProveedor from proveedores"
                cursor.execute(consultaUltimoProv)
                prove = cursor.fetchone()
                proveedorElegido = prove[0]
                print("proveedor elegido : ", proveedorElegido)
            else:
                proveedorElegido = 0

    ##################################################################################
    # tendremos que hacer lo mismo con el productos.


    # introduzco estas 3 variables antes de los if, para que no nos den error por no inicializarlas.
    addProductoPresupuesto = {}
    cantidad = None
    crearProducto = "k"
    listaProductos=[]
    if proveedorElegido != 0:
        print("\nLISTADO DE PRODUCTOS. ELIGE UN PRODUCTO.\n")
        if len(prodComprados) > 0 :
            # Tener en cuenta que un presupuesto puede tener varios productos
            # Tendremos que añadir a un listado los productos escogidos.

            print("|{:^4}|{:^20}|{:^20}|".format("ID", "PRODUCTO", "PRECIO"))
            for prod in prodComprados:
                print("|{:^4}|{:^20}|{:^20}|".format(prod[0],prod[1],prod[2]))
                listaProductos.append(prod[0])

            seguir = "k"
            while seguir != "NO":
                if seguir == "SI":
                    print("|{:^4}|{:^20}|{:^20}|".format("ID", "PRODUCTO", "PRECIO"))
                    for prod in prodComprados:
                        print("|{:^4}|{:^20}|{:^20}|".format(prod[0],prod[1],prod[2]))
                        listaProductos.append(prod[0])
                    seguir = "k"
                productoElegido = Seleccion.seleccion2(-1, listaProductos)
                cantidad = None

                while cantidad == None or cantidad == "Dato no valido.":
                    try:
                        print("Cantidad a comprar: ")
                        cantidad = int(input())
                    except:
                        print("Dato no valido.")

                addProductoPresupuesto[productoElegido] = cantidad

                while seguir != "SI" and seguir != "NO":
                    print("Deseas continuar añadiendo productos: SI / NO")
                    seguir = input().upper()

        else:
            print("No hay productos. Hay que crear un producto antes de realizar un presupuesto.")

            while crearProducto != "SI" and crearProducto != "NO":
                print("Quieres crear un producto nuevo: si / no")
                crearProducto = input().upper()
                if crearProducto == "SI":
                    # llamar a OPCIONESCOMPRADOR - AddProveedor - CrearProveedor()
                    AddProducto.CrearProducto(db)
                    try:
                        print("Cantidad a comprar: ")
                        cantidad = int(input())
                    except:
                        print("Dato no valido.")

                    consultaUltimoProducto = "select idProducto from productoscomprados"
                    cursor.execute(consultaUltimoProducto)
                    producto = cursor.fetchone()
                    addProductoPresupuesto[producto[0]] = cantidad
                else:
                    crearProducto = "NO"

        ##### EL USUARIO LOGADO SERÁ EL COMPRADOR SIEMPRE
        fechaPresupuesto = ""
        if crearProducto != 0 and crearProducto != "NO":
            print("Fecha del presupuesto (yyyy-mm-dd): ")

            while True:
                try:
                    fechaPresupuesto = input()  # Aqui me pasa lo mismo, tengo que dar un enter para continuar cuando es correcto el dato.
                    datetime.strptime(fechaPresupuesto, '%Y-%m-%d')
                    break
                except:
                    print("No ha introducido una fecha correcta. Vuelva a intentarlo: ")


        # el usuario con rol "Comprador" que es el que está logado, será el comprador que solicita el presupuesto al proveedor.
            cursor.execute("select idUsuario from userlogin")
            idUser = cursor.fetchone()

        #insertar el presupuesto. "presupuestoscompras"
            datosPres=(proveedorElegido,fechaPresupuesto,idUser[0])
            insertarPresupuesto = "INSERT INTO presupuestoscompras (idProveedor, FechaPresupuesto, idComprador) VALUES (%s, %s, %s)"
            cursor.execute(insertarPresupuesto, datosPres)

        ##############################################################################################################
        #ESTAMOS SUPONIENDO QUE NO SE PUEDE REPETIR ESTOS 3 DATOS EN EL MISMO DIA - IDPROVEEDOR, FECHA E IDCOMPRADOR
        ##############################################################################################################


        #insertar en la tabla "presupuestoscomprasproductos" cada producto.
            consultaUltimoPres = "select idPresupuesto from presupuestoscompras where idProveedor = %s and FechaPresupuesto = %s and idComprador =%s"
            cursor.execute(consultaUltimoPres, datosPres)
            presupuesto = cursor.fetchone()

            for k, v in addProductoPresupuesto.items():
                datosPres=(presupuesto[0], k, v)
                insertarPresProd = "INSERT INTO presupuestoscomprasproductos (idPresupuesto, idProducto, Cantidad) VALUES (%s, %s, %s)"
                cursor.execute(insertarPresProd, datosPres)
            db.commit()
            print("Se ha creado el presupuesto.")
        elif crearProducto == "NO":
            print("No hay productos.")
    else:
        print("No hay un proveedor elegido.")
