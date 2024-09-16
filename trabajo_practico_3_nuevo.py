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
    self.estado = '1'.ljust(1) if self.estado else '0'.ljust(1)  
    self.hobbies = self.hobbies.ljust(255)
    self.materia_favorita = self.materia_favorita.ljust(16)
    self.deporte_favorito = self.deporte_favorito.ljust(16)
    self.materia_fuerte = self.materia_fuerte.ljust(16)
    self.materia_debil = self.materia_debil.ljust(16)
    self.biografia = self.biografia.ljust(255)
    self.pais = self.pais.ljust(32)
    self.ciudad = self.ciudad.ljust(32)
    self.fecha_nacimiento = self.fecha_nacimiento.strftime("%Y/%m/%d").ljust(10)
    return self  # Retornar el objeto formateado


def convertir_a_alu(registro_formateado):
    alumno = alu()
    alumno.id = int(registro_formateado.id.strip())  
    alumno.email = registro_formateado.email.strip()  
    alumno.nombre = registro_formateado.nombre.strip()
    alumno.sexo = registro_formateado.sexo.strip()
    alumno.contrasenia = registro_formateado.contrasenia.strip()
    alumno.estado = registro_formateado.estado.strip() == '1'  
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

class mod:
    def __init__(self):
        self.nro_id = 0
        self.email = ""
        self.contrasenia = ""
        self.estado = True

def formatear_mod(self):
    self.id = str(self.id).ljust(4)  # Convertir id en cadena y aplicamos ljust()
    self.email = self.email.ljust(32)
    self.contrasenia = self.contrasenia.ljust(32)
    self.estado = '1'.ljust(1) if self.estado else '0'.ljust(1)  # Estado como 1 o 0
    return self

def convertir_a_mod(registro_formateado):
    moder = mod()
    moder.id = int(registro_formateado.id.strip())  # Convertir id a entero
    moder.email = registro_formateado.email.strip()  # Eliminar espacios extra
    moder.contrasenia = registro_formateado.contrasenia.strip()
    moder.estado = registro_formateado.estado.strip() == '1'  # Convertir a booleano
    return moder


class admin:
    def __init__(self):
        self.nro_id = 0
        self.email = ""
        self.contrasenia = ""

def formatear_admin(self):
    self.id = str(self.id).ljust(4)  # Convertir id en cadena y aplicamos ljust()
    self.email = self.email.ljust(32)
    self.contrasenia = self.contrasenia.ljust(32)
    return self

def convertir_a_admin(registro_formateado):
    administrador = admin()
    administrador.id = int(registro_formateado.id.strip())  # Convertir id a entero
    administrador.email = registro_formateado.email.strip()  # Eliminar espacios extra
    administrador.contrasenia = registro_formateado.contrasenia.strip()
    return administrador


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

def crear_registro_mod(nro_id, email, contrasenia, estado):
    reg = mod()
    reg.id = nro_id
    reg.email = email
    reg.contrasenia = contrasenia
    reg.estado = estado
    return reg


def crear_registro_admin(nro_id, email, contrasenia):
    reg = admin()
    reg.id = nro_id
    reg.email = email
    reg.contrasenia = contrasenia
    return reg


# Verificación y apertura de archivos
def abrir_archivo(archivo_fisico,modo= "r+b"):
    if os.path.exists(archivo_fisico):
        # Si el archivo existe, lo abrimos en modo lectura/escritura binaria
        archivo_logico = open(archivo_fisico, modo)
    else:
        # Si no existe, lo creamos en modo escritura/lectura binaria
        archivo_logico = open(archivo_fisico, "w+b")
    return archivo_logico

def buscar_alumno(busqueda,dato):
    tipo = ["id","mail"]
    if busqueda not in tipo:
        print("no existe esa busqueda")
    else:
        archivo_logico = abrir_archivo(af_alumnos)
        tam = os.path.getsize(af_alumnos)
        pos = 0
        archivo_logico.seek(0,0)
        alum = pickle.load(archivo_logico)
        while (archivo_logico.tell() < tam) and (alum.busqueda != dato):
            pos = archivo_logico.tell()
            alum = pickle.load(archivo_logico)
        if alum.busqueda == dato:
            return pos
        else:
            return -1

