def intsimp(a,b,c):
    i=a*b*c
    return i
def intcomp(d,e,f,n):
    cf=d*(1+e/n)**n*f
    return cf

tpi=int(input("ingrese si quiere calcular interes simle(1) o interes compuesto(2)"))

if tpi==1:
    c=int(input("Ingrese el valor de capital "))
    t=float("ingrese la tasa de interes (en decimal)")
    x=int("ingrese la cantidad de tiempo")
    print("El interes simple es: ", intsimp(c,t,x))
else:
    if tpi==2:
        r=int(input("Ingrese el valor de capital inicial "))
        y=float(input("ingrese la tasa de interes (en decimal)"))
        p=int(input("ingrese el periodo del ahorro"))
        x=float(input("ingrese las veces que se quiere que se capitalice"))
        print("El capital final es: ", intcomp(r,y,p,x))
    else:
        print("opcion equivocada")