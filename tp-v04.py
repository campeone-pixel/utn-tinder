from datetime import datetime
import getpass
import math
import os.path
import pickle
import random

"""
Integrantes:
- Poses, Matias Abel
- Porcel, Santiago
- OROÑO, Martin
- Bellocci, Francisco
Comision 11
"""

# ------ Funciones para imprimir los datos --------


def listado_administradores():
    archivo_logico = abrir_archivo(AF_ADMINISTRADORES)
    tam = os.path.getsize(AF_ADMINISTRADORES)
    if tam == 0:
        print("No hay administradores para mostrar.")
    else:
        archivo_logico.seek(0, 0)
        print(f"{'ID':<5} {'Email':<25} {'Contraseña':<15}")
        print("-" * 50)
        while archivo_logico.tell() < tam:
            admin_archivo = reconvertir_a_admin(pickle.load(archivo_logico))
            salida = (
                f"{admin_archivo.nro_id:<5} "
                f"{admin_archivo.email:<25} "
                f"{admin_archivo.contrasenia:<15}"
            )
            print(salida)
        archivo_logico.close()


def imprimir_registro_puntero_administradores():
    tam = os.path.getsize(AF_ADMINISTRADORES)
    archivo_logico = abrir_archivo(AF_ADMINISTRADORES)
    while archivo_logico.tell() < tam:
        pickle.load(archivo_logico)
        print("Tamaño del archivo:", tam)
        print("Posición actual del puntero:", archivo_logico.tell())
    archivo_logico.close()


def imprimir_registro_puntero_likes():
    tam = os.path.getsize(AF_LIKES)
    archivo_logico = abrir_archivo(AF_LIKES)
    while archivo_logico.tell() < tam:
        registro_like = pickle.load(archivo_logico)
        print(
            f"Remitente: {registro_like.remitente}, Destinatario: {registro_like.destinatario}"
        )
        print("Tamaño del archivo:", tam)
        print("Posición actual del puntero:", archivo_logico.tell())

    archivo_logico.close()


def listado_likes():
    tam = os.path.getsize(AF_LIKES)
    if tam == 0:
        print("No hay likes para mostrar.")
    else:
        archivo_logico = abrir_archivo(AF_LIKES)
        archivo_logico.seek(0, 0)
        print(f"{'Remitente':<15} {'Destinatario':<15} {'sumado':<15} ")
        print("-" * 30)
        while archivo_logico.tell() < tam:
            like = pickle.load(archivo_logico)
            salida = (
                f"{like.remitente:<15} " f"{like.destinatario:<15}" f"{like.sumado:<15}"
            )
            print(salida)
        archivo_logico.close()


def listado_moderadores():
    archivo_logico = abrir_archivo(AF_MODERADORES)
    tam = os.path.getsize(AF_MODERADORES)
    if tam == 0:
        print("No hay moderadores para mostrar.")
    else:
        archivo_logico.seek(0, 0)
        print(
            f"{'ID':<5} {'Email':<25} {'Contraseña':<15} {'reportes_aceptados':<15} {'reportes_ignorados':<15} {'reportes_procesados':<15}"
        )
        print("-" * 50)
        while archivo_logico.tell() < tam:
            moderador_archivo = reconvertir_a_mod(pickle.load(archivo_logico))
            salida = (
                f"{moderador_archivo.nro_id:<5} "
                f"{moderador_archivo.email:<25} "
                f"{moderador_archivo.contrasenia:<15}"
                f"{moderador_archivo.reportes_aceptados:<15}"
                f"{moderador_archivo.reportes_ignorados:<15}"
                f"{moderador_archivo.reportes_procesados:<15}"
            )
            print(salida)
        archivo_logico.close()


def imprimir_registro_puntero_moderadores():
    tam = os.path.getsize(AF_MODERADORES)
    archivo_logico = abrir_archivo(AF_MODERADORES)
    while archivo_logico.tell() < tam:
        pickle.load(archivo_logico)
        print("Tamaño del archivo:", tam)
        print("Posición actual del puntero:", archivo_logico.tell())
    archivo_logico.close()


def listado_reportes():
    archivo_logico = abrir_archivo(AF_REPORTES)
    tam = os.path.getsize(AF_REPORTES)
    if tam == 0:
        print("No hay reportes para mostrar.")
    else:
        archivo_logico.seek(0, 0)
        print(
            f"{'ID':<5} {'reportante':<25} {'reportado':<15} {'razon':<15} {'estado':<15}"
        )
        print("-" * 50)
        while archivo_logico.tell() < tam:
            reporte_archivo = reconvertir_a_reporte(pickle.load(archivo_logico))
            salida = (
                f"{reporte_archivo.nro_id:<5} "
                f"{reporte_archivo.id_reportante:<25}"
                f"{reporte_archivo.id_reportado:<15}"
                f"{reporte_archivo.razon_reporte:<15}"
                f"{reporte_archivo.estado:<15}"
            )
            print(salida)
        archivo_logico.close()


def imprimir_registro_puntero_reportes():
    tam = os.path.getsize(AF_REPORTES)
    archivo_logico = abrir_archivo(AF_REPORTES)
    while archivo_logico.tell() < tam:
        pickle.load(archivo_logico)
        print("Tamaño del archivo:", tam)
        print("Posición actual del puntero:", archivo_logico.tell())
    archivo_logico.close()


def listado_alumnos(direccion):
    tam = os.path.getsize(direccion)
    if tam == 0:
        print("No hay nada para mostrar.")
    else:
        archivo_logico = abrir_archivo(direccion)
        archivo_logico.seek(0, 0)

        print(
            f"{'ID':<5} {'Email':<25} {'Nombre':<25} {'Sexo':<20} {'Contraseña':<25} {'Estado':<25} {'Fecha Nacimiento':<40} {'punto':<15}"
        )
        print("-" * 150)
        while archivo_logico.tell() < tam:
            alum_archivo = reconvertir_a_alu(pickle.load(archivo_logico))
            salida = (
                f"{alum_archivo.nro_id:<5} "
                f"{alum_archivo.email:<25} "
                f"{alum_archivo.nombre:<25} "
                f"{alum_archivo.sexo:<20} "
                f"{alum_archivo.contrasenia:<25} "
                f"{alum_archivo.estado:<25} "
                f"{str(alum_archivo.fecha_nacimiento):<40}"
                f"{str(alum_archivo.punto):<15}"
            )
            print(salida)

        archivo_logico.close()


def imprimir_registro_puntero_alumnos():
    tam = os.path.getsize(AF_ALUMNOS)
    archivo_logico = abrir_archivo(AF_ALUMNOS)
    while archivo_logico.tell() < tam:
        pickle.load(archivo_logico)
        print("tamanio del archivo", tam)
        print("donde esta el puntero", archivo_logico.tell())


# ------ Direccion archivos fisicos y control de archivos logicos --------


AF_ALUMNOS = ".\\alumnos.dat"
AF_MODERADORES = ".\\moderadores.dat"
AF_ADMINISTRADORES = ".\\administradores.dat"
AF_LIKES = ".\\likes.dat"
AF_REPORTES = ".\\reportes.dat"


def abrir_archivo(archivo_fisico):
    if os.path.exists(archivo_fisico):
        archivo_logico = open(archivo_fisico, "r+b")
    else:
        archivo_logico = open(archivo_fisico, "w+b")
    return archivo_logico


# ------ Manejo de Fechas --------

"""
var:
    edad: int
"""


def calcular_edad(fecha_nacimiento):

    edad = int((datetime.today() - fecha_nacimiento).days / 365.2425)
    return edad


def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


"""
var:
    anio: int
"""


def obtener_anio():
    while True:
        anio = input("Ingrese el año (aaaa): ")
        if anio.isdigit() and 1800 <= int(anio) <= datetime.now().year:
            return int(anio)
        print("Año inválido. Debe ser un número entre 1800 y el año actual.")


"""
var:
    mes: int
"""


def obtener_mes():
    while True:
        mes = input("Ingrese el mes (mm): ")
        if mes.isdigit() and 1 <= int(mes) <= 12:
            return int(mes)
        print("Mes inválido. Debe ser un número entre 01 y 12.")


"""
var:
    dia,max_dia: int
"""


def obtener_dia(anio, mes):
    max_dia = 0
    while True:
        dia = input("Ingrese el día (dd): ")
        if dia.isdigit():
            dia = int(dia)
            if mes in [1, 3, 5, 7, 8, 10, 12]:
                max_dia = 31
            elif mes in [4, 6, 9, 11]:
                max_dia = 30
            elif mes == 2:
                if es_bisiesto(anio):
                    max_dia = 29
                else:
                    max_dia = 28
            if 1 <= dia <= max_dia:
                return dia
            else:
                print(f"Día inválido para el mes {mes}. Debe ser entre 1 y {max_dia}.")
        else:
            print("Día inválido. Debe ser un número.")


