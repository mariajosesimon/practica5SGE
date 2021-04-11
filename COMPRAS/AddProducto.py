

def CrearProducto(db):
    nombreProducto = None
    precio = 0.0
    cantidad = None

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

    while cantidad == None:
        try:
            print("Cantidad a comprar: ")
            cantidad = int(input())
        except:
            cantidad = None
            print("Dato no valido.")

    datos = (nombreProducto, precio, cantidad)
    insertarProd = "INSERT INTO productoscomprados( NombreProducto, 	Precio, Stock) VALUES (%s, %s, %s)"
    cursor = db.cursor()
    cursor.execute(insertarProd, datos)
    print("Se ha añadido el producto a la base de datos.")

    db.commit()


    print("Se ha creado el producto.")

