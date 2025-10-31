# Simulador de compras exitosas (Bitcoin)
monto = int(input("Ingrese el monto disponible a invertir: "))

Inversion = 0
contador = 0

while monto >= Inversion:
    Inversion = int(input("¿Cuanto deseas invertir del monto?: "))
    if monto >= Inversion:
        print ("Uste ha realizado una compra")
        contador = +1
        SD = monto - Inversion
        print("El total de compras es: ", contador)
        print("Su saldo restante es: ", SD)
    else:
        print("Ingrese un monto menor o igual a: ", monto)