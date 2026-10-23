#Programa para calcular áreas
#área cuadrado; lado x lado
lado=float(input("ingresa lado"))
areaCuadrado=lado*lado
print("El área es ", areaCuadrado)
print(f"El área es {areaCuadrado}")
#area de un triangulo
base=float(input("Ingresa la base"))
altura=float(input("Ingresa la altura"))
areaTriangulo=(base * altura)/2
print("El area es " , areaTriangulo)
#area de un trapecio 
baseMayor=float(input("Ingresa la base mayor"))
baseMenor=float(input("Ingresa la base menor"))
alturaTrapecio=float(input("Inngresa la altura")) 
areaTrapecio=((baseMayor + baseMenor)* alturaTrapecio)/2 
print("El área del trapecio es ", areaTrapecio) 
#area circulo
radio=float(input("ingresa el radio del circulo"))
areaCirculo=(radio * radio) * 3.1416
print("El area del circulo es ", areaCirculo)
#area pentagono
perimetro=float(input("ingresa el perimetro del pentagono"))
apotema=float(input("Ingresa el apotema"))
areaPentagono=(perimetro * apotema)/2 
print("El area del pentagono es ", areaPentagono)