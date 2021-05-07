
import LOGIN as LOGIN
from LOGIN import CrearPW
from LOGIN import Fortaleza
from LOGIN import GeneradorPassw

def cambio(db):

    nombre=""
    cursor = db.cursor()

    while nombre == "":
        print("CUAL ES TU USUARIO: ")
        nombre = input("\nNombre de usuario: ").lower()

    consultaNombre = 'select usuario from usuarios where usuario like %s'
    cursor.execute(consultaNombre, nombre)
    existe = cursor.fetchone()

    try:
        if existe[0]:
            seguridad = LOGIN.GeneradorPassw.generadorPW()
            print("Hay que crear la contraseña con los parámetros marcados.")

            print("Recuerda:"
                  "\nTiene que tener una longitud", seguridad[0],
                  "\nMayusculas", seguridad[1],
                  "\nMinusculas", seguridad[2],
                  "\nSímbolos", seguridad[3],
                  "\nNúmeros", seguridad[4])


            print("Su contraseña es:", LOGIN.Fortaleza.fort(seguridad))
            contrasenna = LOGIN.CrearPW.TuPW(seguridad)

            actualizacion = "update usuarios set password = '"+ contrasenna + "' where usuario = '" + existe[0] + "'"

            cursor.execute(actualizacion)
            db.commit()

    except:
        print("El usuario indicado no existe. \nHable con RRHH")
