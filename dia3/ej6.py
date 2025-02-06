def fibon(f):
    a=0
    b=1
    for i in range(1,f):
        print(a)
        print(b)
        a=a+b
        b=b+a

def fibonpar(r):
    a=0
    b=1
    for i in range(1,r):
        if a%2==0 and b%2==0:
            print(a)
            print(b)
        elif a%2==0:
            print(a)
        elif b%2==0:
            print(b)
        a=a+b
        b=b+a

def sumafibon(c):
    a=0
    b=1
    for i in range(1,c):
        c+=a+b
        a=a+b
        b=b+a
    return c



valor=int(input("Ingrese la cantidad de veces que quiere que se haga la sucesion de fibonacci "))

print("La sucesion de fibonacci es: ")
print(fibon(valor))
print("")
print("La sucesion de fibonacci (solo pares): ")
print(fibonpar(valor))
print("")
print("La suma de la serie de fibonacci es: ")
print(sumafibon(valor))