def listado_alumnos(direccion):
    tam = os.path.getsize(direccion)
    if tam ==0:
        print("no hay nada para mostrar")
    else:
        archivo_logico = abrir_archivo(direccion)
        archivo_logico.seek(0,0)
        while archivo_logico.tell()<tam:
            alum = pickle.load(archivo_logico)
            
            salida = '{:<5} {:<25} {:<20} {:<6} {:<15}'.format(
                alum.nro_id, alum.email, alum.nombre, alum.sexo, alum.contrasenia
            )
            print(salida)  # Imprimir la salida formateada
        archivo_logico.close()  # Cerrar el archivo

def listado_moderadores(direccion):
    tam = os.path.getsize(direccion)
    if tam == 0:
        print("No hay moderadores para mostrar.")
    else:
        archivo_logico = abrir_archivo(direccion)
        archivo_logico.seek(0, 0)  # Volver al principio del archivo
        print(f"{'ID':<5} {'Email':<25} {'Contraseña':<15}")
        print("-" * 50)
        while archivo_logico.tell() < tam:
            moderador = pickle.load(archivo_logico)
            salida = '{:<5} {:<25} {:<15}'.format(
                moderador.nro_id, moderador.email, moderador.contrasenia
            )
            print(salida)  # Imprimir la salida formateada
        archivo_logico.close()  # Cerrar el archivo

def listado_administradores(direccion):
    tam = os.path.getsize(direccion)
    if tam == 0:
        print("No hay administradores para mostrar.")
    else:
        archivo_logico = abrir_archivo(direccion)
        archivo_logico.seek(0, 0)  # Volver al principio del archivo
        print(f"{'ID':<5} {'Email':<25} {'Contraseña':<15}")
        print("-" * 50)
        while archivo_logico.tell() < tam:
            administrador = pickle.load(archivo_logico)
            salida = '{:<5} {:<25} {:<15}'.format(
                administrador.nro_id, administrador.email, administrador.contrasenia
            )
            print(salida)  # Imprimir la salida formateada
        archivo_logico.close()  # Cerrar el archivo

def guardar_alumno(clase, direccion):
    clase = formatear_alum(clase)  # Formateamos el objeto antes de guardarlo
    archivo_logico = abrir_archivo(direccion, "ab")  # Abrimos en modo append binario
    pickle.dump(clase, archivo_logico)  # Guardamos el objeto en el archivo
    archivo_logico.flush()  # Aseguramos que los datos se escriban
    archivo_logico.close()  # Cerramos el archivo

def guardar_moderador(moderador, direccion):
    moderador = formatear_mod(moderador)  # Formatear el objeto antes de guardarlo
    archivo_logico = abrir_archivo(direccion, "ab")  # Abrir en modo append binario
    pickle.dump(moderador, archivo_logico)  # Guardar el objeto en el archivo
    archivo_logico.flush()  # Asegurarse de escribir los datos
    archivo_logico.close()  # Cerrar el archivo

def guardar_administrador(administrador, direccion):
    administrador = formatear_admin(administrador)  # Formatear el objeto antes de guardarlo
    archivo_logico = abrir_archivo(direccion, "ab")  # Abrir en modo append binario
    pickle.dump(administrador, archivo_logico)  # Guardar el objeto en el archivo
    archivo_logico.flush()  # Asegurarse de escribir los datos
    archivo_logico.close()  # Cerrar el archivo
def inicializacion():
    alumno1 = crear_registro_alu(
        nro_id=1,
        email="alumno1@mail.com",
        nombre="Alumno Uno",
        sexo="M",
        contrasenia="pass123",
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
        """ if opcion == "1":
            intentos = 3
            while intentos > 0:
                mail = input("Ingrese su email: ")
                contraseña = getpass.getpass("Ingrese su contraseña: ")
                existe = existe_usuario(mail, contraseña)
                if (
                    existe
                    and que_role(mail, contraseña) == "estudiante"
                    and estudiante_activo_por_mail(mail)
                ):
                    informacion_login[0] = mail
                    informacion_login[1] = que_role(mail, contraseña)
                    print("Inicio exitoso\n")
                    intentos = 0
                elif existe and que_role(mail, contraseña) == "moderador":
                    informacion_login[0] = mail
                    informacion_login[1] = que_role(mail, contraseña)
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
            agregar_estudiante()
            print("registro exitoso")
        elif opcion == "3":
            print("Saliendo del programa...")
            informacion_login[0] = "salir"
        else:
            print("Opción no válida. Por favor, ingrese una opción válida (1, 2, o 3).") """


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
            elif informacion_login[1] == "estudiante":
                estudiante()


main()
