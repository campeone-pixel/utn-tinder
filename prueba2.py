from datetime import datetime
import getpass
import random
import os

# Definición de variables globales
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
        "Lorem ipsum dolor sit amet.",
        "Argentina",
        "Buenos Aires",
        "2000/08/16",
    ],
    [
        "2",
        "julian",
        "masculino",
        "2",
        "activo",
        "estudiar matemáticas y hacer muchos cálculos de integrales",
        "matemáticas",
        "ajedrez",
        "física",
        "literatura",
        "Lorem ipsum dolor sit amet.",
        "Argentina",
        "Córdoba",
        "1987/07/11",
    ],
    [
        "3",
        "carolina",
        "femenino",
        "3",
        "activo",
        "surf, andar en bici, estudiar física",
        "física",
        "surf",
        "química",
        "historia",
        "Lorem ipsum dolor sit amet.",
        "Argentina",
        "Rosario",
        "2002/08/16",
    ],
    [
        "4",
        "miguel",
        "masculino",
        "4",
        "no_activo",
        "leer libros de ciencia ficción y jugar al tenis",
        "literatura",
        "tenis",
        "biología",
        "química",
        "Lorem ipsum dolor sit amet.",
        "España",
        "Madrid",
        "1995/05/20",
    ],
    [
        "estudiante5@ayed.com",
        "lucía",
        "femenino",
        "999000",
        "activo",
        "tocar la guitarra y aprender idiomas",
        "música",
        "guitarra",
        "inglés",
        "francés",
        "Lorem ipsum dolor sit amet.",
        "México",
        "Ciudad de México",
        "1998/10/30",
    ],
    [
        "estudiante6@ayed.com",
        "javier",
        "masculino",
        "111222",
        "activo",
        "programar y jugar videojuegos",
        "informática",
        "videojuegos",
        "matemáticas",
        "historia",
        "Lorem ipsum dolor sit amet.",
        "Colombia",
        "Bogotá",
        "2001/03/15",
    ],
    [
        "estudiante7@ayed.com",
        "sofía",
        "femenino",
        "333555",
        "activo",
        "dibujar y practicar yoga",
        "arte",
        "yoga",
        "historia del arte",
        "literatura",
        "Lorem ipsum dolor sit amet.",
        "Chile",
        "Santiago",
        "1999/09/05",
    ],
    [
        "estudiante8@ayed.com",
        "diego",
        "masculino",
        "444777",
        "no_activo",
        "viajar y estudiar economía",
        "viajar",
        "economía",
        "geografía",
        "ciencias políticas",
        "Lorem ipsum dolor sit amet.",
        "Perú",
        "Lima",
        "1997/12/25",
    ],
    [
        "estudiante8@ayed.com",
        "diego2",
        "masculino",
        "444777",
        "no_activo",
        "viajar y estudiar economía",
        "viajar",
        "economía",
        "geografía",
        "ciencias políticas",
        "Lorem ipsum dolor sit amet.",
        "Perú",
        "Lima",
        "1997/12/25",
    ],
    [
        "estudiante8@ayed.com",
        "diego3",
        "masculino",
        "444777",
        "no_activo",
        "viajar y estudiar economía",
        "viajar",
        "economía",
        "geografía",
        "ciencias políticas",
        "Lorem ipsum dolor sit amet.",
        "Perú",
        "Lima",
        "1997/12/25",
    ],
]

moderadores = [
    ["9", "9"],
    ["", ""],
    ["", ""],
    ["", ""],
]

likes = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

tabla_ids = [0, 1, 2, 3, 4, 5, 6, 7]

tabla_reportes = [[""] * 3 for n in range(56)]

informacion_login = ["", ""]


def imprimir_tabla(array, fila=None):
    if not array:
        print("El array está vacío.")
        return
    max_columns = max(len(row) for row in array)
    col_widths = [0] * max_columns
    for row in array:
        for i, item in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(item)))

    def imprimir_fila(fila_array):
        for i, dato in enumerate(fila_array):
            print(f"{str(dato):<{col_widths[i]}}", end=" | ")
        print()

    if fila is not None:
        if 0 <= fila < len(array):
            imprimir_fila(array[fila])
        else:
            print(f"Fila {fila} no es válida. Debe estar entre 0 y {len(array) - 1}.")
    else:
        for fila_array in array:
            imprimir_fila(fila_array)


