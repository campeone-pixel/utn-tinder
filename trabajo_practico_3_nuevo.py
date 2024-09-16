from datetime import datetime
import getpass
import random
import os
import math
import os
import os.path
import pickle
import io

"""
Integrantes:
- Matias Abel Poses
- Santiago Porcel
- OROÑO, Martin
Comision 11
"""

# Definición de variables globales
"""
Tipos de arreglos:

est: array [8][8] of string
mod: array [4][2] of string
lk: array [8][8] of integer
id: array [8] of integer
tabla_rep: array [56][3] of integer
info_login: array [2] of string

Declarativa de variables:

estudiantes = est
moderadores = mod
likes = lk
tabla_reportes = tabla_rep
informacion_login = info_login
tabla_ids= id
"""
af_alumnos = ".\\alumnos.dat"
af_moderadores = ".\\moderadores.dat"
af_administradores = ".\\administradores.dat"


class alu:
    def __init__(self):
        self.id = ""
        self.email = ""
        self.nombre = ""
        self.sexo = ""
        self.contrasenia = ""
        self.estado = True
        self.hobbies = ""
        self.materia_favorita = ""
        self.deporte_favorito = ""
        self.materia_fuerte = ""
        self.materia_debil = ""
        self.biografia = ""
        self.pais = ""
        self.ciudad = ""
        self.fecha_nacimiento = ""


class mod:
    def __init__(self):
        self.id = 0
        self.email = ""
        self.contrasenia = ""
        self.estado = True


class admin:
    def __init__(self):
        self.id = 0
        self.email = ""
        self.contrasenia = ""


def crear_registro(
    nro_id,
    email,
    nombre,
    sexo,
    contrasenia,
    estado,
    hobbies,
    materia_favorita,
    deporte_favorito,
    materia_fuerte,
    materia_debil,
    biografia,
    pais,
    ciudad,
    fecha_nacimiento,
):
    reg = alu()
    reg.id = nro_id.ljust(5)
    reg.email = email.ljust(30)
    reg.nombre = nombre.ljust(32)
    reg.sexo = sexo.ljust(1)
    reg.contrasenia = contrasenia.ljust(32)
    reg.estado = estado
    reg.hobbies = hobbies.ljust(255)
    reg.materia_favorita = materia_favorita.ljust(16)
    reg.deporte_favorito = deporte_favorito.ljust(16)
    reg.materia_fuerte = materia_fuerte.ljust(16)
    reg.materia_debil = materia_debil.ljust(16)
    reg.biografia = biografia.ljust(255)
    reg.pais = pais.ljust(32)
    reg.ciudad = ciudad.ljust(32)
    reg.fecha_nacimiento = fecha_nacimiento

    return reg


# Verificación y apertura de archivos
def abrir_archivo(archivo_fisico):
    if os.path.exists(archivo_fisico):
        # Si el archivo existe, lo abrimos en modo lectura/escritura binaria
        archivo_logico = open(archivo_fisico, "r+b")
    else:
        # Si no existe, lo creamos en modo escritura/lectura binaria
        archivo_logico = open(archivo_fisico, "w+b")
    return archivo_logico


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


"""
var:
    me_gusta: int
"""


def inicializacion():
    ai_alumnos = abrir_archivo(af_alumnos)
    alumno1 = crear_registro(
        nro_id="1",
        email="juan.perez@gmail.com",
        nombre="Juan Perez",
        sexo="M",
        contrasenia="pass1234",
        estado=True,
        hobbies="Leer",
        materia_favorita="Matemáticas",
        deporte_favorito="Fútbol",
        materia_fuerte="Física",
        materia_debil="Historia",
        biografia="Estudiante aplicado.",
        pais="Argentina",
        ciudad="Buenos Aires",
        fecha_nacimiento="1998-05-15",
    )

    alumno2 = crear_registro(
        nro_id="2",
        email="ana.lopez@yahoo.com",
        nombre="Ana Lopez",
        sexo="F",
        contrasenia="pass5678",
        estado=True,
        hobbies="Deportes",
        materia_favorita="Física",
        deporte_favorito="Tenis",
        materia_fuerte="Programación",
        materia_debil="Arte",
        biografia="Amante del deporte.",
        pais="Chile",
        ciudad="Santiago",
        fecha_nacimiento="2000-07-20",
    )

    alumno3 = crear_registro(
        nro_id="3",
        email="carlos.garcia@outlook.com",
        nombre="Carlos Garcia",
        sexo="M",
        contrasenia="pass9012",
        estado=True,
        hobbies="Videojuegos",
        materia_favorita="Historia",
        deporte_favorito="Natación",
        materia_fuerte="Química",
        materia_debil="Lengua",
        biografia="Fanático de los videojuegos.",
        pais="Uruguay",
        ciudad="Montevideo",
        fecha_nacimiento="2002-03-10",
    )

    pickle.dump(alumno1, ai_alumnos)
    pickle.dump(alumno2, ai_alumnos)
    pickle.dump(alumno3, ai_alumnos)
    ai_alumnos.close()


inicializacion()
