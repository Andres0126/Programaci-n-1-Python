n = int(input("ingrese el valor de n: "))
m = int(input("ingrese el valor de m: "))
suma = 0
i = n

while i <= m:
    if i % 2 != 0:
        suma += i
        print(f"Iteración: i = {i}, suma parcial = {suma}")
    i += 1
print("La suma de los números pares entre", n, "y", m, "es:", suma)

