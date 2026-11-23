print("---GRIMES DISC SHOP---")
discos=[
    {
        "Nombre del disco": "Visions",
        "Precio del disco": "$500",
        "Artista": "Grimes",
        "Stock":10
    },
    {
        "Nombre del disco": "Masterpiece",
        "Precio del disco": "$500",
        "Artista": "Big Thief",
        "Stock":10
    },
    {
        "Nombre del disco": "GREENGREEN",
        "Precio del disco": "$600",
        "Artista": "Cortis",
        "Stock":10
    }
    {
        "Nombre del disco": "COLOR OUTSIDE THE LINES",
        "Precio del disco": "$400"
        "Artista": "Cortis"
    }
]
#Mostrar las opciones del menú
menu = ["1. Agregar disco"
"2. Ver discos"
"3. Eliminar disco"
"4. Modificar disco"
"5. Mostrar discos en espera de restock"
"6. Buscar discos por cierto criterio"
"7. Vender disco"
"8. Salir"
]
op=0
while op==0:
    print(menu)
    op=int(input("Ingrese el número de la opción que desea: "))

    if op==1:
        album={
            "Nombre del disco": input("Ingrese el nombre del disco: "),
            "Precio del disco": float(input("Ingrese el precio del disco: ")),
            "Artista": input("Ingresa el nombre del artista: "),
            "Stock":int(input("Ingrese la cantidad de discos"))
        }
        discos.append(album)
        op=0
    elif op==2:
        print(discos)
        op=0
    elif op==3:
        print(discos)
        discoEliminar=input("Ingrese el nombre del disco que desea eliminar")
        i=0
        while i < len(discos):
            if discos[i]["Nombre del disco"] == discoEliminar:
                discos.remove(discos[i])
                print(discos)
        i=i+1
        op=0
    elif op==4:
        print(discos)
        discoMod=input("Ingrese el nombre del disco que quiere modificar")
        i=0
        while i < len(discos):
            if discos[i]["Nombre del disco"] == discoMod:
                print("1.Nombre del disco")
                print("2.Precio del disco")
                print("3.Artista del disco")
                print("4.cantidad en stock")
                opMod=int(input("¿Qué desea modificar del disco?"))
                if opMod==1:
                    nuevoNom=input("Ingrese el nuevo nombre")
                    discos[i]["Nombre del disco"] = nuevoNom
                elif opMod==2:
                    nuevoPre=int(input("Ingrese el nuevo precio"))
                    discos[i]["Precio del disco"] = nuevoPre
                elif opMod==3:
                    nuevoArt=input("Ingrese el nuevo artista")
                    discos[i]["Artista"] = nuevoArt
                elif opMod==4:
                    nuevoSto=int(input("Ingrese la nueva cantidad en stock"))
                print(discos)
                break
# opcion 5
    elif op==5:
        for disco in discos:
            if disco["Stock"] == 0:
                print(disco)
                print("Este disco está en espera de restock")
    elif op==6:
        menu2 = [
            "---CRITERIOS---"
            "1. Artista"
            "2. Precio"
        ]
        print(menu2)
        crit=int(input("¿Que criterio quiere usar para buscar su disco? "))
        if crit==1:
            art=input("¿Que artista quiere buscar?")
            for disco in discos:
                if disco["Artista"] == art:
                    print(disco)
    elif op==7:
        print(discos)
        discoVen=input("¿Que disco desea vender?")
        venCan=int(input("¿Cuantos discos desea vender?"))
        for disco in discos:
            if discoVen==disco["Nombre del disco"]:
                disco["Stock"] = disco["Stock"] - venCan
                print(disco)
