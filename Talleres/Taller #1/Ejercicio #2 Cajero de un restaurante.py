#El cajero de un restaurante desea controlar el flujo de caja en un día de trabajo cualquiera. Antes 
#de abrir al público, el gerente del establecimiento le entrega la base para el día, la cual consiste en 
#una suma de dinero que debe registrar en la caja y con la cual se espera pueda desempeñarse sin 
#contratiempos. Durante su jornada tendrá ingresos por concepto de las ventas que se realicen, 
#también habrán salidas de caja para la compra de insumos o gastos eventuales que deban realizarse.  

#Se espera un algoritmo, que reciba el registro de cada una de las operaciones a medida que vayan 
#sucediendo. El cajero también requiere un informe del saldo en la caja después de cada registro. 
#El algoritmo deberá dar un mensaje de alerta en el caso que el saldo sea inferior o igual al 15 % de 
#la base asignada. Al cierre del restaurante, se requiere los saldos finales (saldo en la caja, ingresos 
#y egresos) y la cantidad de cada una de las operaciones realizadas. 

#Solicitar la base inicial de la caja
base = float(input("Ingrese la base inicial de la caja: "))
saldo = base  # El saldo inicial es igual a la base
ingresos = 0  # Variable para acumular los ingresos
egresos = 0   # Variable para acumular los egresos
operaciones = 0  # Contador de operaciones realizadas

# Ciclo para registrar las operaciones
while True:
    print("\nSeleccione el tipo de operación:")
    print("1. Ingreso")
    print("2. Egreso")
    print("3. Cerrar caja")
    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:  # Registrar un ingreso
        monto = float(input("Ingrese el monto del ingreso: "))
        saldo += monto  # Sumar el monto al saldo
        ingresos += monto  # Acumular el ingreso
        operaciones += 1  # Incrementar el contador de operaciones
        print(f"Saldo actual: {saldo:.2f}")
    elif opcion == 2:  # Registrar un egreso
        monto = float(input("Ingrese el monto del egreso: "))
        saldo -= monto  # Restar el monto del saldo
        egresos += monto  # Acumular el egreso
        operaciones += 1  # Incrementar el contador de operaciones
        print(f"Saldo actual: {saldo:.2f}")
    elif opcion == 3:  # Cerrar la caja
        print("\nCerrando caja...")
        break  # Salir del ciclo
    else:
        print("Opción no válida. Intente nuevamente.")

    # Verificar si el saldo es menor o igual al 15% de la base
    if saldo <= 0.15 * base:
        print("¡Alerta! El saldo es inferior o igual al 15% de la base inicial.")

# Mostrar el informe final
print("\n--- Informe Final ---")
print(f"Saldo final en la caja: {saldo:.2f}")
print(f"Total de ingresos: {ingresos:.2f}")
print(f"Total de egresos: {egresos:.2f}")
print(f"Cantidad total de operaciones: {operaciones}")