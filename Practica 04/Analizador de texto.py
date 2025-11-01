texto = input("ingrese un texto de tu elección")
texto = texto.lower()

letra1 = input("ingresa la primera letra:").lower()
letra2 = input("ingrese la segunda letra:").lower()
letra3 = input("ingrese la tercera letra:").lower()

contador1=0
contador2=0
contador3=0

for caracter in texto:
    if caracter == letra1:
        contador1=contador1 + 1
    elif caracter == letra2:
        contador2=contador2 + 1
    elif caracter == letra3:
        contador3=contador3 + 1

palabras=texto.split(" ")
cantidad_palabras=len(palabras)

primera_letra=texto[0]
ultima_letra=texto[-1]

texto_invertido = "".join(palabras[::-1])
tiene_python = "python" in texto

print ("""\nTEXTO ANALIZADO""")
print (f"La letra",{letra1},"aparece",{contador1},"veces.")
print (f"La letra",{letra2},"aparece",{contador2},"veces.")
print (f"La letra",{letra3},"aparece",{contador3},"veces.")

print (f"La primera letra del texto:",primera_letra)
print (f"La ultima letra del texto:",ultima_letra)
print (f"\n Texto con palabras en orden inverso:\n",{texto_invertido})

if tiene_python:
    print ("La palabra python SI se encuentra en el texto.")
else:
    print("La palabra python No se encuentra en el texto.")