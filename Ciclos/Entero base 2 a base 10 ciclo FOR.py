#Pasar de un número entero en base 2 a base 10 mientras el usuario 
#ingresa bit a bit. Usar un bucle for para hacer el ejercicio.

signo_n = 1
n = 0
for i in range(6):
    bit = int(input(f"Ingrese el bit {i} (0 o 1): "))
    if bit not in (0, 1):
        print("Entrada inválida. Debe ser 0 o 1.")
        break
    if i == 0:
        if bit == 1: 
            signo_n = -1 
    if 1 <= i <= 5:
        n = bit * 2**(5-i) + n
n = signo_n * n
print("El número en base 10 es:", n)