"""
var:
    anio,mes,dia: int
"""


def pedir_fecha():
    anio = obtener_anio()
    mes = obtener_mes()
    dia = obtener_dia(anio, mes)
    mes_str = str(mes) if mes > 9 else "0" + str(mes)
    dia_str = str(dia) if dia > 9 else "0" + str(dia)
    return str(anio) + "/" + mes_str + "/" + dia_str


# ---- Alumnos ----
class Alu:
    def __init__(self):
        self.nro_id = 0
        self.email = ""
        self.nombre = ""
        self.sexo = ""
        self.contrasenia = ""
        self.estado = True
        self.hobbies = ""
        self.materia_favorita = ""
        self.deporte_favorito = ""
        self.materia_fuerte = ""
        self.materia_debil = ""
        self.biografia = ""
        self.pais = ""
        self.ciudad = ""
        self.fecha_nacimiento = datetime.strptime("1900/12/12", "%Y/%m/%d")
        self.punto = 0
        self.super_like_disponible = True
        self.credito_revelar = 1


def formatear_alum(self):
    self.nro_id = self.nro_id
    self.email = self.email.ljust(32)
    self.nombre = self.nombre.ljust(32)
    self.sexo = self.sexo.ljust(1)
    self.contrasenia = self.contrasenia.ljust(32)
    self.hobbies = self.hobbies.ljust(255)
    self.materia_favorita = self.materia_favorita.ljust(16)
    self.deporte_favorito = self.deporte_favorito.ljust(16)
    self.materia_fuerte = self.materia_fuerte.ljust(16)
    self.materia_debil = self.materia_debil.ljust(16)
    self.biografia = self.biografia.ljust(255)
    self.pais = self.pais.ljust(32)
    self.ciudad = self.ciudad.ljust(32)
    self.fecha_nacimiento = self.fecha_nacimiento.strftime("%Y/%m/%d").ljust(10)
    self.punto = self.punto
    self.super_like_disponible = self.super_like_disponible
    self.credito_revelar = self.credito_revelar
    return self


def reconvertir_a_alu(registro_formateado):
    alumno = Alu()
    alumno.nro_id = registro_formateado.nro_id
    alumno.email = registro_formateado.email.strip()
    alumno.nombre = registro_formateado.nombre.strip()
    alumno.sexo = registro_formateado.sexo.strip()
    alumno.contrasenia = registro_formateado.contrasenia.strip()
    alumno.estado = registro_formateado.estado
    alumno.hobbies = registro_formateado.hobbies.strip()
    alumno.materia_favorita = registro_formateado.materia_favorita.strip()
    alumno.deporte_favorito = registro_formateado.deporte_favorito.strip()
    alumno.materia_fuerte = registro_formateado.materia_fuerte.strip()
    alumno.materia_debil = registro_formateado.materia_debil.strip()
    alumno.biografia = registro_formateado.biografia.strip()
    alumno.pais = registro_formateado.pais.strip()
    alumno.ciudad = registro_formateado.ciudad.strip()
    alumno.fecha_nacimiento = datetime.strptime(
        registro_formateado.fecha_nacimiento, "%Y/%m/%d"
    )
    alumno.punto = registro_formateado.punto
    alumno.super_like_disponible = registro_formateado.super_like_disponible
    alumno.credito_revelar = registro_formateado.credito_revelar
    return alumno


def pos_alumno_id(nro_id):
    archivo_logico = abrir_archivo(AF_ALUMNOS)
    tam_archivo = os.path.getsize(AF_ALUMNOS)
    posicion = 0
    archivo_logico.seek(0, 0)
    registro = reconvertir_a_alu(pickle.load(archivo_logico))
    while archivo_logico.tell() < tam_archivo and registro.nro_id != nro_id:
        posicion = archivo_logico.tell()
        registro = reconvertir_a_alu(pickle.load(archivo_logico))
    if registro.nro_id == nro_id:
        return posicion
    else:
        return -1


def reg_alumno_id(nro_id):
    posicion = pos_alumno_id(nro_id)
    if posicion != -1:
        archivo_logico = abrir_archivo(AF_ALUMNOS)
        archivo_logico.seek(posicion, 0)
        registro = reconvertir_a_alu(pickle.load(archivo_logico))
        archivo_logico.close()
        return registro
    else:
        return None


def modificacion_alum(email):

    print("Modificacion de Datos Personales")
    opciones = ["s", "n"]

    posicion = pos_alumno_email(email)
    if posicion != -1:
        archivo_logico = abrir_archivo(AF_ALUMNOS)
        archivo_logico.seek(posicion, 0)
        registro_convert = reconvertir_a_alu(pickle.load(archivo_logico))

        print(f"Nombre: {registro_convert.nombre}")
        respuesta = ""
        while respuesta not in opciones:
            respuesta = input("¿Desea modificar el nombre? (s/n): ").lower()
        if respuesta == "s":
            registro_convert.nombre = input("Ingrese nuevo nombre: ")

        print(f"Email: {registro_convert.email}")
        respuesta = ""
        while respuesta not in opciones:
            respuesta = input("¿Desea modificar el email? (s/n): ").lower()
        if respuesta == "s":
            registro_convert.email = input("Ingrese nuevo email: ")

        print(f"Sexo: {registro_convert.sexo}")
        respuesta = ""
        while respuesta not in opciones:
            respuesta = input("¿Desea modificar el sexo? (s/n): ").lower()
        if respuesta == "s":
            registro_convert.sexo = input("Ingrese nuevo sexo (M/F): ")

        print(f"Contraseña: {registro_convert.contrasenia}")
        respuesta = ""
        while respuesta not in opciones:
            respuesta = input("¿Desea modificar la contraseña? (s/n): ").lower()
        if respuesta == "s":
            registro_convert.contrasenia = input("Ingrese nueva contraseña: ")

        print(f"Hobbies: {registro_convert.hobbies}")
        respuesta = ""
        while respuesta not in opciones:
            respuesta = input("¿Desea modificar los hobbies? (s/n): ").lower()
        if respuesta == "s":
            registro_convert.hobbies = input("Ingrese nuevos hobbies: ")

        print(f"Materia favorita: {registro_convert.materia_favorita}")
        respuesta = ""
        while respuesta not in opciones:
            respuesta = input("¿Desea modificar la materia favorita? (s/n): ").lower()
        if respuesta == "s":
            registro_convert.materia_favorita = input(
                "Ingrese nueva materia favorita: "
            )

        print(f"Deporte favorito: {registro_convert.deporte_favorito}")
        respuesta = ""
        while respuesta not in opciones:
            respuesta = input("¿Desea modificar el deporte favorito? (s/n): ").lower()
        if respuesta == "s":
            registro_convert.deporte_favorito = input(
                "Ingrese nuevo deporte favorito: "
            )

        print(f"Materia fuerte: {registro_convert.materia_fuerte}")
        respuesta = ""
        while respuesta not in opciones:
            respuesta = input("¿Desea modificar la materia fuerte? (s/n): ").lower()
        if respuesta == "s":
            registro_convert.materia_fuerte = input("Ingrese nueva materia fuerte: ")

        print(f"Materia débil: {registro_convert.materia_debil}")
        respuesta = ""
        while respuesta not in opciones:
            respuesta = input("¿Desea modificar la materia débil? (s/n): ").lower()
        if respuesta == "s":
            registro_convert.materia_debil = input("Ingrese nueva materia débil: ")

        print(f"Biografía: {registro_convert.biografia}")
        respuesta = ""
        while respuesta not in opciones:
            respuesta = input("¿Desea modificar la biografía? (s/n): ").lower()
        if respuesta == "s":
            registro_convert.biografia = input("Ingrese nueva biografía: ")

        print(f"País: {registro_convert.pais}")
        respuesta = ""
        while respuesta not in opciones:
            respuesta = input("¿Desea modificar el país? (s/n): ").lower()
        if respuesta == "s":
            registro_convert.pais = input("Ingrese nuevo país: ")

        print(f"Ciudad: {registro_convert.ciudad}")
        respuesta = ""
        while respuesta not in opciones:
            respuesta = input("¿Desea modificar la ciudad? (s/n): ").lower()
        if respuesta == "s":
            registro_convert.ciudad = input("Ingrese nueva ciudad: ")

        print(
            f"Fecha de nacimiento: {registro_convert.fecha_nacimiento.strftime('%Y-%m/%d')}"
        )
        respuesta = ""
        while respuesta not in opciones:
            respuesta = input(
                "¿Desea modificar la fecha de nacimiento? (s/n): "
            ).lower()
        if respuesta == "s":
            fecha_nueva = pedir_fecha()
            registro_convert.fecha_nacimiento = datetime.strptime(
                fecha_nueva, "%Y/%m/%d"
            )

        archivo_logico.seek(posicion, 0)
        registro_formateado = formatear_alum(registro_convert)
        pickle.dump(registro_formateado, archivo_logico)
        archivo_logico.flush()
        archivo_logico.close()


