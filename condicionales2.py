calif=float(input("Dame tu calificación"))
if calif==10:
    print("Excelente!")
elif calif==9:
    print("Muy bien")
elif calif==8:
    print("Bien")
elif calif==7:
    print("Puedes mejorar")
elif calif==6:
    print("Ay mijo")
else:
    print("nub")

#temperatura
temp=float(input("Ingresa la temperatura"))
if temp>=40:
    print("Hace mucho calor")
elif temp>=30 and temp<40:
    print("Está templadito")
elif temp>=20 and temp<30:
    print("Está fresco")
elif temp<20:
    print("Hace frio")
else:
    print("no valido")