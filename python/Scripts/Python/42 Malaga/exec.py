import sys

# Comprobar si se proporcionan argumentos y unirlos en una única cadena
if len(sys.argv) > 1:
    texto = " ".join(sys.argv[1:])
else:
    print("Uso: python programa.py texto")
    sys.exit()

# Invertir el orden de los caracteres de la cadena
texto_invertido = texto[::-1]

# Cambiar las letras mayúsculas por minúsculas y viceversa
texto_final = ""
for letra in texto_invertido:
    if letra.islower():
        texto_final += letra.upper()
    else:
        texto_final += letra.lower()

# Imprimir el resultado final
print(texto_final)