def alta_alumno():
    nuevo_alumno = Alu()
    nuevo_alumno.nombre = input("Ingrese el nombre del alumno: ")

    nuevo_alumno.email = input("Ingrese el email del alumno: ")
    while existe_mail("alumnos", nuevo_alumno.email):
        print("Email existente. Ingrese un nuevo mail")
        nuevo_alumno.email = input("Ingrese el email del alumno: ")

    nuevo_alumno.sexo = ""
    while nuevo_alumno.sexo not in ["M", "F"]:
        nuevo_alumno.sexo = input("Ingrese el sexo (M/F): ").upper()
    nuevo_alumno.contrasenia = input("Ingrese la contraseña: ")
    nuevo_alumno.hobbies = input("Ingrese los hobbies: ")
    nuevo_alumno.materia_favorita = input("Ingrese la materia favorita: ")
    nuevo_alumno.deporte_favorito = input("Ingrese el deporte favorito: ")
    nuevo_alumno.materia_fuerte = input("Ingrese la materia fuerte: ")
    nuevo_alumno.materia_debil = input("Ingrese la materia débil: ")
    nuevo_alumno.biografia = input("Ingrese la biografía: ")
    nuevo_alumno.pais = input("Ingrese el país: ")
    nuevo_alumno.ciudad = input("Ingrese la ciudad: ")
    fecha_nueva = pedir_fecha()
    nuevo_alumno.fecha_nacimiento = datetime.strptime(fecha_nueva, "%Y/%m/%d")
    nuevo_alumno.nro_id = generador_id("alumnos")

    clase = formatear_alum(nuevo_alumno)
    archivo_logico = abrir_archivo(AF_ALUMNOS)
    archivo_logico.seek(0, 2)
    pickle.dump(clase, archivo_logico)
    archivo_logico.flush()

    archivo_logico.close()


def baja_alumno_id(nro_id):
    posicion = pos_alumno_id(nro_id)
    archivo_logico = abrir_archivo(AF_ALUMNOS)
    archivo_logico.seek(posicion, 0)
    registro = reconvertir_a_alu(pickle.load(archivo_logico))
    registro.estado = False
    archivo_logico.seek(posicion, 0)
    formateado = formatear_alum(registro)
    pickle.dump(formateado, archivo_logico)
    archivo_logico.flush()
    archivo_logico.close()


def baja_alumno_nombre(posicion):
    archivo_logico = abrir_archivo(AF_ALUMNOS)
    archivo_logico.seek(posicion, 0)
    registro = reconvertir_a_alu(pickle.load(archivo_logico))
    registro.estado = False
    archivo_logico.seek(posicion, 0)
    formateado = formatear_alum(registro)
    pickle.dump(formateado, archivo_logico)
    archivo_logico.flush()
    archivo_logico.close()


def pos_alumno_email(email):
    archivo_logico = abrir_archivo(AF_ALUMNOS)
    tam_archivo = os.path.getsize(AF_ALUMNOS)
    posicion = 0
    archivo_logico.seek(0, 0)
    if tam_archivo != 0:
        registro = reconvertir_a_alu(pickle.load(archivo_logico))
        while archivo_logico.tell() < tam_archivo and registro.email != email:
            posicion = archivo_logico.tell()
            registro = reconvertir_a_alu(pickle.load(archivo_logico))
        if registro.email == email:
            return posicion
        else:
            return -1
    else:
        return -1


def reg_alumno_email(email):
    posicion = pos_alumno_email(email)
    if posicion != -1:
        archivo_logico = abrir_archivo(AF_ALUMNOS)
        archivo_logico.seek(posicion, 0)
        if archivo_logico.tell() < os.path.getsize(AF_ALUMNOS):
            registro = reconvertir_a_alu(pickle.load(archivo_logico))
            return registro
        archivo_logico.close()
    return None


def buscar_estudiante_por_nombre(name):
    archivo_logico = abrir_archivo(AF_ALUMNOS)
    tam_archivo = os.path.getsize(AF_ALUMNOS)
    posicion = 0
    archivo_logico.seek(0, 0)
    registro = reconvertir_a_alu(pickle.load(archivo_logico))
    while archivo_logico.tell() < tam_archivo and registro.nombre != name:
        posicion = archivo_logico.tell()
        registro = reconvertir_a_alu(pickle.load(archivo_logico))
    if registro.nombre == name:
        return posicion
    else:
        return -1
    archivo_logico.close()


# ---- Moderadores ----
class Mod:
    def __init__(self):
        self.nro_id = 0
        self.email = ""
        self.contrasenia = ""
        self.estado = True
        self.reportes_aceptados = 0
        self.reportes_ignorados = 0
        self.reportes_procesados = 0


def formatear_mod(self):
    self.nro_id = self.nro_id
    self.email = self.email.ljust(32)
    self.contrasenia = self.contrasenia.ljust(32)
    return self


def reconvertir_a_mod(registro_formateado):
    moder = Mod()
    moder.nro_id = registro_formateado.nro_id
    moder.email = registro_formateado.email.strip()
    moder.contrasenia = registro_formateado.contrasenia.strip()
    moder.estado = registro_formateado.estado
    moder.reportes_aceptados = registro_formateado.reportes_aceptados
    moder.reportes_ignorados = registro_formateado.reportes_ignorados
    moder.reportes_procesados = registro_formateado.reportes_procesados
    return moder


def mod_mod_con_id(nro_id):
    opciones = ["s", "n"]
    posicion = pos_mod_id(nro_id)
    if posicion != -1:
        archivo_logico = abrir_archivo(AF_MODERADORES)
        registro_convert = reconvertir_a_mod(pickle.load(archivo_logico))

        print(f"Email: {registro_convert.email}")
        respuesta = ""
        while respuesta not in opciones:
            respuesta = input("¿Desea modificar el email? (s/n): ").lower()
        if respuesta == "s":
            registro_convert.email = input("Ingrese nuevo email: ")

        print(f"Contraseña: {registro_convert.contrasenia}")
        respuesta = ""
        while respuesta not in opciones:
            respuesta = input("¿Desea modificar la contraseña? (s/n): ").lower()
        if respuesta == "s":
            registro_convert.contrasenia = input("Ingrese nueva contraseña: ")

        archivo_logico.seek(posicion, 0)
        registro_formateado = formatear_mod(registro_convert)
        pickle.dump(registro_formateado, archivo_logico)
        archivo_logico.flush()


def pos_mod_id(nro_id):
    archivo_logico = abrir_archivo(AF_MODERADORES)
    tam_archivo = os.path.getsize(AF_MODERADORES)
    posicion = 0
    archivo_logico.seek(0, 0)
    registro = reconvertir_a_mod(pickle.load(archivo_logico))
    while archivo_logico.tell() < tam_archivo and registro.nro_id != nro_id:
        posicion = archivo_logico.tell()
        registro = reconvertir_a_mod(pickle.load(archivo_logico))
    if registro.nro_id == nro_id:

        return posicion
    else:
        return -1


def pos_mod_email(email):
    archivo_logico = abrir_archivo(AF_MODERADORES)
    tam_archivo = os.path.getsize(AF_MODERADORES)
    if tam_archivo != 0:
        posicion = 0
        archivo_logico.seek(0, 0)
        registro = reconvertir_a_mod(pickle.load(archivo_logico))
        while archivo_logico.tell() < tam_archivo and registro.email != email:
            posicion = archivo_logico.tell()
            registro = reconvertir_a_mod(pickle.load(archivo_logico))
        if registro.email == email:
            return posicion
        else:
            return -1
    else:
        return -1


def reg_mod_email(email):
    posicion = pos_mod_email(email)
    if posicion != -1:
        archivo_logico = abrir_archivo(AF_MODERADORES)
        archivo_logico.seek(posicion, 0)
        if archivo_logico.tell() < os.path.getsize(AF_MODERADORES):
            registro = reconvertir_a_mod(pickle.load(archivo_logico))
            archivo_logico.close()
            return registro
    else:
        return None


def alta_moderador():
    nuevo_moderador = Mod()
    nuevo_moderador.email = input("Ingrese el email del moderador: ")
    nuevo_moderador.contrasenia = input("Ingrese la contraseña del moderador: ")
    nuevo_moderador.estado = True
    nuevo_moderador.nro_id = generador_id("moderador")
    clase = formatear_mod(nuevo_moderador)
    archivo_logico = abrir_archivo(AF_MODERADORES)
    archivo_logico.seek(0, 2)
    pickle.dump(clase, archivo_logico)
    archivo_logico.flush()
    archivo_logico.close()


def baja_moderador(nro_id):
    posicion = pos_mod_id(nro_id)
    if posicion != -1:
        archivo_logico = abrir_archivo(AF_MODERADORES)
        archivo_logico.seek(posicion, 0)
        registro = reconvertir_a_mod(pickle.load(archivo_logico))
        registro.estado = False
        archivo_logico.seek(posicion, 0)
        formateado = formatear_mod(registro)
        pickle.dump(formateado, archivo_logico)
        archivo_logico.flush()
        archivo_logico.close()


