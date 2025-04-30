#Resolver una función cuadrática con la formula 

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

d = 0


if a == 0 :
    print("No es una función cuadrática.")
    exit()

d = (b**2)-(4*a*c)

if d > 0:
    x1 = (-b + (d**(1/2)))/(2*a)
    x2 = (-b - (d**(1/2)))/(2*a)
elif d == 0:
    x1 = (-b/(2*a))
    x2 = x1
else:
    print("No tiene sln")
    exit()

print("Soluciones reales y diferentes:")
print("x1=", x1)
print("x2=",x2)

