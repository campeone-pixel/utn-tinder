# Datos de los estudiantes
estudiante1_email = "estudiante1@ayed.com"
estudiante1_contraseña = "111222"
estudiante2_email = "estudiante2@ayed.com"
estudiante2_contraseña = "333444"
estudiante3_email = "estudiante3@ayed.com"
estudiante3_contraseña = "555666"

# Función para el inicio de sesión
def login():
    intentos = 3
    while intentos > 0:
        email = input("Ingrese su email: ")
        contraseña = (input("Ingrese su contraseña: "))
        
        if (email == estudiante1_email and contraseña == estudiante1_contraseña) or \
           (email == estudiante2_email and contraseña == estudiante2_contraseña) or \
           (email == estudiante3_email and contraseña == estudiante3_contraseña):
            print("Inicio de sesión exitoso.")
            return
        else:
            intentos -= 1
            print("Email o contraseña incorrectos. Intentos restantes:", intentos)
    
    print("Ha excedido el número de intentos. Programa cerrado.")

# Iniciar sesión
login()