def inicializacion():
    for i in range(8):
        for j in range(8):
            if (
                estudiante_activo_por_mail(estudiantes[i][0])
                and estudiante_activo_por_mail(estudiantes[j][0])
            ) and (estudiantes[i][0] != estudiantes[j][0]):
                me_gusta = random.randint(0, 1)
                likes[i][j] = me_gusta
            else:
                likes[i][j] = 0


def calcular_edad(fecha_nacimiento):
    fecha_nac = datetime.strptime(fecha_nacimiento, "%Y/%m/%d")
    edad = int((datetime.today() - fecha_nac).days / 365.2425)
    return edad


def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


def obtener_anio():
    while True:
        anio = input("Ingrese el año (aaaa): ")
        if anio.isdigit() and 1800 <= int(anio) <= datetime.now().year:
            return int(anio)
        else:
            print("Año inválido. Debe ser un número entre 1800 y el año actual.")


def obtener_mes():
    while True:
        mes = input("Ingrese el mes (mm): ")
        if mes.isdigit() and 1 <= int(mes) <= 12:
            return int(mes)
        else:
            print("Mes inválido. Debe ser un número entre 01 y 12.")


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


def pedir_fecha():
    anio = obtener_anio()
    mes = obtener_mes()
    dia = obtener_dia(anio, mes)
    mes_str = str(mes) if mes > 9 else "0" + str(mes)
    dia_str = str(dia) if dia > 9 else "0" + str(dia)
    return str(anio) + "/" + mes_str + "/" + dia_str


def incrementar_id():
    max_id = 0
    for i in tabla_ids:
        if i > max_id:
            max_id = i
    return max_id + 1


def buscar_estudiante_por_mail(email):
    posicion = 0
    while email != estudiantes[posicion][0] and posicion < 8:
        posicion = posicion + 1
    if email != estudiantes[posicion][0]:
        posicion = -1
    return posicion


def buscar_estudiante_por_nombre(nombre):
    posicion = 0
    while nombre != estudiantes[posicion][1] and posicion < 8:
        posicion = posicion + 1
    if nombre != estudiantes[posicion][1]:
        posicion = -1
    return posicion


def eliminar_estudiante_por_email(email):
    posicion = buscar_estudiante_por_mail(email)
    estudiantes[posicion][4] = "no_activo"


def eliminar_estudiante_por_indice(id_est):
    estudiantes[id_est][4] = "no_activo"


def buscar_id(posicion):
    if posicion >= 0 and posicion < 8:
        return tabla_ids[posicion]
    else:
        return None


def modificar_id(posicion):
    if posicion >= 0 and posicion < 8:
        nuevo_id = incrementar_id()
        tabla_ids[posicion] = nuevo_id


def indice_de_estudiante_por_id(id_est):
    posicion = 0
    while posicion < 8 and tabla_ids[posicion] != id_est:
        posicion += 1
    if posicion < 8:
        return posicion
    else:
        return -1


def eliminar_estudiante_por_id(id_est):
    posicion = indice_de_estudiante_por_id(id_est)
    if posicion != -1:
        estudiantes[posicion][4] = "no_activo"
    else:
        print("No existe el estudiante con ese ID")


def agregar_estudiante():
    posicion = -1
    i = 0
    while i < 8 and posicion == -1:
        if estudiantes[i][0] == "" or estudiantes[i][4] == "no_activo":
            posicion = i
        i += 1

    if posicion != -1:
        nuevos_datos = hacer_preguntas(nuevo=True)
        for i in range(14):
            estudiantes[posicion][i] = nuevos_datos[i]
        modificar_id(posicion)
    else:
        print("No hay lugar, siga participando")


def modificar_estudiante_por_mail(email):
    posicion = buscar_estudiante_por_mail(email)

    print("Ingrese los nuevos datos del estudiante:")
    nuevos_datos = hacer_preguntas()
    for i in range(1, 14):
        if nuevos_datos[i]:
            estudiantes[posicion][i] = nuevos_datos[i]


