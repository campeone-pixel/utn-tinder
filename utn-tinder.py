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
        "2000/08/16"                   
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
        "1987/07/11"
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
        "2002/08/16"
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
        "1995/05/10"
    ],
    [
        "",  // email
        "",  // nombre
        "",  // sexo
        "",  // contraseña
        "no_activo",  // estado
        "",  // hobbies
        "",  // materia_favorita
        "",  // deporte_favorito
        "",  // materia_fuerte
        "",  // materia_debil
        "",  // biografia
        "",  // país
        "",  // ciudad
        ""   // fecha_nacimiento
    ],
    [
        "",  // email
        "",  // nombre
        "",  // sexo
        "",  // contraseña
        "no_activo",  // estado
        "",  // hobbies
        "",  // materia_favorita
        "",  // deporte_favorito
        "",  // materia_fuerte
        "",  // materia_debil
        "",  // biografia
        "",  // país
        "",  // ciudad
        ""   // fecha_nacimiento
    ],
    [
        "",  // email
        "",  // nombre
        "",  // sexo
        "",  // contraseña
        "no_activo",  // estado
        "",  // hobbies
        "",  // materia_favorita
        "",  // deporte_favorito
        "",  // materia_fuerte
        "",  // materia_debil
        "",  // biografia
        "",  // país
        "",  // ciudad
        ""   // fecha_nacimiento
    ],
    [
        "",  // email
        "",  // nombre
        "",  // sexo
        "",  // contraseña
        "no_activo",  // estado
        "",  // hobbies
        "",  // materia_favorita
        "",  // deporte_favorito
        "",  // materia_fuerte
        "",  // materia_debil
        "",  // biografia
        "",  // país
        "",  // ciudad
        ""   // fecha_nacimiento
    ]
];


def inicializacion():
    import random

    likes = [0] * 8

    for i in range(8):
        fila_nueva = [0] * 8
        for j in range(8):
            fila_nueva[j] = random.randint(0, 1)
        likes[i] = fila_nueva



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


# ----------------------------------------------------------------------------


# Funcion Inicio de sesion.
def login():
    global mail_estudiante_conectado
    intentos = 3
    while intentos > 0:
        email = input("Ingrese su email: ")
        contraseña = getpass.getpass("Ingrese su contraseña: ")

        if (
            (email == estudiante1_email and contraseña == estudiante1_contrasenia)
            or (email == estudiante2_email and contraseña == estudiante2_contrasenia)
            or (email == estudiante3_email and contraseña == estudiante3_contrasenia)
        ):
            print("inicio exitoso\n")
            mail_estudiante_conectado = email
            main()
            intentos = 0
        elif intentos != 1:
            intentos = intentos - 1
            print("intente nuevamente")
            print("intentos restantes: ", intentos)
        else:
            print("credenciales invalidas. Cerrando programa...")
            intentos = 0


# Funcion Gestionar mi perfil ,opcion 1.
def gestionar_perfil():
    global estudiante1_fecha_nac, estudiante1_hobbies, estudiante1_biografia
    global estudiante2_fecha_nac, estudiante2_hobbies, estudiante2_biografia
    global estudiante3_fecha_nac, estudiante3_hobbies, estudiante3_biografia

    menu_gestionar_perfil()
    opcion = input("Por favor, seleccione una opción: ")
    print("---------------------------------------------------------------------------")

    while opcion != "0":
        if opcion == "1":
            if mail_estudiante_conectado == "estudiante1@ayed.com":
                print("Fecha de Nacimiento actual: ", estudiante1_fecha_nac)
                estudiante1_fecha_nac = input("Ingrese nueva fecha nacimiento: ")
                print("Hobbies actuales: ", estudiante1_hobbies)
                estudiante1_hobbies = input("Ingrese nuevos hobbies: ")
                print("Biografia actual: ", estudiante1_biografia)
                estudiante1_biografia = input("Ingrese nueva biografia: ")
            elif mail_estudiante_conectado == "estudiante2@ayed.com":
                print("Fecha de Nacimiento actual: ", estudiante2_fecha_nac)
                estudiante2_fecha_nac = input("Ingrese nueva fecha nacimiento: ")
                print("Hobbies actuales: ", estudiante2_hobbies)
                estudiante2_hobbies = input("Ingrese nuevos hobbies: ")
                print("Biografia actual: ", estudiante2_biografia)
                estudiante2_biografia = input("Ingrese nueva biografia: ")
            elif mail_estudiante_conectado == "estudiante3@ayed.com":
                print("Fecha de Nacimiento actual: ", estudiante3_fecha_nac)
                estudiante3_fecha_nac = input("Ingrese nueva fecha nacimiento: ")
                print("Hobbies actuales: ", estudiante3_hobbies)
                estudiante3_hobbies = input("Ingrese nuevos hobbies: ")
                print("Biografia actual: ", estudiante3_biografia)
                estudiante3_biografia = input("Ingrese nueva biografia: ")
            else:
                print("no hay ningun estudiante conectado")

        elif opcion == "2":
            print("eliminando perfil")
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

        menu_gestionar_perfil()
        opcion = input("Por favor, seleccione una opción: ")
        print(
            "---------------------------------------------------------------------------"
        )


# Función para guardar una variable en la función Me Gusta.
def func_me_gusta():
    me_gusta = ""
    me_gusta = input("Ingrese nombre estudiante: ")
    while not (
        me_gusta == estudiante1_nombre
        or me_gusta == estudiante2_nombre
        or me_gusta == estudiante3_nombre
    ):
        print("No existe estudiante con ese nombre")
        todos_estudiantes()
        me_gusta = input("Ingrese estudiante nuevamente: ")
        print("\n")
    print("Elegiste a: ", me_gusta)
    print("\n")


