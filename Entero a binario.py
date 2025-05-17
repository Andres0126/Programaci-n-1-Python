
def entero_a_binario():
    # Paso 1: Pedir al usuario un número entero positivo
    while True:
        try:
            n = int(input("Ingrese un número entero > 0: "))
            if n > 0:
                break
            else:
                print("¡El número debe ser mayor que 0!")
        except ValueError:
            print("¡Error! Ingrese un número válido.")

    # Paso 2: Convertir el número a binario (como lista de bits)
    bits = []
    if n == 0:
        bits.append(0)
    else:
        while n > 0:
            bit = n % 2
            bits.insert(0, bit)  # Insertar al inicio para mantener el orden correcto
            n = n // 2

    # Paso 3: Imprimir cada bit línea por línea
    print("\nEl número binario es (bit por bit):")
    for bit in bits:
        print(bit)

# Llamar a la función
entero_a_binario()
