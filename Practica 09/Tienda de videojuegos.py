#Tuplas y Diccionario

info_tienda = ("Blockbuster!")

inventario = {
    "Sonic X Shadow Generations":{'precio':50,'stock':10},
    "God of War":{'precio':60,'stock':15},
    "GTA VI":{'precio':100,'stock':3},
}

print("============ ¡Bienvenido a Blockbuster!============")
#print(f"\nEl precio del segundo juego es: {inventario['minecraft']['precio']}\n")

print("Los juegos en existencia son: \n")

for juegos in inventario:
    print(f"{juegos}    ${inventario[juegos]['precio']}  Unidades: {inventario[juegos]['stock']}".capitalize())

while True:
    
    opcion = input("\nDeseas comprar algun juego? (si/no): \n").lower()

    if opcion == 'si':
        juegoO = input("Ingrese el nombre del juego que quieras comprar: \n").lower()

        if juegoO in inventario:
            print("==========================================")
            print(f"Usted ha comprado el juego: '{juegoO}.'")
            inventario[juegoO]["stock"] -= 1
            print(f"Las copias disponibles de '{juegoO}' ahora son: {inventario[juegoO]['stock']}")
            print("==========================================")
            print(f"Usted ha comprado el juego '{juegoO}.'")
            inventario[juegoO]["stock"] -= 1
            print(f"Las copias disponibles de '{juegoO}' ahora son: {inventario[juegoO]['stock']}")
            print("==========================================")
    
    elif opcion == 'no':
        print("Te esperamos pronto!..")
        break
    else:
        print("Por favor ingrese una respuesta válida..")