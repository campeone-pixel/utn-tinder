from datetime import datetime
import getpass
import random
import os
import math
import os
import os.path
import pickle
import io

"""
Integrantes:
- Poses, Matias Abel 
- Porcel, Santiago 
- OROÑO, Martin
- Bellocci, Francisco
Comision 11
"""

af_alumnos = ".\\alumnos.dat"
af_moderadores = ".\\moderadores.dat"
af_administradores = ".\\administradores.dat"
af_likes = ".\\likes.dat"
af_reportes = ".\\reportes.dat"

informacion_login = ["", ""]

def imprimir_alu(alumno):
    print("Procesando clase 'alu':")
    for atributo, valor in alumno.__dict__.items():
        if not isinstance(valor, str):
            print(f"Atributo: {atributo}, Tipo: {type(valor).__name__}, Valor: {valor}")

def imprimir_mod(moderador):
    print("Procesando clase 'mod':")
    for atributo, valor in moderador.__dict__.items():
        if not isinstance(valor, str):
            print(f"Atributo: {atributo}, Tipo: {type(valor).__name__}, Valor: {valor}")

def imprimir_admin(administrador):
    print("Procesando clase 'admin':")
    for atributo, valor in administrador.__dict__.items():
        if not isinstance(valor, str):
            print(f"Atributo: {atributo}, Tipo: {type(valor).__name__}, Valor: {valor}")


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


def conectado():
    valor = False
    if informacion_login[0] != "":
        valor = True
    return valor


class alu:
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
    alumno = alu()
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
    alumno.fecha_nacimiento = registro_formateado.fecha_nacimiento
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
    fecha_nacimiento,
):
    reg = alu()
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
    archivo_logico = abrir_archivo(af_alumnos)
    tam_archivo = os.path.getsize(af_alumnos)
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
        archivo_logico = abrir_archivo(af_alumnos)
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
        archivo_logico = abrir_archivo(af_alumnos)
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
    nuevo_alumno = alu()
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
    archivo_logico = abrir_archivo(af_alumnos)  
    archivo_logico.seek(0,2)
    pickle.dump(clase, archivo_logico)  
    archivo_logico.flush()  
    archivo_logico.close()  



def baja_alumno(nro_id=-1, mail = ""):
    if nro_id !=-1:
        posicion = pos_alumno_id(nro_id)
    if mail !="":
        posicion = pos_alumno_email(mail)
    if posicion != -1:
        archivo_logico = abrir_archivo(af_alumnos)
        archivo_logico.seek(posicion,0)
        registro = reconvertir_a_alu(pickle.load(archivo_logico))
        registro.estado = False
        archivo_logico.seek(posicion, 0)
        formateado = formatear_alum(registro)
        pickle.dump(formateado,archivo_logico)
        archivo_logico.flush()
        archivo_logico.close()    


def listado_alumnos(direccion):
    tam = os.path.getsize(direccion)
    if tam ==0:
        print("no hay nada para mostrar")
    else:
        archivo_logico = abrir_archivo(direccion)
        archivo_logico.seek(0,0)
        while archivo_logico.tell()<tam:
            alum_archivo = reconvertir_a_alu(pickle.load(archivo_logico))
            salida = '{:<5} {:<25} {:<25} {:<20} {:<25} {:<15}'.format(
                alum_archivo.nro_id, alum_archivo.email, alum_archivo.nombre, alum_archivo.sexo, alum_archivo.contrasenia, str(alum_archivo.fecha_nacimiento)
            )
            print(salida) 
        archivo_logico.close()


def pos_alumno_email(email):
    archivo_logico = abrir_archivo(af_alumnos)
    tam_archivo = os.path.getsize(af_alumnos)
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
        archivo_logico = abrir_archivo(af_alumnos)
        archivo_logico.seek(posicion, 0)
        if archivo_logico.tell() < os.path.getsize(af_alumnos):
            registro = reconvertir_a_alu(pickle.load(archivo_logico))
            archivo_logico.close()
            return registro
        archivo_logico.close()
    return None