def estudiante_activo_por_mail(email):
    valor = False
    posicion = buscar_estudiante_por_mail(email)
    if estudiantes[posicion][4] == "activo":
        valor = True
    return valor


def hacer_preguntas(nuevo=False):
    datos = [""] * 14
    campos = [
        "email",
        "nombre",
        "sexo",
        "contraseña",
        "estado",
        "hobbies",
        "materia favorita",
        "deporte favorito",
        "materia fuerte",
        "materia débil",
        "biografía",
        "país",
        "ciudad",
        "fecha de nacimiento",
    ]

    for i in range(14):
        if i == 0 and not nuevo:
            datos[i] = ""
        else:
            if nuevo:
                if i == 0:
                    datos[i] = input("Ingrese " + campos[i] + ": ")
                    while buscar_estudiante_por_mail(datos[i]) != -1:
                        datos[i] = input("Ingrese " + campos[i] + ": ")
                elif i == 4:
                    datos[i] = "activo"
                elif i == 13:
                    datos[i] = pedir_fecha()
                else:
                    datos[i] = input("Ingrese " + campos[i] + ": ")
            else:
                if i != 4 and i != 13:
                    respuesta = ""
                    while respuesta != "s" and respuesta != "n":
                        respuesta = input(
                            "¿Desea modificar " + campos[i] + "? (s/n): "
                        ).lower()
                    if respuesta == "s":
                        datos[i] = input("Ingrese modificación: ")
                elif i == 13:
                    respuesta = ""
                    while respuesta != "s" and respuesta != "n":
                        respuesta = input(
                            "¿Desea modificar " + campos[i] + "? (s/n): "
                        ).lower()
                    if respuesta == "s":
                        datos[i] = pedir_fecha()
                else:
                    datos[i] = "activo"

    return datos


def existe_usuario(email, password):
    existe = False
    for i in range(8):
        if email == estudiantes[i][0] and password == estudiantes[i][3]:
            existe = True
    for i in range(4):
        if email == moderadores[i][0] and password == moderadores[i][1]:
            existe = True
    return existe


def que_role(email, password):
    role = ""
    for i in range(8):
        if email == estudiantes[i][0] and password == estudiantes[i][3]:
            role = "estudiante"
    for i in range(4):
        if email == moderadores[i][0] and password == moderadores[i][1]:
            role = "moderador"
    return role


def conectado():
    valor = False
    if informacion_login[0] != "":
        valor = True
    return valor


def imprimir_datos_estudiante(un_estudiante):
    NOMBRE = 1
    SEXO = 2
    HOBBIES = 5
    MATERIA_FAVORITA = 6
    DEPORTE_FAVORITO = 7
    MATERIA_FUERTE = 8
    MATERIA_DEBIL = 9
    BIOGRAFIA = 10
    PAIS = 11
    CIUDAD = 12
    FECHA_NACIMIENTO = 13
    print("Nombre:", un_estudiante[NOMBRE])
    print("Sexo:", un_estudiante[SEXO])
    print("Hobbies:", un_estudiante[HOBBIES])
    print("Materia favorita:", un_estudiante[MATERIA_FAVORITA])
    print("Deporte favorito:", un_estudiante[DEPORTE_FAVORITO])
    print("Materia fuerte:", un_estudiante[MATERIA_FUERTE])
    print("Materia débil:", un_estudiante[MATERIA_DEBIL])
    print("Biografía:", un_estudiante[BIOGRAFIA])
    print("País:", un_estudiante[PAIS])
    print("Ciudad:", un_estudiante[CIUDAD])
    edad = calcular_edad(un_estudiante[FECHA_NACIMIENTO])
    if edad is not None:
        print("Edad:", edad)
    else:
        print("Fecha de nacimiento inválida:", un_estudiante[FECHA_NACIMIENTO])


def ver_candidatos():
    for x in range(8):
        if estudiantes[x][0] != informacion_login[0] and estudiante_activo_por_mail(
            estudiantes[x][0]
        ):
            imprimir_datos_estudiante(estudiantes[x])
            func_me_gusta(x)
    print("no hay más estudiantes para matchear")


