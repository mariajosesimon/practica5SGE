'''Cuando se eliminar un presupuesto:
- mostrar los prespupuestos.
- Seleccionar un presupuesto a eliminar
- eliminar el presupuesto.
Hay que revisar que eliminar de la tabla presupuestoscompras y presupuestoscomprasproductos el presupuesto'''
from Chequeos import Seleccion
from LISTADOS import ListarPresupuestos


def EliminarPres(db):

 #Mostar todos los presupuestos.
    print("---------------LISTA DE PRESUPUESTOS---------------------")
    ListarPresupuestos.listarPresupuestos(db, "compras")

    #Guardamos los ids de los presupuestos para que puedan elegir.
    cursor1 = db.cursor()
    consultaPres = "select distinct presupuestoscompras.idPresupuesto, proveedores.idProveedor, presupuestoscompras.FechaPresupuesto,usuarios.NombreUSR from presupuestoscompras,usuarios,presupuestoscomprasproductos, proveedores	where presupuestoscompras.idProveedor = proveedores.idProveedor and	presupuestoscompras.idComprador = usuarios.idUsuario order by presupuestoscompras.idPresupuesto"
    cursor1.execute(consultaPres)
    presupuestos = cursor1.fetchall()
    listapresupuestos = []

    #Elección del presupuesto.
    for presupuesto in presupuestos:
        listapresupuestos.append(presupuesto[0])

    print("---------- ELIGE EL PRESUPUESTO QUE QUIERES ELIMINAR------------------")
    presupuestoElegido = Seleccion.seleccion2(-1, listapresupuestos)

    consultaEliminar = "delete from presupuestoscompras where idPresupuesto = %s"
    cursor = db.cursor()
    cursor.execute(consultaEliminar, presupuestoElegido)
    db.commit()
