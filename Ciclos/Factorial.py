factorial = 0 
n = int(input("ingrese un número entero positivo menor que 50: "))
if 0 < n <= 50: 
    if ( n % 1 == 0):
        factorial = 1
        for i in range( 1, n + 1):
            factorial = i * factorial
            print(f"Iteración {i}: factorial = {factorial}")
        print("El factorial de", n, "es:", factorial)
    else:
        print("El número ingresado no es un entero positivo.")
else:
    print("El número ingresado no es un entero positivo menor o igual que 50.")