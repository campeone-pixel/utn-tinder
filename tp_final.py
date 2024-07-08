"""
INTEGRANTES:
- CALVAGNA, Franco
- OROÑO, Martin
- PORCEL, Santiago
COM111
"""
''' 
VAR
 - pswrd, user, me_gusta, sel, user1, pswrd1, name1, birth1, bio1, hobbi1, user2, pswrd2, name2, birth2, bio2, hobbi2, user3, pswrd3,name3, birth3, bio3, hobbi3: STRING
 - cont,option,age1,age2,age3: INT
 - fecha_nacimiento3, fecha_nacimiento2,fecha_nacimiento1: datetime.datetime
'''
import getpass
import datetime
import os
clear = lambda: os.system('cls')
def login():
    global user,clear,user1,user2,user3,pswrd1,pswrd2,pswrd3,name1,name2,name3,hobbi1,hobbi3,hobbi2,bio1,bio2,bio3,age1,age2,age3,pswrd,option,fecha_nacimiento1,age1,fecha_nacimiento2,age2,fecha_nacimiento3,age3,birth1,birth2,birth3
    print("                                                                                            ")
    print("                                       LOG IN                                                       ")
    print("                                                                                              ")
    
    user1="estudiante1@ayed.com"
    pswrd1="11112222"
    name1="Porcel Santiago"
    birth1="2005-02-24"
    fecha_nacimiento1 = datetime.datetime.strptime(birth1, '%Y-%m-%d')
    age1 = datetime.datetime.now().year - fecha_nacimiento1.year
    
    bio1="soy de sn"
    hobbi1="nadare"
    user2="estudiante2@ayed.com"
    pswrd2="33334444"
    name2="Quito Esteban"
    birth2="2005-02-24"
    fecha_nacimiento2 = datetime.datetime.strptime(birth2, '%Y-%m-%d')
    age2 = datetime.datetime.now().year - fecha_nacimiento2.year
    
    bio2="a"
    hobbi2="leer"
    user3="estudiante3@ayed.com"
    pswrd3="55556666"
    name3="Perez Maria"
    birth3="2005-02-24"
    fecha_nacimiento3 = datetime.datetime.strptime(birth3, '%Y-%m-%d')
    age3 = datetime.datetime.now().year - fecha_nacimiento3.year
    
    bio3="b"
    hobbi3="Dibujar"

def mainmenu():
    print(" ----------------------------------------------------------------------------- ")
    print("                          1. Gestionar mi perfil")
    print("                          2. Gestionar candidatos")
    print("                          3. Matcheos")
    print("                          4. Reportes estadísticos")
    print("                          0. Salir")
    print(" ----------------------------------------------------------------------------- ")
    opciones ()


def validarcontra1():
    global pswrd
    pswrd=getpass.getpass("           Contraseña: ")
    cont = 1
    while (cont != 3) and (pswrd != pswrd1):
        print ("              Contraseña incorrecta")
        cont = cont + 1
        pswrd=getpass.getpass("           Contraseña: ")
    if (pswrd == pswrd1):
        mainmenu ()
        
            


def validarcontra2():
    global pswrd
    pswrd=getpass.getpass("           Contraseña: ")
    cont = 1
    while (cont != 3) and (pswrd != pswrd2):
        print ("              Contraseña incorrecta")
        cont = cont + 1
        pswrd=getpass.getpass("           Contraseña: ")
    if (pswrd == pswrd2):
        mainmenu ()




def validarcontra3():
    global pswrd
    pswrd=getpass.getpass("           Contraseña: ")
    cont = 1
    while (cont != 3) and (pswrd != pswrd3):
        print ("              Contraseña incorrecta")
        cont = cont + 1
        pswrd=getpass.getpass("           Contraseña: ")
    if (pswrd == pswrd3):
        mainmenu ()


def opciones ():
    global option
    option = int(input( "            Seleccione una opcion: "))
    while (option < 0) or (option >4):
        option = int(input( "       La opcion seleccionada no es valida: "))
    while (option > 0)and (option <=4):
        if option == 1:
              opcion1 ()
              clear ()
        elif option == 2:
              opcion2 ()
              clear ()
        elif option == 3:
              print ("En Construcción")
        elif option == 4:
              print ("En Construcción")
        mainmenu ()


def opcion1():
    clear ()
    print(" ----------------------------------------------------------------------------- ")
    print("                          a. Editar mis datos personales")
    print("                          b. Eliminar mi perfil")
    print("                          c. Volver")
    print(" ----------------------------------------------------------------------------- ")
    sel = str(input("                Seleccione una opcion: "))
    while (sel <"a") or (sel>"c"):
        sel = str(input("                Opcion invalida, intentelo de nuevo: "))
    while (sel >="a") and (sel<"c"):
        if sel == "a":
            clear ()
            if pswrd == pswrd1:
                editardatos1()
            elif pswrd == pswrd2:
                editardatos2()
            elif pswrd == pswrd3:
                editardatos3()
        elif sel == "b":
            print ("            En Construcción")
        sel = str(input("                Seleccione una opcion: "))

