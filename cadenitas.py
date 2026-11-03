nombre="Allison"
frase="Un cafecito, riquito riquito"
print(nombre)
print(frase)
#mostra el numero en mayusculas
print(nombre.upper())
print(frase.upper())
#mostrar en minus
print(frase.lower())
#obtener un caracter en una
letra=frase[4]
print(letra)
frase2="El-mundo-es-bonito"
print(frase2.split("-"))
nombreC="Allison Salazar Diaz"
print(nombreC.split(" "))
#dos primeras letras del nombre
letras1=nombreC[0:2]
print(letras1)
#reemplazar en la cadena
nuevaF=frase.replace("riquito", "bonito")
print(nuevaF)
#numero de caracteres de la cadena : largo
largoCadena=len(nuevaF)
print(largoCadena)