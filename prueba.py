import random

likes = [0] * 8

for i in range(8):
    fila_nueva = [0] * 8
    for j in range(8):
        fila_nueva[j] = random.randint(0, 1)
    likes[i] = fila_nueva


print(likes)
