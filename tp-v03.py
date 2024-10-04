"""
Integrantes:
- Poses, Matias Abel
- Porcel, Santiago
- OROÑO, Martin
- Bellocci, Francisco
Comision 11
"""

from datetime import datetime
import getpass
import math
import os.path
import pickle

AF_ALUMNOS = ".\\alumnos.dat"
AF_MODERADORES = ".\\moderadores.dat"
AF_ADMINISTRADORES = ".\\administradores.dat"
AF_LIKES = ".\\likes.dat"
AF_REPORTES = ".\\reportes.dat"

informacion_login = ["", ""]

"""
var:
    edad: int
"""
def calcular_edad(fecha_nacimiento):
    fecha_nac = datetime.strptime(fecha_nacimiento, "%Y/%m/%d")
    edad = int((datetime.today() - fecha_nac).days / 365.2425)
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

def abrir_archivo(archivo_fisico):
    if os.path.exists(archivo_fisico):
        archivo_logico = open(archivo_fisico, "r+b")
    else:
        archivo_logico = open(archivo_fisico, "w+b")
    return archivo_logico


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
    alumno.fecha_nacimiento = datetime.strptime(registro_formateado.fecha_nacimiento, "%Y/%m/%d")
    return alumno

def crear_registro_alu(
    nro_id,
    email,
    nombre,
    sexo,
    contrasenia,
    estado,
    hobbies,
    materia_favorita,
    deporte_favorito,
    materia_fuerte,
    materia_debil,
    biografia,
    pais,
    ciudad,
    fecha_nacimiento):
    reg = Alu()
    reg.nro_id = nro_id
    reg.email = email
    reg.nombre = nombre
    reg.sexo = sexo
    reg.contrasenia = contrasenia
    reg.estado = estado
    reg.hobbies = hobbies
    reg.materia_favorita = materia_favorita
    reg.deporte_favorito = deporte_favorito
    reg.materia_fuerte = materia_fuerte
    reg.materia_debil = materia_debil
    reg.biografia = biografia
    reg.pais = pais
    reg.ciudad = ciudad
    reg.fecha_nacimiento = fecha_nacimiento
    return reg

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
    archivo_logico.close()

def reg_alumno_id(nro_id):
    posicion = pos_alumno_id(nro_id)
    if posicion != -1:
        archivo_logico = abrir_archivo(AF_ALUMNOS)
        archivo_logico.seek(posicion,0)
        registro = reconvertir_a_alu(pickle.load(archivo_logico))
        archivo_logico.close()
        return registro
    else:
        return None

def modificacion_alum(nro_id= None, email = None):

    print("Modificacion de Datos Personales")
    opciones = ["s","n"]
    if nro_id:
        posicion = pos_alumno_id(nro_id)
    if email:
        print("entro aca")
        posicion = pos_alumno_email(email)
    if posicion !=-1:
        archivo_logico = abrir_archivo(AF_ALUMNOS)
        archivo_logico.seek(posicion,0)
        registro_convert= reconvertir_a_alu(pickle.load(archivo_logico))

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
            registro_convert.materia_favorita = input("Ingrese nueva materia favorita: ")

        print(f"Deporte favorito: {registro_convert.deporte_favorito}")
        respuesta = ""
        while respuesta not in opciones:
            respuesta = input("¿Desea modificar el deporte favorito? (s/n): ").lower()
        if respuesta == "s":
            registro_convert.deporte_favorito = input("Ingrese nuevo deporte favorito: ")

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

        print(f"Fecha de nacimiento: {registro_convert.fecha_nacimiento.strftime('%Y-%m/%d')}")
        respuesta = ""
        while respuesta not in opciones:
            respuesta = input("¿Desea modificar la fecha de nacimiento? (s/n): ").lower()
        if respuesta == "s":
            fecha_nueva = pedir_fecha()
            registro_convert.fecha_nacimiento = datetime.strptime(fecha_nueva, "%Y/%m/%d")

        archivo_logico.seek(posicion,0)
        registro_formateado = formatear_alum(registro_convert)
        pickle.dump(registro_formateado,archivo_logico)
        archivo_logico.flush()
        archivo_logico.close()

def alta_alumno( ):
    nuevo_alumno = Alu()
    nuevo_alumno.nombre = input("Ingrese el nombre del alumno: ")

    nuevo_alumno.email = input("Ingrese el email del alumno: ")
    while existe_mail("alumnos",nuevo_alumno.email):
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
    archivo_logico.seek(0,2)
    pickle.dump(clase, archivo_logico)
    archivo_logico.flush()

    archivo_logico.close()

