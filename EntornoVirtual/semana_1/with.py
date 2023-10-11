import psycopg2
from logger_base import log

conexion = psycopg2.connect(
    user="postgres",
    password="jesus123",
    host="localhost",
    port="5432",
    database="prueba"
)

# INSERT
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "INSERT INTO clientes(id_cliente, nombre) Values(%s,%s)"
            valores = (
                ("4","Jesus"),
                ("5","Alfonso"),
                ("6","Pedro")
            )
            cursor.executemany(sentencia,valores)
            registros_insertados = cursor.rowcount 
            log.debug(f"Registros insertados: {registros_insertados}")
except Exception as e:
    log.error(e)
finally:
    conexion.close()