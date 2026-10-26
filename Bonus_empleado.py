nombre=(input("Ingresa tu nombre"))
pagoHora=(float(input("Ingresa tu pago por hora")))
horas=(int(input("Ingresa cuantas horas trabajaste al mes")))
sueldo=pagoHora*horas
print("Tu sueldo es: ", sueldo)
if sueldo>=100 and sueldo<=300:
    print("Tu bono es de $500")
    print("Tu sueldo en total es de: $", sueldo+500)
elif sueldo>300 and sueldo<=1500:
    print("Tu bono es de $1700")
    print("Tu sueldo en total es de: $", sueldo+1700)
elif sueldo>1500 and sueldo<3000:
    print("Tu bono es de $3500")
    print("Tu sueldo en total es de: $", sueldo+3500)
elif sueldo>3000 and sueldo<8000:
    print ("Tu bono es de: $8500")
    print("Tu sueldo en total es de: $", sueldo+8500)
elif sueldo>8000:
    print("Tu bono es de $10000")
    print("Tu sueldo en total es de: $", sueldo+10000)
else:
    print("No valido")