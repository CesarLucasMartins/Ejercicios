# Partiendo de la base del ejercicio de CLASES, se pide:
#  Que la clase Docente, sea herencia de la clase Usuario.

class Usuario:
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono_celular = telefono_celular
        self.email = email

usuario1 = Usuario("Gaston", "Ferretti", "44528956", "20/03/2001", "Chascomus 454", "Bs As", "0245", "Junin", "0263458974", "Tonga@gmail.com")

class Docente(Usuario):
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email):
        super().__init__(nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email)

docente1 = Docente("Gladis", "Sarabia", "38456925", "20/05/1980", "Quilmes 2415", "Cordoba", "5000", "Cordoba", "01154689526","profe@gmail.com")
print("información del docente: ")
print(f"Nombre: {docente1.nombre} {docente1.apellido}")
print(f"DNI: {docente1.dni}")
print(f"Email: {docente1.email}")
print()


#  Generar una clase nueva que sea compra y contenga:
# o Id_Compra
# o Id_Carrito_Compra
# o Id_Medios_Pago
# o Id_Usuario
# o Fecha
# o Monto_Total

class Compra:
    def __init__(self, Id_Compra, Id_Carrito_Compra, Id_Medios_Pago, Id_Usuario, Fecha, Monto_Total):
        self.Id_Compra = Id_Compra
        self.Id_Carrito_Compra = Id_Carrito_Compra
        self.Id_Medios_Pago = Id_Medios_Pago
        self.Id_Usuario = Id_Usuario
        self.Fecha = Fecha
        self.Monto_Total = Monto_Total

compra = Compra("323", "013", "222", "123456", "05/09/2023", 200)

#  Generar una clase de Medios de Contacto que contenga:
# o Id_MedioContacto
# o Fecha
# o Email
# o Telefono
# o Direccion
# o Nombre

class MediosDeContacto:
    def __init__(self, Id_MedioContacto, Fecha, Email, Telefono, Direccion, Nombre):
        self.Id_MedioContacto = Id_MedioContacto
        self.Fecha = Fecha
        self.Email = Email
        self.Telefono = Telefono
        self.Direccion = Direccion
        self.Nombre = Nombre

#  Generar una clase que sea: Tipos de Medio de Contacto en formato enum:
# o WhatsApp
# o Correo electrónico
# o Call center
# o Referido interno

#  La clase Tipos de Medio de Contacto debe heredar de Medios de contacto.

class TiposDeMedioDeContacto(MediosDeContacto):
    def __init__(self, Id_MedioContacto, Fecha, Email, Telefono, Direccion, Nombre, Tipo):
        super().__init__(Id_MedioContacto, Fecha, Email, Telefono, Direccion, Nombre)
        self.Tipo = Tipo


whatsapp_contacto = TiposDeMedioDeContacto("222", "07/07/2020", "", "351456842", "losa 55", "Julia Acosta", "WhatsApp")
correo_contacto = TiposDeMedioDeContacto("223", "10/10/2021", "Maria@gmail.com", "", "Arias 22", "María Rodríguez", "Correo electrónico")
call_center_contacto = TiposDeMedioDeContacto("224", "11/8/2022", "", "3512045789", "Lujan 78", "Carlos Rene", "Call center")
referido_interno_contacto = TiposDeMedioDeContacto("225", "06/12/2023", "", "", "Sociedad b 458", "Ana Gache", "Referido interno")

print("Tipo de Medio de Contacto:", whatsapp_contacto.Tipo)
print("Tipo de Medio de Contacto:", correo_contacto.Tipo)
print("Tipo de Medio de Contacto:", call_center_contacto.Tipo)
print("Tipo de Medio de Contacto:", referido_interno_contacto.Tipo)
