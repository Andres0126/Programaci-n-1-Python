#Diseñar un programa para retirar dinero de un cajero automático en cantidades que son múltiplo 
#de $10. En cada momento, el cajero tiene un número determinado de billetes de $50, $20 y $10. 
#Cuando un cliente pida sacar una cantidad determinada de dinero, mostraremos por pantalla 
#cuantos billetes de cada tipo le damos. Intentaremos darle siempre la menor cantidad de billetes 
#posible. Si no es posible darle el dinero (porque no tenemos suficiente dinero en el cajero o porque 
#la cantidad solicitada no puede darse con una combinación valida de los billetes disponibles) 
#informaremos al usuario. 

retiro = float(input("Cuanto dinero desea retirar: ", ))

billetes_50 = 10  
billetes_20 = 20  
billetes_10 = 30  



# Verificar si la cantidad solicitada es múltiplo de 10
if retiro % 10 != 0:
    print("La cantidad solicitada debe ser múltiplo de 10.")
else:
    billetes_50_necesarios = min(retiro // 50, billetes_50)
    retiro -= billetes_50_necesarios * 50
    print(billetes_50_necesarios)
   