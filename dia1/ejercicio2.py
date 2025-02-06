# Número entero serie
CantidadTerminos = int(input("Ingresa el último número de la sucesión: "))

if CantidadTerminos <= 0:
    print("0")

SUM = 0
for i in range(1, CantidadTerminos + 1):
    if (i % 2 == 0):
        SUM = SUM - (1 / i)
    else:
        SUM = SUM + (1 / i)

print("La cantidad de términos es:", CantidadTerminos)
print("La sumatoria da:", SUM)
##Desarrollado por: Sayara Aparicio ID: 1.098.679.990