# Información de los estudiantes disponibles.
def todos_estudiantes():
    if mail_estudiante_conectado == "estudiante1@ayed.com":
        print("Datos del Estudiante:")
        print("------------------------")
        print("Email:", estudiante2_email)
        print("Contraseña:", estudiante2_contrasenia)
        print("Nombre:", estudiante2_nombre)
        print(
            "Edad:",
            int(
                (
                    datetime.today()
                    - datetime.strptime(estudiante2_fecha_nac, "%Y/%m/%d")
                ).days
                / 365.2425
            ),
        )
        print("Biografía:")
        print(estudiante2_biografia)
        print("Hobbies:", estudiante2_hobbies)
        print("\n")
        print("Datos del Estudiante:")
        print("------------------------")
        print("Email:", estudiante3_email)
        print("Contraseña:", estudiante3_contrasenia)
        print("Nombre:", estudiante3_nombre)
        print(
            "Edad:",
            int(
                (
                    datetime.today()
                    - datetime.strptime(estudiante3_fecha_nac, "%Y/%m/%d")
                ).days
                / 365.2425
            ),
        )
        print("Biografía:")
        print(estudiante3_biografia)
        print("Hobbies:", estudiante3_hobbies)
        print("\n")
    elif mail_estudiante_conectado == "estudiante2@ayed.com":
        print("Datos del Estudiante:")
        print("---------------------")
        print("Email:", estudiante1_email)
        print("Contraseña:", estudiante1_contrasenia)
        print("Nombre:", estudiante1_nombre)
        print(
            "Edad:",
            int(
                (
                    datetime.today()
                    - datetime.strptime(estudiante1_fecha_nac, "%Y/%m/%d")
                ).days
                / 365.2425
            ),
        )
        print("Biografía:")
        print(estudiante1_biografia)
        print("Hobbies:", estudiante1_hobbies)
        print("\n")
        print("Datos del Estudiante:")
        print("------------------------")
        print("Email:", estudiante3_email)
        print("Contraseña:", estudiante3_contrasenia)
        print("Nombre:", estudiante3_nombre)
        print(
            "Edad:",
            int(
                (
                    datetime.today()
                    - datetime.strptime(estudiante3_fecha_nac, "%Y/%m/%d")
                ).days
                / 365.2425
            ),
        )
        print("Biografía:")
        print(estudiante3_biografia)
        print("Hobbies:", estudiante3_hobbies)
        print("\n")
    elif mail_estudiante_conectado == "estudiante3@ayed.com":
        print("Datos del Estudiante:")
        print("---------------------")
        print("Email:", estudiante1_email)
        print("Contraseña:", estudiante1_contrasenia)
        print("Nombre:", estudiante1_nombre)
        print(
            "Edad:",
            int(
                (
                    datetime.today()
                    - datetime.strptime(estudiante1_fecha_nac, "%Y/%m/%d")
                ).days
                / 365.2425
            ),
        )
        print("Biografía:")
        print(estudiante1_biografia)
        print("Hobbies:", estudiante1_hobbies)
        print("\n")
        print("Datos del Estudiante:")
        print("------------------------")
        print("Email:", estudiante2_email)
        print("Contraseña:", estudiante2_contrasenia)
        print("Nombre:", estudiante2_nombre)
        print(
            "Edad:",
            int(
                (
                    datetime.today()
                    - datetime.strptime(estudiante2_fecha_nac, "%Y/%m/%d")
                ).days
                / 365.2425
            ),
        )
        print("Biografía:")
        print(estudiante2_biografia)
        print("Hobbies:", estudiante2_hobbies)
        print("\n")


# Función de Gestionar Candidatos, Opcion 2.
def gestionar_candidatos():
    menu_gestionar_candidatos()
    opcion = input("Por favor, seleccione una opción: ")
    print("---------------------------------------------------------------------------")

    while opcion != "0":
        if opcion == "1":
            todos_estudiantes()
            func_me_gusta()
        elif opcion == "2":
            print("En Construccion\n")
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.\n")

        menu_gestionar_candidatos()
        opcion = input("Por favor, seleccione una opción: ")
        print(
            "---------------------------------------------------------------------------"
        )
    print("\n")


# Ruleta
def ruleta():
    print("Ingresar las probalidades de la persona A, B y C")
    seguir = True
    while seguir:
        match_personaA = input("Ingrese la probalidad de match con la persona A")
        match_personaB = input("Ingrese la probalidad de match con la persona B")
        match_personaC = input("Ingrese la probalidad de match con la persona C")
        while not (
            match_personaA.isdigit()
            and match_personaB.isdigit()
            and match_personaC.isdigit()
        ):
            match_personaA = input("Ingrese la probalidad de match con la persona A")
            match_personaB = input("Ingrese la probalidad de match con la persona B")
            match_personaC = input("Ingrese la probalidad de match con la persona C")
        match_personaA = int(match_personaA)
        match_personaB = int(match_personaB)
        match_personaC = int(match_personaC)
        if match_personaA + match_personaB + match_personaC == 100:
            ganador = random.choices(
                ["Persona A", "Persona B", "Persona B"],
                weights=[match_personaA, match_personaB, match_personaC],
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


# Función del Menu Principal.
def main():
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
            ruleta()
        else:
            print("Opcion Invalida\n")
        menu_principal()
        opcion = input("Por favor, seleccione una opción: ")
        print(
            "---------------------------------------------------------------------------"
        )
    print("Saliendo\n")


login()
