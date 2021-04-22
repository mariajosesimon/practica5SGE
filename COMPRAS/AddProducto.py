

def CrearProducto(db, tabla):
    nombreProducto = None
    precio = 0.0


    print("Datos para crear nuevo producto.")

    while nombreProducto == None or nombreProducto == "":
        print("Nombre producto: ")
        nombreProducto = input().title()

    while precio == None or precio == 0.0:
        try:
            print("Precio: ")
            precio = float(input())
        except:
            print("El precio introducido no es válido.")


    datos = ( nombreProducto, precio)
    insertarProd = "INSERT INTO " + tabla + " ( NombreProducto, Precio) VALUES (%s, %s )"
    cursor = db.cursor()
    cursor.execute(insertarProd, datos)
    print("Se ha añadido el producto a la base de datos.")

    db.commit()


    print("Se ha creado el producto.")

