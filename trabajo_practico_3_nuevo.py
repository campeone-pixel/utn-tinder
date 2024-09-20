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
- Matias Abel Poses
- Santiago Porcel
- OROÑO, Martin
Comision 11
"""

af_alumnos = ".\\alumnos.dat"
af_moderadores = ".\\moderadores.dat"
af_administradores = ".\\administradores.dat"

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
    self.nro_id = str(self.nro_id).ljust(4)  
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
    alumno.nro_id = int(registro_formateado.nro_id.strip())  
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
    alumno.fecha_nacimiento = datetime.strptime(registro_formateado.fecha_nacimiento.strip(), "%Y/%m/%d")
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
        print("entro al while")
        posicion = archivo_logico.tell()
        registro = reconvertir_a_alu(pickle.load(archivo_logico))
    if registro.nro_id == nro_id:
        return posicion
    else:
        return -1


def reg_alumno_id(nro_id):
    posicion = pos_alumno_id(nro_id)
    if posicion != -1:
        archivo_logico = abrir_archivo(af_alumnos)
        archivo_logico.seek(posicion,0)
        registro = reconvertir_a_alu(pickle.load(archivo_logico))
        return registro
    else:
        return None

def mod_alum_con_id(nro_id):
    opciones = ["s","n"]
    posicion = pos_alumno_id(nro_id)
    if posicion !=-1:
        archivo_logico = abrir_archivo(af_alumnos)
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

def guardar_alumno(clase_alu, direccion):

    clase = formatear_alum(clase_alu) 
    archivo_logico = abrir_archivo(direccion)  
    archivo_logico.seek(0,2)
    pickle.dump(clase, archivo_logico)  
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
            salida = '{:<5} {:<25} {:<20} {:<6} {:<15}'.format(
                alum_archivo.nro_id,  alum_archivo.nombre, alum_archivo.sexo, alum_archivo.contrasenia, str(alum_archivo.fecha_nacimiento)
            )
            print(salida) 
        archivo_logico.close() 

def pos_alumno_email(email):
    archivo_logico = abrir_archivo(af_alumnos)
    tam_archivo = os.path.getsize(af_alumnos)
    posicion = 0
    archivo_logico.seek(0, 0)
    registro = reconvertir_a_alu(pickle.load(archivo_logico))
    while archivo_logico.tell() < tam_archivo and registro.email != email:
        posicion = archivo_logico.tell()
        registro = reconvertir_a_alu(pickle.load(archivo_logico))
    if registro.email == email:
        return posicion
    else:
        return -1

def reg_alumno_email(email):
    posicion = pos_alumno_email(email)
    if posicion != -1:
        archivo_logico = abrir_archivo(af_alumnos)
        archivo_logico.seek(posicion, 0)
        registro = reconvertir_a_alu(pickle.load(archivo_logico))
        return registro
    else:
        return None
 


class mod:
    def __init__(self):
        self.nro_id = 0
        self.email = ""
        self.contrasenia = ""
        self.estado = True


class admin:
    def __init__(self):
        self.nro_id = 0
        self.email = ""
        self.contrasenia = ""



def formatear_mod(self):
    self.nro_id = str(self.nro_id).ljust(4) 
    self.email = self.email.ljust(32)
    self.contrasenia = self.contrasenia.ljust(32)
    return self

def formatear_admin(self):
    self.nro_id = str(self.nro_id).ljust(4)  
    self.email = self.email.ljust(32)
    self.contrasenia = self.contrasenia.ljust(32)
    return self


def reconvertir_a_mod(registro_formateado):
    moder = mod()
    moder.nro_id = int(registro_formateado.id.strip())  
    moder.email = registro_formateado.email.strip()  
    moder.contrasenia = registro_formateado.contrasenia.strip()
    moder.estado = registro_formateado.estado
    return moder


def reconvertir_a_admin(registro_formateado):
    administrador = admin()
    administrador.nro_id = int(registro_formateado.id.strip())  
    administrador.email = registro_formateado.email.strip()  
    administrador.contrasenia = registro_formateado.contrasenia.strip()
    return administrador


def crear_registro_mod(nro_id, email, contrasenia, estado):
    reg = mod()
    reg.nro_id = nro_id
    reg.email = email
    reg.contrasenia = contrasenia
    reg.estado = estado
    return reg


def crear_registro_admin(nro_id, email, contrasenia):
    reg = admin()
    reg.nro_id = nro_id
    reg.email = email
    reg.contrasenia = contrasenia
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
    registro = reconvertir_a_mod(pickle.load(archivo_logico))
    while archivo_logico.tell() < tam_archivo and registro.nro_id != nro_id:
        posicion = archivo_logico.tell()
        registro = reconvertir_a_mod(pickle.load(archivo_logico))
    if registro.nro_id == nro_id:
        return posicion
    else:
        return -1

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
    registro = reconvertir_a_admin(pickle.load(archivo_logico))
    while archivo_logico.tell() < tam_archivo and registro.nro_id != nro_id:
        posicion = archivo_logico.tell()
        registro = reconvertir_a_admin(pickle.load(archivo_logico))
    if registro.nro_id == nro_id:
        return posicion
    else:
        return -1


def listado_moderadores(direccion):
    tam = os.path.getsize(direccion)
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

def listado_administradores(direccion):
    tam = os.path.getsize(direccion)
    if tam == 0:
        print("No hay administradores para mostrar.")
    else:
        archivo_logico = abrir_archivo(direccion)
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


def guardar_moderador(clase_mod, direccion):
    mod_formateado = formatear_mod(clase_mod)  
    archivo_logico = abrir_archivo(direccion)  
    archivo_logico.seek(0,2)
    pickle.dump(mod_formateado, archivo_logico)  
    archivo_logico.flush()  
    archivo_logico.close()  

def guardar_administrador(clase_adm, direccion):
    adm_formateado = formatear_admin(clase_adm)  
    archivo_logico = abrir_archivo(direccion)  
    archivo_logico.seek(0,2)
    pickle.dump(adm_formateado, archivo_logico)  
    archivo_logico.flush()  
    archivo_logico.close() 

def pos_mod_email(email):
    archivo_logico = abrir_archivo(af_moderadores)
    tam_archivo = os.path.getsize(af_moderadores)
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
        archivo_logico = abrir_archivo(af_moderadores)
        archivo_logico.seek(posicion, 0)
        registro = reconvertir_a_mod(pickle.load(archivo_logico))
        return registro
    else:
        return None

def pos_admin_email(email):
    archivo_logico = abrir_archivo(af_administradores)
    tam_archivo = os.path.getsize(af_administradores)
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
        archivo_logico = abrir_archivo(af_administradores)
        archivo_logico.seek(posicion, 0)
        registro = reconvertir_a_admin(pickle.load(archivo_logico))
        return registro
    else:
        return None


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


def inicializacion():
    alumno1 = crear_registro_alu(
        nro_id=1,
        email="12",
        nombre="Alumno Uno",
        sexo="M",
        contrasenia="12",
        estado=True,
        hobbies="Leer",
        materia_favorita="Matemáticas",
        deporte_favorito="Fútbol",
        materia_fuerte="Física",
        materia_debil="Historia",
        biografia="Estudiante de ingeniería.",
        pais="Argentina",
        ciudad="Buenos Aires",
        fecha_nacimiento=datetime.strptime("1995/06/01", "%Y/%m/%d")
    )
    alumno2 = crear_registro_alu(
        nro_id=2,
        email="alumno2@mail.com",
        nombre="Alumno Dos",
        sexo="F",
        contrasenia="pass456",
        estado=True,
        hobbies="Correr",
        materia_favorita="Química",
        deporte_favorito="Natación",
        materia_fuerte="Biología",
        materia_debil="Geografía",
        biografia="Estudiante de biología.",
        pais="Argentina",
        ciudad="Rosario",
        fecha_nacimiento=datetime.strptime("1996/07/15", "%Y/%m/%d")
    )
    alumno3 = crear_registro_alu(
        nro_id=3,
        email="alumno3@mail.com",
        nombre="Alumno Tres",
        sexo="M",
        contrasenia="pass789",
        estado=True,
        hobbies="Programar",
        materia_favorita="Computación",
        deporte_favorito="Ajedrez",
        materia_fuerte="Matemáticas",
        materia_debil="Arte",
        biografia="Estudiante de ciencias de la computación.",
        pais="Argentina",
        ciudad="Córdoba",
        fecha_nacimiento=datetime.strptime("1997/03/22", "%Y/%m/%d")
    )  
    moderador1 = crear_registro_mod(
        nro_id=1,
        email="moderador@mail.com",
        contrasenia="modpass123",
        estado=True
    )
    administrador1 = crear_registro_admin(
        nro_id=1,
        email="admin@mail.com",
        contrasenia="adminpass456"
    )




    guardar_alumno(alumno1,af_alumnos)
    guardar_alumno(alumno2,af_alumnos)
    guardar_alumno(alumno3,af_alumnos)
    guardar_moderador(moderador1,af_moderadores)
    guardar_administrador(administrador1,af_administradores)
    
    imprimir_alu(reg_alumno_id(1))



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
            """ modificar_estudiante_por_mail(informacion_login[0]) """
        elif opcion == "2":
            print("Eliminando perfil")
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
            """ ver_candidatos() """
        elif opcion == "2":
            """ reportar_candidato() """
        elif opcion != "0":
            print("Opción no válida. Por favor, seleccione una opción válida.\n")



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
            """ gestionar_candidatos() """
        elif opcion == "3":
            """ edad_faltante() """
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
                print(existe)
                if (
                    existe
                    and existe[1] == "alumno"
            
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
            """ agregar_estudiante() """
            print("registro exitoso")
        elif opcion == "3":
            print("Saliendo del programa...")
            informacion_login[0] = "salir"
        else:
            print("Opción no válida. Por favor, ingrese una opción válida (1, 2, o 3).")



def main():
    inicializacion()
    listado_alumnos(af_alumnos)
    listado_administradores(af_administradores)
    listado_moderadores(af_moderadores)
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
