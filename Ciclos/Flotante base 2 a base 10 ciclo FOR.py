n = 0
m = 0
signo_n = 1
signo_m = 1
for i in range(1, 9):
    bit = int(input(f"Ingrese el bit {i} (0 o 1): "))
    if i == 1:
        if bit == 1:
            signo_m = -1
    if i == 2 and bit == 1:
        signo_n = -1
    if 3 <= i <= 4:
        n = bit* 2**(4-i) + n 
        print(f"n: {n}")
    if 5 <= i <= 9:
        m = bit * 2**(4-i) + m
        print(f"m: {m}")
print(signo_n)
print(signo_m)
print (n)
print (m)
n = signo_n * n
m = signo_m * m
print(m*(2**n))