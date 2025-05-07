HT = float(input("Ingrese la cantidad de horas trabajadas:"))
TH = float(input("Ingrese las tarifas de horario:"))

Salario_b= HT*TH

#Deducciónes 

#DS deducción de salud
#Dp deducción de pensión 
DS = 0.03 * (Salario_b)
DP = 0.04 * (Salario_b)

print("Su deducción de salud es de: ", DS)
print("Su deducción de pensión es de:", DP)

#Umbral impuestos

if Salario_b > 10000000:
    UI = 0.02*(Salario_b-10000000)
else:
    UI=0

#Pago neto

PN = Salario_b - (DS + DP + UI)

print("Su pago neto es de: ", PN)
