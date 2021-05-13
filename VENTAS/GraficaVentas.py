import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Shadow

def GrafVentas(db):

    consulta=("select usuarios.NombreUSR, SUM(productoscreados.Precio * facturaventasproductos.Cantidad) as total "
              " from productoscreados, facturaventasproductos, usuarios,"
              " facturasventas WHERE facturasventas.idFactura = facturaventasproductos.idFactura "
              "AND facturaventasproductos.idProducto = productoscreados.idProducto and "
              "facturasventas.idVendedor = usuarios.idUsuario GROUP by usuarios.NombreUSR")
    cursor = db.cursor()
    cursor.execute(consulta)
    datos = cursor.fetchall()

    diccionario={}

    for dato in datos:
        diccionario[dato[0]]=dato[1]

   # print(diccionario)


    figura = plt.figure(figsize=(5, 5))
    ejes = figura.add_axes([0.1, 0.1, 0.8, 0.8])
    etiquetas = diccionario.keys()
    valores = diccionario.values()


    quesitos = plt.pie(valores,  labels=etiquetas, autopct= make_autopct(valores),   shadow=True)
    plt.title("IMPORTES VENTAS", bbox={"facecolor":"0.8", "pad":5})
    plt.legend()

#Loop para añadir etiqueta y borde
    for w in quesitos[0]:
    # Añadir la etiqueta
        w.set_gid(w.get_label())

    # Sin bordes en los quesitos
        w.set_edgecolor("none")

#Por cada quesito, añadiremos sombra --> estética
    for w in quesitos[0]:
    # Añade sombras
        s = Shadow(w, -0.01, -0.01)
        s.set_gid(w.get_gid() + "_shadow")
        s.set_zorder(w.get_zorder() - 0.1)
        ejes.add_patch(s)

        plt.show()



def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d}  ({p:.2f}%)'.format(v=val, p=pct)

    return my_autopct
