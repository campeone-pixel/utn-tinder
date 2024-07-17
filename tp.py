from datetime import datetime
import getpass
import random

import os


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
        "Lorem ipsum dolor sit amet.",
        "Argentina",
        "Rosario",
        "2002/08/16",
    ],
    [
        "estudiante4@ayed.com",
        "miguel",
        "masculino",
        "777888",
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

tabla_ids = [100, 101, 102, 103, 0, 0, 0, 0]


informacion_login = ["", ""]


def inicializacion(tabla_likes, est):
    for i in range(8):
        for j in range(8):
            if (
                estudiante_activo_por_mail(est[i][0], est)
                and estudiante_activo_por_mail(est[j][0], est)
            ) and (est[i][0] != est[j][0]):
                me_gusta = random.randint(0, 1)
                tabla_likes[i][j] = me_gusta
            else:
                tabla_likes[i][j] = "no"


def imprimir_tabla(array, fila=None):
    if not array:
        print("El array está vacío.")
        return
    # Calcular el ancho máximo de cada columna considerando todas las filas
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


# Función para incrementar el número de ID
def incrementar_id(t_ids):
    max_id = 0
    for i in t_ids:
        if i > max_id:
            max_id = i
    return max_id + 1


# Función para buscar el número de ID según la posición en el array
def buscar_id(t_ids, posicion):
    if (
        posicion >= 0 and posicion < 8
    ):  # Usamos 8 porque sabemos que la longitud del array es 8
        return t_ids[posicion]
    else:
        return None  # Retornar None si la posición es inválida


# Función para modificar un número de ID según la posición en el array
def modificar_id(t_ids, posicion):
    if (
        posicion >= 0 and posicion < 8
    ):  # Usamos 8 porque sabemos que la longitud del array es 8
        nuevo_id = incrementar_id(t_ids)
        t_ids[posicion] = nuevo_id
        return True  # Retornar True si la modificación fue exitosa
    else:
        return False  # Retornar False si la posición es inválida


def indice_de_estudiante_por_id(id_est, t_ids):
    posicion = 0
    while posicion < 8 and t_ids[posicion] != id_est:
        posicion += 1
    if posicion < 8:
        return posicion
    else:
        return -1


# Función para eliminar estudiante por su ID
def eliminar_estudiante_por_id(id_est, est, t_ids):
    posicion = indice_de_estudiante_por_id(id_est, t_ids)
    if posicion != -1:
        est[posicion][4] = "no_activo"
    else:
        print("No existe el estudiante con ese ID")


def buscar_estudiante_por_mail(email, est):
    posicion = 0
    while email != est[posicion][0] and posicion < 8:
        posicion = posicion + 1
    if email != est[posicion][0]:
        posicion = -1
    return posicion


def buscar_estudiante_por_nombre(nombre, est):
    posicion = 0
    while nombre != est[posicion][1] and posicion < 8:
        posicion = posicion + 1
    if nombre != est[posicion][1]:
        posicion = -1
    return posicion


def eliminar_estudiante_por_email(email, est):
    posicion = buscar_estudiante_por_mail(email, est)
    est[posicion][4] = "no_activo"


def eliminar_estudiante_por_indice(id_est, est):
    est[id_est][4] = "no_activo"


def agregar_estudiante(est):
    posicion = -1
    i = 0
    while i < 8 and posicion == -1:
        if est[i][0] == "" or est[i][4] == "no_activo":
            posicion = i
        i += 1

    nuevos_datos = hacer_preguntas(nuevo=True)
    for i in range(14):
        est[posicion][i] = nuevos_datos[i]


def modificar_estudiante_por_mail(email, est):
    posicion = buscar_estudiante_por_mail(email, est)

    print("Ingrese los nuevos datos del estudiante:")
    nuevos_datos = hacer_preguntas()
    for i in range(1, 14):  # Saltar email
        if nuevos_datos[i]:
            est[posicion][i] = nuevos_datos[i]


def estudiante_activo_por_mail(email, est):
    valor = False
    posicion = buscar_estudiante_por_mail(email, est)
    if est[posicion][4] == "activo":
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
        if i == 0 and not nuevo:  # Saltar email en modificación
            datos[i] = ""
        else:
            if nuevo:
                datos[i] = input("Ingrese " + campos[i] + ": ")
            else:
                respuesta = ""
                while respuesta != "s" and respuesta != "n":
                    respuesta = input(
                        "¿Desea modificar " + campos[i] + "? (s/n): "
                    ).lower()
                if respuesta == "s":
                    datos[i] = input("Ingrese modificación: ")

            if i == 13 and datos[i] != "":
                datos[i] = pedir_fecha()

    return datos


def existe_usuario(email, password, est, mod):
    existe = False
    for i in range(8):
        if email == est[i][0] and password == est[i][3]:
            existe = True
    for i in range(4):
        if email == mod[i][0] and password == mod[i][1]:
            existe = True
    return existe


def que_role(email, password, est, mod):
    role = ""
    for i in range(8):
        if email == est[i][0] and password == est[i][3]:
            role = "estudiante"
    for i in range(4):
        if email == mod[i][0] and password == mod[i][1]:
            role = "moderador"
    return role


def conectado(inf_login):
    valor = False
    if inf_login[0] != "":
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
    if edad:
        print("Edad:", edad)
    else:
        print("Fecha de nacimiento inválida:", un_estudiante[FECHA_NACIMIENTO])


def ver_candidatos(est, tabla_likes, inf_login):
    for x in range(8):
        if est[x][0] != inf_login[0] and estudiante_activo_por_mail(est[x][0], est):
            imprimir_datos_estudiante(est[x])
            func_me_gusta(est, tabla_likes, inf_login, x)
    print("no hay mas estudiantes para matchear")


def func_me_gusta(est, tabla_likes, inf_login, match):
    respuesta = ""
    while respuesta != "s" and respuesta != "n":
        respuesta = input("¿Desea hacer match? (s/n): ").lower()
        if respuesta == "s":
            posicio_estud_conec = buscar_estudiante_por_mail(inf_login[0], est)
            tabla_likes[posicio_estud_conec][match] = 1


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


def gestionar_perfil(est, inf_login):
    opcion = ""
    while opcion != "0":
        opcion = imprimir_menu_gestionar_perfil()
        if opcion == "1":
            modificar_estudiante_por_mail(inf_login[0], est)
        elif opcion == "2":
            print("Eliminando perfil")
            eliminar_estudiante_por_email(inf_login[0], est)
            inf_login[0] = ""
            opcion = "0"
        elif opcion != "0":
            print("Opción no válida. Por favor, seleccione una opción válida.")


def gestionar_candidatos(est, tabla_likes, inf_login):
    opcion = ""
    while opcion != "0":
        opcion = imprimir_menu_gestionar_candidatos()
        if opcion == "1":
            ver_candidatos(est, tabla_likes, inf_login)

        elif opcion == "2":
            print("En Construccion\n")
        elif opcion != "0":
            print("Opción no válida. Por favor, seleccione una opción válida.\n")


def estudiante(est, mod, tabla_likes, inf_login):
    opcion = ""
    while opcion != "6":
        opcion = imprimir_menu_estudiante()
        if opcion == "1":
            gestionar_perfil(est, inf_login)
            if not conectado(inf_login):
                opcion = "6"
        elif opcion == "2":
            gestionar_candidatos(est, tabla_likes, inf_login)
        elif opcion == "3":
            print("En construcción\n")
        elif opcion == "4":
            print("En construcción\n")
        elif opcion == "5":
            print("En construcción\n")
        elif opcion == "6":
            inf_login[0] = ""
        else:
            print("Opción inválida\n")
        if not conectado(inf_login):
            opcion = "6"


def inicio_sesion(est, mod, inf_login):
    opcion = ""
    while inf_login[0] == "" and opcion != "3":
        opcion = imprimir_menu_inicio_sesion()
        if opcion == "1":
            intentos = 3
            while intentos > 0:
                mail = input("Ingrese su email: ")
                contraseña = getpass.getpass("Ingrese su contraseña: ")
                existe = existe_usuario(mail, contraseña, est, mod)
                if (
                    existe
                    and que_role(mail, contraseña, est, mod) == "estudiante"
                    and estudiante_activo_por_mail(mail, est)
                ):
                    inf_login[0] = mail
                    inf_login[1] = que_role(mail, contraseña, est, mod)
                    print("Inicio exitoso\n")
                    intentos = 0
                elif existe and que_role(mail, contraseña, est, mod) == "moderador":
                    inf_login[0] = mail
                    inf_login[1] = que_role(mail, contraseña, est, mod)
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
            print("Funcionalidad de registro aún no implementada.")
        elif opcion == "3":
            print("Saliendo del programa...")
            inf_login[0] = "salir"
        else:
            print("Opción no válida. Por favor, ingrese una opción válida (1, 2, o 3).")


def main(est, mod, inf_login, tabla_likes, t_ids):
    inicializacion(tabla_likes, est)

    while inf_login[0] == "":
        inf_login[0], inf_login[1] = "", ""
        inicio_sesion(est, mod, inf_login)
        if conectado(inf_login):
            if inf_login[1] == "moderador":
                print("Sos un moderador")
                moderador(est, mod, inf_login, tabla_likes, t_ids)
            elif inf_login[1] == "estudiante":
                estudiante(est, mod, tabla_likes, inf_login)


def moderador(est, mod, inf_login, tabla_likes, t_ids):
    menu_moderador()
    opcion = input("Por favor,seleccione una opcion: ")
    while opcion != "3":
        if opcion == "1":
            gestionar_usuario(est, mod, inf_login, tabla_likes, t_ids)
        elif opcion == "2":
            gestionar_reportes()
        else:
            print("Opcion invalida")
        menu_moderador()
        opcion = input("Por favor,seleccione una opcion: ")
    print("Saliendo\n")


def gestionar_usuario(est, mod, inf_login, tabla_likes, t_ids):
    # menu_gest_user()

    name = input(
        "Seleccione el nombre del usuario que quiere desactivar, si no lo conoce coloque '*': "
    )

    if name != "*":
        posicion = buscar_estudiante_por_nombre(name, est)
        if posicion == -1:
            print("no existe ese estudiante")
        else:
            eliminar_estudiante_por_indice(posicion, est)

    if name == "*":
        id_est = input(
            "Seleccione el id del usuario que quiere desactivar, si no lo conoce coloque '0': "
        )
        while not id_est.isdigit():
            id_est = input(
                "Seleccione el id del usuario que quiere desactivar, si no lo conoce coloque '0': "
            )

        eliminar_estudiante_por_id(int(id_est), est, t_ids)
        imprimir_tabla(est)
    if name == "*" and id_est == -1:
        print("Necesitamos más datos para eliminar al usuario")


# def menu_gest_user():
#     opcion = int("seleccione una opcion: ")


def gestionar_reportes():
    print("menu gest rep")


def menu_moderador():
    print("1. Gestionar usuarios")
    print("2. Gestionar reportes")
    print("3. Salir")


main(estudiantes, moderadores, informacion_login, likes, tabla_ids)


imprimir_tabla(estudiantes, 0)