def baja_alumno_id(nro_id):
    posicion = pos_alumno_id(nro_id)
    archivo_logico = abrir_archivo(AF_ALUMNOS)
    archivo_logico.seek(posicion,0)
    registro = reconvertir_a_alu(pickle.load(archivo_logico))
    registro.estado = False
    archivo_logico.seek(posicion, 0)
    formateado = formatear_alum(registro)
    pickle.dump(formateado,archivo_logico)
    archivo_logico.flush()
    archivo_logico.close()

def baja_alumno_nombre(posicion):
    archivo_logico = abrir_archivo(AF_ALUMNOS)
    archivo_logico.seek(posicion,0)
    registro = reconvertir_a_alu(pickle.load(archivo_logico))
    registro.estado = False
    archivo_logico.seek(posicion, 0)
    formateado = formatear_alum(registro)
    pickle.dump(formateado,archivo_logico)
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


def buscar_estudiante_por_nombre (name):
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
class Mod():
    def __init__(self):
        self.nro_id = 0
        self.email = ""
        self.contrasenia = ""
        self.estado = True

def formatear_mod(self):
    self.nro_id = self.nro_id
    self.email = self.email.ljust(32)
    self.contrasenia = self.contrasenia.ljust(32)
    return self

def reconvertir_a_mod(registro_formateado):
    moder = Mod()
    moder.nro_id =registro_formateado.nro_id
    moder.email = registro_formateado.email.strip()
    moder.contrasenia = registro_formateado.contrasenia.strip()
    moder.estado = registro_formateado.estado
    return moder

def crear_registro_mod(nro_id, email, contrasenia, estado):
    reg = Mod()
    reg.nro_id = nro_id
    reg.email = email
    reg.contrasenia = contrasenia
    reg.estado = estado
    return reg

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
    print("entro aca")
    print (type(registro.nro_id))
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

def baja_moderador(nro_id=-1, mail=""):
    if nro_id != -1:
        posicion = pos_mod_id(nro_id)

    if mail != "":
        posicion = pos_mod_email(mail)
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

def crear_registro_admin(nro_id, email, contrasenia):
    reg = Admin()
    reg.nro_id = nro_id
    reg.email = email
    reg.contrasenia = contrasenia
    return reg

def mod_admin_con_id(nro_id):
    opciones = ["s", "n"]
    posicion = pos_admin_id(nro_id)
    if posicion != -1:
        archivo_logico = abrir_archivo(AF_ADMINISTRADORES)
        registro_convert = reconvertir_a_admin(pickle.load(archivo_logico))

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
        registro_formateado = formatear_admin(registro_convert)
        pickle.dump(registro_formateado, archivo_logico)
        archivo_logico.flush()

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

def baja_administrador(nro_id=-1, mail=""):
    if nro_id != -1:
        posicion = pos_admin_id(nro_id)
    if mail != "":
        posicion = pos_admin_email(mail)
    if posicion != -1:
        archivo_logico = abrir_archivo(AF_ADMINISTRADORES)
        archivo_logico.seek(posicion, 0)
        registro = reconvertir_a_admin(pickle.load(archivo_logico))
        archivo_logico.seek(posicion, 0)
        registro.estado = False
        formateado = formatear_admin(registro)
        pickle.dump(formateado, archivo_logico)
        archivo_logico.flush()
        archivo_logico.close()


# ---- Likes ----
class Likes:
    def __init__(self):
        self.remitente=0
        self.destinatario = 0

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



# ---- Reportes ----
class Reportes:
    def __init__(self):
        self.reporte_id = 0
        self.id_reportante= 0
        self.id_reportado = 0
        self.razon_reporte = ""
        self.estado = 0

def crear_registro_reporte(reporte_id,reportante,reportado,razon):
    nuevo_reporte = Reportes( )
    nuevo_reporte.reporte_id = reporte_id
    nuevo_reporte.id_reportante = reportante
    nuevo_reporte.id_reportado = reportado
    nuevo_reporte.razon_reporte = razon
    nuevo_reporte.estado = 0
    return nuevo_reporte

def formatear_reportes( registro_a_formatear):
    registro_a_formatear.razon_reporte = registro_a_formatear.ljust(255)
    return registro_a_formatear

