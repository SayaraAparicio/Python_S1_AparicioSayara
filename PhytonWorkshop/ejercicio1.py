##De Celsius a Farenheit
def convertirTempFahrenheit(c):
    fahrenheit = (9/5) * (c+32)
    return fahrenheit

##Fahrenheit a Celsius
def convertirTempcelsius(f):
    celsius = (5/9) * (f-32)
    return celsius

##conversion
pregunta = input("Ingresa el valor de C para convertir a grados Celsius y F para convertir a grados Fahrenheit ") 
print(pregunta)

if (pregunta=="F"):
    c =float(input("Ingresa la temperatura en grados Celsius:"))
    f = convertirTempFahrenheit(c)
    print("La temperatura en grados en Fahrenheit es:", c)
elif (pregunta=="C"):
    f=float(input("Ingresa la temperatura en grados fahrenheit:"))
    c = convertirTempcelsius(f)
    print("La temperatura en grados Celsius es,", f)

