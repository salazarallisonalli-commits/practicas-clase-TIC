#listas
alumnos=["juanito", "angelito"]
#diccionarios
alumno1={
    "nombre": "juanito",
    "edad": 15,
    "promedio":8.2
}
alumno2={
    "nombre": "angelito",
    "edad":18,
    "promedio":10
}
#onsultar valores
#forma 1
print("nombre: ", alumno1["nombre"])
#forma2 
print("nombre: ", alumno1.get("nombre"))
#modificar algun cambio
alumno1["nombre"]="pedrito"
print("nombre: ", alumno1.get("nombre"))
#mostrar clave/editar 
for clave, valor in alumno1.items():
    print(clave, ":", valor)
    