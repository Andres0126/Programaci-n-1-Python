#Realizar un programa para calcula las suma de los primers n terminos. El usuario ingresa el valor de n. usar el while
n = int(input("Ingrese el valor de n: "))
suma = 0
i = 1
while i <= n:
    suma += i
    i += 1
print("La suma de los primeros", n, "términos es:", suma)

