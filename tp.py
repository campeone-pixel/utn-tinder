# TP1 Algoritmo y Estructura de Datos.
# Integrantes:Gamero Candela, Poses Matias, Sosa Agustin, Pérez Ivo.

import getpass
from datetime import datetime
import random

estudiantes = [
    [
        "estudiante1@ayed.com",
        "leonardo",
        "masculino",
        "111222",
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
    [],
    [],
    [],
    [],
]


def inicializacion():
    import random

    likes = [0] * 8

    for i in range(8):
        fila_nueva = [0] * 8
        for j in range(8):
            fila_nueva[j] = random.randint(0, 1)
        likes[i] = fila_nueva


def inicio_sesion(estudiantes):
    esta_conectado = False
    mail_estudiante_conectado = None
    intentos = 3
    while intentos > 0:
        email = input("Ingrese su email: ")
        contraseña = getpass.getpass("Ingrese su contraseña: ")

        if existe_usuario(email, contraseña, estudiantes):
            print("inicio exitoso\n")
            mail_estudiante_conectado = email
            esta_conectado = True
            return [mail_estudiante_conectado, esta_conectado]
            intentos = 0
        elif intentos != 1:
            intentos = intentos - 1
            print("intente nuevamente")
            print("intentos restantes: ", intentos)
        else:
            print("credenciales invalidas. Cerrando programa...")
            mail_estudiante_conectado = None
            esta_conectado = False
            return [mail_estudiante_conectado, esta_conectado]
            intentos = 0


def existe_usuario(email, password, estudiantes):
    existe = False
    for i in range(8):
        print(estudiantes[i][0])
        # if email == estudiantes[i][0] and password == estudiantes[i][3]:
        #     existe = True

    return existe


def estudiante():
    pass


def moderador():
    pass


def main():
    informacion_login = inicio_sesion(estudiantes)

    while informacion_login[1]:
        print("entro")


main()
