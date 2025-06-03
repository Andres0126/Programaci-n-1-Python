a = float(input("Ingresa un número positivo a: "))

error_maximo = float(input("Ingresa el error relativo en %: "))
error_maximo = error_maximo / 100 

# Inicio
x_0 = a / 2  # Semilla inicial
error_relativo = error_maximo + 1  
#Bucle while
while error_relativo >= error_maximo:
    x_1 = (x_0 + a / x_0) / 2
    error_relativo = abs((x_1 - x_0) / x_1)
    print(f"Valor aproximado actual: {x_1}  Error relativo: {error_relativo}")
    x_0 = x_1

print(f"La raíz cuadrada aproximada de {a} es: {x_1}")
