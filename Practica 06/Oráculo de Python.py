def iniciar_oraculo():
    
    while True:
        print()
        opcion = input("¿Deseas conocer tu destino?(Si/No) ").lower()
        if opcion == "no":
            print("El oráculo esperará por ti.")
            break

        Nombre = input("Dime tu nombre ").capitalize()
        print(f"Hola, {Nombre}. Bienvenido al Oráculo de Python ✨.")
        year = int(input("Dime tu año de nacimiento "))
        Edad = 2025 - year
        Numero = int(input(f"{Nombre}, por favor elige un número del 1 al 4: "))
        
        def calcular_elemento(year):
            resultado = year%10
            if resultado == 0 or resultado == 1:
                elemento = "Metal"
            elif resultado == 2 or resultado == 3:
                elemento = "Agua"
            elif resultado == 4 or resultado == 5:
                elemento = "Madera"
            elif resultado == 6 or resultado == 7:
                elemento = "Fuego" 
            elif resultado == 8 or resultado == 9:
                elemento = "Tierra"
            return elemento
        Elem = calcular_elemento(year)
        print(f"Su elemento es: {Elem}")
        print()
        calcular_elemento(year)

        def generar_prediccion():
            if Numero == 1:
                mensaje = f"Oh, {Nombre}, espíritu del elemento {Elem}… Los vientos del destino murmuran tu nombre. El equilibrio de tu esencia se mueve entre la luz y la sombra, y el poder del elemento {Elem} fluye en ti, guiándote hacia el cambio. Confía en tu intuición, pues solo quien comprende su propio elemento puede descifrar el camino que el universo le revela."
            elif Numero == 2:
                mensaje = f"{Nombre}, tu esencia vibra en armonía con el elemento {Elem}. El firmamento ha hablado: una decisión marcará tu destino. Sigue la corriente del {Elem}, y descubrirás la verdad que el cosmos guarda para ti."
            elif Numero == 3:
                mensaje = f"{Nombre}, portador del elemento {Elem}, el universo observa tus pasos con atención. Tu elemento no es solo fuerza, es reflejo de tu alma. Cuando lo aceptes sin temor, los caminos se abrirán ante ti."
            elif Numero == 4:
                mensaje = f"{Nombre}, has sido elegido por el elemento {Elem}, los hilos del azar se entretejen a tu alrededor. Nada es casualidad: cada encuentro, cada pérdida, ha sido guiado por la esencia del elemento {Elem} que vive en ti."
            return mensaje
        Mens = generar_prediccion()
        print(f"""✨ Mensaje del Oráculo ✨: 
°--------------------------°
{Mens}
°--------------------------°""")
iniciar_oraculo()