'''He creado esta funcion porque la utilizo en varias funciones.
 El objetivo es cherquear que el numero
seleccionado está dentro del rango del listado, ya sea de clientes, oportunidades...
 dentro de los parametros que he pasado'''


def seleccion(datoElegido, listado):

    while (datoElegido < 1 or datoElegido > len(listado)):
        try:
            datoElegido = int(input())
            if (datoElegido < 1 or datoElegido > len(listado)):
                print("Dato no valido. Vuelve a seleccionar.")
            else:
                break
        except:
            print("Dato no valido. Vuelve a seleccionar.")
            datoElegido = -1

    return datoElegido


#utilizo esta funcion "seleccion2" porque cuando se factura un presupuesto,
# el id desaparace, y la funcion "seleccion"  mostraba la  longitud de los elementos, por ejemplo,
# si tenia los presupuestos 1,2,3,4 y factuo el 3 en la siguiente ocasion,
# con la de "seleccion", la longitud del listado es de 3, pey si quiero esccoger el presupuesto 4 daba error.

def seleccion2(datoElegido, listado):

    ids = []

    for dato in listado:
        ids.append(int(dato[0]))


    while not(datoElegido in ids):
        try:
            datoElegido = int(input())
            if not(datoElegido in ids):
                print("Dato no valido. Vuelve a seleccionar.")
            else:
                break
        except:
            print("Dato no valido. Vuelve a seleccionar.")
            datoElegido = -1

    return datoElegido
