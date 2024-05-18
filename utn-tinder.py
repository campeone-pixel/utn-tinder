import getpass
from datetime import datetime
import random

estudiante1_email = "estudiante1@ayed.com"
estudiante1_contrasenia = "111222"
estudiante1_nombre = "leonardo"
estudiante1_fecha_nac = "2000/08/16"
estudiante1_biografia = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
estudiante1_hobbies = "estudio humanidades y me gusta el pensamiento lateral"

estudiante2_email = "estudiante2@ayed.com"
estudiante2_contrasenia = "333444"
estudiante2_nombre = "julian"
estudiante2_fecha_nac = "1987/07/11"
estudiante2_biografia = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
estudiante2_hobbies = "estudiar matematicas y hacer muchos calculos de integrales"


estudiante3_email = "estudiante3@ayed.com"
estudiante3_contrasenia = "555666"
estudiante3_nombre = "carolina"
estudiante3_fecha_nac = "2002/08/16"
estudiante3_biografia = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
estudiante3_hobbies = "surf, andar en bici, estudiar fisica"

mail_estudiante_conectado = ""


def menu_principal():
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadísticos")
    print("5. Ruleta")
    print("6. Salir")


def menu_gestionar_perfil():
    print("1. Gestionar mi perfil")
    print("2. Eliminar mi perfil")
    print("0. Volver\n")


def menu_gestionar_candidatos():
    print("1. Gestionar candidatos")
    print("2. Reportar un candidato")
    print("0. Volver\n")


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


def ruleta():

    print(
        "De 3 personas selecciona las posibiladades de cada uno, sumando la probalidades total en 100 por ciento"
    )
    match_personaA = int(input("Ingrese la probalidad de match con la persona A"))
    match_personaB = int(input("Ingrese probalidad de matcheo con la persona B"))
    match_personaC = int(input("Ingrese probalidad de matcheo con la persona C"))

    while match_personaA + match_personaB + match_personaC != 100:
        print("Las probalidades no suman 100 por ciento")
        print(
            "De 3 personas selecciona las posibiladades de cada uno, sumando la probalidades total en 100 por ciento"
        )
        match_personaA = int(input("Ingrese la probalidad de match con la persona A"))
        match_personaB = int(input("Ingrese probalidad de matcheo con la persona B"))
        match_personaC = int(input("Ingrese probalidad de matcheo con la persona C"))

    ganador = random.choices(
        ["Persona A", "Persona B", "Persona B"],
        weights=[match_personaA, match_personaB, match_personaC],
    )

    print("La persona seleccionada es: ", ganador)


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