def func_me_gusta(match):
    respuesta = ""
    while respuesta != "s" and respuesta != "n":
        respuesta = input("¿Desea hacer match? (s/n): ").lower()
        if respuesta == "s":
            posicio_estud_conec = buscar_estudiante_por_mail(informacion_login[0])
            likes[posicio_estud_conec][match] = 1


def reportar_candidato():
    continuar = True

    while continuar:
        email_reportado = input("Ingrese el email del candidato que desea reportar: ")
        if email_reportado == "":
            print("No se ingresó email. Terminando el reporte.")
            continuar = False
        else:
            posicion_reportado = buscar_estudiante_por_mail(email_reportado)
            if posicion_reportado == -1 or not estudiante_activo_por_mail(
                email_reportado
            ):
                print("El email ingresado no corresponde a un candidato activo.")
                continuar = False
            else:
                mensaje = input("Ingrese el motivo del reporte: ")

                i = 0
                espacio_encontrado = False

                while i < 55:
                    if tabla_reportes[i][0] == "":
                        tabla_reportes[i][0] = email_reportado
                        tabla_reportes[i][1] = mensaje
                        tabla_reportes[i][2] = "0"
                        print("Reporte enviado exitosamente.")
                        espacio_encontrado = True
                        continuar = False
                        i = 55
                    else:
                        i += 1

                if not espacio_encontrado and i >= 8:
                    print("No hay espacio para más reportes.")


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


def imprimir_menu_estudiante():
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadísticos")
    print("5. Ruleta")
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


def gestionar_perfil():
    opcion = ""
    while opcion != "0":
        opcion = imprimir_menu_gestionar_perfil()
        if opcion == "1":
            modificar_estudiante_por_mail(informacion_login[0])
        elif opcion == "2":
            print("Eliminando perfil")
            eliminar_estudiante_por_email(informacion_login[0])
            informacion_login[0] = ""
            opcion = "0"
        elif opcion != "0":
            print("Opción no válida. Por favor, seleccione una opción válida.")


def gestionar_candidatos():
    imprimir_tabla(likes)
    opcion = ""
    while opcion != "0":
        opcion = imprimir_menu_gestionar_candidatos()
        if opcion == "1":
            ver_candidatos()
        elif opcion == "2":
            reportar_candidato()
        elif opcion != "0":
            print("Opción no válida. Por favor, seleccione una opción válida.\n")


def reporte_estadistico():
    match_correspondidos = 0
    likes_no_correspondido = 0
    likes_no_reciprocos = 0
    posicion = buscar_estudiante_por_mail(informacion_login[0])
    for i in range(8):
        if likes[posicion][i] == 1 and likes[i][posicion] == 1:
            match_correspondidos += 1
        elif likes[posicion][i] == 1 and likes[i][posicion] == 0:
            likes_no_correspondido += 1
        elif likes[posicion][i] == 0 and likes[i][posicion] == 1:
            likes_no_reciprocos += 1

    print("Match correspondidos:", match_correspondidos)
    print("Likes no correspondidos:", likes_no_correspondido)
    print("Likes no recíprocos:", likes_no_reciprocos)


def estudiante():
    opcion = ""
    while opcion != "6":
        opcion = imprimir_menu_estudiante()
        if opcion == "1":
            gestionar_perfil()
            if not conectado():
                opcion = "6"
        elif opcion == "2":
            gestionar_candidatos()
        elif opcion == "3":
            print("En construcción\n")
        elif opcion == "4":
            reporte_estadistico()
        elif opcion == "5":
            print("En construcción\n")
        elif opcion == "6":
            informacion_login[0] = ""
        else:
            print("Opción inválida\n")
        if not conectado():
            opcion = "6"


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
            print("Opción no válida. Por favor, ingrese una opción válida (1, 2, o 3).")


def main():
    inicializacion()

    while informacion_login[0] == "":
        informacion_login[0], informacion_login[1] = "", ""
        inicio_sesion()
        if conectado():
            if informacion_login[1] == "moderador":
                print("Sos un moderador")
                moderador()
            elif informacion_login[1] == "estudiante":
                estudiante()


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


