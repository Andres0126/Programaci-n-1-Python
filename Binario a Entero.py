n = int(input("Ingresa un número entero > 0: "))

# Convierte el número a binario (string) y remueve el '0b' al inicio
binario = bin(n)[2:]

# Imprime cada bit línea por línea
for bit in binario:
    print(bit)