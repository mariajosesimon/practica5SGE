
'''
- 1º que debemos hacer es comprobar si hay material comprado
para poder producir algo y si tenemos suficiente stock. Lo vemos en (productoscomprados)
si no hay material no se puede crear la orden de produccion.
- 2º Existe el producto que quieres crear: si/no  (productoscreados)
    - si existe, que elija el id
    - no existe, hay que generar el producto (nombre+precio)

'''
from datetime import datetime

from Chequeos import Seleccion
from COMPRAS import AddProducto
#FechaOrden
#idProductoFinal
#idProductor


def CrearOrdenProd(db, tabla):

    cursor = db.cursor()
    hayMaterial = "SELECT idProducto, NombreProducto, stock FROM productoscomprados WHERE stock > 0"
    cursor.execute(hayMaterial)
    materiales = cursor.fetchall()

    if len(materiales) > 0:

        guion = "-"
        #Mostrar si hay productos creados.

#--------------------------ELECCION DEL PRODUCTO QUE SE QUIERE FABRICAR ----------------------------------

        consultaProductosCreados = ("select idProducto, NombreProducto from productoscreados")

        cursor.execute(consultaProductosCreados)
        productos = cursor.fetchall()
        idProductos =[]

        if (len(productos) > 0):
            for producto in productos:
                print(guion.rjust(50, "-"))
                print("|{:^4}|{:^20}|".format(producto[0], producto[1]))
                idProductos.append(producto[0]) # guardamos en un listado los indices para poder seleccionar 1 o que creen uno nuevo


        crearNuevoProducto = 0
        productoElegido = -1
        while crearNuevoProducto != "SI" and crearNuevoProducto != "NO":
            print("El producto que quieres producir está en el listado mostrado?: si / no")
            crearNuevoProducto = input().upper()
            if crearNuevoProducto == "SI":
                print("Elige un producto a producir: ")
                productoElegido = Seleccion.seleccion2(-1, idProductos)


            elif crearNuevoProducto == "NO":
                #Hay que crear un producto a producir.
                #Reutilizo la funcion creada en "COMPRAS--> ADDPRODUCTO" ya que es igual.
                AddProducto.CrearProducto(db, tabla)
                consultaUltimoProd='SELECT max(idProducto) FROM productoscreados'
                cursor.execute(consultaUltimoProd)
                productoElegido = cursor.fetchone()



#--------------------------------PRODUCTOS NECESARIOS PARA PRODUCIR -------------------------------------

        addProductoOrden = {}
        listaProductos = []
        print("\nLISTADO DE PRODUCTOS. ELIGE UN PRODUCTO.\n")
        if len(materiales) > 0 :
            # Tener en cuenta que un presupuesto puede tener varios productos
            # Tendremos que añadir a un listado los productos escogidos.

            print("|{:^4}|{:^20}|{:^20}|".format("ID", "PRODUCTO", "STOCK"))
            for prod in materiales:
                print("|{:^4}|{:^20}|{:^20}|".format(prod[0],prod[1],prod[2]))
                listaProductos.append(prod[0])

            seguir = "k"
            while seguir != "NO":
                if seguir == "SI":
                    print("|{:^4}|{:^20}|{:^20}|".format("ID", "PRODUCTO", "STOCK"))
                    for prod in materiales:
                        print("|{:^4}|{:^20}|{:^20}|".format(prod[0],prod[1],prod[2]))
                        listaProductos.append(prod[0])
                    seguir = "k"
                productoElegido = Seleccion.seleccion2(-1, listaProductos)
                cantidad = None

                while cantidad == None or cantidad == "Dato no valido.":
                    try:
                        print("Cantidad a utilizar: ")
                        cantidad = int(input())
                    except:
                        print("Dato no valido.")

                addProductoOrden[productoElegido] = cantidad

                while seguir != "SI" and seguir != "NO":
                    print("Deseas continuar añadiendo productos: SI / NO")
                    seguir = input().upper()


# -------------------------------Fecha de la orden -------------------------------------------------------
        fechaOrden = ""

        print("Fecha de la orden (yyyy-mm-dd): ")
        # while True:
        #     try:
        #         fechaOrden = input()
        #         datetime.strptime(fechaOrden, '%Y-%m-%d')
        #         break
        #     except:
        #         print("No ha introducido una fecha correcta. Vuelva a intentarlo: ")

# -------------------------------cantidad a producir -------------------------------------------------------

        cantidadProducida = 0
        while cantidadProducida == None or cantidadProducida == "Dato no valido.":
            try:
                print("Cantidad a producir: ")
                cantidadProducida = int(input())
            except:
                print("Dato no valido.")

# -------------------------------USUARIO PRODUCTOR -------------------------------------------------------

        cursor.execute("select idUsuario from userlogin")
        idUser = cursor.fetchone()


# -------------------------------CREAR LA ORDEN DE PRODUCCION -------------------------------------------------------


        datosOrden = (productoElegido,fechaOrden,idUser, cantidadProducida)
        annadirOrden = "INSERT INTO ordenproduccion (idProductoFinal, FechaOrden, idProductor, cantidadProducida) VALUES (%s, %s, %s, %s)"
        cursor.execute(annadirOrden, datosOrden)

#----------------- ACTUALIZAR LA TABLA  productoscreados  EL STOCK------------------------------

    # --- Revisar si hay stock para sumar ------
        #He refactorizado para reutilizar esta funcion
        tabla2 = "productoscreados"
        ActualizarStock(cantidadProducida, cursor, productoElegido, tabla2 )



#-------------- los productosutilizadosproduccion se tienen que restar a la tabla de productoscomprados
# ---- se tienen que añadir a la tabla----
# Tengo que realizarlo en el ultimo paso porque necesito el id de la orden de produccion.

        consultaOrden = "select max(idOrden) from ordenproduccion"
        cursor.execute(consultaOrden)
        nOrden = cursor.fetchone()

        for k, v in addProductoOrden.items():
            datos = (nOrden, k, v)
            annadirOrden = "INSERT INTO productosutilizadosproduccion (idOrden, idProductoUtilizado, Cantidad) VALUES (%s, %s, %s)"
            cursor.execute(annadirOrden, datos)
            tabla3 = 'productoscomprados'
            ActualizarStock(cantidadProducida, cursor, productoElegido, tabla3 )
            db.commit()


    else:
        print("No hay material comprado para poder producir. \nPongase en contacto con el departamento de compras.")


def ActualizarStock(cantidadProducida, cursor, productoElegido, tabla4):


    consultaStock = "select Stock from %s where idProducto = %s" # -----------------no devuelve nada mal la consulta.
    datos = (tabla4, productoElegido)
    cursor.execute(consultaStock, datos)
    cantidadStock = cursor.fetchone()
    print(cantidadStock)
    for cantidad in cantidadStock:
        print(type(cantidad[0]))

    totalActualizar = 0
    if cantidad[0] == None:
        totalActualizar = cantidadProducida
    else:
        if (tabla == 'productoscomprados'):
            totalActualizar = int(cantidadStock[0]) - int(cantidadProducida)
        elif (tabla == 'productoscreados'):
            totalActualizar = int(cantidadStock[0]) + int(cantidadProducida)

    print(type(totalActualizar))
    modificarStock = "UPDATE " + tabla + " set Stock = '" + str(totalActualizar) + "' where idProducto = '" + str(productoElegido) + "'"
    cursor.execute(modificarStock)

