class mod:
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
    moder = mod()
    moder.nro_id =registro_formateado.id
    moder.email = registro_formateado.email.strip()  
    moder.contrasenia = registro_formateado.contrasenia.strip()
    moder.estado = registro_formateado.estado
    return moder

def crear_registro_mod(nro_id, email, contrasenia, estado):
    reg = mod()
    reg.nro_id = nro_id
    reg.email = email
    reg.contrasenia = contrasenia
    reg.estado = estado
    return reg

def mod_mod_con_id(nro_id):
    opciones = ["s", "n"]
    posicion = pos_mod_id(nro_id)
    if posicion != -1:
        archivo_logico = abrir_archivo(af_moderadores)
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
    archivo_logico = abrir_archivo(af_moderadores)
    tam_archivo = os.path.getsize(af_moderadores)
    posicion = 0
    archivo_logico.seek(0, 0)

    if tam_archivo > 0:
        registro = reconvertir_a_mod(pickle.load(archivo_logico))
        while archivo_logico.tell() < tam_archivo:
            if registro.nro_id == nro_id:
                archivo_logico.close()
                return posicion
            posicion = archivo_logico.tell()
            if archivo_logico.tell() < tam_archivo:
                registro = reconvertir_a_mod(pickle.load(archivo_logico))
        archivo_logico.close()
    return -1

def pos_mod_email(email):
    archivo_logico = abrir_archivo(af_moderadores)
    tam_archivo = os.path.getsize(af_moderadores)
    posicion = 0
    archivo_logico.seek(0, 0)

    if tam_archivo > 0:
        registro = reconvertir_a_mod(pickle.load(archivo_logico))
        while archivo_logico.tell() < tam_archivo:
            if registro.email == email:
                archivo_logico.close()
                return posicion
            posicion = archivo_logico.tell()
            if archivo_logico.tell() < tam_archivo:
                registro = reconvertir_a_mod(pickle.load(archivo_logico))
        archivo_logico.close()
    return -1



def reg_mod_email(email):
    posicion = pos_mod_email(email)
    if posicion != -1:
        archivo_logico = abrir_archivo(af_moderadores)
        archivo_logico.seek(posicion, 0)
        if archivo_logico.tell() < os.path.getsize(af_moderadores):
            registro = reconvertir_a_mod(pickle.load(archivo_logico))
            archivo_logico.close()
            return registro
        archivo_logico.close()
    return None

def listado_moderadores(direccion):
    archivo_logico = abrir_archivo(af_moderadores)
    tam = os.path.getsize(af_moderadores)
    if tam == 0:
        print("No hay moderadores para mostrar.")
    else:
        archivo_logico = abrir_archivo(direccion)
        archivo_logico.seek(0, 0)  
        print(f"{'ID':<5} {'Email':<25} {'Contraseña':<15}")
        print("-" * 50)
        while archivo_logico.tell() < tam:
            moderador_archivo = pickle.load(archivo_logico)
            salida = '{:<5} {:<25} {:<15}'.format(
                moderador_archivo.nro_id, moderador_archivo.email, moderador_archivo.contrasenia
            )
            print(salida)  
        archivo_logico.close()

def alta_moderador():
    nuevo_moderador = mod()
    nuevo_moderador.email = input("Ingrese el email del moderador: ")
    nuevo_moderador.contrasenia = input("Ingrese la contraseña del moderador: ")
    nuevo_moderador.estado = True
    clase = formatear_mod(nuevo_moderador)
    archivo_logico = abrir_archivo(af_moderadores)
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
        archivo_logico = abrir_archivo(af_moderadores)
        archivo_logico.seek(posicion, 0)
        registro = reconvertir_a_mod(pickle.load(archivo_logico))
        registro.estado = False
        archivo_logico.seek(posicion, 0)
        formateado = formatear_mod(registro)
        pickle.dump(formateado, archivo_logico)
        archivo_logico.flush()
        archivo_logico.close()


