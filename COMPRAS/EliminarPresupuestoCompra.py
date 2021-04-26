'''Cuando se eliminar un presupuesto:
- mostrar los prespupuestos.
- Seleccionar un presupuesto a eliminar
- eliminar el presupuesto.
Hay que revisar que eliminar de la tabla presupuestoscompras y presupuestoscomprasproductos el presupuesto'''
from Chequeos import Seleccion
from LISTADOS import ListarPresupuestos
from LISTADOS.SeleccionPresupuesto import SeleccionPresupuestoID


def EliminarPres(db):

 #Mostar todos los presupuestos.
    consultaPres = "select distinct presupuestoscompras.idPresupuesto, proveedores.idProveedor, presupuestoscompras.FechaPresupuesto,usuarios.NombreUSR from presupuestoscompras,usuarios,presupuestoscomprasproductos, proveedores	where presupuestoscompras.idProveedor = proveedores.idProveedor and	presupuestoscompras.idComprador = usuarios.idUsuario order by presupuestoscompras.idPresupuesto"

    print("---------------LISTA DE PRESUPUESTOS---------------------")
    ListarPresupuestos.listarPresupuestos(db, "compras")

    presupuestoElegido = SeleccionPresupuestoID(db, consultaPres)

    consultaEliminar = "delete from presupuestoscompras where idPresupuesto = %s"
    cursor = db.cursor()
    cursor.execute(consultaEliminar, presupuestoElegido)
    db.commit()
