from Chequeos import Seleccion


def SeleccionPresupuestoCompra(db):
    # Guardamos los ids de los presupuestos para que puedan elegir.
    cursor1 = db.cursor()
    consultaPres = "select distinct presupuestoscompras.idPresupuesto, proveedores.idProveedor, presupuestoscompras.FechaPresupuesto,usuarios.NombreUSR from presupuestoscompras,usuarios,presupuestoscomprasproductos, proveedores	where presupuestoscompras.idProveedor = proveedores.idProveedor and	presupuestoscompras.idComprador = usuarios.idUsuario order by presupuestoscompras.idPresupuesto"
    cursor1.execute(consultaPres)
    presupuestos = cursor1.fetchall()
    listapresupuestos = []
    # Elección del presupuesto.
    for presupuesto in presupuestos:
        listapresupuestos.append(presupuesto[0])
    print("---------- ELIGE UN PRESUPUESTO ------------------")
    presupuestoElegido = Seleccion.seleccion2(-1, listapresupuestos)
    return presupuestoElegido