def reconvertir_a_reporte(registro_formateado):
    registro_formateado.razon_reporte = registro_formateado.razon_reporte.strip()
    return(registro_formateado)

def alta_reporte(reportante, reportado,razon_reporte):
    reporte = crear_registro_reporte(reportante, reportado, razon_reporte)
    reporte.reporte_id =generador_id("reportes")
    registro_formateado= formatear_reportes(reporte)
    archivo_logico = abrir_archivo(AF_REPORTES)
    archivo_logico.seek(0, 2)
    pickle.dump(registro_formateado, archivo_logico)
    archivo_logico.flush()
    archivo_logico.close()

def posicion_reporte_reportante_reportado(id_reportante,id_reportado):
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
    posicion = 0
    archivo_logico.seek(0, 0)
    registro = reconvertir_a_reporte(pickle.load(archivo_logico))
    while archivo_logico.tell() < tam_archivo:
        if registro.reportante == nro_id:
            posicion = archivo_logico.tell()
            archivo_logico.close()
            return posicion
        else:
            registro = reconvertir_a_admin(pickle.load(archivo_logico))
    archivo_logico.close()
    return -1

def modificar_reporte_estado(nro_id,estado):
    archivo_logico = abrir_archivo(AF_REPORTES)
    tam_archivo = os.path.getsize(AF_REPORTES)
    posicion = posicion_reporte_id(nro_id)
    archivo_logico.seek(posicion, 0)
    registro = reconvertir_a_reporte(pickle.load(archivo_logico))
    registro.estado = estado
    registro_formateado = formatear_reportes(registro)
    archivo_logico.seek(posicion, 0)
    pickle.dump(registro_formateado, archivo_logico)
    archivo_logico.flush()
    archivo_logico.close()

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
            admin_archivo = pickle.load(archivo_logico)
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
        print(f"Remitente: {registro_like.remitente}, Destinatario: {registro_like.destinatario}")
        print("Tamaño del archivo:", tam)
        print("Posición actual del puntero:", archivo_logico.tell())

    archivo_logico.close()

def listado_likes():
    tam = os.path.getsize(AF_LIKES)
    archivo_logico = abrir_archivo(AF_LIKES)
    print("Listado de Likes:")
    while archivo_logico.tell() < tam:
        like = pickle.load(archivo_logico)
        print(f"Remitente: {like.remitente}, Destinatario: {like.destinatario}")
    archivo_logico.close()