class admin:
    def __init__(self):
        self.nro_id = 0
        self.email = ""
        self.contrasenia = ""

def formatear_admin(self):
    self.nro_id =self.nro_id
    self.email = self.email.ljust(32)
    self.contrasenia = self.contrasenia.ljust(32)
    return self

def reconvertir_a_admin(registro_formateado):
    administrador = admin()
    administrador.nro_id = registro_formateado.nro_id
    administrador.email = registro_formateado.email.strip()  
    administrador.contrasenia = registro_formateado.contrasenia.strip()
    return administrador

def crear_registro_admin(nro_id, email, contrasenia):
    reg = admin()
    reg.nro_id = nro_id
    reg.email = email
    reg.contrasenia = contrasenia
    return reg

def mod_admin_con_id(nro_id):
    opciones = ["s", "n"]
    posicion = pos_admin_id(nro_id)
    if posicion != -1:
        archivo_logico = abrir_archivo(af_administradores)
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
    archivo_logico = abrir_archivo(af_administradores)
    tam_archivo = os.path.getsize(af_administradores)
    posicion = 0
    archivo_logico.seek(0, 0)

    if tam_archivo > 0:
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
    archivo_logico = abrir_archivo(af_administradores)
    tam_archivo = os.path.getsize(af_administradores)
    posicion = 0
    archivo_logico.seek(0, 0)

    if tam_archivo > 0:  
        registro = reconvertir_a_admin(pickle.load(archivo_logico))
        while archivo_logico.tell() < tam_archivo:
            if registro.email == email:
                archivo_logico.close()
                return posicion
            posicion = archivo_logico.tell()
            if archivo_logico.tell() < tam_archivo:  
                registro = reconvertir_a_admin(pickle.load(archivo_logico))
        archivo_logico.close()
    return -1 


def reg_admin_email(email):
    posicion = pos_admin_email(email)
    if posicion != -1:
        archivo_logico = abrir_archivo(af_administradores)
        archivo_logico.seek(posicion, 0)
        registro = reconvertir_a_admin(pickle.load(archivo_logico))
        return registro
    else:
        return None

def listado_administradores():
    archivo_logico = abrir_archivo(af_administradores)
    tam = os.path.getsize(af_administradores)
    if tam == 0:
        print("No hay administradores para mostrar.")
    else:
        archivo_logico = abrir_archivo(af_administradores)
        archivo_logico.seek(0, 0)  
        print(f"{'ID':<5} {'Email':<25} {'Contraseña':<15}")
        print("-" * 50)
        while archivo_logico.tell() < tam:
            admin_archivo = pickle.load(archivo_logico)
            salida = '{:<5} {:<25} {:<15}'.format(
                admin_archivo.nro_id, admin_archivo.email, admin_archivo.contrasenia
            )
            print(salida)  
        archivo_logico.close() 

def alta_administrador():
    nuevo_administrador = admin()
    nuevo_administrador.email = input("Ingrese el email del administrador: ")
    nuevo_administrador.contrasenia = input("Ingrese la contraseña del administrador: ")
    clase = formatear_admin(nuevo_administrador)
    archivo_logico = abrir_archivo(af_administradores)
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
        archivo_logico = abrir_archivo(af_administradores)
        archivo_logico.seek(posicion, 0)
        registro = reconvertir_a_admin(pickle.load(archivo_logico))
        archivo_logico.seek(posicion, 0)
        registro.estado = False
        formateado = formatear_admin(registro)
        pickle.dump(formateado, archivo_logico)
        archivo_logico.flush()
        archivo_logico.close()




class likes:
    def __init__(self):
        self.remitente=0
        self.destinatario = 0

def nuevo_like(remitente, destinatario):
    lk = likes()
    lk.remitente = remitente
    lk.destinatario = destinatario
    archivo_logico = abrir_archivo(af_likes)
    archivo_logico.seek(0, 2)
    pickle.dump(lk, archivo_logico)
    archivo_logico.flush()
    archivo_logico.close()