def opcion2():
    clear ()
    print(" ----------------------------------------------------------------------------- ")
    print("                          a. Ver candidatos")
    print("                          b. Eliminar un matcheo")
    print("                          c. Volver")
    print(" ----------------------------------------------------------------------------- ")
    sel = str(input("                Seleccione una opcion: "))
    while (sel <"a") or (sel>"c"):
        sel = str(input("                Opcion invalida, intentelo de nuevo: "))
    while (sel >="a") and (sel<"c"):
        if sel == "a":
            clear ()
            vercandidatos()
        elif sel == "b":
            print ("            En Construcción")
        sel = str(input("                Seleccione una opcion: "))



def editardatos1():
    global name1,birth1,fecha_nacimiento1,bio1,age1,hobbi1 
    name1 = str(input("         Ingrese su nombre: "))
    birth1= str(input("        Ingrese su fecha de nacimiento (YYYY-MM-DD): "))
    fecha_nacimiento1 = datetime.datetime.strptime(birth1, '%Y-%m-%d')
    age1 = datetime.datetime.now().year - fecha_nacimiento1.year
    
    bio1 = str (input("        Ingrese su biografia: "))
    hobbi1= str (input("        Ingrese su hobbie: "))
    clear ()
    print(" ----------------------------------------------------------------------------- ")
    print("                          a. Editar mis datos personales")
    print("                          b. Eliminar mi perfil")
    print("                          c. Volver")
    print(" ----------------------------------------------------------------------------- ")

def editardatos2():  
    global name2,bio2,age2,birth2,hobbi2  
    name2 = str(input("         Ingrese su nombre: "))
    birth2= str(input("        Ingrese su fecha de nacimiento (YYYY-MM-DD): "))
    fecha_nacimiento2 = datetime.datetime.strptime(birth1, '%Y-%m-%d')
    age2 = datetime.datetime.now().year - fecha_nacimiento2.year
    
    bio2 = str (input("        Ingrese su biografia: "))
    hobbi2= str (input("        Ingrese su hobbie: "))
    clear ()
    print(" ----------------------------------------------------------------------------- ")
    print("                          a. Editar mis datos personales")
    print("                          b. Eliminar mi perfil")
    print("                          c. Volver")
    print(" ----------------------------------------------------------------------------- ")

def editardatos3():   
    global name3,bio3,age3,birth3,hobbi3 
    name3 = str(input("         Ingrese su nombre: "))
    birth3= str(input("        Ingrese su fecha de nacimiento (YYYY-MM-DD): "))
    fecha_nacimiento3 = datetime.datetime.strptime(birth1, '%Y-%m-%d')
    age3 = datetime.datetime.now().year - fecha_nacimiento3.year
    
    bio3 = str (input("        Ingrese su biografia: "))
    hobbi3= str (input("        Ingrese su hobbie: "))
    clear ()
    print(" ----------------------------------------------------------------------------- ")
    print("                          a. Editar mis datos personales")
    print("                          b. Eliminar mi perfil")
    print("                          c. Volver")
    print(" ----------------------------------------------------------------------------- ")

def vercandidatos ():
    global me_gusta
    print ("            Datos del primer candidato: ")
    print ("            Nombre: ",name1)
    print("            Edad:",age1)
    print ("            Biografia: ",bio1)
    print ("            Hobbies: ",hobbi1)
    print ("                                        ")
    print ("            Datos del segundo candidato: ")
    print ("            Nombre: ",name2)
    print("            Edad:",age2)
    print ("            Biografia: ",bio2)
    print ("            Hobbies: ",hobbi2)
    print ("                                        ")
    print ("            Datos del tercer candidato: ")
    print ("            Nombre: ",name3)
    print("            Edad:",age3)
    print ("            Biografia: ",bio3)
    print ("            Hobbies: ",hobbi3)


    me_gusta= str(input("            Ingrese el nombre del candidato que le interesa: "))
    while (me_gusta!=name1) and (me_gusta!=name2) and (me_gusta!=name3):
        print ("            Nombre incorrecto: ")
        me_gusta= str(input("            Ingrese el nombre del candidato que le interesa: "))
    if (me_gusta==name1) or (me_gusta==name2) or (me_gusta==name3):
        clear ()
        print(" ----------------------------------------------------------------------------- ")
        print("                          a. Ver candidatos")
        print("                          b. Eliminar un matcheo")
        print("                          c. Volver")
        print(" ----------------------------------------------------------------------------- ")





login ()
user=str(input("            Mail: "))
while (user != user1) and (user != user2) and (user != user3):
    print ("El mail ingresado es inexistente, vuelva a intentarlo.")
    user=str(input("            Mail: "))
if user == user1:
    validarcontra1()
elif user == user2:
    validarcontra2()
elif user == user3:
    validarcontra3()





    