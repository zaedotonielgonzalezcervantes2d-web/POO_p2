import mysql.connector

try:
    conexion= mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='bd_estudiantes'
    )
    cursor=conexion.cursor(buffered=True)
    print("Conexión exitosa a la base de datos.")

except:
    print(f"Lamentablemente, por el momento no es posible conectarse a la base de datos...")