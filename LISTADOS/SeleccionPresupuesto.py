from Chequeos import Seleccion


def SeleccionPresupuestoID(db, consulta):
    # Guardamos los ids de los presupuestos para que puedan elegir.
    cursor1 = db.cursor()
    cursor1.execute(consulta)
    presupuestos = cursor1.fetchall()
    listapresupuestos = []
    # Elección del presupuesto.
    for presupuesto in presupuestos:
        listapresupuestos.append(presupuesto[0])
    print("---------- ELIGE UN PRESUPUESTO ------------------")
    presupuestoElegido = Seleccion.seleccion2(-1, listapresupuestos)
    return presupuestoElegido
