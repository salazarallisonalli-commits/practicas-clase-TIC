edad=int(input("Ingresa tu edad"))
permiso=input("¿Tienes permiso de tus padres?")
acompañante=input("¿Tienes un acompañante?")
if edad>=18 or permiso=="si":
    print("Puedes entrar al concierto")
else:
    print("No puedes entrar al concierto")

if edad>=18 or permiso=="si":
    print("puedes entrar al concierto")
elif edad>=18 or acompañante=="si":
    print("Puedes entrar al concierto")
else:
    print("No puedes entrar al concierto")