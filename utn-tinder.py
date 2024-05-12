import getpass
from datetime import datetime

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


def calcular_edad(fecha_nacimiento):
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y/%m/%d")
    dias_anios = 365.2425
    age = int((datetime.today() - fecha_nacimiento).days / dias_anios)
    return age


def menu_principal():
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadísticos")
    print("5. Salir")

    opcion = int(input("Por favor, seleccione una opción:"))
    print("--------------------------------------------------")
    return opcion


def login():

    intentos = 3

    while intentos > 0:
        email = input("Ingrese su email: ")
        contraseña = getpass.getpass("Ingrese su contraseña: ")
        if (
            (email == estudiante1_email and contraseña == estudiante1_contrasenia)
            or (email == estudiante2_email and contraseña == estudiante2_contrasenia)
            or (email == estudiante3_email and contraseña == estudiante3_contrasenia)
        ):
            print("inicio exitoso")
            return True, email  # ahora  es true
        elif intentos != 1:
            intentos = intentos - 1
            print("intente nuevamente")
            print("intentos restantes:", intentos)
        else:
            print("credenciales invalidas\n")
            return False, None  # ahora  es false


def gestionar_perfil(estudiante):
    print("1. Gestionar mi perfil")
    print("2. Eliminar mi perfil")
    print("0. Volver")

    opcion = int(input("Por favor, seleccione una opción: "))

    while opcion != 0:
        if opcion == 1:

            if estudiante == "estudiante1@ayed.com":
                print("Fecha de Nacimiento actual: ", estudiante1_fecha_nac)
                estudiante1_fecha_nac = input("Ingrese nueva fecha nacimiento: ")
                print("Hobbies actuales: ", estudiante1_hobbies)
                estudiante1_hobbies = input("Ingrese nuevos hobbies: ")
                print("Biografia actual: ", estudiante1_biografia)
                estudiante1_biografia = input("Ingrese nueva biografia: ")
            elif estudiante == "estudiante2@ayed.com":
                print("Fecha de Nacimiento actual: ", estudiante2_fecha_nac)
                estudiante2_fecha_nac = input("Ingrese nueva fecha nacimiento: ")
                print("Hobbies actuales: ", estudiante2_hobbies)
                estudiante2_hobbies = input("Ingrese nuevos hobbies: ")
                print("Biografia actual: ", estudiante2_biografia)
                estudiante2_biografia = input("Ingrese nueva biografia: ")
            elif estudiante == "estudiante3@ayed.com":
                print("Fecha de Nacimiento actual: ", estudiante3_fecha_nac)
                estudiante3_fecha_nac = input("Ingrese nueva fecha nacimiento: ")
                print("Hobbies actuales: ", estudiante3_hobbies)
                estudiante3_hobbies = input("Ingrese nuevos hobbies: ")
                print("Biografia actual: ", estudiante3_biografia)
                estudiante3_biografia = input("Ingrese nueva biografia: ")
            else:
                print("no hay ningun estudiante conectado")

        elif opcion == 2:
            print("eliminando perfil\n")

        elif opcion == 0:
            print("Volviendo\n")
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
        print("1. Gestionar mi perfil")
        print("0. Volver")
        opcion = int(input("Por favor, seleccione una opción:"))


def gestionar_candidatos(estudiante):
    print("1. Gestionar candidatos")
    print("2. Reportar un candidato")
    print("0. Volver")
    opcion = int(input("Por favor, seleccione una opción: "))

    while opcion != 0:

        def todos_estudiantes():
            print("Datos del Estudiante:")
            print("---------------------")
            print("Email:", estudiante1_email)
            print("Contraseña:", estudiante1_contrasenia)
            print("Nombre:", estudiante1_nombre)
            print("Edad:", calcular_edad(estudiante1_fecha_nac))
            print("Biografía:")
            print(estudiante1_biografia)
            print("Hobbies:", estudiante1_hobbies)
            print("\n")
            print("Datos del Estudiante 2:")
            print("------------------------")
            print("Email:", estudiante2_email)
            print("Contraseña:", estudiante2_contrasenia)
            print("Nombre:", estudiante2_nombre)
            print("Edad:", calcular_edad(estudiante2_fecha_nac))
            print("Biografía:")
            print(estudiante2_biografia)
            print("Hobbies:", estudiante2_hobbies)
            print("\n")
            print("Datos del Estudiante 3:")
            print("------------------------")
            print("Email:", estudiante3_email)
            print("Contraseña:", estudiante3_contrasenia)
            print("Nombre:", estudiante3_nombre)
            print("Edad:", calcular_edad(estudiante3_fecha_nac))
            print("Biografía:")
            print(estudiante3_biografia)
            print("Hobbies:", estudiante3_hobbies)
            print("\n")

        if opcion == 1:
            todos_estudiantes()

            me_gusta = input("Ingrese nombre estudiante")
            while (
                me_gusta != estudiante1_nombre
                or me_gusta != estudiante2_nombre
                or me_gusta != estudiante3_nombre
            ):
                print("No existe estudiante con ese nombre")
                todos_estudiantes()
                me_gusta = input("Ingrese estudiante nuevamente")

        elif opcion == 0:
            print("Candidato reportado\n")
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.\n")
        print("1. Gestionar candidatos")
        print("0. Volver")
        opcion = int(input("Por favor, seleccione una opción: "))


def main():
    conectado, estudiante = login()

    while conectado:
        opcion = menu_principal()
        while opcion != 5:
            if opcion == 1:
                gestionar_perfil(estudiante)
            elif opcion == 2:
                gestionar_candidatos(estudiante)
            elif opcion == 3:
                print("En construccion\n")
            elif opcion == 4:
                print("En construccion\n")
        print("Saliendo")
        print("-----------------------------------------------------------------------")
        conectado = False


main()