def modificar_moderador_por_email(
    email,
    nuevo_email=None,
    nueva_contrasenia=None,
    nuevo_estado=None,
    nuevos_reportes_aceptados=None,
    nuevos_reportes_ignorados=None,
    nuevos_reportes_procesados=None,
):
    posicion = pos_mod_email(email)
    if posicion == -1:
        print("El email ingresado no se encuentra.")
        return
    archivo_logico = abrir_archivo(AF_MODERADORES)
    archivo_logico.seek(posicion, 0)
    registro = reconvertir_a_mod(pickle.load(archivo_logico))
    if nuevo_email is not None:
        registro.email = nuevo_email
    if nueva_contrasenia is not None:
        registro.contrasenia = nueva_contrasenia
    if nuevo_estado is not None:
        registro.estado = nuevo_estado
    if nuevos_reportes_aceptados is not None:
        registro.reportes_aceptados = nuevos_reportes_aceptados
    if nuevos_reportes_ignorados is not None:
        registro.reportes_ignorados = nuevos_reportes_ignorados
    if nuevos_reportes_procesados is not None:
        registro.reportes_procesados = nuevos_reportes_procesados

    archivo_logico.seek(posicion, 0)
    registro_formateado = formatear_mod(registro)
    pickle.dump(registro_formateado, archivo_logico)
    archivo_logico.flush()
    archivo_logico.close()


# ---- Administradores ----
class Admin:
    def __init__(self):
        self.nro_id = 0
        self.email = ""
        self.contrasenia = ""
        self.estado = True


def formatear_admin(self):
    self.nro_id = self.nro_id
    self.email = self.email.ljust(32)
    self.contrasenia = self.contrasenia.ljust(32)
    return self


def reconvertir_a_admin(registro_formateado):
    clase_administrador = Admin()
    clase_administrador.nro_id = registro_formateado.nro_id
    clase_administrador.email = registro_formateado.email.strip()
    clase_administrador.contrasenia = registro_formateado.contrasenia.strip()
    clase_administrador.estado = registro_formateado.estado
    return clase_administrador


def pos_admin_id(nro_id):
    archivo_logico = abrir_archivo(AF_ADMINISTRADORES)
    tam_archivo = os.path.getsize(AF_ADMINISTRADORES)
    posicion = 0
    archivo_logico.seek(0, 0)
    registro = reconvertir_a_admin(pickle.load(archivo_logico))
    while archivo_logico.tell() < tam_archivo:
        if registro.nro_id == nro_id:
            archivo_logico.close()
            return posicion
        posicion = archivo_logico.tell()
        if archivo_logico.tell() < tam_archivo:
            registro = reconvertir_a_admin(pickle.load(archivo_logico))
    archivo_logico.close()
    return -1


def pos_admin_email(email):
    archivo_logico = abrir_archivo(AF_ADMINISTRADORES)
    tam_archivo = os.path.getsize(AF_ADMINISTRADORES)
    posicion = 0
    archivo_logico.seek(0, 0)
    registro = reconvertir_a_admin(pickle.load(archivo_logico))
    while archivo_logico.tell() < tam_archivo and registro.email != email:
        posicion = archivo_logico.tell()
        registro = reconvertir_a_admin(pickle.load(archivo_logico))
    if registro.email == email:
        return posicion
    else:
        return -1


def reg_admin_email(email):
    posicion = pos_admin_email(email)
    if posicion != -1:
        archivo_logico = abrir_archivo(AF_ADMINISTRADORES)
        archivo_logico.seek(posicion, 0)
        if archivo_logico.tell() < os.path.getsize(AF_ADMINISTRADORES):
            registro = reconvertir_a_admin(pickle.load(archivo_logico))
            archivo_logico.close()
            return registro

    else:
        return None


def alta_administrador():
    nuevo_administrador = Admin()
    nuevo_administrador.email = input("Ingrese el email del administrador: ")
    nuevo_administrador.contrasenia = input("Ingrese la contraseña del administrador: ")
    nuevo_administrador.nro_id = generador_id("administrador")
    clase = formatear_admin(nuevo_administrador)
    archivo_logico = abrir_archivo(AF_ADMINISTRADORES)
    archivo_logico.seek(0, 2)
    pickle.dump(clase, archivo_logico)
    archivo_logico.flush()
    archivo_logico.close()


def verificar_existencia_administrador():
    archivo_logico = abrir_archivo(AF_ADMINISTRADORES)
    tam_archivo = os.path.getsize(AF_ADMINISTRADORES)
    if tam_archivo == 0:
        print("No existe ningún administrador. Debes crear uno.")
        alta_administrador()
    archivo_logico.close()


# ---- Likes ----
class Likes:
    def __init__(self):
        self.remitente = 0
        self.destinatario = 0
        self.sumado = False


def nuevo_like(remitente, destinatario):
    lk = Likes()
    lk.remitente = remitente
    lk.destinatario = destinatario
    archivo_logico = abrir_archivo(AF_LIKES)
    archivo_logico.seek(0, 2)
    pickle.dump(lk, archivo_logico)
    archivo_logico.flush()
    archivo_logico.close()


def existe_like(remitente, destinatario):
    archivo_logico = abrir_archivo(AF_LIKES)
    tam_archivo = os.path.getsize(AF_LIKES)
    archivo_logico.seek(0, 0)
    while archivo_logico.tell() < tam_archivo:
        like = pickle.load(archivo_logico)
        if like.remitente == remitente and like.destinatario == destinatario:
            archivo_logico.close()
            return True
    archivo_logico.close()
    return False


def hay_match(usuario1, usuario2):
    archivo_logico = abrir_archivo(AF_LIKES)
    tam_archivo = os.path.getsize(AF_LIKES)
    archivo_logico.seek(0, 0)
    like_usuario1_a_usuario2 = False
    like_usuario2_a_usuario1 = False
    while archivo_logico.tell() < tam_archivo:
        like = pickle.load(archivo_logico)
        if like.remitente == usuario1 and like.destinatario == usuario2:
            like_usuario1_a_usuario2 = True
        if like.remitente == usuario2 and like.destinatario == usuario1:
            like_usuario2_a_usuario1 = True
        if like_usuario1_a_usuario2 and like_usuario2_a_usuario1:
            archivo_logico.close()
            return True
    archivo_logico.close()
    return False


def posicion_like(nro):
    archivo_logico = abrir_archivo(AF_LIKES)
    tam_archivo = os.path.getsize(AF_LIKES)
    archivo_logico.seek(0, 0)
    pos = 0
    like = pickle.load(archivo_logico)
    while archivo_logico.tell() < tam_archivo and like.remitente != nro:
        pos = archivo_logico.tell()
        like = pickle.load(archivo_logico)
    if like.remitente == nro:
        return pos
    else:
        return -1

    archivo_logico.close()


def cambiar_estado_sumado(id_1, id_2):
    archivo_logico = abrir_archivo(AF_LIKES)
    tam_archivo = os.path.getsize(AF_LIKES)
    archivo_logico.seek(0, 0)
    modificado = False
    while archivo_logico.tell() < tam_archivo and not modificado:
        posicion = archivo_logico.tell()
        like = pickle.load(archivo_logico)
        if like.remitente == id_1 and like.destinatario == id_2:
            like.sumado = True
            archivo_logico.seek(posicion, 0)
            pickle.dump(like, archivo_logico)
            modificado = True
    archivo_logico.flush()
    archivo_logico.close()


def usar_super_like(remitente_id, destinatario_id):
    remitente = reg_alumno_id(remitente_id)
    if remitente.super_like_disponible:
        nuevo_like(remitente_id, destinatario_id)
        nuevo_like(destinatario_id, remitente_id)
        remitente.super_like_disponible = False
        pos_remitente = pos_alumno_id(remitente_id)
        archivo_logico = abrir_archivo(AF_ALUMNOS)
        archivo_logico.seek(pos_remitente, 0)
        formateado_remitente = formatear_alum(remitente)
        pickle.dump(formateado_remitente, archivo_logico)
        archivo_logico.flush()
        archivo_logico.close()
        print(f"Super-like usado con éxito con el ID {destinatario_id}.")
    else:
        print("No tienes super-like disponible.")


