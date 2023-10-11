import psycopg2
from logger_base import log

conexion = psycopg2.connect(
    user="postgres",
    password="jesus123",
    host="localhost",
    port="5432",
    database="prueba"
)

# UPDATE
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "DELETE FROM clientes WHERE id_cliente=%s"
            entrada = input("ID´s a eliminar")
            valores = tuple((entrada.split(',')),)
            cursor.executemany(sentencia,valores)
            registros_eliminados = cursor.rowcount 
            log.debug(f"Registros Eliminados: {registros_eliminados}")
except Exception as e:
    log.error(e)
finally:
    conexion.close()