def existe_like(remitente, destinatario):
    archivo_logico = abrir_archivo(af_likes)
    tam_archivo = os.path.getsize(af_likes)
    archivo_logico.seek(0, 0)
    while archivo_logico.tell() < tam_archivo:
        like = pickle.load(archivo_logico)
        if like.remitente == remitente and like.destinatario == destinatario:
            archivo_logico.close()
            return True
    archivo_logico.close()
    return False

def hay_match(usuario1, usuario2):
    archivo_logico = abrir_archivo(af_likes)
    tam_archivo = os.path.getsize(af_likes)
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



class reportes:
    def __init__(self):
        self.id_reportante= 0
        self.id_reportado = 0 
        self.razon_reporte = ""
        self.estado = 0


def existe_usuario(email, password):

    alumno = reg_alumno_email(email)
    if alumno and alumno.contrasenia == password:
        return [alumno.email,  "alumno"]

    moderador = reg_mod_email(email)
    if moderador and moderador.contrasenia == password:
        return [moderador.email,  "moderador"]

    administrador = reg_admin_email(email)
    if administrador and administrador.contrasenia == password:
        return [administrador.email,  "administrador"]

    return None

def generador_id(nombre_archivo):
    if nombre_archivo == "alumnos":
        tam = os.path.getsize(af_alumnos)
    elif nombre_archivo == "moderador":
        tam = os.path.getsize(af_moderadores)
    if nombre_archivo == "alumnos":
        archivo_logico = abrir_archivo(af_alumnos)
    elif nombre_archivo == "moderador":
        archivo_logico = abrir_archivo(af_moderadores)

    nro_id = 0
    while archivo_logico.tell() < tam:
            registro = pickle.load(archivo_logico)
            nro_id = registro.nro_id

    archivo_logico.close()
    return nro_id + 1


def existe_mail(nombre_archivo, mail):
    condicion = False
    if nombre_archivo == "alumnos":
        archivo_logico = abrir_archivo(af_alumnos)
        archivo_logico.seek(0,0)
        posicion = pos_alumno_email(mail)
        if posicion != -1:
            condicion = True
    elif nombre_archivo == "moderador":
        archivo_logico = abrir_archivo(af_moderadores)
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
            modificacion_alum(None,informacion_login[0])
            print("Datos Modificados")
        elif opcion == "2":
            baja_alumno(None,informacion_login[0])
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
    tam = os.path.getsize(af_alumnos)
    if tam == 0:
        print("no hay alumnos para mostrar")
    else:
        archivo_logico = abrir_archivo(af_alumnos)
        remitente = reconvertir_a_alu(reg_alumno_email(informacion_login[0]))
        id_remitente = remitente.nro_id
        while archivo_logico.tell()<tam:

            registro = reconvertir_a_alu(pickle.load(archivo_logico))
            if registro.nro_id != id_remitente:
                imprimir_datos_estudiante(registro)
                opciones = ["s","n"]
                respuesta = ""
                while respuesta not in opciones:
                    respuesta = input("¿Quiere darle like? (s/n): ").lower()
                if respuesta == "s":
                    id_destinatario = registro.nro_id
                    nuevo_like(remitente,id_destinatario)
            

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


"""
var:
    opcion:string

"""


def moderador():
    opcion = ""
    while opcion != "3":
        opcion = imprimir_menu_moderador()
        if opcion == "1":
            """ menu_gest_user() """
        elif opcion == "2":
            """ gestionar_reportes() """
        elif opcion == "3":
            """ informacion_login[0] = "" """
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
        if not conectado():
            opcion = "3"



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
            """ matcheos_comb() """
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


""" def imprimir_tabla_ids_estudiantes():
    print("ID".ljust(5) + "Email".ljust(25) + "Nombre".ljust(15) + "Estado".ljust(10))
    for i in range(8):
        print(
            str(tabla_ids[i]).ljust(5)
            + estudiantes[i][0].ljust(25)
            + estudiantes[i][1].ljust(15)
            + estudiantes[i][4].ljust(10)
        )"""

