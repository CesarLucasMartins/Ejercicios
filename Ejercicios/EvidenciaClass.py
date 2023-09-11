class CursoDeOficio:
    def __init__(self, fecha_comienzo, titulo, descripcion, objetivo, programa, costo, duracion, foto, estado, categoria):
        self.fecha_comienzo = fecha_comienzo
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
        return self.fecha_comienzo

    def set_fecha_comienzo(self, nueva_fecha_inicio):
        self.fecha_comienzo = nueva_fecha_inicio

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def get_descripcion(self):
        return self.descripcion

    def set_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

    def get_objetivo(self):
        return self.objetivo

    def set_objetivo(self, nuevos_objetivo):
        self.objetivo = nuevos_objetivo

    def get_programa(self):
        return self.programa

    def set_programa(self, nuevo_programa):
        self.programa = nuevo_programa

    def get_costo(self):
        return self.costo

    def set_costo(self, nuevo_costo):
        self.costo = nuevo_costo

    def get_duracion(self):
        return self.duracion

    def set_duracion(self, nueva_duracion):
        self.duracion = nueva_duracion

    def get_foto(self):
        return self.foto

    def set_foto(self, nueva_foto):
        self.foto = nueva_foto

    def get_estado(self):
        return self.estado

    def set_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def get_categoria(self):
        return self.categoria

    def set_categoria(self, nueva_categoria):
        self.categoria = nueva_categoria

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase:
    def __init__(self, fecha, titulo, contenido, URLDrive):
        self.fecha = fecha
        self.titulo = titulo
        self.contenido = contenido
        self.URLDrive = URLDrive

    def get_fecha(self):
        return self.fecha

    def set_fecha(self, nueva_fecha):
        self.fecha = nueva_fecha

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def get_contenido(self):
        return self.contenido

    def set_contenido(self, nuevo_contenido):
        self.contenido = nuevo_contenido

    def get_URLDrive(self):
        return self.URLDrive

    def set_URLDrive(self, nueva_URLDrive):
        self.URLDrive = nueva_URLDrive

class Docente:
    def __init__(self, apellido, nombre, dni, fecha_nacimiento, direccion, localidad, cod_postal, provincia, telefono_celular, email):
        self.apellido = apellido
        self.nombre = nombre
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.localidad = localidad
        self.cod_postal = cod_postal
        self.provincia = provincia
        self.telefono_celular = telefono_celular
        self.email = email
        self.estado = "Activo"
        self.roles = ["Docente"]

    def get_apellido(self):
        return self.apellido

    def set_apellido(self, nuevo_apellido):
        self.apellido = nuevo_apellido

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_dni(self):
        return self.dni

    def set_dni(self, nuevo_dni):
        self.dni = nuevo_dni

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def set_fecha_nacimiento(self, nueva_fecha_nacimiento):
        self.fecha_nacimiento = nueva_fecha_nacimiento

    def get_direccion(self):
        return self.direccion

    def set_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion

    def get_localidad(self):
        return self.localidad

    def set_localidad(self, nueva_localidad):
        self.localidad = nueva_localidad

    def get_cod_postal(self):
        return self.cod_postal

    def set_cod_postal(self, nuevo_cod_postal):
        self.cod_postal = nuevo_cod_postal

    def get_provincia(self):
        return self.provincia

    def set_provincia(self, nueva_provincia):
        self.provincia = nueva_provincia

    def get_telefono_celular(self):
        return self.telefono_celular

    def set_telefono_celular(self, nuevo_telefono_celular):
        self.telefono_celular = nuevo_telefono_celular

    def get_email(self):
        return self.email

    def set_email(self, nuevo_email):
        self.email = nuevo_email

class UsuarioFinal:
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
        self.carrito_compras = CarritoCompras()

    def activar_cuenta(self):
        if "@" in self.email:
            self.activado = True
            print(f"Cuenta activada con éxito {self.email}.")
        else:
            print(f"Correo inválido. La cuenta {self.email} es inválida, no se pudo activar.")

    def agregar_al_carrito(self, curso):
        self.carrito_compras.agregar_curso(curso)

    def seleccionar_medio_pago(self, nombre_medio_pago, detalles_medio_pago):
        self.medio_pago = {"nombre": nombre_medio_pago, "detalles": detalles_medio_pago}

    def confirmar_compra(self):
        if self.activado and self.medio_pago:
            monto_total = self.carrito_compras.calcular_total()
            print(f"--║ Compra Confirmada! ║-- {self.nombre} {self.apellido}. Monto total: ${monto_total}")
            print("GRACIAS POR SU COMPRA!")
        else:
            print("No se puede confirmar la compra. Verifique que su cuenta esté activada y que haya seleccionado un medio de pago.")

