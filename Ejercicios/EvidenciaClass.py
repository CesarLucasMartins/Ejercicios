#1. Crear todas las clases que fueran necesarias para iniciar un proceso de desarrollo de
# software de la siguiente situación:
# Una empresa privada que se dedica a la venta de cursos de oficios, desea desarrollar un
# sistema web para poder publicar su oferta académica. Dicho sistema debe mostrar una serie
# de cursos disponibles.
# Por cada curso se deberá visualizar la fecha de comienzo, título, descripción, objetivos,
# programa, costo, duración en meses, foto y estado (disponible o no disponible, en base a su
# estado deberán verse o no en el sitio).
# A su vez, cada curso pertenece a alguna de las
# siguientes categorías (Inicial, Intermedio, Avanzado). 

class curso_de_oficio:
    def __init__(self, fecha_comiezo, titulo, descripcion, objetivo, programa, costo, duracion, foto, estado, categoria):
        self.fecha_comienzo = fecha_comiezo
        self.titulo = titulo
        self.descripcion = descripcion
        self.objetivo = objetivo
        self.programa = programa
        self.costo = costo
        self.duracion = duracion
        self.foto = foto
        self.estado = estado
        self.categoria = categoria

    def get_fecha_comienzo(self):
        return self._fecha_inicio

    def set_fecha_comienzo(self, nueva_fecha_inicio):
        self._fecha_inicio = nueva_fecha_inicio

    def get_titulo(self):
        return self._titulo

    def set_titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo

    def get_descripcion(self):
        return self._descripcion

    def set_descripcion(self, nueva_descripcion):
        self._descripcion = nueva_descripcion

    def get_objetivo(self):
        return self._objetivo

    def set_objetivo(self, nuevos_objetivo):
        self._objetivo = nuevos_objetivo

    def get_programa(self):
        return self._programa

    def set_programa(self, nuevo_programa):
        self._programa = nuevo_programa

    def get_costo(self):
        return self._costo

    def set_costo(self, nuevo_costo):
        self._costo = nuevo_costo

    def get_duracion(self):
        return self._duracion

    def set_duracion(self, nueva_duracion):
        self._duracion = nueva_duracion

    def get_foto(self):
        return self._foto

    def set_foto(self, nueva_foto):
        self._foto = nueva_foto

    def get_estado(self):
        return self._estado

    def set_estado(self, nuevo_estado):
        self._estado = nuevo_estado

    def get_categoria(self):
        return self._categoria

    def set_categoria(self, nueva_categoria):
        self._categoria = nueva_categoria

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

categoria_inicial = Categoria ("Inicial")

curso_1 = curso_de_oficio ("02-10-2023", "Metrologia" , "uso de herramientas de medicion", "Analisis industrial", " a definir", "$20.000", "3 meses", "pic.jpg", "Disponible", categoria_inicial) 

curso_2 = curso_de_oficio ("05-09-2023", "CNC", "manejo de herramientas con cnc" , "programar y utilizar cnc" , "a definir" , "$30.000" , "3 meses", "pic.jpg", "Disponible", categoria_inicial)

if curso_1.estado:
    print("El curso de Metrologia está disponible.")
else:
    print("El curso de Metrologia no está disponible.")

if curso_2.estado:
    print("El curso de CNC está disponible.")
else:
    print("El curso de CNC no está disponible.")




#Por otro lado, los cursos contienen un
# conjunto de clases, en donde por cada clase se debe mostrar la fecha, título, contenido,
# URLDrive.

class Clase:
    def __init__(self, fecha, titulo, contenido, URLDrive):
        self._fecha = fecha
        self._titulo = titulo
        self._contenido = contenido
        self._URLDrive = URLDrive

    def get_fecha(self):
        return self._fecha

    def set_fecha(self, nueva_fecha):
        self._fecha = nueva_fecha

    def get_titulo(self):
        return self._titulo

    def set_titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo

    def get_contenido(self):
        return self._contenido

    def set_contenido(self, nuevo_contenido):
        self._contenido = nuevo_contenido

    def get_URLDrive(self):
        return self._URLDrive

    def set_URLDrive(self, nueva_URLDrive):
        self._URLDrive = nueva_URLDrive

info_curso1 = Clase("02-09-2023", "Introduccion", "Herramientas Basicas", "https://drive.google.com/file/d/1DMUj7i6_nUJWmhH1jt")

info_curso2 = Clase("05-09-2023", "Inicios industriales", "Herramientas", "https://drive.google.com/file/d/")

fecha = info_curso1.get_fecha()
print("La fecha de la clase:", fecha)

info_curso2.set_titulo("Inicios industriales")
print("Título de la clase:", info_curso2.get_titulo())



# Cada clase de un curso la dicta un docente, y este puede participar en el dictado de varias
# clases y de varios cursos. De cada docente se desea guardar su apellido, nombre, dni, fecha
# nacimiento, dirección, localidad, código postal, provincia, teléfono celular, email.


