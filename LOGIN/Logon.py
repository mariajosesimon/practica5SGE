import pymysql

def logarse(db):
    print("USUARIO: ")
    usr = input()
    print("CONTRASEÑA: ")
    password = input()

    # aqui tengo que revisar:
    # - si el usuario y si la contraseña son correctas accederá al menu correspondiente y además está en activo
    # - si el usuario existe y la contraseña es incorrecta, podrá ir a cambiar la contraseña.
    # - si el usuario no existe, debe salir un mensaje indicando que un usuario de RH debe darlo de alta.

    cursor = db.cursor()

    # Existe el usuario
    usrExiste = 'SELECT usuario FROM usuarios WHERE  usuario = "' + usr + '"'
    cursor.execute(usrExiste)
    usuarioExiste = cursor.fetchone()

    if usuarioExiste == None:
        return (print("El usuario no existe. \nContacte con RH para dar de alta."))
    else:
        #El usuario está activo?
        activo = 'SELECT activo FROM usuarios WHERE  usuario = "' + usr + '"'
        cursor.execute(activo)
        usrActivo = cursor.fetchone()

        if usrActivo[0] == 0:
            return (print("El usuario no está activo. \nContacte con RH para activar."))
        else:
            # Existe el usuario y contraseña + usuario está activo nos devuelve todos los datos del usuario.
            consultaUSR = 'SELECT * FROM usuarios WHERE usuario = "' + usr + '" and password = "' + password + '" '
            cursor.execute(consultaUSR)
            resultado = cursor.fetchall()

            dept=None

            for a in resultado:
                dept = a[7]
            if id != None:
                # Voy a utilizar una tabla para guardar el usuario logado.

                cursor.execute("DROP TABLE IF EXISTS USERLOGIN")
                tabla = "CREATE TABLE USERLOGIN AS (" + consultaUSR + ")"
                cursor.execute(tabla)
                #Devolvemos el código de departamento, ya que en funcion de éste mostrará un menu u otro.
                return(dept)

            else:
                return(print("Contraseña incorrecta"))

