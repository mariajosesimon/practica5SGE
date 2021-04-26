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
    consultaPres = "select distinct presupuestosventas.idPresupuesto, clientes.idClientes, presupuestosventas.FechaPresupuesto,usuarios.NombreUSR from presupuestosventas,usuarios,presupuestosventassproductos, clientes where presupuestosventas.idCliente = clientes.idCliente and	presupuestosventas.idVendedor= usuarios.idUsuario order by presupuestosventas.idPresupuesto"

    print("---------------LISTA DE PRESUPUESTOS---------------------")
    ListarPresupuestos.listarPresupuestos(db, "ventas")

    presupuestoElegido = SeleccionPresupuestoID(db, consultaPres)

    consultaEliminar = "delete from presupuestosventas where idPresupuesto = %s"
    cursor = db.cursor()
    cursor.execute(consultaEliminar, presupuestoElegido)
    db.commit()