class Docente:
    def __init__(self, apellido, nombre, dni, fecha_nacimiento, direccion, localidad, cod_postal, provincia, telefono_celular, email):
        self._apellido = apellido
        self._nombre = nombre
        self._dni = dni
        self._fecha_nacimiento = fecha_nacimiento
        self._direccion = direccion
        self._localidad = localidad
        self._cod_postal = cod_postal
        self._provincia = provincia
        self._telefono_celular = telefono_celular
        self._email = email

    
    def get_apellido(self):
        return self._apellido

    def set_apellido(self, nuevo_apellido):
        self._apellido = nuevo_apellido

    
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    
    def get_dni(self):
        return self._dni

    def set_dni(self, nuevo_dni):
        self._dni = nuevo_dni

    
    def get_fecha_nacimiento(self):
        return self._fecha_nacimiento

    def set_fecha_nacimiento(self, nueva_fecha_nacimiento):
        self._fecha_nacimiento = nueva_fecha_nacimiento

    
    def get_direccion(self):
        return self._direccion

    def set_direccion(self, nueva_direccion):
        self._direccion = nueva_direccion

    
    def get_localidad(self):
        return self._localidad

    def set_localidad(self, nueva_localidad):
        self._localidad = nueva_localidad

    
    def get_cod_postal(self):
        return self._cod_postal

    def set_cod_postal(self, nuevo_cod_postal):
        self._cod_postal = nuevo_cod_postal

    
    def get_provincia(self):
        return self._provincia

    def set_provincia(self, nueva_provincia):
        self._provincia = nueva_provincia

    
    def get_telefono_celular(self):
        return self._telefono_celular

    def set_telefono_celular(self, nuevo_telefono_celular):
        self._telefono_celular = nuevo_telefono_celular

    
    def get_email(self):
        return self._email

    def set_email(self, nuevo_email):
        self._email = nuevo_email


docente1 = Docente ("Gache", "Jose", "34851268", "01/11/1989", "Lujan 254", "Cordoba", "5000", "Cordoba", "351456852", "jpse@gmail.com")

apellido = docente1.get_apellido()
print("Apellido del docente:", apellido)

docente1.set_nombre("Juan")
print("Nombre del docente:", docente1.get_nombre())

docente2 = Docente("Herrera", "Soledad", "25214589", "03/05/1976", "Avellamea 4587", "Cordoba", "5014", "Cordoba", "3514789562", "Sole@gmail.com")

print("Apellido del docente 2:", docente2.get_apellido())
print("Nombre del docente 2:", docente2.get_nombre())
print("DNI del docente 2:", docente2.get_dni())



# Por otra parte, los interesados en inscribirse a un curso deberán crearse una cuenta de usuario
# final, donde deberán registrar su datos personales (nombre, apellido, dni, dirección, fecha
# nacimiento, dirección, localidad, código postal, provincia, teléfono celular, email), además de
# confirmar y reconfirmar una clave de acceso. Para la activación de la cuenta de usuario final se
# deberá validar que el email sea verdadero y esté en funcionamiento, enviando un correo
# automático al email registrado.

class Usuario_Final:
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email, clave_acceso):
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
        self.clave_acceso = clave_acceso
        self.activado = False 

    def activar_cuenta(self):
        if "@" in self.email:
            self.activado = True
            print(f"Cuenta activada con éxito {self.email}.")
        else:
            print(f"Correo inválido. La cuenta {self.email} es invalida, no se pudo activar.")

usuario1 = Usuario_Final("Gaston", "Ferretti", "44528956", "20/03/2001", "Chascomus 454", "Bs As", "0245", "Junin", "0263458974", "Tonga@gmail.com", "Hola123")

usuario1.activar_cuenta()

usuario2 = Usuario_Final("Florencia", "Funes", "405462541", "29/08/1992", "Tablada 589 ", "Cordoba", "5000", "Cordoba", "351236841", "Florgmail.com", "ispc4587")

usuario2.activar_cuenta()





    
# Los usuarios públicos registrados pueden inscribirse a uno o más cursos. 
# Además, el sitio
# deberá proveer la posibilidad de registrar 2 roles más de usuarios quienes también tendrán
# interacción con el sistema: Administrador, Docente. Los usuarios también deben tener
# asociado un estado (Activo / Inactivo).

class Usuario:
    def __init__(self, nombre, apellido, dni, direccion, fecha_nacimiento, email, telefono, clave_acceso, estado):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
        self.email = email
        self.telefono = telefono
        self.clave_acceso = clave_acceso
        self.estado = estado
        self.roles = []
        self.cursos_inscriptos = []

    def agregar_rol(self, rol):
        self.roles.append(rol)

    def quitar_rol(self, rol):
        if rol in self.roles:
            self.roles.remove(rol)
    
    def inscripcion_a_curso(self, curso):
        if curso not in self.cursos_inscriptos:
            self.cursos_inscriptos.append(curso)
            print(f"{self.nombre} se ha inscrito en el curso {curso}.")
        else:
            print(f"{self.nombre} ya está inscrito en el curso {curso}.")

    