def revelar_candidatos(myid):
    estudiante1 = reg_alumno_id(myid)
    if estudiante1.credito_revelar > 0:
        allikes = abrir_archivo(AF_LIKES)
        tamlikes = os.path.getsize(AF_LIKES)
        allikes.seek(0, 0)
        candidatos = ["", "", ""]
        indice = 0
        while allikes.tell() < tamlikes and indice < 3:
            like = pickle.load(allikes)
            if like.destinatario == myid and not hay_match(myid, like.remitente):
                candidatos[indice] = like.remitente
                indice += 1
        allikes.close()
        likes_encontrados = False
        for candidato in candidatos:
            if pos_alumno_id(candidato) != -1:
                estudiante_candidato = reg_alumno_id(candidato)
                print(
                    f"Tienes un like de: {estudiante_candidato.nombre}, mail: {estudiante_candidato.email}"
                )
                likes_encontrados = True
        if not likes_encontrados:
            print("No tienes candidatos que no hayas correspondido.")
        estudiante1.credito_revelar -= 1
        pos_estudiante = pos_alumno_id(myid)
        archivo_logico = abrir_archivo(AF_ALUMNOS)
        archivo_logico.seek(pos_estudiante, 0)
        formateado_estudiante = formatear_alum(estudiante1)
        pickle.dump(formateado_estudiante, archivo_logico)
        archivo_logico.flush()
        archivo_logico.close()
    else:
        print(
            "No tienes créditos disponibles para revelar candidatos. Compra el Pase Gold."
        )


# ---- Reportes ----
class Reportes:
    def __init__(self):
        self.nro_id = 0
        self.id_reportante = 0
        self.id_reportado = 0
        self.razon_reporte = ""
        self.estado = 0


def crear_registro_reporte(reporte_id, reportante, reportado, razon):
    nuevo_reporte = Reportes()
    nuevo_reporte.nro_id = reporte_id
    nuevo_reporte.id_reportante = reportante
    nuevo_reporte.id_reportado = reportado
    nuevo_reporte.razon_reporte = razon
    nuevo_reporte.estado = 0
    return nuevo_reporte


def formatear_reportes(registro_a_formatear):
    registro_a_formatear.razon_reporte = registro_a_formatear.razon_reporte.ljust(255)
    return registro_a_formatear


def reconvertir_a_reporte(registro_formateado):
    registro_formateado.razon_reporte = registro_formateado.razon_reporte.strip()
    return registro_formateado


def alta_reporte(reportante, reportado, razon_reporte):
    reporte = crear_registro_reporte(
        generador_id("reporte"), reportante, reportado, razon_reporte
    )
    registro_formateado = formatear_reportes(reporte)
    archivo_logico = abrir_archivo(AF_REPORTES)
    archivo_logico.seek(0, 2)
    pickle.dump(registro_formateado, archivo_logico)
    archivo_logico.flush()
    archivo_logico.close()


def posicion_reporte_reportante_reportado(id_reportante, id_reportado):
    archivo_logico = abrir_archivo(AF_REPORTES)
    tam_archivo = os.path.getsize(AF_REPORTES)
    posicion = 0
    archivo_logico.seek(0, 0)
    registro = reconvertir_a_reporte(pickle.load(archivo_logico))
    while archivo_logico.tell() < tam_archivo:
        if registro.reportante == id_reportante and registro.reportado == id_reportado:
            posicion = archivo_logico.tell()
            archivo_logico.close()
            return posicion
        else:
            registro = reconvertir_a_admin(pickle.load(archivo_logico))
    archivo_logico.close()
    return -1


def posicion_reporte_id(nro_id):
    archivo_logico = abrir_archivo(AF_REPORTES)
    tam_archivo = os.path.getsize(AF_REPORTES)
    archivo_logico.seek(0, 0)

    while archivo_logico.tell() < tam_archivo:
        posicion = archivo_logico.tell()
        registro = reconvertir_a_reporte(pickle.load(archivo_logico))
        if registro.nro_id == nro_id:
            archivo_logico.close()
            return posicion

    archivo_logico.close()
    return -1


def modificar_reporte_estado(nro_id, estado):
    posicion = posicion_reporte_id(nro_id)
    archivo_logico = abrir_archivo(AF_REPORTES)
    archivo_logico.seek(posicion, 0)
    registro = reconvertir_a_reporte(pickle.load(archivo_logico))
    registro.estado = estado
    registro_formateado = formatear_reportes(registro)
    archivo_logico.seek(posicion, 0)
    pickle.dump(registro_formateado, archivo_logico)
    archivo_logico.flush()
    archivo_logico.close()


# ---- Comprobaciones ----
def conectado():
    valor = False
    if informacion_login[0] != "":
        valor = True
    return valor


def existe_usuario(email, password):
    registro_alumno = reg_alumno_email(email)
    if registro_alumno and registro_alumno.contrasenia == password:
        return [registro_alumno.email, "alumno"]
    registro_moderador = reg_mod_email(email)
    if registro_moderador and registro_moderador.contrasenia == password:
        print(registro_moderador.email)
        return [registro_moderador.email, "moderador"]
    registro_administrador = reg_admin_email(email)
    if registro_administrador and registro_administrador.contrasenia == password:
        return [registro_administrador.email, "administrador"]
    return None


def generador_id(nombre_archivo):
    if nombre_archivo == "moderador":
        tam = os.path.getsize(AF_MODERADORES)
        archivo_logico = abrir_archivo(AF_MODERADORES)
    elif nombre_archivo == "administrador":
        tam = os.path.getsize(AF_ADMINISTRADORES)
        archivo_logico = abrir_archivo(AF_ADMINISTRADORES)
    elif nombre_archivo == "reporte":
        tam = os.path.getsize(AF_REPORTES)
        archivo_logico = abrir_archivo(AF_REPORTES)
    else:
        tam = os.path.getsize(AF_ALUMNOS)
        archivo_logico = abrir_archivo(AF_ALUMNOS)
    nro_id = 0
    while archivo_logico.tell() < tam:
        registro = pickle.load(archivo_logico)
        nro_id = registro.nro_id
    archivo_logico.close()
    return nro_id + 1


def existe_mail(nombre_archivo, mail):
    condicion = False
    if nombre_archivo == "alumnos":
        archivo_logico = abrir_archivo(AF_ALUMNOS)
        archivo_logico.seek(0, 0)
        posicion = pos_alumno_email(mail)
        if posicion != -1:
            condicion = True
    elif nombre_archivo == "moderador":
        archivo_logico = abrir_archivo(AF_MODERADORES)
        archivo_logico.seek(0, 0)
        posicion = pos_alumno_email(mail)
        if posicion != -1:
            condicion = True
    elif nombre_archivo == "administrador":
        archivo_logico = abrir_archivo(AF_ADMINISTRADORES)
        archivo_logico.seek(0, 0)
        posicion = pos_alumno_email(mail)
        if posicion != -1:
            condicion = True
    archivo_logico.close()
    return condicion


def estudiante_activo_por_mail(email):
    valor = False
    registro = reg_alumno_email(email)
    if registro.estado:
        valor = True
    return valor


def moderador_activo_por_mail(email):
    valor = False
    registro = reg_mod_email(email)
    if registro.estado:
        valor = True
    return valor


def reportes_est_estudiantes():
    allikes = abrir_archivo(AF_LIKES)
    tamlikes = os.path.getsize(AF_LIKES)
    allikes.seek(0, 0)
    alumno_conectado = reg_alumno_email(informacion_login[0])
    myid = alumno_conectado.nro_id
    matchs = 0
    likes_dados_no_correspondidos = 0
    likes_recibidos_no_respondidos = 0
    total_candidatos = 0
    alalum = abrir_archivo(AF_ALUMNOS)
    tamalum = os.path.getsize(AF_ALUMNOS)
    alalum.seek(0, 0)
    while alalum.tell() < tamalum:
        alumno = pickle.load(alalum)
        if alumno.nro_id != myid:
            total_candidatos += 1
    alalum.close()
    while allikes.tell() < tamlikes:
        rlike = pickle.load(allikes)
        if rlike.remitente == myid:
            if hay_match(myid, rlike.destinatario):
                matchs += 1
            else:
                likes_dados_no_correspondidos += 1
        elif rlike.destinatario == myid:
            if not hay_match(myid, rlike.remitente):
                likes_recibidos_no_respondidos += 1
    allikes.close()
    if total_candidatos > 0:
        porcentaje_match = (matchs * 100) / total_candidatos
    else:
        porcentaje_match = 0
    print(f"Matcheados sobre el porcentaje posible: {porcentaje_match:.2f}%")
    print(f"Likes dados y no recibidos: {likes_dados_no_correspondidos}")
    print(f"Likes recibidos y no respondidos: {likes_recibidos_no_respondidos}")


# ---- Bonustracks ----
"""
type:
    edades: array [ 0 a 5] of int
var:
    edades:edades
    aux: int

"""


def edad_faltante():
    edades = [21, 18, 20, 19, 23, 24]
    for i in range(0, 4):
        for j in range(i + 1, 5):
            if edades[j] < edades[i]:
                aux = edades[i]
                edades[i] = edades[j]
                edades[j] = aux
    print(edades)
    for i in range(0, 5):
        if edades[i] + 1 != edades[i + 1]:
            print("el numero que falta es:", edades[i] + 1)


