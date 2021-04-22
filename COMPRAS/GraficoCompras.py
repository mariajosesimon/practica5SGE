''' grafica: productos stock en quesitos'''
import numpy as np
import matplotlib.pyplot as plt

def GraficaProductosStock(db):

    consulta="SELECT sum(facturacomprasproductos.Cantidad), productoscomprados.NombreProducto FROM facturacomprasproductos, productoscomprados where productoscomprados.idProducto = facturacomprasproductos.idProducto group by facturacomprasproductos.idProducto"
    cursor = db.cursor()
    cursor.execute(consulta)
    datos = cursor.fetchall()


    etiquetas = []
    valores = []

    for dato in datos:
        etiquetas.append(dato[1])
        valores.append(dato[0])

    plt.title("PRODUCTOS EN STOCK")
    plt.ylabel('STOCK DISPONIBLE')
    plt.xlabel('PRODUCTOS')

    y_pos = np.arange(len(etiquetas))
    plt.bar(y_pos, valores, width=0.2, color=(0.5,0.7,0.7,1))
    plt.ylim(0, max(valores)+1)

    plt.xticks(y_pos, etiquetas)
    plt.show()
