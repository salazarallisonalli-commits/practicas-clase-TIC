peliculas=[]
cantidadPelis=int(input("cuantas peliculas quieres agregar"))
i=0
while i<cantidadPelis:
    peli=input("Ingresa la peli: ")
    peliculas.append(peli)
    print(peliculas)
    i=i+1
peliBuscar=input("que peli buscas")
if peliBusar in peliculas:
    print("si está")
else:
    print("No está pero dejame agregarla")
    peliculas.append(peliBuscar)
    print(peliculas)
peliBorrar=input("que pelicula quieres borrar: ")
peliculas.remove(peliBorrar)
print(peliculas)