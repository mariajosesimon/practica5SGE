'''https://www.analyticslane.com/2020/11/16/pandas-como-crear-un-dataframe-vacio-y-agregar-datos/'''

import pandas as pd
import numpy as np
import numpy

import matplotlib.pyplot as plt


def produccionAnual(db):
    consulta = "select NombreProducto as 'Nombre Producto', " \
               "COUNT(cantidadProducida) as 'Cantidad producida'," \
               " year(FechaOrden) as 'Año' " \
               "FROM ordenproduccion, " \
               "productoscreados " \
               "where" \
               " ordenproduccion.idProductoFinal = productoscreados.idProducto" \
               " group by idProductoFinal,year(FechaOrden) "
    cursor = db.cursor()
    cursor.execute(consulta)

    resultadoconsulta = cursor.fetchall()

    datos = [[]]
    anios = []
    productos = []

    for i in resultadoconsulta:
        datos.append([i[0], i[1], i[2]])
        if i[2] not in anios:
           anios.append(i[2])
        if i[0] not in productos:
           productos.append(i[0])

    lista=[]
    otralista=[]
    listatres=[]
    l=[]

    for a in anios:
        for p in productos:
            listatres.append(0)
        lista.append(listatres.copy())
     #   otralista.append(listatres.copy())
      #  l.append(listatres.copy())
        listatres.clear()

    contar = 0
    contadordos=0

    for a in anios:
        producto = resultadoconsulta[0][0]
        for i in resultadoconsulta:
            if i[0] != producto:
                producto=i[0]
                contar+=1
            if i[2] ==a :
                lista[contadordos][contar]= i[1]

        contar=0
        contadordos +=1

    print(lista)
    print(resultadoconsulta)

    a = np.array(lista)
   # print("shape = ", np.shape(a))
    milista=[]
    milista2=[]
    diccionario={}
    i=-1
    j=0
    for p in productos:
        i=i+1
        for j in range(0,3):
            milista.append(lista[j][i])

        milista2 = milista.copy()
        diccionario[p]= milista2
        milista.clear()

  #  print(diccionario)


    # Creamos las barras: primero los nombres, luego los datos y añadimos color (rgb + opacidad)
    etiquetas=[]
    valores=[]
    i=0
    for k, v in diccionario.items():
        for val in v:
            etiquetas.append(k)
            valores.append(v[i])
            i=i+1
        i=0

    colores=['yellow', 'blue', 'red', 'green', 'pink', 'black']
    pintar=[]
    leyenda={}

    while i < len(anios):
        pintar.append(colores[i])
        leyenda[anios[i]]=colores[i]
        i=i+1

    print(etiquetas)
    print(valores)

    width= 0.20

    pos_y=np.arange(len(etiquetas))
    plt.bar(pos_y, valores, color=pintar, width=width, label=anios)


        # Añadimos título y nombre a los ejes
    plt.title('PRODUCTOS CREADOS')
    plt.ylabel('CANTIDAD CREADA')



        # Añadimos los nombres
    plt.xticks(pos_y, etiquetas)
    plt.legend()

        # Mostramos gráfica
    plt.show()


