# Números Amigos
n1 = int(input("Ingresa N1: "))
n2 = int(input("Ingresa N2: "))
suma1 = 0
suma2 = 0

for i in range(1, n1):
    if (n1 % i == 0):
        suma1 += i

for i in range(1, n2):
    if (n2 % i == 0):
        suma2 += i

if suma1 == n2 and suma2 == n1:
    print(n1, "y", n2, "son números amigos")
else:
    print(n1, "y", n2, "no son números amigos")
##Desarrollado por: Sayara Aparicio ID: 1.098.679.990