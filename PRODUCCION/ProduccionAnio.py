import pandas as pd
import matplotlib.pyplot as plt
def produccionAnual(db):

    consulta = "select NombreProducto as 'Nombre Producto', COUNT(cantidadProducida) as 'Cantidad producida', year(FechaOrden) as 'Año' FROM ordenproduccion, productoscreados where ordenproduccion.idProductoFinal = productoscreados.idProducto group by idProductoFinal, year(FechaOrden)"
    cursor = db.cursor()
    cursor.execute(consulta)

    resultadoconsulta = cursor.fetchall()


    datos =[[]]


    for i in resultadoconsulta:
        datos.append([i[0], i[1], i[2]])



    df=pd.DataFrame(datos,columns=["Producto","cantidad","Anio"])
    df.plot(x=["Producto","Anio"], y=["cantidad"], kind="bar",figsize=(9,8))
    plt.show()
