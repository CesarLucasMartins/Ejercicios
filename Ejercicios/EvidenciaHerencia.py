# Partiendo de la base del ejercicio de CLASES, se pide:
#  Que la clase Docente, sea herencia de la clase Usuario.

from EvidenciaClass import Usuario

class Docente(Usuario):
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email):
        super().__init__(nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email)

#  Generar una clase nueva que sea compra y contenga:
# o Id_Compra
# o Id_Carrito_Compra
# o Id_Medios_Pago
# o Id_Usuario
# o Fecha
# o Monto_Total

class Compra:
    def __init__(self, Id_Compra, Id_Carrito_Compra, Id_Medios_Pago, Id_Usuario, Fecha, Monto_Total):
        self._Id_Compra = Id_Compra
        self._Id_Carrito_Compra = Id_Carrito_Compra
        self._Id_Medios_Pago = Id_Medios_Pago
        self._Id_Usuario = Id_Usuario
        self._Fecha = Fecha
        self._Monto_Total = Monto_Total

    def get_Id_Compra(self):
        return self._Id_Compra

    def set_Id_Compra(self, nuevo_Id_Compra):
        self._Id_Compra = nuevo_Id_Compra

    def get_Id_Carrito_Compra(self):
        return self._Id_Carrito_Compra

    def set_Id_Carrito_Compra(self, nuevo_Id_Carrito_Compra):
        self._Id_Carrito_Compra = nuevo_Id_Carrito_Compra

    def get_Id_Medios_Pago(self):
        return self._Id_Medios_Pago

    def set_Id_Medios_Pago(self, nuevo_Id_Medios_Pago):
        self._Id_Medios_Pago = nuevo_Id_Medios_Pago

    def get_Id_Usuario(self):
        return self._Id_Usuario

    def set_Id_Usuario(self, nuevo_Id_Usuario):
        self._Id_Usuario = nuevo_Id_Usuario

    def get_Fecha(self):
        return self._Fecha

    def set_Fecha(self, nueva_Fecha):
        self._Fecha = nueva_Fecha

    def get_Monto_Total(self):
        return self._Monto_Total

    def set_Monto_Total(self, nuevo_Monto_Total):
        self._Monto_Total = nuevo_Monto_Total

#  Generar una clase de Medios de Contacto que contenga:
# o Id_MedioContacto
# o Fecha
# o Email
# o Telefono
# o Direccion
# o Nombre

class MediosDeContacto:
    def __init__(self, Id_MedioContacto, Fecha, Email, Telefono, Direccion, Nombre):
        self._Id_MedioContacto = Id_MedioContacto
        self._Fecha = Fecha
        self._Email = Email
        self._Telefono = Telefono
        self._Direccion = Direccion
        self._Nombre = Nombre

    def get_Id_MedioContacto(self):
        return self._Id_MedioContacto

    def set_Id_MedioContacto(self, nuevo_Id_MedioContacto):
        self._Id_MedioContacto = nuevo_Id_MedioContacto

    def get_Fecha(self):
        return self._Fecha

    def set_Fecha(self, nueva_Fecha):
        self._Fecha = nueva_Fecha

    def get_Email(self):
        return self._Email

    def set_Email(self, nuevo_Email):
        self._Email = nuevo_Email

    def get_Telefono(self):
        return self._Telefono

    def set_Telefono(self, nuevo_Telefono):
        self._Telefono = nuevo_Telefono

    def get_Direccion(self):
        return self._Direccion

    def set_Direccion(self, nueva_Direccion):
        self._Direccion = nueva_Direccion

    def get_Nombre(self):
        return self._Nombre

    def set_Nombre(self, nuevo_Nombre):
        self._Nombre = nuevo_Nombre

#  Generar una clase que sea: Tipos de Medio de Contacto en formato enum:
# o WhatsApp
# o Correo electrónico
# o Call center
# o Referido interno

#  La clase Tipos de Medio de Contacto debe heredar de Medios de contacto.

class TiposDeMedioDeContacto(MediosDeContacto):
    def __init__(self, Id_MedioContacto, Fecha, Email, Telefono, Direccion, Nombre, Tipo):
        super().__init__(Id_MedioContacto, Fecha, Email, Telefono, Direccion, Nombre)
        self._Tipo = Tipo
      
    def get_Tipo(self):
        return self._Tipo

    def set_Tipo(self, nuevo_Tipo):
        self._Tipo = nuevo_Tipo
        
"""compra = Compra("579", "456", "789", "usuario123", "2023-09-11", 500.0)

id_compra = compra.get_Id_Compra()
print(f"Id de Compra: {id_compra}")
nuevo_id_compra = "789"
compra.set_Id_Compra(nuevo_id_compra)
print(f"Nuevo Id de Compra: {compra.get_Id_Compra()}")"""

