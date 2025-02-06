# Mayor y menor
for i in range(1, 11):
    N = int(input("Ingresa número: "))
    if i == 1:
        grande = N
        pequeño = N
    elif N > grande:
        grande = N
    elif N < pequeño:
        pequeño = N
print("El mayor es:", grande)
print("El menor es:", pequeño)
##Desarrollado por: Sayara Aparicio ID: 1.098.679.990