"""
var:
    name:string

"""


""" def desactivar_usuario():
    imprimir_tabla_ids_estudiantes()
    name = input(
        "Seleccione el nombre del usuario que quiere desactivar, si no lo conoce coloque '*': "
    )

    if name != "*":
        posicion = buscar_estudiante_por_nombre(name)
        pass
        if posicion == -1:
            print("No existe ese estudiante")
        else:
            eliminar_estudiante_por_indice(posicion)
            print("Estudiante eliminado\n")

    if name == "*":
        id_est = input(
            "Seleccione el ID del usuario, si no lo conoce coloque un numero mayor a 7 o menor a 0: "
        )
        while not id_est.isdigit():
            id_est = input(
                "Seleccione el ID del usuario, si no lo conoce coloque un numero mayor a 7 o menor a 0: "
            )
        if 0 <= int(id_est) < 8:
            eliminar_estudiante_por_id(int(id_est))
            print("Estudiante eliminado")
        else:
            print("Necesitamos más datos para eliminar al usuario")"""

"""
var:
    opcion:string

"""


def menu_gest_user():
    print("1. Desactivar usuario.")
    print("2. Volver.")
    opcion = input("Seleccione una opción: ")
    while opcion != "2":
        if opcion == "1":
            """ desactivar_usuario() """
            print("1. Desactivar usuario.")
            print("2. Volver.")
            opcion = input("Seleccione una opción: ")
        else:
            opcion = input("Seleccione una opción: ")
    print("Saliendo\n")


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


""" def matcheos_comb():
    cont = 0
    for i in range(8):
        if estudiantes[i][4] == "activo":
            cont = cont + 1
    print("las combinaciones posibles son", math.comb(cont, 2)) 

 """

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
                elif existe and existe[1] == "moderador":
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

def imprimir_registro_puntero ():
    tam = os.path.getsize(af_alumnos)
    archivo_logico = abrir_archivo(af_alumnos)
    
    while archivo_logico.tell() < tam:
        registro = pickle.load(archivo_logico)
        
        print("tamanio del archivo",tam)
        print("donde esta el puntero",archivo_logico.tell())

def imprimir_registro_puntero_likes():
    tam = os.path.getsize(af_likes)  
    archivo_logico = abrir_archivo(af_likes)  
    
    while archivo_logico.tell() < tam:
        like = pickle.load(archivo_logico)
        print(f"Remitente: {like.remitente}, Destinatario: {like.destinatario}")
        print("Tamaño del archivo:", tam)
        print("Posición actual del puntero:", archivo_logico.tell())

    archivo_logico.close()


def listado_likes():
    tam = os.path.getsize(af_likes)  
    archivo_logico = abrir_archivo(af_likes)
    
    print("Listado de Likes:")
    while archivo_logico.tell() < tam:
        like = pickle.load(archivo_logico)
        print(f"Remitente: {like.remitente}, Destinatario: {like.destinatario}")
    
    archivo_logico.close()

def main():
    alumnos = abrir_archivo(af_alumnos)
    alumnos.close()
    moderadores_todos = abrir_archivo(af_moderadores)
    moderadores_todos.close()
    administradores_todos = abrir_archivo(af_administradores)
    administradores_todos.close()
    likes_todos = abrir_archivo(af_likes)
    likes_todos.close()
    reportes_todos = abrir_archivo(af_reportes)
    reportes_todos.close()
    print("-------------------------------")
    imprimir_registro_puntero()
    print("-------------------------------")
    listado_alumnos(af_alumnos)
    print("-------------------------------")
    imprimir_registro_puntero_likes()
    print("-------------------------------")
    listado_likes()

    while informacion_login[0] == "":
        informacion_login[0], informacion_login[1] = "", ""
        inicio_sesion()
        if conectado():
            if informacion_login[1] == "moderador":
                print("Sos un moderador")
                moderador()
            elif informacion_login[1] == "alumno":
                estudiante()


main()
