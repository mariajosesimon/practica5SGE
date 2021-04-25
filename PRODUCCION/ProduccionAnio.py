'''https://www.analyticslane.com/2020/11/16/pandas-como-crear-un-dataframe-vacio-y-agregar-datos/'''

import pandas as pd

import matplotlib.pyplot as plt


def produccionAnual(db):
    consulta = "select NombreProducto as 'Nombre Producto', COUNT(cantidadProducida) as 'Cantidad producida', year(FechaOrden) as 'Año' FROM ordenproduccion, productoscreados where ordenproduccion.idProductoFinal = productoscreados.idProducto group by idProductoFinal, year(FechaOrden)"
    cursor = db.cursor()
    cursor.execute(consulta)

    resultadoconsulta = cursor.fetchall()

    datos = [[]]

    for i in resultadoconsulta:
        datos.append([i[0], i[1], i[2]])

    df = pd.DataFrame(columns=['Nombre', 'Anio', 'Cantidad'])

    for i in resultadoconsulta:
        df = df.append({'Nombre': i[0], 'Anio': i[2], 'Cantidad': i[1]}, ignore_index=True)

