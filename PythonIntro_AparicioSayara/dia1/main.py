print ("Hola Mundo!")

## /////////////////////
## -- FUNDAMENTOS DE PROGRAMACIÓN
## /////////////////////

##Tiposdedatos
##1.String ""
cadenaTexto = "Textico"
print(type(cadenaTexto)) ##Imprimir tipo de dato

##2. NumeroEntero
numeroEntero = 2
print(type(numeroEntero))

##3. Numero flotante - float
numeroFlotante= 1.1
print(type(numeroFlotante))

##4. Numero doble - double
numerodoble = 3.1416586945930949587349567
print(type(numerodoble))

##5. Booleano - True/False
booleanito = True
print(type(booleanito))


##Entradas por parte del usuario
x=input ("Ingresa un número") ##todo input es texto - String
print(type(x))


##Conversion de tipos de datos - caste
##Sintaxis - tpoDato (Dato_a_convertir)
x=int(input("Ingresa un número:"))
print(type(x))

##Ejercicio - sumar dos numeros x parte del usuario
num1 = int(input("Ingresa el primer número:"))
num2 = int(input("Ingresa el segundo número"))
resultadoSumatoria = num1+num2
print("El resultado dado es de:", resultadoSumatoria)

##Ciclo for y while
##Ciclo normal
for i in range(5): ##i es el iterador e irá hasta el 5 
     print(i)
##Ciclo desde hasta
print("########")
for i in range(0,5): ##i será el iterador eirá de 0 hasta 5
     print(i) 
##Ciclo con pasos
print("########")
for i in range(0,5,2):##i será el iterador e irá desde el cero hasta el 5 en paso de 2 en 2
    print(i)

##Ciclo While
booleanito1 = True
while (booleanito1):
     print(booleanito1)
     booleanito1 = False


##4 tipos de funciones 
##Funcion sin para,etros y sin retornos
def funcion1():
     print("Soy una función increíble!!")


funcion1()

##Funcion sin parametros pero con retorno 
def funcion2():
     return 5
print("Su número es:", funcion2())

##Funcion con parametros pero sin retorno
def funcion3 (nombre,apellido):
     print("Su nombre es:",nombre,"",apellido)
funcion3("Sayara","Aparicio")

##Función con parametros y retornos
def funcion4 (a,b):
     c=a**b
     return c
funcionA= int(input("Ingrese número base"))
funcionB= int(input("Ingrese elevación deseada"))
print("El resultado de su elevación es de:",funcion4(funcionA,funcionB))

##Desarollado por : Sayara Aparicio ID. 1098.679.990