"""
var:
    cont:int
"""


def matcheos_comb():
    cont = 0
    archivo_logico = abrir_archivo(AF_ALUMNOS)
    tam_archivo = os.path.getsize(AF_ALUMNOS)
    archivo_logico.seek(0, 0)
    while archivo_logico.tell() < tam_archivo:
        alumno = pickle.load(archivo_logico)
        if alumno.estado:
            cont = cont + 1

    archivo_logico.close()
    print("las combinaciones posibles son", math.comb(cont, 2))


def bonustrack_punto():
    allikes = abrir_archivo(AF_LIKES)
    tamlikes = os.path.getsize(AF_LIKES)
    allikes.seek(0, 0)
    racha = 0
    while allikes.tell() < tamlikes:
        try:
            like = pickle.load(allikes)
        except EOFError:
            print("Error: Fin de archivo alcanzado inesperadamente.")
            return
        remitente = like.remitente
        destinatario = like.destinatario
        if not like.sumado:
            if hay_match(remitente, destinatario):
                alalum = abrir_archivo(AF_ALUMNOS)
                p_remitente = pos_alumno_id(remitente)
                alalum.seek(p_remitente, 0)
                regalu_remitente = reconvertir_a_alu(pickle.load(alalum))
                regalu_remitente.punto += 1
                racha += 1
                if racha >= 3:
                    regalu_remitente.punto += 1
                alalum.seek(p_remitente, 0)
                formateado_remitente = formatear_alum(regalu_remitente)
                pickle.dump(formateado_remitente, alalum)
                p_destinatario = pos_alumno_id(destinatario)
                alalum.seek(p_destinatario, 0)
                regalu_destinatario = reconvertir_a_alu(pickle.load(alalum))
                regalu_destinatario.punto += 1
                if racha >= 3:
                    regalu_destinatario.punto += 1
                alalum.seek(p_destinatario, 0)
                formateado_destinatario = formatear_alum(regalu_destinatario)
                pickle.dump(formateado_destinatario, alalum)
                cambiar_estado_sumado(remitente, destinatario)
                cambiar_estado_sumado(destinatario, remitente)
                alalum.flush()
                alalum.close()
            else:
                racha = 0
                alalum = abrir_archivo(AF_ALUMNOS)
                p = pos_alumno_id(remitente)
                alalum.seek(p, 0)
                regalu = reconvertir_a_alu(pickle.load(alalum))
                if regalu.punto > 0:
                    regalu.punto -= 1
                    alalum.seek(p, 0)
                    formateado = formatear_alum(regalu)
                    pickle.dump(formateado, alalum)
                alalum.flush()
                alalum.close()
    alum = abrir_archivo(AF_ALUMNOS)
    tamalu = os.path.getsize(AF_ALUMNOS)
    alum.seek(0, 0)
    print("PUNTAJES:")
    while alum.tell() < tamalu:
        try:
            r = reconvertir_a_alu(pickle.load(alum))
        except EOFError:
            print("Error: Fin de archivo alcanzado inesperadamente.")
            return
        print("alumno: ", r.nombre, "puntos: ", r.punto)

    alum.close()


def ruleta():
    print("Ingresar las probalidades de la persona A, B y C")
    seguir = True
    while seguir:
        match_persona_a = input("Ingrese la probalidad de match con la persona A")
        match_persona_b = input("Ingrese la probalidad de match con la persona B")
        match_persona_c = input("Ingrese la probalidad de match con la persona C")
        while not (
            match_persona_a.isdigit()
            and match_persona_b.isdigit()
            and match_persona_c.isdigit()
        ):
            match_persona_a = input("Ingrese la probalidad de match con la persona A")
            match_persona_a = input("Ingrese la probalidad de match con la persona B")
            match_persona_c = input("Ingrese la probalidad de match con la persona C")
        match_persona_a = int(match_persona_a)
        match_persona_b = int(match_persona_a)
        match_persona_c = int(match_persona_c)
        if match_persona_a + match_persona_b + match_persona_c == 100:
            ganador = random.choices(
                ["Persona A", "Persona B", "Persona C"],
                weights=[match_persona_a, match_persona_b, match_persona_c],
            )[0]
            print("La persona seleccionada es: ", ganador)
        else:
            print("El porcentaje total no esta dentro del 100 por ciento")
        respuesta = input("quiere seguir intentado? Si/No").capitalize()
        while not (respuesta == "S" or respuesta == "N"):
            respuesta = input("Quieres seguir intentado? S / N :").capitalize()
        if respuesta == "S":
            seguir = True
        else:
            seguir = False


# ---- Navegacion ----
def imprimir_datos_estudiante(un_estudiante):
    print("Nombre:", un_estudiante.nombre)
    print("Sexo:", un_estudiante.sexo)
    print("Hobbies:", un_estudiante.hobbies)
    print("Materia favorita:", un_estudiante.materia_favorita)
    print("Deporte favorito:", un_estudiante.deporte_favorito)
    print("Materia fuerte:", un_estudiante.materia_fuerte)
    print("Materia débil:", un_estudiante.materia_debil)
    print("Biografía:", un_estudiante.biografia)
    print("País:", un_estudiante.pais)
    print("Ciudad:", un_estudiante.ciudad)
    edad = calcular_edad(un_estudiante.fecha_nacimiento)
    if edad is not None:
        print("Edad:", edad)
    else:
        print("Fecha de nacimiento inválida:", un_estudiante.fecha_nacimiento)


def imprimir_datos_reporte(reporte):
    print("Nro id:", reporte.nro_id)
    print("reportante:", reporte.id_reportante)
    print("reportado:", reporte.id_reportado)
    print("razon:", reporte.razon_reporte)
    print("estado:", reporte.estado)


"""
var:
    opcion: int
"""


def imprimir_menu_inicio_sesion():
    print("Seleccione una opción:")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")
    opcion = input("Ingrese el número de su opción: ")
    while not (opcion == "1" or opcion == "2" or opcion == "3"):
        print("Opción no válida. Por favor, ingrese una opción válida (1, 2, o 3).")
        opcion = input("Ingrese el número de su opción: ")
    os.system("cls")
    return opcion


"""
var:
    opcion: int
"""


def imprimir_menu_estudiante():
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. BONUSTRACK - Edad Faltante")
    print("4. Reportes estadísticos")
    print("5. BONUSTRACK - Combinaciones")
    print("6. BONUSTRACK - Ruleta")
    if reg_alumno_email(informacion_login[0]).credito_revelar > 0:
        print("7. Revelar candidatos")
    print("8. Salir")
    opcion = input("Por favor, seleccione una opción: ")
    os.system("cls")
    return opcion


"""
var:
   opcion: int
"""


def imprimir_menu_gestionar_perfil():
    print("1. Editar mis datos personales")
    print("2. Eliminar mi perfil")
    print("0. Volver\n")
    opcion = input("Por favor, seleccione una opción: ")
    while not (opcion == "0" or opcion == "1" or opcion == "2"):
        print("Opción no válida. Por favor, seleccione una opción válida.")
        opcion = input("Por favor, seleccione una opción: ")
    os.system("cls")
    return opcion


"""
var:
   opcion: int
"""


def imprimir_menu_gestionar_candidatos():
    print("1. Ver Candidatos")
    print("2. Reportar un candidato")
    print("0. Volver\n")
    opcion = input("Por favor, seleccione una opción: ")
    while not (opcion == "0" or opcion == "1" or opcion == "2"):
        print("Opción no válida. Por favor, seleccione una opción válida.")
        opcion = input("Por favor, seleccione una opción: ")
    os.system("cls")
    return opcion


"""
var:
   opcion: string
"""


def gestionar_perfil():
    opcion = ""
    while opcion != "0":
        opcion = imprimir_menu_gestionar_perfil()
        if opcion == "1":
            print(informacion_login[0])
            modificacion_alum(informacion_login[0])
            print("Datos Modificados")
        elif opcion == "2":
            baja_alumno_id(informacion_login[0])
            informacion_login[0] = ""
            print("Se ha dado de baja el perfil")
            opcion = "0"
        elif opcion != "0":
            print("Opción no válida. Por favor, seleccione una opción válida.")


"""
var:
   opcion: string
"""


def gestionar_candidatos():
    opcion = ""
    while opcion != "0":
        opcion = imprimir_menu_gestionar_candidatos()
        if opcion == "1":
            ver_candidatos()
        elif opcion == "2":
            reportar_candidato()
        elif opcion != "0":
            print("Opción no válida. Por favor, seleccione una opción válida.\n")


