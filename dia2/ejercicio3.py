import math
def clasificar_numero(numero):
    resultado = {}
    resultado["pares"] = "Par" if numero % 2 == 0 else "Impar"




    if numero > 1:
        es_primo = True
        for i in range(2, int(math.sqrt(numero)) + 1):
            if numero % i == 0:
                es_primo = False
                break
        resultado["primo_o_no"] = "Primo" if es_primo else "Compuesto"
    else:
        resultado["primo_o_no"] = "No es primo ni compuesto"


    raiz = math.isqrt(numero)
    resultado["cuadrado_perfecto"] = "Sí" if raiz * raiz == numero else "No"

    return resultado


numero = int(input("Ingrese un número: "))
resultado = clasificar_numero(numero)


print(f"El número {numero} es {resultado['pares']}, {resultado['primo_o_no']} y {'es' if resultado['cuadrado_perfecto'] == 'Sí' else 'no es'} un cuadrado perfecto.") 
