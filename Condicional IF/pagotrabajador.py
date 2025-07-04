IP = 0
print("ingrese el tipo de trabajador")
print("1. Contratista")
print("2. Asalariado")
Ti=int(input("Ingrese una opción (1 o 2): "))
HT = float(input("Ingrese la horas trabajadas: "))
TH = float(input("Ingrese la tarifa horaria: "))
PB = HT*TH
if Ti == 1:
    ds = 0.05*PB
    dp = 0.06*PB 
    if PB > 15000000:
        IP = 0.04 * PB
    PN = PB -(ds+dp+IP)
else: 
    ds = 0.025*PB
    dp = 0.035*PB 
    if PB > 15000000:
        IP = 0.04 * PB
    PN = PB -(ds+dp+IP)
print ("Su salud es: ", ds)
print ("Su pensión es: ", dp)
print ("Su impuesto es: ", IP)
print ("Su pago neto es: ", PN)
