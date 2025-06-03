#Bucle while 
#Ciclo repetitivo que se repite mientras una condicion sea verdadera
#Se le conoce como un bucle que se repite indeterminadamente mientras que se cumpla una condicion

#Estructura del ciclo while
# while condicion:

#     instrucciones
# Ejemplo 1: indefinido de veces
# Calcular la raiz cuadrada de un numero
import math

""""umero = float(input("Introduce un numero: "))
while numero < 0:
    print("El numero no puede ser negativo. Por favor, introduce un numero positivo.")
    numero = float(input("Introduce un numero: "))
raiz_cuadrada = math.sqrt(numero)
print(f"La raiz cuadrada de {numero} es {raiz_cuadrada:.2f}")"""

# Ejemplo 2: determinado de veces
# Imprimir un mensaje 10 veces

"""i = 0
while i < 10:
print("Hola, mundo!")
i += 1  # Incrementar el contador para evitar un bucle infinito"""

# Contar del 1 al 10
i = 0
while i < 10:
    print(i)  # Imprimir el valor actual de i
    i += 1  # Incrementar el contador
    
# While es un bucle que se repite mientras una condicion sea verdadera
# Si la condicion es falsa, el bucle se detiene