from Persona import Persona
from conexion import conexion
from cursor_del_pool import Cursor_del_Pool
from logger_base import log

class PersonaDAO:
    _SELECCIONAR = "SELECT * From clientes ORDER BY id_cliente"
    _INSERTAR = "INSERT INTO clientes(id_cliente, nombre, apellido, email) VALUES(%s,%s,%s,%s)"
    _ACTUALIZAR = "UPDATE clientes SET nombre=%s, apellido=%s, email=%s WHERE id_cliente=%s"
    _DELETE = "DELETE FROM clientes WHERE id_cliente=%s"
    
    @classmethod
    def seleccionar(cls):
        with Cursor_del_Pool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            print(registros)
            clientes = []
            for r in registros:
                clientes.append(Persona(r[0], [1], [2], [3]))
            return clientes
    
    @classmethod
    def insertar(cls,cliente):
        with Cursor_del_Pool() as cursor:
            valores = (cliente.id_cliente,cliente.Nombre, cliente.Apellido, cliente.Email)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls,cliente):
        with Cursor_del_Pool() as cursor:
            valores = (cliente.Nombre, cliente.Apellido, cliente.Email,cliente.id_cliente)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
        
    @classmethod
    def eliminar(cls,id_cliente):
        with Cursor_del_Pool() as cursor:
            valores = (id_cliente)
            cursor.execute(cls._DELETE,valores)
            return cursor.rowcount
            
if __name__== "__main__":
    # Insertar a la BD
    persona1 = Persona(id_cliente="3",nombre="Juan", apellido="Perez",email="juanperez@gmail.com")
    insercion = PersonaDAO.insertar(persona1)
    log.debug("Clientes agregados", insercion)
    # Update
    persona1.idCliente = 1
    actualizar = PersonaDAO.actualizar(persona1)
    log.debug("Cliente actualizado")
    # Delete
    eliminar = PersonaDAO.eliminar(6)
    log.debug("Cliente eliminado")
    # Select de los registros en la BD
    clientes = PersonaDAO.seleccionar()
    for cliente in clientes:
        log.debug(cliente)
        