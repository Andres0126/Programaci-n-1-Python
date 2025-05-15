a1 = float(input("Ingrese el valor de a1: "))
b1 = float(input("Ingrese el valor de b1: "))
c1 = float(input("Ingrese el valor de c1: "))

a2 = float(input("Ingrese el valor de a2: "))
b2 = float(input("Ingrese el valor de b2: "))
c2 = float(input("Ingrese el valor de c2: "))

if (a1==0) & (b1==0):
    print("No es un sistema de eecuaciones, verifique")
elif (a2==0) & (b2==0):
    print("No es un sistema de eecuaciones, verifique")
else:
    if (a1!=0) & (a2 != 0):
        if (b1 !=0) & (b2 != 0):
            x = c2/(((a1+((b1*c2)/b2))+(a2*b1)/b2))
            y = (c1 - a1*x)/b1
            print("Este es el valor de y: ", y)
            print("Este es el valor de x: ", x)
        else:
              print("No es un sistema de dos ecuaciones, verifique")
        