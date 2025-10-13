while True:
    print("\n MINI CALCULADORA")
    print("1.Sumar dos números")
    print("2.Restar dos números")
    print("3.Multiplicar dos números")
    print("4.Dividir dos números")
    print("5.Salir")

# Pedimos los dos números al usuario

    opcion = input("Elige una operación (1, 2, 3, 4, 5)") 
    if opcion == "1":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 + num2
        print("El resultado de la suma es:", resultado)

    elif opcion == "2":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 - num2
        print("El resultado de la resta es:", resultado)

    elif opcion == "3":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 * num2
        print("El resultado de la multiplicación es:", resultado)

    elif opcion == "4":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        if num2 != 0:
            resultado = num1 / num2
            print("El resultado de la división es:", resultado)
        else:
            print("Error: No se puede dividir entre cero :(.)")

    elif opcion == "5":
        print("Gracias por usarme, Hasta pronto :), ")
        break   # Sale del bucle y termina el programa

    else:
        print("Lo siento, opción no válida, intenta de nuevo.")