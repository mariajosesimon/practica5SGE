def listarPresupuestos(db, entidad):
    consultaPres = None
    consultaProd = None
    nombreProveedor = None
    nombreProducto = None
    proveedor = None
    comprador = None

    id = "ID"
    fecha = "FECHA PRESUPUESTO"
    productoNombre = "PRODUCTO"
    cantidad = "CANTIDAD"
    total = "TOTAL"
    guion = "-"
    precio = "PRECIO"
    espacio =" "

    if entidad == "compras":
        proveedor = "PROVEEDOR"
        comprador = "AGENTE COMPRADOR"
        consultaPres = "select distinct presupuestoscompras.idPresupuesto, proveedores.Nombre, presupuestoscompras.FechaPresupuesto,usuarios.NombreUSR from presupuestoscompras,usuarios,presupuestoscomprasproductos, proveedores	where presupuestoscompras.idProveedor = proveedores.idProveedor and	presupuestoscompras.idComprador = usuarios.idUsuario order by presupuestoscompras.idPresupuesto"
        consultaProd = "select presupuestoscomprasproductos.idPresupuesto,	productoscomprados.NombreProducto, presupuestoscomprasproductos.cantidad, productoscomprados.Precio from presupuestoscomprasproductos, productoscomprados where presupuestoscomprasproductos.idProducto = productoscomprados.idProducto"
    elif entidad == "ventas":
        proveedor = "CLIENTE"
        comprador = "AGENTE VENDEDOR"
        consultaPres = "select distinct presupuestosventas.idPresupuesto, clientes.Nombre, presupuestosventas.FechaPresupuesto,usuarios.NombreUSR from presupuestosventas,usuarios,presupuestosventasproductos, clientes	where presupuestosventas.idCliente = clientes.idCliente and	presupuestosventas.idVendedor = usuarios.idUsuario order by presupuestosventas.idPresupuesto"
        consultaProd = "select presupuestosventasproductos.idPresupuesto, productoscreados.NombreProducto, presupuestosventasproductos.cantidad, productoscreados.Precio from presupuestosventasproductos, productoscreados where presupuestosventasproductos.idProducto = productoscreados.idProducto"


    cursor1 = db.cursor()
    cursor1.execute(consultaPres)
    presupuestos = cursor1.fetchall()

    cursor2 = db.cursor()
    cursor2.execute(consultaProd)
    productos = cursor2.fetchall()

    for presupuesto in presupuestos:

        print(guion.rjust(90, "-"))
        print("|{:^4}|{:^20}|{:^20}|{:^20}|".format(id, proveedor, fecha, comprador))
        print("|{:^4}|{:^20}|{:^20}|{:^20}|".format(presupuesto[0], presupuesto[1], str(presupuesto[2]), presupuesto[3]))
        print(guion.rjust(90, "-"))
        print("|{:^4}|{:^20}|{:^20}|{:^20}|{:^20}|".format(espacio, productoNombre, cantidad, precio, total))

        for producto in productos:

            if producto[0] == presupuesto[0]:

                totales = producto[2]*producto[3]
                print("|{:^4}|{:^20}|{:^20}|{:^20}|{:^20}|".format(espacio, producto[1], producto[2], producto[3], totales))







