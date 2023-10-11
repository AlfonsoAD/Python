from logger_base import log
from conexion import conexion

class Cursor_del_Pool:
    def __init__(self) -> None:
        self.__conexion = None
        self.__cursor = None
        
    def __enter__(self):
        log.debug("INICIO DE BLOQUE WITH")
        self.__conexion = conexion.obtener_conexion()
        self.__cursor = self.__conexion.cursor()
        return self.__cursor
    
    
    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.debug("SE EJECUTA EXIT")
        if valor_excepcion:
            self.__conexion.rollback()
        else:
            self.__conexion.commit()
        self.__cursor.close()
        conexion.liberar_conexion(self.__conexion)
    
if __name__ == "__main__":
    with Cursor_del_Pool() as cursor:
        log.debug("BLOQUE WITH")
        cursor.execute("SELECT * FROM clientes")
        log.debug(cursor.fetchall())
        