def reportar_candidato():
    opciones = ["nombre", "id"]
    respuesta = ""
    al_reporte = abrir_archivo(AF_REPORTES)
    al_alumno = abrir_archivo(AF_ALUMNOS)
    al_reporte.seek(0, 2)
    while respuesta not in opciones:
        respuesta = input(
            "¿Desea reportar el alumno con Nombre o Id? (Nombre/Id): "
        ).lower()
    posicion_alumno_reportante = pos_alumno_email(informacion_login[0])
    al_alumno.seek(posicion_alumno_reportante, 0)
    nro_id_reportante = reconvertir_a_alu(pickle.load(al_alumno)).nro_id
    if respuesta == "nombre":
        nombre = input("Ingrese el nombre: ")
        if buscar_estudiante_por_nombre(nombre) != -1:
            posicion_alumno_reportado = buscar_estudiante_por_nombre(nombre)
            al_alumno.seek(posicion_alumno_reportado, 0)
            nro_id_reportado = reconvertir_a_alu(pickle.load(al_alumno)).nro_id

            if nro_id_reportante == nro_id_reportado:
                print("No puedes reportarte a ti mismo.")
            else:
                razon = input("Describa la razón del reporte: ")
                alta_reporte(nro_id_reportante, nro_id_reportado, razon)
                print("Se realizó el reporte con éxito.")
        else:
            print("No existe el alumno.")
    elif respuesta == "id":
        nro_id = int(input("Ingrese el ID: "))
        if pos_alumno_id(nro_id) != -1:
            posicion_alumno_reportado = pos_alumno_id(nro_id)
            al_alumno.seek(posicion_alumno_reportado, 0)
            nro_id_reportado = reconvertir_a_alu(pickle.load(al_alumno)).nro_id
            if nro_id_reportante == nro_id_reportado:
                print("No puedes reportarte a ti mismo.")
            else:
                razon = input("Describa la razón del reporte: ")
                alta_reporte(nro_id_reportante, nro_id_reportado, razon)
                print("Se realizó el reporte con éxito.")
        else:
            print("No existe el alumno.")


def ver_candidatos():
    tam = os.path.getsize(AF_ALUMNOS)
    if tam == 0:
        print("No hay alumnos para mostrar.")
    else:
        archivo_logico = abrir_archivo(AF_ALUMNOS)
        remitente = reg_alumno_email(informacion_login[0])
        id_remitente = remitente.nro_id
        opciones_sin_super_like = ["l", "n"]
        opciones_con_super_like = ["l", "s", "n"]
        while archivo_logico.tell() < tam:
            try:
                registro = reconvertir_a_alu(pickle.load(archivo_logico))
            except EOFError:
                print("Error: Fin de archivo alcanzado inesperadamente.")
                return
            if registro.nro_id != id_remitente and registro.estado:
                imprimir_datos_estudiante(registro)
                respuesta = ""
                if remitente.super_like_disponible:
                    while respuesta not in opciones_con_super_like:
                        respuesta = input(
                            "¿Quiere darle like (l), super-like (s) o no (n)? "
                        ).lower()
                else:
                    while respuesta not in opciones_sin_super_like:
                        respuesta = input("¿Quiere darle like (l) o no (n)? ").lower()
                id_destinatario = registro.nro_id
                if respuesta == "l":
                    nuevo_like(id_remitente, id_destinatario)
                    print(f"Like dado al ID {id_destinatario}.")
                elif respuesta == "s" and remitente.super_like_disponible:
                    usar_super_like(id_remitente, id_destinatario)
                    remitente.super_like_disponible = False
                elif respuesta == "n":
                    print(f"No se dio like al ID {id_destinatario}.")
        archivo_logico.close()


def imprimir_menu_moderador():
    print("1. Gestionar usuarios")
    print("2. Gestionar reportes")
    print("3. Salir\n")
    opcion = input("Por favor, seleccione una opción: ")
    while not (opcion == "1" or opcion == "2" or opcion == "3"):
        print("Opción no válida. Por favor, seleccione una opción válida.")
        opcion = input("Por favor, seleccione una opción: ")
    os.system("cls")
    return opcion


def estudiante():
    alumno = reg_alumno_email(informacion_login[0])
    opcion = ""
    while opcion != "8":
        opcion = imprimir_menu_estudiante()
        if opcion == "1":
            gestionar_perfil()
            if not conectado():
                opcion = "8"
        elif opcion == "2":
            gestionar_candidatos()
        elif opcion == "3":
            edad_faltante()
        elif opcion == "4":
            reportes_est_estudiantes()
        elif opcion == "5":
            matcheos_comb()
        elif opcion == "6":
            ruleta()
        elif opcion == "7":
            if alumno.credito_revelar > 0:
                revelar_candidatos(alumno.nro_id)
            else:
                print("Opción inválida\n")
        elif opcion == "8":
            informacion_login[0] = ""
        else:
            print("Opción inválida\n")
        if not conectado():
            opcion = "8"


"""
var:
    opcion:string

"""


def menu_moderador():
    opcion = ""
    while opcion != "3":
        opcion = imprimir_menu_moderador()
        if opcion == "1":
            menu_gest_user()
        elif opcion == "2":
            gestionar_reportes()
        elif opcion == "3":
            informacion_login[0] = ""
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
        if not conectado():
            opcion = "3"


def imprimir_menu_administrador():
    print("Módulo 3: Administradores")
    print("1. Gestionar usuarios")
    print("2. Gestionar reportes")
    print("3. Reportes estadísticos")
    print("4. Punteando Candidatos")
    print("5. Volver")
    return input("Selecciona una opción: ")


def eliminar_usuario():
    opcion = ""
    while opcion == "" and opcion != "s":
        print("'s' Si desea salir")
        opcion = input("¿Qué desea eliminar? Estudiante 'e', Moderador 'm': ").lower()
        while opcion not in ["e", "m", "s"]:
            print("Opción no válida")
            print("'s' Si desea salir")
            opcion = input(
                "¿Qué desea eliminar? Estudiante 'e', Moderador 'm': "
            ).lower()
        if opcion == "e":
            listado_alumnos(AF_ALUMNOS)
            nro_id = input("Seleccione el usuario que desea eliminar por id: ")
            hay_error = True
            while hay_error:
                try:
                    nro_id = int(nro_id)
                    hay_error = False
                except ValueError:
                    print("ID no válido, por favor ingrese un número.")
                    nro_id = input("Seleccione el usuario que desea eliminar por id: ")
            posicion = pos_alumno_id(nro_id)
            if posicion != -1:
                baja_alumno_id(nro_id)
                print(f"Alumno con ID {nro_id} eliminado.")
            else:
                print("No se encontró el alumno.")
        elif opcion == "m":
            listado_moderadores()
            nro_id = input("Seleccione el usuario que desea eliminar por id: ")
            hay_error = True
            while hay_error:
                try:
                    nro_id = int(nro_id)
                    hay_error = False
                except ValueError:
                    print("ID no válido, por favor ingrese un número.")
                    nro_id = input("Seleccione el usuario que desea eliminar por id: ")
            posicion = pos_mod_id(nro_id)
            if posicion != -1:
                baja_moderador(nro_id)
                print(f"Moderador con ID {nro_id} eliminado.")
            else:
                print("No se encontró el moderador.")

        else:
            print("Volviendo al menú anterior...")


def gestionar_usuarios():
    opcion = ""
    while opcion != "3":
        print("Gestionar Usuarios")
        print("1. Eliminar un usuario (incluyendo moderadores)")
        print("2. Dar de alta un moderador")
        print("3. Volver")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            eliminar_usuario()
        elif opcion == "2":
            alta_moderador()
        elif opcion == "3":
            print("Volviendo al menú principal...")
        else:
            print("Opción inválida\n")


def administrador():
    opcion = ""
    while opcion != "5":
        opcion = imprimir_menu_administrador()
        if opcion == "1":
            gestionar_usuarios()
            if not conectado():
                opcion = "5"
        elif opcion == "2":
            gestionar_reportes()
        elif opcion == "3":
            reporte_estadistico()
        elif opcion == "4":
            bonustrack_punto()
        elif opcion == "5":
            print("Saliendo del módulo de administradores...")
            informacion_login[0] = ""
        else:
            print("Opción inválida\n")
        if not conectado():
            opcion = "5"