class Administrador:
    def __init__(self, nombre, apellido, dni, direccion, fecha_nacimiento, email, telefono, clave_acceso):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
        self.email = email
        self.telefono = telefono
        self.clave_acceso = clave_acceso
        self.estado = "Activo"
        self.roles = ["Administrador"]

    def deshabilitar_cuenta(self, usuario):
        usuario.estado = "Inactivo"
        print(f"Cuenta de {usuario.nombre} deshabilitada.")


class Docente:
    def __init__(self, nombre, apellido, dni, direccion, fecha_nacimiento, email, telefono, clave_acceso):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
        self.email = email
        self.telefono = telefono
        self.clave_acceso = clave_acceso
        self.estado = "Activo"
        self.roles = ["Docente"]

    def dictar_clase(self, clase):
        self.clases_dictadas.append(clase)
        print(f"{self.nombre} ha dictado la clase: {clase}.")


estudiante1 = Usuario("Gaston", "Ferretti", "44528956", "Chascomus 454", "20/03/2001", "Tonga@gmail.com", "0263458974", "Hola123", "Activo")
admin1 = Administrador("Admin", "Admin", "40125856", "Valparaiso 874", "15/03/1999", "admin@gmail.com", "351247896", "admin1234")
docente1 = Docente("Gladis", "Sarabia", "38456925", "Quilmes 2415", "20/05/1980", "profe@gmail.com", "01154689526", "profe1234")

estudiante1.agregar_rol("Estudiante")

estudiante1.estado = "Inactivo"

print(f"{estudiante1.nombre} tiene los siguientes roles: {', '.join(estudiante1.roles)}")
print(f"Estado de {estudiante1.nombre}: {estudiante1.estado}")

print(f"{admin1.nombre} tiene los siguientes roles: {', '.join(admin1.roles)}")
print(f"Estado de {admin1.nombre}: {admin1.estado}")

print(f"{docente1.nombre} tiene los siguientes roles: {', '.join(docente1.roles)}")
print(f"Estado de {docente1.nombre}: {docente1.estado}")




# Por último, los usuarios finales podrán agregar uno o más cursos en un carrito de compras,
# donde se deberá visualizar: Foto, título del curso, duración, costo. Una vez confirmados los
# ítems del carrito, deberá seleccionar el medio de pago, los cuales pueden ser: Tarjeta de
# crédito/débito y transferencia bancaria; a fin de tener más datos acerca de los medios de
# pago, deberán registrarse los datos básicos de tarjetas y transferencias). Al confirmar la
# compra, se deberá registrar además la fecha de compra, el usuario que realiza la compra y el
# monto total. Dada la consigna anterior, se pide: identificar, analizar y documentar los
# requisitos según el formato de historias de usuario. Para la creación de las historias, hacer uso
# del repositorio Github, a través de creación de issues.

class Usuario_Final:
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email, clave_acceso):
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
        self.clave_acceso = clave_acceso
        self.activado = False
        self.carrito_compras = None
        self.medio_pago = None

    def activar_cuenta(self):
        if "@" in self.email:
            self.activado = True
            print(f"Cuenta activada con éxito {self.email}.")
        else:
            print(f"Correo inválido. La cuenta {self.email} es invalida, no se pudo activar.")

    def agregar_al_carrito(self, curso):
        if self.carrito_compras is None:
            self.carrito_compras = CarritoCompras()
        self.carrito_compras.agregar_curso(curso)

    def seleccionar_medio_pago(self, medio_pago):
        self.medio_pago = medio_pago

    def confirmar_compra(self):
        if self.activado and self.medio_pago:
            monto_total = self.carrito_compras.calcular_total()
            print(f"Compra confirmada por {self.nombre} {self.apellido}. Monto total: ${monto_total}")
        else:
            print("No se puede confirmar la compra. Verifique que su cuenta esté activada y que haya seleccionado un medio de pago.")


class Curso:
    def __init__(self, foto, titulo, duracion, costo):
        self.foto = foto
        self.titulo = titulo
        self.duracion = duracion
        self.costo = costo


class CarritoCompras:
    def __init__(self):
        self.cursos = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def calcular_total(self):
        total = sum(curso.costo for curso in self.cursos)
        return total


class MedioPago:
    def __init__(self, nombre, datos):
        self.nombre = nombre
        self.datos = datos

    def registrar_datos(self):
        pass

curso1 = Curso("fotometro.jpg", "Curso de Metrologia", "3 meses", 20000)
curso2 = Curso("fotocnc.jpg", "Curso de CNC", "3 meses ",30000 )


usuario = Usuario_Final(
    "Gaston", "Ferretti", "44528956", "20/03/2001", "Chascomus 454", "Cordoba", "5000", "Provincia", "0263458974", "Tonga@gmail.com", "clave123")

usuario.activar_cuenta()

usuario.agregar_al_carrito(curso1)
usuario.agregar_al_carrito(curso2)

medio_pago = MedioPago("Tarjeta de Crédito", "Número de tarjeta: 1234-5678-1234-5678")
usuario.seleccionar_medio_pago(medio_pago)

usuario.confirmar_compra()
