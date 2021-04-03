import csv
import LOGIN as LOGIN
from LOGIN import CrearPW
from LOGIN import Fortaleza
from LOGIN import GeneradorPassw
from LOGIN import Recorrer
from LOGIN import ElegirRol




def registro():
    seguridad = []
    rolUSR = ''
    data = ()

    # abro primero el archivo en modo lectura para revisar si existe algun usuario con el mismo nombre

    if ExisteFile.checkFileExistance('Archivos/usuarios.csv'):
        with open("Archivos/usuarios.csv") as csvfichero:
            reader = csv.reader(csvfichero, delimiter=',')
            data = list(reader)

    # Solicito el nombre para recorrer el csv e indicar que si existe que no se puede crear.
    # Envio los datos del archivo y el nombre a la funcion Recorrer -- recorre

    nombre = ''
    while len(nombre) <= 1:
        print("DATOS PARA REGISTRAR UN NUEVO USUARIO: ")
        nombre = input("\nNombre de usuario: ").lower()

    if Recorrer.recorreUsuario(data, nombre):
        return "El usuario ya existe"
    else:
        seguridad = LOGIN.GeneradorPassw.generadorPW()
        rolUSR = ElegirRol.rol()
        # print(seguridad)
        print("Hay que crear la contraseña con los parámetros marcados.")
        # Necesito saber como escribir el true=si y falso = no
        print("Recuerda:"
              "\nTiene que tener una longitud", seguridad[0],
              "\nMayusculas", seguridad[1],
              "\nMinusculas", seguridad[2],
              "\nSímbolos", seguridad[3],
              "\nNúmeros", seguridad[4])

        # llamar a una funcion que diga: fortaleza XXXX

        print("Su contraseña es:", LOGIN.Fortaleza.fort(seguridad))
        contrasenna = LOGIN.CrearPW.TuPW(seguridad)
        with open("Archivos/usuarios.csv", 'a+', newline='') as usuariosEscribirCSV:
            columnas = ['usuario', 'password', 'rol']
            writer = csv.DictWriter(usuariosEscribirCSV, fieldnames=columnas)
            writer.writerow({'usuario': nombre, 'password': contrasenna, 'rol': rolUSR})
        return "Usuario creado"
