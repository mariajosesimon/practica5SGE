import pymysql

def conexion():
    # Establecemos conexión con la base de datos
    db = pymysql.connect(host="127.0.0.1", user="root", db="mibd", port=3306)



