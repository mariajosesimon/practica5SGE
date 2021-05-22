'''Para facturar hay que elegir un presupuesto.
eliminar el presupuesto de presupuestos -> desencadena que en la tbla presupuestoventasproductos desaparezca el presupuesto
así que hay que copiar esos datos a otra tabla.
añadir el stock a productoscomprados.
'''
from datetime import datetime

from Chequeos import Seleccion
from LISTADOS import ListarPresupuestos
from LISTADOS.SeleccionPresupuesto import SeleccionPresupuestoID


def facturarVenta(db):
    fechaFactura = ""
    cursor = db.cursor()
    crearTablaFacturasVentas = "CREATE TABLE IF NOT EXISTS facturasventas (  idFactura int(11) NOT NULL AUTO_INCREMENT,  nFactura int(11) NOT NULL,  idCliente int(11) NOT NULL,  FechaFactura date NOT NULL,  idVendedor int(11) NOT NULL,  PRIMARY KEY (idFactura))"
    cursor.execute(crearTablaFacturasVentas)
    db.commit()
    crearTablaFacturasVentasProductos ="CREATE TABLE IF NOT EXISTS facturaventasproductos (  idFactura int(11) NOT NULL,  idProducto int(11) NOT NULL,  Cantidad int(11) NOT NULL,  idConcepto int(11) NOT NULL AUTO_INCREMENT,  PRIMARY KEY (idConcepto),  FOREIGN KEY (idFactura) REFERENCES facturasventas (idFactura) ON DELETE CASCADE ON UPDATE CASCADE,  FOREIGN KEY (idProducto) REFERENCES productoscreados (idProducto) ON DELETE CASCADE ON UPDATE CASCADE)"
    cursor.execute(crearTablaFacturasVentasProductos)
    db.commit()
    consulta = "select count(*) from presupuestosventas"
    cursor.execute(consulta)
    hayDatos = cursor.fetchone()
    consultaPres = "select distinct presupuestosventas.idPresupuesto, clientes.idCliente, presupuestosventas.FechaPresupuesto,usuarios.NombreUSR from presupuestosventas,usuarios,presupuestosventasproductos, clientes where presupuestosventas.idCliente = clientes.idCliente and presupuestosventas.idVendedor= usuarios.idUsuario order by presupuestosventas.idPresupuesto"


    if (hayDatos[0] > 0):
        # Mostar todos los presupuestos.
        print("---------------LISTA DE PRESUPUESTOS---------------------")
        ListarPresupuestos.listarPresupuestos(db, 'ventas')
        presupuestoElegido = SeleccionPresupuestoID(db, consultaPres)

        #------DATOS PARA LA FACTURA -----------FACTURASVENTAS-----------
        # Fecha factura
        print("Fecha de la factura (yyyy-mm-dd): ")

        while True:
            try:
                fechaFactura = input()  # Aqui me pasa lo mismo, tengo que dar un enter para continuar cuando es correcto el dato.
                datetime.strptime(fechaFactura, '%Y-%m-%d')
                break
            except:
                print("No ha introducido una fecha correcta. Vuelva a intentarlo: ")


        consultaPresupuesto = "Select * from presupuestosventas where idPresupuesto = %s"
        cursor.execute(consultaPresupuesto, presupuestoElegido)
        presupuesto = cursor.fetchone()
      #  print(presupuesto[0]) idPresupuesto / idProveedor / FechaPresupuesto / idComprador

        nfactura = int(str(presupuesto[0]) + str(presupuesto[2]).replace('-', ''))

        insertarFactura = "insert into facturasventas (nFactura, idCliente, FechaFactura, idVendedor) values (%s, %s, %s,%s) "
        datosFactura = (nfactura, presupuesto[1], fechaFactura, presupuesto[3])
        cursor.execute(insertarFactura, datosFactura)
        db.commit()


         #------DATOS PARA FACTURAVENTASVENTASPRDOCTOS--- e inserccion--------

        consultaProductosPres = "select * from presupuestosventasproductos where idPresupuesto = %s"
        cursor.execute(consultaProductosPres, presupuestoElegido )
        productos = cursor.fetchall()
        db.commit()



        ultimafactura = "select idFactura from facturasventas where nFactura = %s"
        cursor.execute(ultimafactura, str(nfactura))
        lastFactura = cursor.fetchone()

        print(lastFactura[0])

        for prod in productos:
            datos = (lastFactura[0], int(prod[1]), int(prod[2]))
            insertarProducto = "insert into facturaventasproductos (idFactura, idProducto, Cantidad) VALUES (%s, %s, %s)"
            cursor.execute(insertarProducto, datos)
            db.commit()
            #---- MODIFICAR EL STOCK EN PRODUCTOSCOMPRADOS
            stock = "select Stock from productoscreados where idProducto = %s"
            cursor.execute(stock, prod[1])
            stockComprado = cursor.fetchone()
            #print(stockComprado[0])
            #print(prod[1])
            totalActualizar = 0

            if stockComprado[0] == None:
                totalActualizar = prod[2]
            else:
                totalActualizar = int(stockComprado[0]) + int(prod[2])

            modificarStock = "UPDATE productoscreados set Stock = '" + str(totalActualizar) + "' where idProducto = '" + str(prod[1]) + "'"
            cursor.execute(modificarStock)
            db.commit()



        consultaEliminar = "delete from presupuestosventas where idPresupuesto = %s"
        cursor = db.cursor()
        cursor.execute(consultaEliminar, presupuestoElegido)
        db.commit()
    else:
        print("No hay presupuestos pendientes de facturar.")
