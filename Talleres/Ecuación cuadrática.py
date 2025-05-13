#Programar en python el seudocodigo del siguiente punto del taller:
#Diseñar  un  algoritmo  para  resolver  una  ecuación  de  segundo  grado  ax2 + 𝑏𝑥+ c =0. 
# Dicho algoritmo debe considerar los tres posibles: 
# 1. El polinomio no tiene raíces reales, es decir, que el polinomio tenga raíces complejas; 
# 2. El polinomio tiene dos raíces iguales; 
# 3. El polinomio tiene dos raíces reales diferentes. 

a = float(input("Ingrese el valor de a:"))
b = float(input("Ingrese el valor de b:"))
c = float(input("Ingrese el valor de c:"))

if (a==0):
    print("No es una función cuadrática")
    x1 = None
    x2 = None
else:
    d = (b**2) - (4*(a*c))
    if (d > 0): # 3. El polinomio tiene dos raíces reales diferentes. 
        x1 = ((-b**2) + (d**(1/2))) / 2*a
        x2 = ((-b**2) - (d**(1/2))) / 2*a
    elif (d == 0):# 2. El polinomio tiene dos raíces iguales; 
        x1 = (-b)/(2*a)
        x2 = x1
    else: # 1. El polinomio no tiene raíces reales, es decir, que el polinomio tenga raíces complejas; 
        print("El polinomio tiene raices complejas")
        x1 = None
        x2 = None
if x1 is not None and x2 is not None:
    print("X1 es igual a: ", x1)
    print("x2 es igual a: ", x2)