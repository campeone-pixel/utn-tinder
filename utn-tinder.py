# Datos de los estudiantes
estudiante1_email = "estudiante1@ayed.com"
estudiante1_contrasenia = "111222"
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

            return estudiante_conectado, email_estudiante_conectado
        else:
            intentos -= 1
            print("Email o contraseña incorrectos. Intentos restantes:", intentos)
    return False, ""


def editar_datos_personales():
    pass


def ver_candidatos():
    pass


def main():
    print("Bienvenido a UTN Tinder.")

    estudiante_conectado, email_estudiante_conectado = login()

    if estudiante_conectado:
        print("inicio exitoso", email_estudiante_conectado)

        # Imprimir el menú
        print("1. Gestionar mi perfil")
        print("2. Gestionar candidatos")
        print("3. Matcheos")
        print("4. Reportes estadísticos")
        print("0. Salir")

        opcion = input("Por favor, seleccione una opción: ")

        if opcion == "1":
            editar_datos_personales()
        elif opcion == "2":
            ver_candidatos()
        elif opcion == "3":
            print("En construccion")
        elif opcion == "4":
            print("En construccion")
        elif opcion == "0":
            print("En construccion")
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
    else:
        print("credenciales invalidas")


main()