def reporte_estadistico():
    tam = os.path.getsize(AF_REPORTES)
    tam_mod = os.path.getsize(AF_MODERADORES)
    if tam == 0:
        print("No hay reportes realizados.")
    else:
        archivo_logico = abrir_archivo(AF_REPORTES)
        archivo_logico_mod = abrir_archivo(AF_MODERADORES)
        archivo_logico.seek(0, 0)
        contador_total = 0
        contador_ignorados = 0
        contador_aceptados = 0
        mail_mod_may_cant_rep_acep = ""
        mail_mod_may_cant_rep_ign = ""
        mail_mod_may_cant_rep_proc = ""
        while archivo_logico.tell() < tam:
            reporte = reconvertir_a_reporte(pickle.load(archivo_logico))
            contador_total += 1
            if reporte.estado == 2:
                contador_ignorados += 1
            elif reporte.estado == 1:
                contador_aceptados += 1
        archivo_logico.close()
        print("La cantidad de reportes total es:", contador_total)
        print("La cantidad de reportes ignorados es:", contador_ignorados)
        print("La cantidad de reportes aceptados es:", contador_aceptados)
        if tam_mod == 0:
            print("No hay moderadores registrados aún.")
        else:
            archivo_logico_mod.seek(0, 0)
            procesado = 0
            ignorado = 0
            aceptado = 0
            while archivo_logico_mod.tell() < tam_mod:
                try:
                    reg_mod = reconvertir_a_mod(pickle.load(archivo_logico_mod))
                except EOFError:
                    print("Error: Fin de archivo alcanzado inesperadamente.")
                    return
                if reg_mod.reportes_aceptados >= aceptado:
                    mail_mod_may_cant_rep_acep = reg_mod.email
                    aceptado = reg_mod.reportes_aceptados
                if reg_mod.reportes_ignorados >= ignorado:
                    mail_mod_may_cant_rep_ign = reg_mod.email
                    ignorado = reg_mod.reportes_ignorados
                if reg_mod.reportes_procesados >= procesado:
                    mail_mod_may_cant_rep_proc = reg_mod.email
                    procesado = reg_mod.reportes_procesados
            if mail_mod_may_cant_rep_acep:
                mod1 = reg_mod_email(mail_mod_may_cant_rep_acep)
                print("El moderador con más reportes aceptados es:", mod1.email)
            else:
                print("No hay moderador con reportes aceptados.")
            if mail_mod_may_cant_rep_ign:
                mod2 = reg_mod_email(mail_mod_may_cant_rep_ign)
                print("El moderador con más reportes ignorados es:", mod2.email)
            else:
                print("No hay moderador con reportes ignorados.")
            if mail_mod_may_cant_rep_proc:
                mod3 = reg_mod_email(mail_mod_may_cant_rep_proc)
                print("El moderador con más reportes procesados es:", mod3.email)
            else:
                print("No hay moderador con reportes procesados.")


def menu_gest_user():
    opcion = ""
    while opcion != "2":
        print("1. Desactivar usuario.")
        print("2. Volver.")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            desactivar_usuario()
        elif opcion == "2":
            print("Saliendo\n")
        else:
            print("Opción inválida, por favor seleccione una opción válida.")


def desactivar_usuario():
    tam_archivo = os.path.getsize(AF_ALUMNOS)
    if tam_archivo == 0:
        print("No hay estudiantes en el archivo.")
    else:
        listado_alumnos(AF_ALUMNOS)
        name = input(
            "Seleccione el nombre del usuario que quiere desactivar, si no lo conoce coloque '*': "
        )
        if name != "*":
            posicion = buscar_estudiante_por_nombre(name)
            if posicion == -1:
                print("No existe ese estudiante")
            else:
                baja_alumno_nombre(posicion)
                print("Estudiante eliminado\n")
        else:
            try:
                id_est = int(input("Ingrese el id del usuario: "))
                posicion_por_id = pos_alumno_id(id_est)
                if posicion_por_id != -1:
                    baja_alumno_id(id_est)
                    print("Estudiante eliminado")
                else:
                    print("No existe ese estudiante")
            except ValueError:
                print("El ID ingresado no es válido. Debe ser un número entero.")


"""
var:
    opcion:string

"""


def gestionar_reportes():
    opcion = ""
    while opcion != "2":
        print("1. Ver Reportes")
        print("2. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_reportes()
        elif opcion == "2":
            print("Volviendo al menú principal...\n")
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.\n")


"""
var:
    opcion:string
    email_reportado: string
    poscion_reportado: int
"""


def ver_reportes():
    tam = os.path.getsize(AF_REPORTES)
    if tam == 0:
        print("No hay reportes para mostrar.")
    else:
        archivo_logico = abrir_archivo(AF_REPORTES)
        archivo_logico.seek(0, 0)
        salir = False
        reportes_pendientes = False
        while archivo_logico.tell() < tam and not salir:
            try:
                reporte = reconvertir_a_reporte(pickle.load(archivo_logico))
            except EOFError:
                print("Error: Fin de archivo alcanzado inesperadamente.")
                return
            if reporte.estado == 0:
                reportante_activo = estudiante_activo_por_mail(
                    reg_alumno_id(reporte.id_reportante).email
                )
                reportado_activo = estudiante_activo_por_mail(
                    reg_alumno_id(reporte.id_reportado).email
                )
                if reportante_activo and reportado_activo:
                    reportes_pendientes = True
                    imprimir_datos_reporte(reporte)
                    opciones = ["si", "no"]
                    respuesta = ""
                    while respuesta not in opciones:
                        respuesta = input(
                            "¿Si para aceptarlo, No para ignorarlo: "
                        ).lower()
                    if respuesta == "si":
                        baja_alumno_id(reporte.id_reportado)
                        modificar_reporte_estado(reporte.nro_id, 1)
                        if informacion_login[1] == "moderador":
                            moderador = reg_mod_email(informacion_login[0])
                            modificar_moderador_por_email(
                                informacion_login[0],
                                nuevos_reportes_aceptados=moderador.reportes_aceptados
                                + 1,
                                nuevos_reportes_procesados=moderador.reportes_procesados
                                + 1,
                            )
                    else:
                        modificar_reporte_estado(reporte.nro_id, 2)
                        if informacion_login[1] == "moderador":
                            moderador = reg_mod_email(informacion_login[0])
                            modificar_moderador_por_email(
                                informacion_login[0],
                                nuevos_reportes_ignorados=moderador.reportes_ignorados
                                + 1,
                                nuevos_reportes_procesados=moderador.reportes_procesados
                                + 1,
                            )
                    respuesta_salir = ""
                    while respuesta_salir not in ["si", "no"]:
                        respuesta_salir = input(
                            "¿Desea seguir revisando más reportes? (si/no): "
                        ).lower()

                    if respuesta_salir == "no":
                        salir = True
        if not reportes_pendientes:
            print("No hay reportes para revisar.")
        archivo_logico.close()


# ------------- Control de inicio de sesion -------------------

informacion_login = ["", ""]

"""
var:
    opcion:string
    email: string
    contrasenia: string
    existe: booleano
    intentos: int
"""


def inicio_sesion():
    opcion = ""
    while informacion_login[0] == "" and opcion != "3":
        opcion = imprimir_menu_inicio_sesion()
        if opcion == "1":
            intentos = 3
            while intentos > 0:
                mail = input("Ingrese su email: ")
                contraseña = getpass.getpass("Ingrese su contraseña: ")
                existe = existe_usuario(mail, contraseña)
                if (
                    existe
                    and existe[1] == "alumno"
                    and estudiante_activo_por_mail(mail)
                ):
                    informacion_login[0] = existe[0]
                    informacion_login[1] = existe[1]
                    print("Inicio exitoso\n")
                    intentos = 0
                elif (
                    existe
                    and existe[1] == "moderador"
                    and moderador_activo_por_mail(mail)
                ):
                    informacion_login[0] = existe[0]
                    informacion_login[1] = existe[1]
                    print("Inicio exitoso\n")
                    intentos = 0
                elif existe and existe[1] == "administrador":
                    informacion_login[0] = existe[0]
                    informacion_login[1] = existe[1]
                    print("Inicio exitoso\n")
                    intentos = 0
                elif intentos != 1:
                    intentos -= 1
                    print("Intente nuevamente")
                    print("Intentos restantes:", intentos)
                else:
                    print("Credenciales inválidas.")
                    intentos = 0
        elif opcion == "2":
            alta_alumno()
            print("registro exitoso")
        elif opcion == "3":
            print("Saliendo del programa...")
            informacion_login[0] = "salir"
        else:
            print("Opción no válida. Por favor, ingrese una opción válida (1, 2, o 3).")


# ------------- Programa Principal-------------------


def main():
    verificar_existencia_administrador()
    alumnos = abrir_archivo(AF_ALUMNOS)
    alumnos.close()
    moderadores_todos = abrir_archivo(AF_MODERADORES)
    moderadores_todos.close()
    administradores_todos = abrir_archivo(AF_ADMINISTRADORES)
    administradores_todos.close()
    likes_todos = abrir_archivo(AF_LIKES)
    likes_todos.close()
    reportes_todos = abrir_archivo(AF_REPORTES)
    reportes_todos.close()

    # listado_alumnos(AF_ALUMNOS)
    # print("\n")

    # listado_likes()
    # print("\n")

    # listado_administradores()
    # print("\n")

    # listado_moderadores()
    # print("\n")

    # listado_reportes()
    # print("\n")

    while informacion_login[0] == "":
        informacion_login[0], informacion_login[1] = "", ""
        inicio_sesion()
        if conectado():
            if informacion_login[1] == "moderador":
                print("Sos un moderador")
                menu_moderador()
            elif informacion_login[1] == "alumno":
                estudiante()
            elif informacion_login[1] == "administrador":
                administrador()


main()
