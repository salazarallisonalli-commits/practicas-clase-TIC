sexo=(input("Ingresa tu sexo"))
edad=(int(input("Ingresa tu edad")))
estado=(input("Ingresa tu estado civil"))
hijos=(int(input("Ingresa la cantidad de hijos que tienes")))
if sexo=="mujer" and hijos==1 and edad<18:
    print("Eres mujer, tienes un hijo y eres menor de edad entonces el apoyo será de $800")
elif sexo=="mujer" and hijos==1 and edad>=18:
    print("Eres mujer, tienes un hijo y eres mayor de edad entonces el apoyo será de $300")
elif sexo=="mujer" and hijos>1 and edad<18:
    print("Eres mujer, tienes mas de un hijo y eres menor de edad entonces el apoyo será de $1500")
elif sexo=="mujer" and hijos>1 and edad>=18:
    print("Eres mujer, tienes más de un hijo y eres mayor de edad entonces el apoyo será de $500")
elif sexo=="hombre" and hijos>=1 and estado=="soltero":
    print("Eres hombre y tienes hijos, el apoyo será de $780")
else:
    print ("No valido")