# TP1 Algoritmo y Estructura de Datos.
# Integrantes:Gamero Candela, Poses Matias, Sosa Agustin, Pérez Ivo.

import getpass
from datetime import datetime
import random

estudiantes = [
    [
        "1",
        "leonardo",
        "masculino",
        "1",
        "activo",
        "estudio humanidades y me gusta el pensamiento lateral",
        "historia",
        "fútbol",
        "filosofía",
        "matemáticas",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        "Argentina",
        "Buenos Aires",
        "2000/08/16",
    ],
    [
        "estudiante2@ayed.com",
        "julian",
        "masculino",
        "333444",
        "activo",
        "estudiar matemáticas y hacer muchos cálculos de integrales",
        "matemáticas",
        "ajedrez",
        "física",
        "literatura",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        "Argentina",
        "Córdoba",
        "1987/07/11",
    ],
    [
        "estudiante3@ayed.com",
        "carolina",
        "femenino",
        "555666",
        "activo",
        "surf, andar en bici, estudiar física",
        "física",
        "surf",
        "química",
        "historia",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        "Argentina",
        "Rosario",
        "2002/08/16",
    ],
    [
        "estudiante4@ayed.com",
        "martina",
        "femenino",
        "777888",
        "activo",
        "leer libros, pintar, tocar el piano",
        "literatura",
        "natación",
        "arte",
        "biología",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        "Argentina",
        "Mendoza",
        "1995/05/10",
    ],
    [
        "estudiante3@ayed.com",
        "carolina",
        "femenino",
        "555666",
        "activo",
        "surf, andar en bici, estudiar física",
        "física",
        "surf",
        "química",
        "historia",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        "Argentina",
        "Rosario",
        "2002/08/16",
    ],
    [
        "estudiante3@ayed.com",
        "carolina",
        "femenino",
        "555666",
        "activo",
        "surf, andar en bici, estudiar física",
        "física",
        "surf",
        "química",
        "historia",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        "Argentina",
        "Rosario",
        "2002/08/16",
    ],
    [
        "estudiante3@ayed.com",
        "carolina",
        "femenino",
        "555666",
        "activo",
        "surf, andar en bici, estudiar física",
        "física",
        "surf",
        "química",
        "historia",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        "Argentina",
        "Rosario",
        "2002/08/16",
    ],
    [
        "estudiante3@ayed.com",
        "carolina",
        "femenino",
        "555666",
        "activo",
        "surf, andar en bici, estudiar física",
        "física",
        "surf",
        "química",
        "historia",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        "Argentina",
        "Rosario",
        "2002/08/16",
    ],
]

moderadores = [
    ["2", "2"],  # Datos del único moderador inicial
    ["", ""],  # Datos vacíos para el segundo moderador
    ["", ""],  # Datos vacíos para el tercer moderador
    ["", ""],  # Datos vacíos para el cuarto moderador
]


# Funciones para imprimir las opciones del Menú
def menu_principal():
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadísticos")
    print("5. Ruleta")
    print("6. Salir")


def menu_gestionar_perfil():
    print("1. Editar mis datos personales")
    print("2. Eliminar mi perfil")
    print("0. Volver\n")


def menu_gestionar_candidatos():
    print("1. Ver Candidatos")
    print("2. Reportar un candidato")
    print("0. Volver\n")


# Funcion Gestionar mi perfil ,opcion 1.
def gestionar_perfil():

    menu_gestionar_perfil()
    opcion = input("Por favor, seleccione una opción: ")
    print("---------------------------------------------------------------------------")
    while opcion != "0":
        if opcion == "1":
            print("no hay ningun estudiante conectado")
        elif opcion == "2":
            print("eliminando perfil")
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
        menu_gestionar_perfil()
        opcion = input("Por favor, seleccione una opción: ")


def gestionar_candidatos():
    menu_gestionar_candidatos()
    opcion = input("Por favor, seleccione una opción: ")
    print("---------------------------------------------------------------------------")
    while opcion != "0":
        if opcion == "1":
            print("entro al 1")
        elif opcion == "2":
            print("En Construccion\n")
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.\n")

        menu_gestionar_candidatos()
        opcion = input("Por favor, seleccione una opción: ")


def inicializacion():
    import random

    likes = [0] * 8

    for i in range(8):
        fila_nueva = [0] * 8
        for j in range(8):
            fila_nueva[j] = random.randint(0, 1)
        likes[i] = fila_nueva


def inicio_sesion(estudiantes, moderadores):
    esta_conectado = False
    mail_estudiante_conectado = None
    intentos = 3
    while intentos > 0:
        email = input("Ingrese su email: ")
        contraseña = getpass.getpass("Ingrese su contraseña: ")
        existe = existe_usuario(email, contraseña, estudiantes, moderadores)[0]
        role = existe_usuario(email, contraseña, estudiantes, moderadores)[1]

        if existe:
            print("inicio exitoso\n")
            mail_estudiante_conectado = email
            esta_conectado = True
            intentos = 0
            return [mail_estudiante_conectado, esta_conectado, role]
        elif intentos != 1:
            intentos = intentos - 1
            print("intente nuevamente")
            print("intentos restantes: ", intentos)
        else:
            print("credenciales invalidas. Cerrando programa...")
            mail_estudiante_conectado = None
            esta_conectado = False
            intentos = 0
            return [mail_estudiante_conectado, esta_conectado, role]


def existe_usuario(email, password, estudiantes, moderadores):
    existe = False
    role = ""
    for i in range(8):

        if email == estudiantes[i][0] and password == estudiantes[i][3]:
            existe = True
            role = "estudiante"
    for i in range(4):

        if email == moderadores[i][0] and password == moderadores[i][1]:
            existe = True
            role = "moderador"
    return [existe, role]


def estudiante():
    menu_principal()
    opcion = input("Por favor, seleccione una opción: ")
    print("---------------------------------------------------------------------------")
    while opcion != "6":
        if opcion == "1":
            gestionar_perfil()
        elif opcion == "2":
            gestionar_candidatos()
        elif opcion == "3":
            print("En construccion\n")
        elif opcion == "4":
            print("En construccion\n")
        elif opcion == "5":
            print("En construccion\n")
        else:
            print("Opcion Invalida\n")
        menu_principal()
        opcion = input("Por favor, seleccione una opción: ")
        print(
            "---------------------------------------------------------------------------"
        )
    print("Saliendo\n")


def moderador():
    pass


def main():
    informacion_login = inicio_sesion(estudiantes, moderadores)

    if informacion_login[2] == "moderador":
        print("sos un moderador")
    elif informacion_login[2] == "estudiante":

        while informacion_login[1]:
            estudiante()
            informacion_login[1] = False


main()