def listado_moderadores():
    archivo_logico = abrir_archivo(AF_MODERADORES)
    tam = os.path.getsize(AF_MODERADORES)
    if tam == 0:
        print("No hay moderadores para mostrar.")
    else:
        archivo_logico.seek(0, 0)
        print(f"{'ID':<5} {'Email':<25} {'Contraseña':<15}")
        print("-" * 50)
        while archivo_logico.tell() < tam:
            moderador_archivo = pickle.load(archivo_logico)
            salida = (
                f"{moderador_archivo.nro_id:<5} "
                f"{moderador_archivo.email:<25} "
                f"{moderador_archivo.contrasenia:<15}"
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

def listado_alumnos(direccion):
    tam = os.path.getsize(direccion)
    if tam == 0:
        print("no hay nada para mostrar")
    else:
        archivo_logico = abrir_archivo(direccion)
        archivo_logico.seek(0, 0)
        while archivo_logico.tell() < tam:
            alum_archivo = reconvertir_a_alu(pickle.load(archivo_logico))
            salida = (
                f'{alum_archivo.nro_id:<5} '
                f'{alum_archivo.email:<25} '
                f'{alum_archivo.nombre:<25} '
                f'{alum_archivo.sexo:<20} '
                f'{alum_archivo.contrasenia:<25} '
                f'{alum_archivo.estado:<25} '
                f'{str(alum_archivo.fecha_nacimiento):<15}'
            )
            print(salida)
        archivo_logico.close()

def imprimir_registro_puntero_alumnos ():
    tam = os.path.getsize(AF_ALUMNOS)
    archivo_logico = abrir_archivo(AF_ALUMNOS)
    while archivo_logico.tell() < tam:
        pickle.load(archivo_logico)
        print("tamanio del archivo",tam)
        print("donde esta el puntero",archivo_logico.tell())

# ---- Comprobaciones ----
def conectado():
    valor = False
    if informacion_login[0] != "":
        valor = True
    return valor

def existe_usuario(email, password):
    registro_alumno = reg_alumno_email(email)
    if registro_alumno and registro_alumno.contrasenia == password:
        return [registro_alumno.email,  "alumno"]
    registro_moderador = reg_mod_email(email)
    if registro_moderador and registro_moderador.contrasenia == password:
        print(registro_moderador.email)
        return [registro_moderador.email,  "moderador"]
    registro_administrador = reg_admin_email(email)
    if registro_administrador and registro_administrador.contrasenia == password:
        return [registro_administrador.email,  "administrador"]
    return None

def generador_id(nombre_archivo):
    if nombre_archivo == "alumnos":
        tam = os.path.getsize(AF_ALUMNOS)
        archivo_logico = abrir_archivo(AF_ALUMNOS)
    elif nombre_archivo == "moderador":
        tam = os.path.getsize(AF_MODERADORES)
        archivo_logico = abrir_archivo(AF_MODERADORES)
    elif nombre_archivo == "administrador":
        tam = os.path.getsize(AF_ADMINISTRADORES)
        archivo_logico = abrir_archivo(AF_ADMINISTRADORES)
    elif nombre_archivo == "reporte":
        tam = os.path.getsize(AF_ADMINISTRADORES)
        archivo_logico = abrir_archivo(AF_ADMINISTRADORES)
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
        archivo_logico.seek(0,0)
        posicion = pos_alumno_email(mail)
        if posicion != -1:
            condicion = True
    elif nombre_archivo == "moderador":
        archivo_logico = abrir_archivo(AF_MODERADORES)
        archivo_logico.seek(0,0)
        posicion = pos_alumno_email(mail)
        if posicion != -1:
            condicion = True
    elif nombre_archivo == "administrador":
        archivo_logico = abrir_archivo(AF_ADMINISTRADORES)
        archivo_logico.seek(0,0)
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

    archivo_logico.close()
    print("las combinaciones posibles son", math.comb(cont, 2))




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
    print("6. Salir")
    opcion = input("Por favor, seleccione una opción: ")
    while not (
        opcion == "1"
        or opcion == "2"
        or opcion == "3"
        or opcion == "4"
        or opcion == "5"
        or opcion == "6"
    ):
        print("Opción no válida. Por favor, seleccione una opción válida.")
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
            """ reportar_candidato() """
        elif opcion != "0":
            print("Opción no válida. Por favor, seleccione una opción válida.\n")

def ver_candidatos():
    tam = os.path.getsize(AF_ALUMNOS)
    if tam == 0:
        print("no hay alumnos para mostrar")
    else:
        archivo_logico = abrir_archivo(AF_ALUMNOS)
        remitente = reconvertir_a_alu(reg_alumno_email(informacion_login[0]))
        id_remitente = remitente.nro_id
        while archivo_logico.tell()<tam:

            registro = reconvertir_a_alu(pickle.load(archivo_logico))
            if registro.nro_id != id_remitente and registro.estado:
                imprimir_datos_estudiante(registro)
                opciones = ["s","n"]
                respuesta = ""
                while respuesta not in opciones:
                    respuesta = input("¿Quiere darle like? (s/n): ").lower()
                if respuesta == "s":
                    id_destinatario = registro.nro_id
                    nuevo_like(id_remitente,id_destinatario)

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
    opcion = ""
    while opcion != "6":
        opcion = imprimir_menu_estudiante()
        if opcion == "1":
            gestionar_perfil()
            if not conectado():
                opcion = "6"
        elif opcion == "2":
            gestionar_candidatos()
        elif opcion == "3":
            edad_faltante()
        elif opcion == "4":
            """ reporte_estadistico() """
        elif opcion == "5":
            matcheos_comb()
        elif opcion == "6":
            informacion_login[0] = ""
        else:
            print("Opción inválida\n")
        if not conectado():
            opcion = "6"

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
    print("4. Volver")
    return input("Selecciona una opción: ")

def eliminar_usuario ():
    opcion = ""
    while opcion == "" and opcion != "s":
        print ("'s' Si desea salir")
        opcion = input ("Que desea eliminar? Estudiante 'e', Moderador 'm': ")
        while opcion != "e" and opcion != "m" and opcion !="s":
            print ("Opcion no valida")
            print ("'s' Si desea salir")
            opcion = input ("Que desea eliminar? Estudiante 'e', Moderador 'm': ")
        if opcion == "e":
            listado_alumnos(AF_ALUMNOS)
            nro_id =int(input("Seleccione el usuario que desea eliminar por id: "))
            baja_alumno_id(nro_id)
        elif opcion == "m":
            listado_moderadores()
            nro_id =int(input("Seleccione el usuario que desea eliminar por id: "))
            baja_moderador(nro_id)
        else:
            print ("Volviendo al menu anterior ")

def gestionar_usuarios():
    opcion = ""
    while opcion != "4":
        print("Gestionar Usuarios")
        print("1. Eliminar un usuario (incluyendo moderadores)")
        print("2. Dar de alta un moderador")
        print("3. Desactivar usuario")
        print("4. Volver")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            eliminar_usuario()
        elif opcion == "2":
            alta_moderador()
        elif opcion == "3":
            baja_administrador(None, informacion_login[0])
        elif opcion == "4":
            print("Volviendo al menú principal...")
        else:
            print("Opción inválida\n")

def administrador():
    opcion = ""
    while opcion != "4":
        opcion = imprimir_menu_administrador()
        if opcion == "1":
            gestionar_usuarios()
            if not conectado():
                opcion = "4"
        elif opcion == "2":
            gestionar_reportes()
        elif opcion == "3":
            """ reporte_estadistico() """
        elif opcion == "4":
            print("Saliendo del módulo de administradores...")
            informacion_login[0] = ""
        else:
            print("Opción inválida\n")
        if not conectado():
            opcion = "4"

def menu_gest_user():
    print("1. Desactivar usuario.")
    print("2. Volver.")
    opcion = input("Seleccione una opción: ")
    while opcion != "2":
        if opcion == "1":
            desactivar_usuario()
            opcion = input("Seleccione una opción: ")
        else:
            opcion = input("Seleccione una opción: ")
    print("Saliendo\n")

def desactivar_usuario():
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

    if name == "*":
        id_est = int(input(
            "Seleccione el ID del usuario, si no lo conoce coloque un numero mayor a 7 o menor a 0: "
        ))
        if 0 <= int(id_est) < 8:
            baja_alumno_id(id_est)
            print("Estudiante eliminado")
        else:
            print("Necesitamos más datos para eliminar al usuario")

"""
var:
    opcion:string

"""
def gestionar_reportes():
    print("1. Ver Reportes")
    print("2. Volver")
    opcion = input("Seleccione una opción: ")

    while opcion != "1" and opcion != "2":
        print("1. Ver Reportes")
        print("2. Volver")
        opcion = input("Seleccione una opción: ")

    while opcion == "1":
        """ ver_reportes() """
        print("1. Ver Reportes")
        print("2. Volver")
        opcion = input("Seleccione otra opción: ")

"""
var:
    opcion:string
    email_reportado: string
    poscion_reportado: int
"""
""" def ver_reportes():
    for i in range(56):
        if tabla_reportes[i][2] == "0":
            print("Reporte sin revisar:")
            print("Usuario reportado:", tabla_reportes[i][0])
            print("Motivo del reporte:", tabla_reportes[i][1])
            print("¿Quiere ignorar el reporte? '2', ¿Quiere desactivar el usuario? '1'")
            opcion = input("Seleccione una opción: ")
            while opcion != "1" and opcion != "2":
                print("Opción inválida.")
                opcion = input("Seleccione una opción: ")
            if opcion == "1":
                email_reportado = tabla_reportes[i][0]
                posicion_reportado = buscar_estudiante_por_mail(email_reportado)
                if posicion_reportado != -1:
                    eliminar_estudiante_por_indice(posicion_reportado)
                    tabla_reportes[i][2] = "1"
            elif opcion == "2":
                tabla_reportes[i][2] = "2"
            print("Reporte actualizado.") """

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
                elif existe and existe[1] == "moderador" and moderador_activo_por_mail(mail):
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

def main():
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

    # Solo para ver los cambios de datos
    # print("-------------------------------")
    imprimir_registro_puntero_alumnos()
    print("-------------------------------")
    listado_alumnos(AF_ALUMNOS)
    print("-------------------------------")
    # imprimir_registro_puntero_likes()
    # print("-------------------------------")
    # listado_likes()
    # print("-------------------------------")
    # listado_administradores()
    # print("-------------------------------")
    # imprimir_registro_puntero_administradores()
    # print("-------------------------------")
    # listado_moderadores()
    # print("-------------------------------")
    # imprimir_registro_puntero_moderadores()
    # print("-------------------------------")
    # print("\n")
    # Solo para ver los cambios de datos

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
