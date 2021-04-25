'''Para facturar hay que elegir un presupuesto.
eliminar el presupuesto de presupuestos -> desencadena que en la tbla presupuestocomprasproductos desaparezca el presupuesto
así que hay que copiar esos datos a otra tabla.
añadir el stock a productoscomprados.
'''
from datetime import datetime

from Chequeos import Seleccion
from LISTADOS import ListarPresupuestos
from LISTADOS.SeleccionPresCompra import SeleccionPresupuestoCompra


def facturarCompra(db):
    fechaFactura = ""
    cursor = db.cursor()

    consulta = "select count(*) from presupuestoscompras"
    cursor.execute(consulta)
    hayDatos = cursor.fetchone()


    if (hayDatos[0] > 0):
        # Mostar todos los presupuestos.
        print("---------------LISTA DE PRESUPUESTOS---------------------")
        ListarPresupuestos.listarPresupuestos(db, "compras")
        presupuestoElegido = SeleccionPresupuestoCompra(db)

        #------DATOS PARA LA FACTURA -----------FACTURASCOMPRAS-----------
        # Fecha factura
        print("Fecha de la factura (yyyy-mm-dd): ")

        while True:
            try:
                fechaFactura = input()  # Aqui me pasa lo mismo, tengo que dar un enter para continuar cuando es correcto el dato.
                datetime.strptime(fechaFactura, '%Y-%m-%d')
                break
            except:
                print("No ha introducido una fecha correcta. Vuelva a intentarlo: ")


        consultaPresupuesto = "Select * from presupuestoscompras where idPresupuesto = %s"
        cursor.execute(consultaPresupuesto, presupuestoElegido)
        presupuesto = cursor.fetchone()
      #  print(presupuesto[0]) idPresupuesto / idProveedor / FechaPresupuesto / idComprador

        nfactura = int(str(presupuesto[0]) + str(presupuesto[2]).replace('-', ''))

        insertarFactura = "insert into facturascompras (nFactura, idProveedor, FechaFactura, idComprador) values (%s, %s, %s,%s) "
        datosFactura = (nfactura, presupuesto[1], fechaFactura, presupuesto[3])
        cursor.execute(insertarFactura, datosFactura)
        db.commit()


         #------DATOS PARA FACTURACOMPRASCOMPRASPRDOCTOS--- e inserccion--------

        consultaProductosPres = "select * from presupuestoscomprasproductos where idPresupuesto = %s"
        cursor.execute(consultaProductosPres, presupuestoElegido )
        productos = cursor.fetchall()
        db.commit()

    #********************************************************************************************************************
    #*******************AQUI ME DA ERROR, NO ENCUENTRA EL IDFACTURA *****************************************************
    #********************************************************************************************************************

        ultimafactura = "select idFactura from facturascompras where nFactura = %s"
        cursor.execute(ultimafactura, str(nfactura))
        lastFactura = cursor.fetchone()

        print(lastFactura[0])

        for prod in productos:
            datos = (lastFactura[0], int(prod[1]), int(prod[2]))
            insertarProducto = "insert into facturacomprasproductos (idFactura, idProducto, Cantidad) VALUES (%s, %s, %s)"
            cursor.execute(insertarProducto, datos)
            db.commit()
            #---- MODIFICAR EL STOCK EN PRODUCTOSCOMPRADOS
            stock = "select Stock from productoscomprados where idProducto = %s"
            cursor.execute(stock, prod[1])
            stockComprado = cursor.fetchone()
            #print(stockComprado[0])
            #print(prod[1])
            totalActualizar = 0

            if stockComprado[0] == None:
                totalActualizar = prod[2]
            else:
                totalActualizar = int(stockComprado[0]) + int(prod[2])

            modificarStock = "UPDATE productoscomprados set Stock = '" + str(totalActualizar) + "' where idProducto = '" + str(prod[1]) + "'"
            cursor.execute(modificarStock)
            db.commit()



        consultaEliminar = "delete from presupuestoscompras where idPresupuesto = %s"
        cursor = db.cursor()
        cursor.execute(consultaEliminar, presupuestoElegido)
        db.commit()
    else:
        print("No hay presupuestos pendientes de facturar.")
