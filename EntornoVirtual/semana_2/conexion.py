import psycopg2
from psycopg2 import pool
from logger_base import log

class conexion:
    _DATABASE = "prueba"
    _USERNAME = "postgres"
    _PASSWORD = "jesus123"
    _HOST = "localhost"
    _PORT = "5432"
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None
    
    @classmethod
    def obtener_pool(cls):
        try:
            if cls._pool == None:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON,
                    cls._MAX_CON,
                    host = cls._HOST,
                    user = cls._USERNAME,
                    password = cls._PASSWORD,
                    port = cls._PORT,
                    database = cls._DATABASE
                )
                log.debug("CREACION DEL POOL", pool)
                return cls._pool
            else:
                return cls._pool
        except Exception as e :
            log.error(e)
            
                        
    @classmethod
    def obtener_conexion(cls):
        conexion = cls.obtener_pool().getconn()
        log.debug(f"CONEXION OBTENIDA {conexion}")
        return conexion
        
    @classmethod
    def liberar_conexion(cls, conexion):
        cls.obtener_pool().putconn(conexion)
        log.debug(f"CONEXION REGRESADA {conexion}")
        
    @classmethod
    def cerrar_conexiones(cls):
        cls.obtener_pool().closeall()
        log.debug("CONEXIONES CERRADAS")
        
        
        
        
