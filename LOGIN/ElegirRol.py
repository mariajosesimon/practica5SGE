# elegir rol comprador, vendedor, comercial y productor
import Chequeos

def rol():
    opc = -1
    roles=['comprador', 'vendedor', 'productor']
    print("\n --- ELEGIR ROL ---"
        "\n 1. Comprador"
        "\n 2. Vendedor"
        "\n 4. Productor")

    #Utilización de "Seleccion" para elegir un dato-rol en el listado de roles
    opc = Chequeos.Seleccion.seleccion(opc, roles)
    return roles[opc-1]
