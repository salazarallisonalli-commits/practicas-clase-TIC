nombres=["Angel", "karla", "luis", "mateo", "maria", "luis", "karla"]
print(f"los nombres que se tienen son{nombres}")
nombreBuscar=input("¿Que nombre deseas buscar?: ")
encontrado=False
contador=0
i=0
while i<len(nombres):
    if nombres[i]==nombreBuscar:
        encontrado=True
        contador=contador+1
        print("Encontrado en a posición:", i)
    i=i+1
if encontrado==True:
    print("Nombre encontrado")
    print("Aparece", contador, "veces")
else:
    print("Nombre no encontrado")

nombre=input("Ingresa un nombre")
cantidad=nombres.lower().count(nombre)
if cantidad >1:
    nombres.remove(nombre)
    print(nombres)
else:
    print(nombres)