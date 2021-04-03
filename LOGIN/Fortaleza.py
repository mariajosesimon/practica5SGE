'''contar cuantos parametros son true, y si listaParametros[0] > 0
       Determinar fortaleza:
    debil: cumple 0-1 requisitos.
    media: cumple 2-3 requisitos
    fuerte: cumple 4-5 requisitos
'''


def fort(listaParametros):
    fuerza = listaParametros.count(True)
    if listaParametros[0] > 0:
        fuerza = fuerza + 1

    if fuerza < 2:
        fuerza = "debil"
    elif fuerza == 2 or fuerza == 3:
        fuerza = "media"
    else:
        fuerza = "fuerte"

    return fuerza
