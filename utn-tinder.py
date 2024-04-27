estudiante1_email = "mati"
estudiante1_contrasenia = "1"
estudiante1_nombre = "111222"
estudiante1_fecha_nac = "111222"
estudiante1_biografia = []
estudiante1_hobbies = []

estudiante2_email = "estudiante2@ayed.com"
estudiante2_contrasenia = "333444"
estudiante2_nombre = "111222"
estudiante2_fecha_nac = "111222"
estudiante2_biografia = []
estudiante2_hobbies = []

estudiante3_email = "estudiante3@ayed.com"
estudiante3_contrasenia = "555666"
estudiante3_nombre = "111222"
estudiante3_fecha_nac = "111222"
estudiante3_biografia = []
estudiante3_hobbies = []


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
        contraseña = input("Ingrese su contraseña: ")
        if (
            (email == estudiante1_email and contraseña == estudiante1_contrasenia)
            or (email == estudiante2_email and contraseña == estudiante2_contrasenia)
            or (email == estudiante3_email and contraseña == estudiante3_contrasenia)
        ):
            print("inicio exitoso")
            return True  # ahora  es true
        elif intentos != 1:
            intentos = intentos - 1
            print("intente nuevamente")
            print("intentos restantes:", intentos)
        else:
            print("credenciales invalidas\n")
            return False  # ahora  es false


def gestionar_perfil():
    print("1. Gestionar mi perfil")
    print("0. Volver")

    """
    Gestionar mi perfil
    a. Editar mis datos personales
    b. Eliminar mi perfil
    c. Volver
    """
    opcion = int(input("Por favor, seleccione una opción: "))

    while opcion != 0:
        if opcion == 1:
            print(
                "ya gestionamos tu perfil de ",
                "\n",
            )
        elif opcion == 0:
            print("Volviendo\n")
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
        print("1. Gestionar mi perfil")
        print("0. Volver")
        opcion = int(input("Por favor, seleccione una opción:"))


def gestionar_candidatos():
    print("1. Gestionar candidatos")
    print("0. Volver")
    opcion = int(input("Por favor, seleccione una opción: "))

    """
    2. Gestionar candidatos
        a. Ver candidatos
        b. Reportar un candidato
        c. Volver
    """

    while opcion != 0:
        if opcion == 1:
            print(
                "ya gestionamos los candidatos de ",
                "\n",
            )
        elif opcion == 0:
            print("Volviendo\n")
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.\n")
        print("1. Gestionar candidatos")
        print("0. Volver")
        opcion = int(input("Por favor, seleccione una opción: "))


def main():
    estudiante_conectado = login()

    while estudiante_conectado:
        opcion = menu_principal()
        while opcion != 5:
            if opcion == 1:
                gestionar_perfil()
            elif opcion == 2:
                gestionar_candidatos()
            elif opcion == 3:
                print("En construccion\n")
            elif opcion == 4:
                print("En construccion\n")
        print("Saliendo")
        print("-----------------------------------------------------------------------")
        estudiante_conectado = False


main()
