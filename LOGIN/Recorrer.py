


# Revisa si el usuario existe antes de dar de alta un nuevo usuario.
def recorreUsuario(archivo, user):
    existe = False
    for fila in archivo:
        if fila[0] == user:
            existe = True
    return existe


# Revisa que ha escrito los datos correcto de usuario y contraseña en el login.
def recorrePassword(archivo, user, password):
    existe = [False, 0]
    for fila in archivo:
        if fila[0] == user and fila[1] == password:
            existe = [True, fila[2]] # DEVUELVE TRUE + EL ROL.
            ##### AQUI GUARDO EL USUARIO EN UN ARCHIVO QUE SE BORRE CADA VEZ QUE SE ABRA.
            almacenLogin =  open("Archivos/login.txt", 'w+')
            almacenLogin.write(user)
            almacenLogin.close()
    return existe

