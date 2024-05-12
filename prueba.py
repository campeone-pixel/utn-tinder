""" cp = 0
sp = 0
n = 0
sn = 0

for x in range(6):
    numero = int(input("numero:"))
    if numero > 0:
        cp = cp + 1
        sp = sp + numero
        p = sp / cp
    else:
        if numero == 0:
            n = n + 1
        else:
            sn = sn + numero
print(
    "promedio valores positivo: ", p, "suma de negativos: ", sn, "cantidad nulos: ", n
)
"""

""" 
t_hs_p = 0
t_hs_s = 0
cs = 0
cp = 0
planta = input("planta:")

while planta != "*":
    seccion = int(input("seccion:"))

    while seccion != 0:
        hs = int(input("horas"))
        while hs != 0:
            t_hs_p = t_hs_p + hs
            t_hs_s = t_hs_s + hs
            cs = cs + 1
            cp = cp + 1
            hs = int(input("horas"))
        print("seccion: ", seccion, "total hs: ", t_hs_s, "total empleados: ", cs)
        cs = 0
        t_hs_s = 0
        seccion = int(input("seccion:"))
    print("planta: ", planta, "total hs: ", t_hs_p, "total empleados: ", cp)
    cp = 0
    t_hs_p = 0
    planta = input("planta:")
"""
boleano = not (False)
print(boleano)
