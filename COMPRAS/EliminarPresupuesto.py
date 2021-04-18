'''Cuando se eliminar un presupuesto:
- mostrar los prespupuestos.
- Seleccionar un presupuesto a eliminar
- eliminar el presupuesto.
Hay que revisar que eliminar de la tabla presupuestoscompras y presupuestoscomprasproductos el presupuesto'''
from Chequeos import Seleccion
from LISTADOS import ListarPresupuestos
from LISTADOS.SeleccionPresCompra import SeleccionPresupuestoCompra


def EliminarPres(db):

 #Mostar todos los presupuestos.
    print("---------------LISTA DE PRESUPUESTOS---------------------")
    ListarPresupuestos.listarPresupuestos(db, "compras")

    presupuestoElegido = SeleccionPresupuestoCompra(db)

    consultaEliminar = "delete from presupuestoscompras where idPresupuesto = %s"
    cursor = db.cursor()
    cursor.execute(consultaEliminar, presupuestoElegido)
    db.commit()
