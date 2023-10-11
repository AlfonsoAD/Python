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
            sentencia = "UPDATE clientes set nombre=%s WHERE id_cliente=%s"
            valores = (
                ("Luis",1),
                ("Jesus",2),
            )
            cursor.executemany(sentencia,valores)
            registros_actualizados = cursor.rowcount 
            log.debug(f"Registros Actualizados: {registros_actualizados}")
except Exception as e:
    log.error(e)
finally:
    conexion.close()