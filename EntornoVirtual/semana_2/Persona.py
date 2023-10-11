from logger_base import log

class Persona:
    def __init__(self, id_cliente = None, nombre = None, apellido = None, email = None) -> None:
        self.id_cliente = id_cliente
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        
    def __str__(self) -> str:
        return f"""
    ID_CLIENTE:{self.id_cliente}, Nombre: {self._nombre}
    Apellido:{self._apellido}, Email:{self._email}
    """
    
    @property
    def idCliente(self):
        return self.id_cliente
    @idCliente.setter
    def idCliente(self,id_cliente):
        self.id_cliente = id_cliente
        
    @property
    def Nombre(self):
        return self._nombre
    @Nombre.setter
    def Nombre(self,nombre):
        self.nombre = nombre
    
    @property
    def Apellido(self):
        return self._apellido
    @Apellido.setter
    def Apellido(self,apellido):
        self._apellido = apellido
        
    @property
    def Email(self):
        return self._email
    @Email.setter
    def Email(self,email):
        self._email = email
        
if __name__ == "__main__":
    persona1 = Persona(7, "Alfonso", "Andrade", "Jesus@gmail.com")
    log.debug(persona1)
    