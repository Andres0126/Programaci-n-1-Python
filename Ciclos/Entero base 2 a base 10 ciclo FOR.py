#Pasar de un número entero en base 2 a base 10 mientras el usuario 
#ingresa bit a bit. Usar un bucle for para hacer el ejercicio.

signo_n = 1
n = 0
for i in range(1, 7):
    bit = int(input(f"Ingrese el bit {i} (0 o 1): "))
    if i == 1:
        if bit == 1: 
            signo_n = -1 
    elif 2 <= i <= 6:
        n = bit * 2**(6-i) + n
n = signo_n * n
print("El número en base 10 es:", n)
