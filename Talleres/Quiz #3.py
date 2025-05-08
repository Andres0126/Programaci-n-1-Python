#Escribir un codigo que determine el menor de 3 numeros enteros reales

x = float(input("Ingrese el valor de x: "))
y = float(input("Ingrese el valor de y: "))
z = float(input("Ingrese el valor de z: "))

if (x<y) & (x<z):
    print("El numero menor es: ", x)
elif (y<x) & (y<z):
    print("El numero menor es: ", y)
else:
    print("El numero menor es: ", z)