class CarritoCompras:
    def __init__(self):
        self.cursos = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def calcular_total(self):
        total = sum(curso.costo for curso in self.cursos)
        return total

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
            print(f"{self.nombre} se ha inscripto en el curso {curso}.")
        else:
            print(f"{self.nombre} ya está inscripto en el curso {curso}.")

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

class Curso:
    def __init__(self, foto, titulo, duracion, costo):
        self.foto = foto
        self.titulo = titulo
        self.duracion = duracion
        self.costo = float(costo)

class MedioPago:
    def __init__(self, nombre, datos):
        self.nombre = nombre
        self.datos = datos

    def registrar_datos(self):
        pass

categoria_inicial = Categoria("Inicial")

curso_1 = CursoDeOficio("02-10-2023", "Metrologia", "uso de herramientas de medicion", "Analisis industrial", "a definir", 20000, "3 meses", "pic.jpg", "Disponible", categoria_inicial)
curso_2 = CursoDeOficio("05-09-2023", "CNC", "manejo de herramientas con cnc", "programar y utilizar cnc", "a definir", 30000, "3 meses", "pic.jpg", "Disponible", categoria_inicial)

if curso_1.estado == "Disponible":
    print("El curso de Metrologia está disponible.")
else:
    print("El curso de Metrologia no está disponible.")

if curso_2.estado == "Disponible":
    print("El curso de CNC está disponible.")
else:
    print("El curso de CNC no está disponible.")

info_curso1 = Clase("02-09-2023", "Introduccion", "Herramientas Basicas", "https://drive.google.com/file/d/1DMUj7i6_nUJWmhH1jt")

info_curso2 = Clase("05-09-2023", "Inicios industriales", "Herramientas", "https://drive.google.com/file/d/")

fecha = info_curso1.get_fecha()
print("La fecha de la clase:", fecha)

info_curso2.set_titulo("Inicios industriales")
print("Título de la clase:", info_curso2.get_titulo())

docente1 = Docente("Gache", "Jose", "34851268", "01/11/1989", "Lujan 254", "Cordoba", "5000", "Cordoba", "351456852", "jpse@gmail.com")
apellido = docente1.get_apellido()
print("Apellido del docente:", apellido)
docente1.set_nombre("Juan")
print("Nombre del docente:", docente1.get_nombre())

docente2 = Docente("Herrera", "Soledad", "25214589", "03/05/1976", "Avellamea 4587", "Cordoba", "5014", "Cordoba", "3514789562", "Sole@gmail.com")
print("Apellido del docente 2:", docente2.get_apellido())
print("Nombre del docente 2:", docente2.get_nombre())
print("DNI del docente 2:", docente2.get_dni())

carrito_compras = CarritoCompras()

usuario1 = UsuarioFinal("Gaston", "Ferretti", "44528956", "20/03/2001", "Chascomus 454", "Bs As", "0245", "Junin", "0263458974", "Tonga@gmail.com", "Hola123")
usuario1.activar_cuenta()


usuario2 = UsuarioFinal("Florencia", "Funes", "405462541", "29/08/1992", "Tablada 589", "Cordoba", "5000", "Cordoba", "351236841", "Flor@gmail.com", "ispc4587")
usuario2.activar_cuenta()

usuario1.agregar_al_carrito(curso_1)
usuario1.agregar_al_carrito(curso_2)
usuario1.seleccionar_medio_pago("Tarjeta de Crédito", "Número de tarjeta: 5458 0077 1458 1258")
usuario1.confirmar_compra()

print(f"Nombre: {usuario1.nombre} {usuario1.apellido}")
print("Cursos en el carrito:")
for curso in usuario1.carrito_compras.cursos:
    print(f"- {curso.titulo}: ${curso.costo}")
print(f"Medio de pago: {usuario1.medio_pago}")