def moderador():
    opcion = ""
    while opcion != "3":
        opcion = imprimir_menu_moderador()
        if opcion == "1":
            menu_gest_user()
        elif opcion == "2":
            gestionar_reportes()
        elif opcion == "3":
            informacion_login[0] = ""
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
        if not conectado():
            opcion = "3"


def imprimir_tabla_ids_estudiantes():
    print("ID".ljust(5) + "Email".ljust(25) + "Nombre".ljust(15) + "Estado".ljust(10))
    for i in range(8):
        print(
            str(tabla_ids[i]).ljust(5)
            + estudiantes[i][0].ljust(25)
            + estudiantes[i][1].ljust(15)
            + estudiantes[i][4].ljust(10)
        )


def desactivar_usuario():
    imprimir_tabla_ids_estudiantes()
    name = input(
        "Seleccione el nombre del usuario que quiere desactivar, si no lo conoce coloque '*': "
    )

    if name != "*":
        posicion = buscar_estudiante_por_nombre(name)
        if posicion == -1:
            print("No existe ese estudiante")
        else:
            eliminar_estudiante_por_indice(posicion)
            print("Estudiante eliminado\n")

    if name == "*":
        id_est = input(
            "Seleccione el ID del usuario que quiere desactivar, si no lo conoce coloque '8': "
        )
        while not id_est.isdigit():
            id_est = input(
                "Seleccione el ID del usuario que quiere desactivar, si no lo conoce coloque un numero mayor a 7 o menor a 0: "
            )
        if 0 <= int(id_est) < 8:
            eliminar_estudiante_por_id(int(id_est))
            print("Estudiante eliminado")
        else:
            print("Necesitamos más datos para eliminar al usuario")


def menu_gest_user():
    print("1. Desactivar usuario.")
    print("2. Volver.")
    opcion = input("Seleccione una opción: ")
    while opcion != "2":
        if opcion == "1":
            desactivar_usuario()
            print("1. Desactivar usuario.")
            print("2. Volver.")
            opcion = input("Seleccione una opción: ")
        else:
            opcion = input("Seleccione una opción: ")
    print("Saliendo\n")


def gestionar_reportes():
    print("1. Ver Reportes")
    print("2. Volver")
    opcion = input("Seleccione una opción: ")

    while opcion != "1" and opcion != "2":
        print("1. Ver Reportes")
        print("2. Volver")
        opcion = input("Seleccione una opción: ")

    while opcion == "1":
        ver_reportes()
        print("1. Ver Reportes")
        print("2. Volver")
        opcion = input("Seleccione otra opción: ")


def ver_reportes():
    for i in range(56):
        if tabla_reportes[i][2] == "0":
            print("Reporte sin revisar:")
            print("Usuario reportado:", tabla_reportes[i][0])
            print("Motivo del reporte:", tabla_reportes[i][1])
            print("¿Quiere ignorar el reporte? '2', ¿Quiere desactivar el usuario? '1'")

            opcion = input("Seleccione una opción: ")
            while opcion != "1" and opcion != "2":
                print("Opción inválida.")
                opcion = input("Seleccione una opción: ")

            if opcion == "1":
                email_reportado = tabla_reportes[i][0]
                posicion_reportado = buscar_estudiante_por_mail(email_reportado)
                if posicion_reportado != -1:
                    eliminar_estudiante_por_indice(posicion_reportado)
                    tabla_reportes[i][2] = "1"
            elif opcion == "2":
                tabla_reportes[i][2] = "2"

            print("Reporte actualizado.")


edades = [0] * 8


def edad_faltante():
    for k in range(8):
        edades[k] = calcular_edad(estudiantes[k][13])
    for i in range(0, 7):
        for j in range(i + 1, 8):
            if edades[j] < edades[i]:
                aux = edades[i]
                edades[i] = edades[j]
                edades[j] = aux
    print(edades)

    for i in range(0, 7):
        if edades[i] + 1 != edades[i + 1] and edades[i] != edades[i + 1]:
            for i in range(edades[i + 1] - edades[i]):
                print("falta este número en la secuencia:", edades[i] + 1)


edad_faltante()


def matcheos_comb():
    cont = 0
    for i in range(8):
        if estudiantes[i][4] == "activo":
            cont = cont + 1
    print(cont * (cont - 1))


matcheos_comb()


main()
