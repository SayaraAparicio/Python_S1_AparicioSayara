# Programa de comparación de números
print("Los números que satisfacen la siguiente expresión P^3 + Q^4 - 2 * P^2 < 680 son:")

for p in range(0, 200):
    for q in range(0, 200):
        expresionMatematica = p**3 + q**4 - 2 * p**2
        if (expresionMatematica < 680):
            print("P: ", p)
            print("Q: ", q)
            print("Resultado:", expresionMatematica)
##Desarrollado por: Sayara Aparicio ID: 1.098.679.990
