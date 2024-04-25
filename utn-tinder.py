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


def login():
    estudiante_conectado = False
    email_estudiante_conectado = ""
    intentos = 3
    while intentos > 0:
        email = input("Ingrese su email: ")
        contraseña = input("Ingrese su contraseña: ")

        if (
            (email == estudiante1_email and contraseña == estudiante1_contrasenia)
            or (email == estudiante2_email and contraseña == estudiante2_contrasenia)
            or (email == estudiante3_email and contraseña == estudiante3_contrasenia)
        ):
            estudiante_conectado = True
            email_estudiante_conectado = email
            print("inicio exitoso", email_estudiante_conectado)
            return estudiante_conectado, email_estudiante_conectado
        elif intentos == 1:
            intentos -= 1
            print("credenciales invalidas")
            return False, ""
        else:
            intentos -= 1
            print("Email o contraseña incorrectos. Intentos restantes:", intentos)
    return False, ""


def gestionar_perfil(estudiante_conectado, email_estudiante_conectado):
    print("1. Gestionar mi perfil")
    print("0. Volver")
    opcion = input("Por favor, seleccione una opción: ")
    if opcion == "1":
        print("ya gestionamos tu perfil de " + email_estudiante_conectado.capitalize())
        main(estudiante_conectado, email_estudiante_conectado)
    elif opcion == "0":
        print("Volviendo")
        main(estudiante_conectado, email_estudiante_conectado)
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")


def gestionar_candidatos(estudiante_conectado, email_estudiante_conectado):
    print("1. Gestionar candidatos")
    print("0. Volver")
    opcion = input("Por favor, seleccione una opción: ")
    if opcion == "1":
        print(
            "ya gestionamos los candidatos de "
            + email_estudiante_conectado.capitalize()
        )
        main(estudiante_conectado, email_estudiante_conectado)
    elif opcion == "0":
        print("Volviendo")
        main(estudiante_conectado, email_estudiante_conectado)
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")


def main(estudiante_conectado, email_estudiante_conectado):
    print("Perfil: " + email_estudiante_conectado.capitalize())

    if estudiante_conectado:
        print("1. Gestionar mi perfil")
        print("2. Gestionar candidatos")
        print("3. Matcheos")
        print("4. Reportes estadísticos")
        print("0. Salir")

        opcion = input("Por favor, seleccione una opción: ")

        if opcion == "1":
            gestionar_perfil(estudiante_conectado, email_estudiante_conectado)
        elif opcion == "2":
            gestionar_candidatos(estudiante_conectado, email_estudiante_conectado)
        elif opcion == "3":
            print("En construccion")
        elif opcion == "4":
            print("En construccion")
        elif opcion == "0":
            print("Saliendo")
            main(False, "")
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
    else:
        estudiante_conectado, email_estudiante_conectado = login()  # type: ignore
        if estudiante_conectado:
            main(estudiante_conectado, email_estudiante_conectado)


main(False, "")
